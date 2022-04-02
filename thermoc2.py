import Adafruit_MAX31855.MAX31855 as MAX31855
from globals import runMeasurements

# Raspberry Pi software SPI configuration.
CLK = 13
CS  = 19
DO  = 26
sensor = MAX31855.MAX31855(CLK, CS, DO)

runMeasurements(sensor)