
#include "WiFi.h"
#include "ArduinoJson.h"
#include <HTTPClient.h>

#define SSID "triplex09"
#define PWD
#define SERVER "api.thingspeak.com"

String API_KEY = "QI5S8B9MQZUNI1YV";
WiFiClient client;

void setup() {
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
    HTTPClient http;
    String serverPath = "http://api.thingspeak.com/channels/1169779/fields/3/last.json?api_key=" + API_KEY;
    // https://api.thingspeak.com/channels/9/fields/2/last.csv?api_key=E52AWRAV1RSXQQJW&status=true
    http.begin(serverPath.c_str());
    //http.addHeader("Content-Type", "application/x-www-form-urlencoded");
    //String httpRequestData = "?api_key=" + API_KEY + "&field3=" + String(1);
    //Serial.println(httpRequestData);
    int httpResponseCode = http.GET();
    Serial.println(httpResponseCode);
    if (httpResponseCode<400) {
        String payload = http.getString();
        Serial.println(payload);
      StaticJsonDocument<300> JSONObj;
      DeserializationError err = deserializeJson(JSONObj, payload);
      if(err){
        Serial.println("Failed to parse.");
        Serial.println(err.c_str());
      } else{
        const char *field = JSONObj["field3"];
        //int value = parsed["Value"];
        Serial.println(field);
      }
    }
    http.end();
  delay(10000);
}
