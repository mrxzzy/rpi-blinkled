# rpi-blinkled

Very small script that flashes an LED to indicate when the system has finished booting. Setups a new systemd target that activates when multi-user target is reached so we can be pretty sure everything is running. When it reaches blinkled.target it will cycle the LED three times quickly (0.2 seconds). 

The pi I wrote this for also has an RTC and on a cold boot it takes a little time for the clock to sync to the system. So there's an extra while loop to check when the year is greater than 2020. That is a slower blink, at 0.6 seconds. 

Once the script exits the LED will stay lit.

