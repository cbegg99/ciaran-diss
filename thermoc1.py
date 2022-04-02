# Import modules
import Adafruit_MAX31855.MAX31855 as MAX31855
from time import sleep, time

# Raspberry Pi configuration.
CLK = 25
CS  = 23
DO  = 24
sensor = MAX31855.MAX31855(CLK, CS, DO)

# Define file path to save
file_path1 = "/home/pi/Ciaran/data_files/test1.csv"

# Function to run the infinite while loop 
i=0


print('Press Ctrl-C to quit.')

# Loop printing measurements every __ seconds.
while True:
    temp = sensor.readTempC()
    print('Thermocouple 1 Temperature: {0:0.3F}*C ')
    sleep(1.0)
    i+=1

    file = open(file_path1, "x")
    seconds=time()
    file.write(str(seconds) + "," + str(temp) + "\n")
    file.close()