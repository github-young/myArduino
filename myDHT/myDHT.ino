#include <DHT.h>

DHT dht(6, DHT11);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
  delay(999);
}

void loop() {
  // put your main code here, to run repeatedly:
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  String outputText = String(t) + ", " + String(h);
  Serial.println(outputText);
  delay(999);
}
