# Import modules
import Adafruit_MAX31855.MAX31855 as MAX31855
from time import sleep, time

# Raspberry Pi configuration.
CLK = 13
CS  = 19
DO  = 26
sensor = MAX31855.MAX31855(CLK, CS, DO)

# Define file path to save
file_path2 = "/home/pi/Ciaran/data_files/test2.csv"

# Function to run the infinite while loop 
i=0


print('Press Ctrl-C to quit.')

# Loop printing measurements every __ seconds.
while True:
    temp = sensor.readTempC()
    print('Thermocouple 2 Temperature: {0:0.3F}*C ')
    sleep(1.0)
    i+=1

    file = open(file_path2, "x")
    seconds=time()
    file.write(str(seconds) + "," + str(temp) + "\n")
    file.close()