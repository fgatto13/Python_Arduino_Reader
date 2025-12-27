#include <Streaming.h>

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int sensor = analogRead(A0);
  Serial << "Current read: " << Serial.print(sensor) << endl;
  delay(1000);
}