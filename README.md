# SYSC 3010 L2M1 Project Repo
## Authors
##### [Alex Bhend](https://github.com/alexbhend)
##### [Cameron Chunr](https://github.com/Cameron-chung)
##### [Justin Huang](https://github.com/Astray909)
##### [Ezra Pierce](https://github.com/ezrapierce000)
## Computing hardware Requirements
#### 3 RaspberryPi SBC running python2 or python3
#### 1 ESP32 Micro Controller
## Hardware Requirements
| Part Name     | Part Number   | Total Quantity| Unit Cost |
| ------------- |:-------------| ------:| -----: |
| Pi camera      | KEYESTUDIO 5MP 1080p | 1 |$13.99|
| IR Photoelectric Switch|	DIYmall 10pcs/Pack|	1(10)	|$20|
| 10k Ohm Resistors	|10EP51210K0 |	1(10)	|$7.52|
|Analog-to-digital converter|	MCP3008 ADC|	1|	10.99|
|47 Ohm Resistors|	100EP51247R0	|1(10)	|$8.66|
|5mm led	|/|	/	|$11.99 (per 100)|
|Stepper motor	|28BYJ-48|	1|	$1.80|
|Motor control board	|ULN2003APG |	1	|$3.29|
|sense HAT|	/	|1	|$48.95|
## Setup Instructions
##### GUI initialize, License Plate Reader initialize
#####   -Navigate to PlateCam folder, using command line, run python2 main.py
#####   -In the same directory, open another terminal and run python2 GUI.py
#####   -(Optional, for Admin GUI) In the same directory, open a third terminal and run python2 GUIAdmin.py
##### Gate module initialize
#####   -Edit file to contain: WiFi Network name, WiFi password, LotID
#####   -Compile esp32_gate_module.ino using Arduino compiler
#####   -Flash board with program, program will start running once flashed
#####   -Open Serial monitor to read debug messages, if needed
##### IR sensors initialize
#####   -All relevant files have been imported to the main file, running.py
#####   -Unfortunately due to the nature of the IR sensors being wired in GPIO, all parking spots and lots must be hard-coded into the running.py file
#####   -By simply running ‘running.py’ the initial vacancies for each floor will be sent to the ThingSpeak channel and polling the spots will begin
##### Web server initialize
#####   -Go to Web_RPi and download the api.py and parkinglot.db
#####   -Edit api.py file to contain the Thingspeak Read and Write api keys
#####   -Ensure that the parkinglot.db has no tables to ensure that when the api.py is used, it will add in the required tables into the parkinglot.db
#####   -Connect the gpio pins, 4 & 17, on the Raspberry Pi to two led lights with resistance to ensure the LEDs do not burn out
#####   -On console run python3 api.py and the reactive program will do all the work

## References
##### [GPIO. (n.d.). Retrieved September 28, 2020](https://www.raspberrypi.org/documentation/usage/gpio/)
##### [ULN2003 Seven Darlington Arrays. (n.d.). Retrieved September 28, 2020](https://www.st.com/en/interfaces-and-transceivers/uln2003.html)
##### [28BYJ-48 - 5V Stepper Motor. (n.d.). Retrieved September 28, 2020](https://components101.com/motors/28byj-48-stepper-motor)
##### [HC-SR404 Ultrasonic Sensor. (n.d.). Retrieved November 5, 2020](https://components101.com/ultrasonic-sensor-working-pinout-datasheet)
