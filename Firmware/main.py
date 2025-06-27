# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.encoder import EncoderHandler

encoder_handler = EncoderHandler()

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

keyboard.modules.append(encoder_handler)

# Regular GPIO Encoder
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.D1, board.D2, board.D3,), # encoder #1 
)

# Define your pins here!
PINS = [board.D9, board.D8, board.D7]

# Tell kmk we are not using a key matrix
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.Z, KC.X, KC.C
    ],
]

encoder_handler.map = [
    ((
        KC.VOLD, KC.VOLU, KC.MUTE
    ))
]

if __name__ == '__main__':
    # This is the main loop of your keyboard
    keyboard.go()
