#include "WiFi.h"
#include "ArduinoJson.h"
#include <Stepper.h>
#include <HTTPClient.h>

#define TEST_PIN 19
#define TEST_DISTANCE 10
#define MOTOR1 13
#define MOTOR2 12
#define MOTOR3 14
#define MOTOR4 27
#define MOTOR_SPEED 300
#define TRIG_PIN 2
#define ECHO_PIN 5
#define TEST1_PIN 26
#define TEST2_PIN 25
#define TEST3_PIN 33
#define TEST4_PIN 32
#define SSID "triplex09"
#define PWD "thisbetterwork2016"
#define SERVER "api.thingspeak.com"
#define THRESHOLD 200
#define TEST_LED 2
// #define LOT_ID "A"

volatile long duration;
volatile int distance;
volatile bool testRequested = false;
String LOT_ID = "A";
String WRITE_API_KEY = "UPJ636UNXXEE2IIG";
String READ_API_KEY = "QI5S8B9MQZUNI1YV";
String TEST_WRITE_API_KEY = "5BI02IP39MVTTD40";
String TEST_READ_API_KEY = "6ABTK950PX9IKSW9";
static String CAR_IS_PRESENT = LOT_ID + "1";
int httpResponseCode;
bool confirmationReceived;

WiFiClient client;

void readFromSonar() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  // Trigger sensor
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);
  // read response
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2;
}

void spinMotor(int steps) {
  
  if(steps > 0){
    Stepper motor = Stepper(64, MOTOR1, MOTOR2, MOTOR3, MOTOR4);
    motor.setSpeed(MOTOR_SPEED);
    motor.step(steps);
  } else {
    Stepper motor = Stepper(64, MOTOR4, MOTOR3, MOTOR2, MOTOR1);
    motor.setSpeed(MOTOR_SPEED);
    motor.step(-1*steps);
  }
  Serial.println("Motor done.");
}

void IRAM_ATTR test_isr() {
  testRequested = true;
  Serial.println("ISR");
}



void setup() {
  pinMode(TEST_LED, OUTPUT);

  // Set up testing isr
  pinMode(TEST_PIN, INPUT_PULLUP);
  attachInterrupt(TEST_PIN, test_isr, FALLING);

  pinMode(TEST1_PIN, OUTPUT);
  pinMode(TEST2_PIN, OUTPUT);
  pinMode(TEST3_PIN, OUTPUT);
  pinMode(TEST4_PIN, OUTPUT);
  digitalWrite(TEST1_PIN, LOW);
  digitalWrite(TEST2_PIN, LOW);
  digitalWrite(TEST3_PIN, LOW);
  digitalWrite(TEST4_PIN, LOW);

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(115200);

  WiFi.begin(SSID, PWD);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println("Wifi Connected!");
}

