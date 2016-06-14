#!/usr/bin/python
import mraa
import time

LED_R = mraa.Gpio(20);
LED_R.dir(mraa.DIR_OUT);
LED_B = mraa.Gpio(18);
LED_B.dir(mraa.DIR_OUT);
LED_G = mraa.Gpio(19);
LED_G.dir(mraa.DIR_OUT);

LED_R.write(0);
LED_B.write(0);
LED_G.write(0);
time.sleep(2);

LED_R.write(1);
LED_B.write(0);
LED_G.write(0);
time.sleep(2);

LED_R.write(0);
LED_B.write(1);
LED_G.write(0);
time.sleep(2);

LED_R.write(0);
LED_B.write(0);
LED_G.write(1);
time.sleep(2);

LED_R.write(1);
LED_B.write(1);
LED_G.write(0);
