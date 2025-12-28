const int dataPin = A0;
const int defaultBaud = 9600;

void setup(){
  Serial.begin(defaultBaud);
  pinMode(LED_BUILTIN, OUTPUT);
}
void loop(){
  int sensor = analogRead(dataPin);
  Serial.print(sensor);
  if (sensor > 300){
    digitalWrite(LED_BUILTIN, HIGH);
  } else {
    digitalWrite(LED_BUILTIN, LOW);
  }
  delay(1000);
}