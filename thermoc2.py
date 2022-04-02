import Adafruit_MAX31855.MAX31855 as MAX31855
from globals import runMeasurements

# Raspberry Pi software SPI configuration.
CLK = 13
CS  = 19
DO  = 26
sensor = MAX31855.MAX31855(CLK, CS, DO)

from time import sleep, time

# Function to run the infinite while loop 
def runMeasurements(sensor):
    i=0

    # Loop printing measurements every second.
    print('Press Ctrl-C to quit.')

    while True:
        temp = sensor.readTempC()
        print('Thermocouple 2 Temperature: {0:0.3F}*C ')
        sleep(1.0)
        i+=1

        file = open("/home/pi/Ciaran/data_files/test2.csv", "a")
        seconds=time()
        file.write(str(seconds) + "," + str(temp) + "\n")
        file.close()