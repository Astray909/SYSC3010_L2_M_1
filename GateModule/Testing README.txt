All tests will be run at the same time, triggered by a button press. The tests for the gate module are as follows:

Test1 - Sonar:
	This test is to ensure that the ESP32 can correctly read a value from the Sonar sensor.
It also test that the sonar sensor is properly calibrated and is reading the correct distance measurement.
The test must first be set up with a target 10cm away from the sonar sensor. The test will then be run and the sensor should read back 
10cm. If it reads back anythin between 9cm-11cm, this is considered a PASS. Anything else will be considered a FAIL.

Test2 - Motor:
	This test is to ensure that the stepper motor can be controlled by the ESP32 and is in a functioning state. This test
also relies on the sonar sensor to verify that the motor target has moved. The motor target should be in a starting position of 10cm away 
from the sonar sensor. The test will then attempt to turn the motor target away from the sonar sensor. The distance will then be measured by the sonar sensor. If the distance is more than
10cm, this is considered a PASS. If the target does not move, this is considered a FAIL.

Test3 - Thingspeak Write:
	This test is to ensure that WiFi is working on the ESP32 and that it has the ability to write to a Thingspeak channel.
This test simply writes to a Thingspeak channel and checks the HTTP response. If the response is 200, it is considered a PASS.
Anything else is considered a FAIL.

Test4 - Thingspeak Read:
	THis test is to ensure that the ESP32 can successfully read from a Thingspeak channel. This test simply reads
from a Thingspeak channel and checks the HTTP response. If the response is 200, it is considered a PASS.
Anything else is considered a FAIL.


Test Program:
	The test program is triggered by a button press. This button press will alert the ESP32 that a test has been requested.
The ESP32 will then stop it's main program and execute the 4 tests. The results of the test are sent over Serial, PASS/FAIL for each test are shown
on LEDs and the results are also sent to a Thingspeak channel for logging. The results logged are in the form of a 4 bit
number. Each test corresponds to a bit TEST 1-BIT0, TEST 2-BIT1, TEST 3-BIT2, TEST 4-BIT3. A 1 denotes a pass, 0 a fail.
