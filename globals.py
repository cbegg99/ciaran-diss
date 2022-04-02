from time import sleep, time

# Define a function to convert celsius to fahrenheit.
def celsiusToFahrenheit(celsius):
    return celsius * 9.0 / 5.0 + 32.0

# Function to run the infinite while loop 
def runMeasurements(sensor):
    i=0

    # Loop printing measurements every second.
    print('Press Ctrl-C to quit.')

    while True:
        temp = sensor.readTempC()
        print('Thermocouple 1 Temperature: {0:0.3F}*C '.format(temp, celsiusToFahrenheit(temp)))
        sleep(1.0)
        i+=1

        file = open("/home/pi/Ciaran/data_files/test1.csv", "a")
        seconds=time()
        file.write(str(seconds) + "," + str(temp) + "\n")
        file.close()