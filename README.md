# Python Arduino Reader
A small project meant to make an Arduino UNO R4 Minima communicate with Python via pyserial and to store read data inside a MySQL database.
## Circuit
<img src="circuit_image.png" style="height: 40dvh; width: auto;"/>
The board used for this project is an Arduino UNO R4 Minima, which is the successor to the widely popular UNO R3, and the circuit is as basic as it gets: 

-   one arduino board
-   one water sensor

The board gets the data from the sensor via the analog pin A0, and gives power via the 5V pin and the GND pin to close the circuit.

A detailed explanation of how the water level sensor works can be found [here](https://lastminuteengineers.com/water-level-sensor-arduino-tutorial/).

Tl;dr the sensor outputs a voltage level between 0 and 5v, directly proportional to the water level. That is the data read from our board using and analog-to-digital converter.

The retrieved data gets then handled in our Python app.

The core code to make the Arduino circuit work is quite simple, as shown in the following block of code.
```c++
#define dataPin A0
#define defaultBaud 9600

void setup(){
    Serial.begin(defaultBaud);
}
void loop(){
    Serial.println(
        analogRead(dataPin)
    );
    delay(1000);
}
```

An alternative, more stable version of the circuit can be found in the ``/ino-code`` folder, alongside the basic code to run it.