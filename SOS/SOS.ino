int timeUnit = 200;

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // "S"
  oneLetter(1, 1, 1, 0, 0);
  // "O"
  oneLetter(3, 3, 3, 0, 0);
  // "S"
  oneLetter(1, 1, 1, 0, 0);
  // delay after a word
  digitalWrite(LED_BUILTIN, LOW);
  unsigned long time = millis();
  String outputText = "Time is: " + String(time, DEC);
  Serial.println(outputText);
  delay(1000);
}

void blinkOnce(int onTime) {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(onTime*timeUnit);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1*timeUnit);
}

void oneLetter(int in1, int in2, int in3, int in4, int in5) {
  // "one letter in Morse code"
  if (in1 != 0) {
    blinkOnce(in1);
  }
  if (in2 != 0) {
    blinkOnce(in2);
  }
  if (in3 != 0) {
    blinkOnce(in3);
  }
  if (in4 != 0) {
    blinkOnce(in4);
  }
  if (in5 != 0) {
    blinkOnce(in5);
  }
  // Spaces between letters is 3 units
  digitalWrite(LED_BUILTIN, LOW);
  delay(3*timeUnit);
}