void test() {
  /*
   * Testing module, triggered by button press.
   * All results will be logged to thingspeak in a 4bit value with
   * Bit0: Sonar test
   * Bit1: Motor test
   * Bit2: Write test
   * Bit3: Read test
   * 
   * Value 15 denotes all tests passing.
   * 
   * Test must be setup with motor 10cm away from sonar module.
   */
  bool sonarPassed, motorPassed, writePassed, readPassed;
  
  digitalWrite(TEST_LED, HIGH);
  
  // Test One
  readFromSonar();
  if ((TEST_DISTANCE - 1) < distance < TEST_DISTANCE + 1) {
    Serial.println("Sonar test passed.");
    digitalWrite(TEST1_PIN, HIGH);
    sonarPassed = true;
  } else {
    Serial.println("Sonar test failed.");
    sonarPassed = false;
  }
  
  // Test Two
  spinMotor(200);
  readFromSonar();
  if ( distance > TEST_DISTANCE + 1) {
    Serial.println("Motor test passed.");
    digitalWrite(TEST2_PIN, HIGH);
    motorPassed = true;
  } else {
    Serial.print("Motor test failed: ");
    Serial.println(distance);
    motorPassed = false;
  }
  // Move back to original position
  spinMotor(-200);

  // ThingSpeak Test
  // Test 3 - Write
  httpResponseCode = writeToThingspeak(TEST_WRITE_API_KEY, "&field1=100");
  if (httpResponseCode == 200) {
    Serial.println("Thingspeak Write test passed.");
    writePassed = true;
    digitalWrite(TEST3_PIN, HIGH);
  } else {
    Serial.println("Thingspeak Write test failed with:");
    Serial.println(httpResponseCode);
    writePassed = false;
  }
  
  //Test 4 - Read
  HTTPClient http;
  String serverPath = "https://api.thingspeak.com/channels/1160863/fields/1/last.json?api_key=" + TEST_READ_API_KEY;
  http.begin(serverPath.c_str());
  httpResponseCode = http.GET();
  if (httpResponseCode == 200) {
    Serial.println("Thingspeak Read test passed");
    readPassed = true;
    digitalWrite(TEST4_PIN, HIGH);
  } else {
    Serial.println("Thingspeak Read test failed.");
    readPassed = false;
  }

  delay(10000);
  digitalWrite(TEST1_PIN, LOW);
  digitalWrite(TEST2_PIN, LOW);
  digitalWrite(TEST3_PIN, LOW);
  digitalWrite(TEST4_PIN, LOW);

  int value = (int(sonarPassed) << 0) | (int(motorPassed) << 1) | (int(writePassed) << 2) | (int(readPassed) << 3);
  // Serial.println(value);
  String fieldValue = "&field3=" + String(value);
  writeToThingspeak(TEST_WRITE_API_KEY, fieldValue);

  digitalWrite(TEST_LED, LOW);
  testRequested = false;
}

int writeToThingspeak(String apiKey, String fieldValue) {
  HTTPClient http;
  String writeServerPath = "http://api.thingspeak.com/update?api_key=" + apiKey;
  http.begin(writeServerPath.c_str());
  // String value = "&field3=A1";
  // String value = "&field3=" + CAR_IS_PRESENT;
  httpResponseCode = http.POST(fieldValue);
  Serial.println(httpResponseCode);
  http.end();
  return httpResponseCode;
}


void loop() {
  if (testRequested) {
    test();
  }

  confirmationReceived = false;
  /*// Clears the trigPin
    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);
    // Trigger sensor
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);
    // read response
    duration = pulseIn(ECHO_PIN, HIGH);
    distance = duration * 0.034 / 2;
  */
  readFromSonar();
  // Serial.print("Distance: ");
  Serial.println(distance);

  // Check if car is there
  if (distance > THRESHOLD) {
    // Write to Thingspeak channel
    /*
      HTTPClient http;
      String writeServerPath = "http://api.thingspeak.com/update?api_key=" + WRITE_API_KEY;
      http.begin(writeServerPath.c_str());
      // String value = "&field3=A1";
      String value = "&field3=" + CAR_IS_PRESENT;
      httpResponseCode = http.POST(value);
      Serial.println(httpResponseCode);
      http.end();
    */
    httpResponseCode = writeToThingspeak(WRITE_API_KEY, "&field3=A1");

    // Wait for reply
    HTTPClient http;
    String serverPath = "http://api.thingspeak.com/channels/1169779/fields/3/last.json?api_key=" + READ_API_KEY;
    http.begin(serverPath.c_str());
    while (!confirmationReceived) {
      httpResponseCode = http.GET();
      if (httpResponseCode < 400) {
        Serial.println("Read from Thingspeak:");
        String payload = http.getString();
        Serial.println(payload);
        StaticJsonDocument<300> JSONObj;
        DeserializationError err = deserializeJson(JSONObj, payload);
        if (err) {
          Serial.println("Failed to parse.");
          Serial.println(err.c_str());
        } else {
          String field = JSONObj["field3"];
          Serial.println(field);
          // ADD TIMEOUT
          if (field.equals("00") || field.equals("0")) {
            Serial.println("Car confirmed, opening gate.");
            spinMotor(100);
            confirmationReceived = true;
          } else {
            Serial.print(".");
          }
        }
      } else {
        Serial.println("HTTP ERROR:");
        Serial.println(httpResponseCode);
      }
    }
  }
  delay(5000);

}
