/*
 * Because the water sensor is always at contact with water, 
 * it usually tends to degrade fast.
 * To prolong its life, we only power it when we need to take a measurement.
 * This is done by powering the sensor through a digital pin. 
 * 
 * The code, wiring and explanation are partially taken from: 
 * https://lastminuteengineers.com/water-level-sensor-arduino-tutorial/
 */

// Pin definitions
const int waterSensorPowerPin = 7;  // Pin to power the water sensor
const int waterSensorPin = A0;      // Analog pin connected to the water sensor
// Since the max value should be around 520, we set the threshold at 500
const int upperThreshold = 500;     // Threshold to trigger alert

void setup() {
  Serial.begin(9600);
  
  // Set the power pin as output
  pinMode(waterSensorPowerPin, OUTPUT);
  
  // Ensure the sensor is powered off initially
  digitalWrite(waterSensorPowerPin, LOW);

  // Set the alert led pin as output
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
    // We create a function to read the water level and print it
    Serial.print("Water Level: ");
    Serial.println(readWaterLevel());
    // Wait for 2 seconds before the next reading
    delay(2000);
}

int readWaterLevel() {
    // Power on the water sensor
    digitalWrite(waterSensorPowerPin, HIGH);
    // Wait for the sensor to stabilize
    delay(100); 
    // Read the water sensor value
    int sensorValue = analogRead(waterSensorPin);
    // Check if the water level is above a certain threshold
    if (sensorValue > upperThreshold) {
        digitalWrite(LED_BUILTIN, HIGH); // Turn on alert LED
    } else {
        digitalWrite(LED_BUILTIN, LOW); // Turn off alert LED
    }
    // Power off the water sensor to prolong its life
    digitalWrite(waterSensorPowerPin, LOW);
    return sensorValue;
}