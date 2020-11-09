#define TRIG_PIN 2
#define ECHO_PIN 5

long duration;
int distance;

void setup() {
  pinMode(TRIG_PIN, OUTPUT); 
  pinMode(ECHO_PIN, INPUT);
  Serial.begin(115200); 
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
  distance= duration*0.034/2;

  Serial.print("Distance: ");
  Serial.println(distance);
  delayMicroseconds(1000);

}
