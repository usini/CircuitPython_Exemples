"""
Allumer une LED avec un bouton
"""
from time import sleep

# Bouton / LED
import board
import digitalio

BROCHE_BOUTON = board.D5
BROCHE_LED = board.BLUE_LED

# Mise en place de la LED
led = digitalio.DigitalInOut(BROCHE_BOUTON)
led.direction = digitalio.Direction.OUTPUT

# Mise en place du bouton
bouton = digitalio.DigitalInOut(BROCHE_LED)
bouton.direction = digitalio.Direction.INPUT
bouton.pull = digitalio.Pull.UP # Mode PullUp (inverse la logique!)

while True:
    if bouton.value is False: # Si le bouton est appuyé
        led.value = True
    if bouton.value is True: # Si le bouton n'est pas appuyé
        led.value = False
