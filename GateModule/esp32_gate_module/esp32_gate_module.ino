#include "WiFi.h"
#include <HTTPClient.h>

#define TRIG_PIN 2
#define ECHO_PIN 5
#define SSID "triplex09"
#define PWD 
#define SERVER "api.thingspeak.com"
#define THRESHOLD 30

long duration;
int distance;
String API_KEY = "UPJ636UNXXEE2IIG";
WiFiClient client;

void setup() {
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

void loop() {
  // Clears the trigPin
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);

  // Trigger sensor
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // read response
  duration = pulseIn(ECHO_PIN, HIGH);
  distance = duration * 0.034 / 2;

  // Serial.print("Distance: ");
  // Serial.println(distance);
  if (distance > THRESHOLD) {
    HTTPClient http;
    String serverPath = "http://api.thingspeak.com/update?api_key=" + API_KEY;
    http.begin(serverPath.c_str());
    //http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    //String httpRequestData = "?api_key=" + API_KEY + "&field3=" + String(1);
    //Serial.println(httpRequestData);
    String value = "&field3=A1";
    int httpResponseCode = http.POST(value);
    Serial.println(httpResponseCode);
    http.end();
  }
  delay(5000);

}
