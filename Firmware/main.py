import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)
keyboard.row_pins = (board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19)
keyboard.diode_orientation = "COL2ROW"  

keyboard.modules.append(Layers(keyboard))
keyboard.extensions.append(MediaKeys())

BASE = 0
IPAD_LAYER = 1

keyboard.keymap = [
    [
        KC.ESC,    KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINS,   KC.EQL,    KC.BSPC,
        KC.TAB,    KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.LBRC,   KC.RBRC,   KC.BSLS,
        KC.CAPS,   KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,   KC.ENT,
        KC.LSFT,   KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.RSFT,   KC.UP,     KC.DEL,
        KC.LCTL,   KC.LALT,  KC.LGUI,  KC.SPACE, KC.SPACE, KC.SPACE, KC.RGUI,  KC.RALT,  KC.TO(IPAD_LAYER),  KC.LEFT,  KC.DOWN,  KC.RGHT,
        KC.F1,     KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,    KC.F8,    KC.F9,    KC.F10,   KC.F11,   KC.F12,
    ],
    
    [
        KC.TO(BASE), KC.BRIGHTNESS_DOWN, KC.BRIGHTNESS_UP, KC.NO, KC.NO, KC.NO, KC.NO, KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK, KC.MUTE, KC.VOLD, KC.VOLU, KC.NO,
        KC.LGUI(KC.TAB), KC.NO, KC.LGUI(KC.W), KC.NO, KC.LGUI(KC.R), KC.LGUI(KC.T), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.CAPS, KC.LGUI(KC.A), KC.LGUI(KC.S), KC.NO, KC.LGUI(KC.F), KC.NO, KC.LGUI(KC.H), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.ENT,
        KC.LSFT, KC.LGUI(KC.LSFT(KC.Z)), KC.NO, KC.LGUI(KC.C), KC.LGUI(KC.V), KC.NO, KC.LGUI(KC.N), KC.NO, KC.NO, KC.NO, KC.NO, KC.RSFT, KC.UP, KC.DEL,
        KC.LCTL, KC.LALT, KC.LGUI, KC.LGUI(KC.SPACE), KC.LGUI(KC.SPACE), KC.LGUI(KC.SPACE), KC.RGUI, KC.RALT, KC.TO(BASE), KC.LEFT, KC.DOWN, KC.RGHT,
        KC.NO, KC.NO, KC.LGUI(KC.LSFT(KC.N3)), KC.LGUI(KC.LSFT(KC.N4)), KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.LGUI(KC.PLUS), KC.LGUI(KC.MINS),
    ],
]


keyboard.go()
