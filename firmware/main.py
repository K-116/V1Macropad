import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.macros.simple import SimpleMacro

# Initialize the Keyboard
keyboard = KMKKeyboard()

# --- HARDWARE CONFIGURATION ---

# 1. SWITCH MATRIX (2 rows x 3 columns = 6 positions, using 5)
keyboard.col_pins = (board.D1, board.D0, board.D4)  # 3 columns
keyboard.row_pins = (board.D2, board.D3)            # 2 rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# 2. ROTARY ENCODER (Volume control)
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
# Pin A = D6, Pin B = D7, Button = D8 (push-to-mute)
encoder_handler.pins = ((board.D6, board.D7, board.D8, False),)



# 4. MODULES & EXTENSIONS
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

# --- MACROS ---

# YouTube URL macro - types the URL when pressed
youtube_macro = SimpleMacro(
    text="https://www.youtube.com\n",  # \n presses Enter after typing
    use_interval=False,
    interval=0,
)

# --- KEY LAYOUT ---
# Physical layout:
# TOP ROW:     [Play/Pause]  [YouTube URL]
# BOTTOM ROW:  [Copy]        [Paste]        [Select All]
#
# Matrix layout (2 rows x 3 columns):
# Row 0 (Top):     [0,0] = Play/Pause    [0,1] = YouTube    [0,2] = Unused
# Row 1 (Bottom):  [1,0] = Copy          [1,1] = Paste       [1,2] = Select All

keyboard.keymap = [
    # Default Layer
    [
        # Row 0 (Top row - 2 buttons)
        KC.MPLY,                    # [0,0] Top-Left: Play/Pause
        youtube_macro,              # [0,1] Top-Right: Types youtube.com URL
        KC.NO,                      # [0,2] Top-Right corner: Not used
        
        # Row 1 (Bottom row - 3 buttons)
        KC.LCTL(KC.C),              # [1,0] Bottom-Left: Copy (Ctrl+C)
        KC.LCTL(KC.V),              # [1,1] Bottom-Middle: Paste (Ctrl+V)
        KC.LCTL(KC.A),              # [1,2] Bottom-Right: Select All (Ctrl+A)
    ]
]

# --- ENCODER MAP ---
# Encoder always controls volume regardless of layer
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD, KC.MUTE),),  # Volume Up/Down, Mute on click
]

if __name__ == '__main__':
    keyboard.go()
