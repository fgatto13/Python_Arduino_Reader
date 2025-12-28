# Python Arduino Reader
A small project meant to make an Arduino UNO R4 Minima communicate with Python via pyserial and to store read data inside a MySQL database.

An interactive version of this README is available [here](https://fgatto13.github.io/Python_Arduino_Reader/).
## Circuit
<img src="assets/circuit_image-2.png" style="max-height: 40dvh; width: auto;"/>
The board used for this project is an Arduino UNO R4 Minima, which is the successor to the widely popular UNO R3, and the circuit is as basic as it gets: 

-   one arduino board
-   one water sensor

The board gets the data from the sensor via the analog pin A0, and gives power via the 5V pin and the GND pin to close the circuit.

[This](https://app.cirkitdesigner.com/) is the software used for designing the circuits.

A detailed explanation of how the water level sensor works can be found [here](https://lastminuteengineers.com/water-level-sensor-arduino-tutorial/).

Tl;dr the sensor outputs a voltage level between 0 and 5v, directly proportional to the water level. That is the data read from our board using and analog-to-digital converter.

The retrieved data gets then handled in our Python app.

The core version of this circuit is presented here:

<img src="assets/circuit_image.png" style="max-height: 40dvh; width: auto;"/>

To make this Arduino circuit work, the core code is quite simple, as shown in the following block.
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

To address the shortcomings of the water level sensor [described here](https://lastminuteengineers.com/water-level-sensor-arduino-tutorial/#:~:text=However%2C%20there’s%20an%20important%20thing%20to%20keep%20in%20mind.%20One%20common%20issue%20with%20these%20sensors%20is%20that%20they%20don’t%20last%20very%20long%20because%20they%20are%20always%20in%20contact%20with%20water.%20When%20the%20sensor%20is%20constantly%20powered%20while%20submerged%2C%20it%20tends%20to%20corrode%20faster%2C%20which%20reduces%20its%20lifespan.), and to prolongue its lifespan, the first circuit was chosen for this project, and the code can be found in the `ino-code/` folder as `data-reader-complete.ino`.

## MySQL DataBase design
To permanently store data, a simple yet effective database was designed, in order to store both the board used, and the data read, along with the timestamp.

What follows is the UML diagram that shows the database design, while the database definition can be found inside the `dbinit.sql` file.
<img src="" style="width=;height=;" alt="database design"/>

Then, the following queries were defined to communicate with the database:
```SQL
    INSERT INTO device (device_name, baud)
    VALUES ();
    INSERT INTO reads (device_id, read_data)
    VALUES();
```

The database connection and management was done via Python, covered in the following section.
## Data reading and Python communication
First of all, to 