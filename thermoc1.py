import Adafruit_MAX31855.MAX31855 as MAX31855
from globals import runMeasurements

# Raspberry Pi software SPI configuration.
CLK = 25
CS  = 23
DO  = 24
sensor = MAX31855.MAX31855(CLK, CS, DO)

runMeasurements(sensor)