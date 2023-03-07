from microbit import *
from ultrasonic import Ultrasonic
ultrasonic= Ultrasonic()

# Define variables for the fan pin
fan = pin1

# Define the drying time in seconds
drying_time = 10000

# Define the threshold for detecting clothes in cm
theclothes_distance = 10

# Define the function for checking the sensor
def is_clothes_present():
    distance = ultrasonic.measure_distance_cm()
    if distance <= theclothes_distance:
        return distance

# Define the function for starting the fan
def start_fan():
    fan.write_digital(1)

# Define the function for stopping the fan
def stop_fan():
    fan.write_digital(0)

# Main loop
while True:
    if is_clothes_present():
        start_fan()
        start_time = running_time()
        elapsed_time = 0
        while elapsed_time < drying_time :
            elapsed_time += 100
            if not is_clothes_present():
                stop_fan()
                break
            sleep(100)
        stop_fan()
        display.show(Image.HAPPY)
        pin0.write_digital(1)
        display.clear()
        sleep(1000)
        display.scroll("The drying process is complete!")
        display.clear()
    else:
        stop_fan()

