import time
import board
import busio
import gc

import adafruit_bme280

ADRESSE_BME280 = 0x76

i2c = busio.I2C(board.SCL, board.SDA) # Crée la connexion i²c

bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, ADRESSE_BME280)

# https://opensource.com/article/19/9/linux-terminal-colors
COLOR_BLACK_FG = "\033[30m"
COLOR_RED_FG = "\033[31m"
COLOR_GREEN_FG = "\033[32m"
COLOR_ORANGE_FG = "\033[33m"
COLOR_BLUE_FG = "\033[34m"
COLOR_MAGENTA_FG = "\033[35m"
COLOR_CYAN_FG = "\033[36m"
COLOR_LIGHT_GRAY_FG = "\033[37m"
COLOR_DEFAULT_FG = "\033[39m"

COLOR_BLACK_FG = "\033[40m"
COLOR_RED_BG = "\033[41m"
COLOR_GREEN_BG = "\033[42m"
COLOR_ORANGE_BG = "\033[43m"
COLOR_BLUE_BG = "\033[44m"
COLOR_MAGENTA_BG = "\033[45m"
COLOR_CYAN_BG = "\033[46m"
COLOR_LIGHT_GRAY_BG = "\033[47m"
COLOR_WHITE_BG = "\033[107m"
COLOR_DEFAULT_BG = "\033[49m"

def effacer_terminal():
    print("\033c")

while True:
    temperature = bme280.temperature
    humidite = bme280.humidity
    pression = bme280.pressure
    effacer_terminal()
    print("%s  ⛅  Capteur Météo " % (COLOR_WHITE_BG))
    print("  %s🌡️     %0.1f°C      %s" % (COLOR_RED_FG, temperature, COLOR_DEFAULT_FG))
    print("  %s💧    %0.1f%%       %s" % (COLOR_BLUE_FG, humidite, COLOR_DEFAULT_FG))
    print("  %s📈    %0.1fhPa   %s" % (COLOR_ORANGE_FG, pression, COLOR_DEFAULT_FG))
    print(COLOR_DEFAULT_BG)
    time.sleep(0.01)


