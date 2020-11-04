"""
Envoyer un tweet à l'aide de l'émulateur de clavier
Mettez l'application twitter en avant puis appuyer sur le bouton
"""
from time import sleep

# Bouton / LED
import board
import digitalio

# Clavier et layout français
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_fr import KeyboardLayoutFR

broche_bouton = board.D5
broche_led = board.BLUE_LED
tweet = "{°_°} : Salut le monde ! \n @circuitpython @labsud @m4dnerd"

# Mise en place de la LED
led = digitalio.DigitalInOut(board.BLUE_LED)
led.direction = digitalio.Direction.OUTPUT

# Mise en place du bouton
bouton = digitalio.DigitalInOut(board.D5)
bouton.direction = digitalio.Direction.INPUT
bouton.pull = digitalio.Pull.UP

# Mise en place du clavier
clavier = Keyboard(usb_hid.devices)
clavier_fr = KeyboardLayoutFR(clavier)

# Vous devez être sur l'application twitter pour envoyer un tweet
def envoyer_tweet(tweet):
    clavier_fr.write("n") # Ouvre la composition d'un tweet
    sleep(0.1)
    clavier_fr.write(tweet) # Ecrit le tweet
    sleep(0.1)
    clavier.press(Keycode.LEFT_CONTROL)
    clavier.press(Keycode.ENTER)
    clavier.release_all()

while True:
    if bouton.value is False: # Si le bouton est appuyé
        led.value = True
        print("Envoi du tweet")
        envoyer_tweet()
        sleep(1)
        led.value = False
        print("Tweet envoyé")

