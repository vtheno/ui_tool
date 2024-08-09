from glfw import PRESS, REPEAT, RELEASE
from glfw import KEY_0
from glfw import KEY_1
from glfw import KEY_2
from glfw import KEY_3
from glfw import KEY_4
from glfw import KEY_5
from glfw import KEY_6
from glfw import KEY_7
from glfw import KEY_8
from glfw import KEY_9
from glfw import KEY_A
from glfw import KEY_APOSTROPHE
from glfw import KEY_B
from glfw import KEY_BACKSLASH
from glfw import KEY_BACKSPACE
from glfw import KEY_C
from glfw import KEY_CAPS_LOCK
from glfw import KEY_COMMA
from glfw import KEY_D
from glfw import KEY_DELETE
from glfw import KEY_DOWN
from glfw import KEY_E
from glfw import KEY_END
from glfw import KEY_ENTER
from glfw import KEY_EQUAL
from glfw import KEY_ESCAPE
from glfw import KEY_F
from glfw import KEY_F1
from glfw import KEY_F10
from glfw import KEY_F11
from glfw import KEY_F12
from glfw import KEY_F13
from glfw import KEY_F14
from glfw import KEY_F15
from glfw import KEY_F16
from glfw import KEY_F17
from glfw import KEY_F18
from glfw import KEY_F19
from glfw import KEY_F2
from glfw import KEY_F20
from glfw import KEY_F21
from glfw import KEY_F22
from glfw import KEY_F23
from glfw import KEY_F24
from glfw import KEY_F25
from glfw import KEY_F3
from glfw import KEY_F4
from glfw import KEY_F5
from glfw import KEY_F6
from glfw import KEY_F7
from glfw import KEY_F8
from glfw import KEY_F9
from glfw import KEY_G
from glfw import KEY_GRAVE_ACCENT
from glfw import KEY_H
from glfw import KEY_HOME
from glfw import KEY_I
from glfw import KEY_INSERT
from glfw import KEY_J
from glfw import KEY_K
from glfw import KEY_KP_0
from glfw import KEY_KP_1
from glfw import KEY_KP_2
from glfw import KEY_KP_3
from glfw import KEY_KP_4
from glfw import KEY_KP_5
from glfw import KEY_KP_6
from glfw import KEY_KP_7
from glfw import KEY_KP_8
from glfw import KEY_KP_9
from glfw import KEY_KP_ADD
from glfw import KEY_KP_DECIMAL
from glfw import KEY_KP_DIVIDE
from glfw import KEY_KP_ENTER
from glfw import KEY_KP_EQUAL
from glfw import KEY_KP_MULTIPLY
from glfw import KEY_KP_SUBTRACT
from glfw import KEY_L
from glfw import KEY_LAST
from glfw import KEY_LEFT
from glfw import KEY_LEFT_ALT
from glfw import KEY_LEFT_BRACKET
from glfw import KEY_LEFT_CONTROL
from glfw import KEY_LEFT_SHIFT
from glfw import KEY_LEFT_SUPER
from glfw import KEY_M
from glfw import KEY_MENU
from glfw import KEY_MINUS
from glfw import KEY_N
from glfw import KEY_NUM_LOCK
from glfw import KEY_O
from glfw import KEY_P
from glfw import KEY_PAGE_DOWN
from glfw import KEY_PAGE_UP
from glfw import KEY_PAUSE
from glfw import KEY_PERIOD
from glfw import KEY_PRINT_SCREEN
from glfw import KEY_Q
from glfw import KEY_R
from glfw import KEY_RIGHT
from glfw import KEY_RIGHT_ALT
from glfw import KEY_RIGHT_BRACKET
from glfw import KEY_RIGHT_CONTROL
from glfw import KEY_RIGHT_SHIFT
from glfw import KEY_RIGHT_SUPER
from glfw import KEY_S
from glfw import KEY_SCROLL_LOCK
from glfw import KEY_SEMICOLON
from glfw import KEY_SLASH
from glfw import KEY_SPACE
from glfw import KEY_T
from glfw import KEY_TAB
from glfw import KEY_U
from glfw import KEY_UNKNOWN
from glfw import KEY_UP
from glfw import KEY_V
from glfw import KEY_W
from glfw import KEY_WORLD_1
from glfw import KEY_WORLD_2
from glfw import KEY_X
from glfw import KEY_Y
from glfw import KEY_Z
from glfw import MOD_ALT
from glfw import MOD_CAPS_LOCK
from glfw import MOD_CONTROL
from glfw import MOD_NUM_LOCK
from glfw import MOD_SHIFT
from glfw import MOD_SUPER
from glfw import MOUSE_BUTTON_1
from glfw import MOUSE_BUTTON_2
from glfw import MOUSE_BUTTON_3
from glfw import MOUSE_BUTTON_4
from glfw import MOUSE_BUTTON_5
from glfw import MOUSE_BUTTON_6
from glfw import MOUSE_BUTTON_7
from glfw import MOUSE_BUTTON_8
from glfw import MOUSE_BUTTON_LAST
from glfw import MOUSE_BUTTON_LEFT
from glfw import MOUSE_BUTTON_MIDDLE
from glfw import MOUSE_BUTTON_RIGHT
action_mappings = {}
key_buttons_mappings = {}
mouse_buttons_mappings = {}
action_mappings[PRESS] = 'PRESS'
action_mappings[REPEAT] = 'REPEAT'
action_mappings[RELEASE] = 'RELEASE'
key_buttons_mappings[KEY_0] = 'KEY_0'
key_buttons_mappings[KEY_1] = 'KEY_1'
key_buttons_mappings[KEY_2] = 'KEY_2'
key_buttons_mappings[KEY_3] = 'KEY_3'
key_buttons_mappings[KEY_4] = 'KEY_4'
key_buttons_mappings[KEY_5] = 'KEY_5'
key_buttons_mappings[KEY_6] = 'KEY_6'
key_buttons_mappings[KEY_7] = 'KEY_7'
key_buttons_mappings[KEY_8] = 'KEY_8'
key_buttons_mappings[KEY_9] = 'KEY_9'
key_buttons_mappings[KEY_A] = 'KEY_A'
key_buttons_mappings[KEY_APOSTROPHE] = 'KEY_APOSTROPHE'
key_buttons_mappings[KEY_B] = 'KEY_B'
key_buttons_mappings[KEY_BACKSLASH] = 'KEY_BACKSLASH'
key_buttons_mappings[KEY_BACKSPACE] = 'KEY_BACKSPACE'
key_buttons_mappings[KEY_C] = 'KEY_C'
key_buttons_mappings[KEY_CAPS_LOCK] = 'KEY_CAPS_LOCK'
key_buttons_mappings[KEY_COMMA] = 'KEY_COMMA'
key_buttons_mappings[KEY_D] = 'KEY_D'
key_buttons_mappings[KEY_DELETE] = 'KEY_DELETE'
key_buttons_mappings[KEY_DOWN] = 'KEY_DOWN'
key_buttons_mappings[KEY_E] = 'KEY_E'
key_buttons_mappings[KEY_END] = 'KEY_END'
key_buttons_mappings[KEY_ENTER] = 'KEY_ENTER'
key_buttons_mappings[KEY_EQUAL] = 'KEY_EQUAL'
key_buttons_mappings[KEY_ESCAPE] = 'KEY_ESCAPE'
key_buttons_mappings[KEY_F] = 'KEY_F'
key_buttons_mappings[KEY_F1] = 'KEY_F1'
key_buttons_mappings[KEY_F10] = 'KEY_F10'
key_buttons_mappings[KEY_F11] = 'KEY_F11'
key_buttons_mappings[KEY_F12] = 'KEY_F12'
key_buttons_mappings[KEY_F13] = 'KEY_F13'
key_buttons_mappings[KEY_F14] = 'KEY_F14'
key_buttons_mappings[KEY_F15] = 'KEY_F15'
key_buttons_mappings[KEY_F16] = 'KEY_F16'
key_buttons_mappings[KEY_F17] = 'KEY_F17'
key_buttons_mappings[KEY_F18] = 'KEY_F18'
key_buttons_mappings[KEY_F19] = 'KEY_F19'
key_buttons_mappings[KEY_F2] = 'KEY_F2'
key_buttons_mappings[KEY_F20] = 'KEY_F20'
key_buttons_mappings[KEY_F21] = 'KEY_F21'
key_buttons_mappings[KEY_F22] = 'KEY_F22'
key_buttons_mappings[KEY_F23] = 'KEY_F23'
key_buttons_mappings[KEY_F24] = 'KEY_F24'
key_buttons_mappings[KEY_F25] = 'KEY_F25'
key_buttons_mappings[KEY_F3] = 'KEY_F3'
key_buttons_mappings[KEY_F4] = 'KEY_F4'
key_buttons_mappings[KEY_F5] = 'KEY_F5'
key_buttons_mappings[KEY_F6] = 'KEY_F6'
key_buttons_mappings[KEY_F7] = 'KEY_F7'
key_buttons_mappings[KEY_F8] = 'KEY_F8'
key_buttons_mappings[KEY_F9] = 'KEY_F9'
key_buttons_mappings[KEY_G] = 'KEY_G'
key_buttons_mappings[KEY_GRAVE_ACCENT] = 'KEY_GRAVE_ACCENT'
key_buttons_mappings[KEY_H] = 'KEY_H'
key_buttons_mappings[KEY_HOME] = 'KEY_HOME'
key_buttons_mappings[KEY_I] = 'KEY_I'
key_buttons_mappings[KEY_INSERT] = 'KEY_INSERT'
key_buttons_mappings[KEY_J] = 'KEY_J'
key_buttons_mappings[KEY_K] = 'KEY_K'
key_buttons_mappings[KEY_KP_0] = 'KEY_KP_0'
key_buttons_mappings[KEY_KP_1] = 'KEY_KP_1'
key_buttons_mappings[KEY_KP_2] = 'KEY_KP_2'
key_buttons_mappings[KEY_KP_3] = 'KEY_KP_3'
key_buttons_mappings[KEY_KP_4] = 'KEY_KP_4'
key_buttons_mappings[KEY_KP_5] = 'KEY_KP_5'
key_buttons_mappings[KEY_KP_6] = 'KEY_KP_6'
key_buttons_mappings[KEY_KP_7] = 'KEY_KP_7'
key_buttons_mappings[KEY_KP_8] = 'KEY_KP_8'
key_buttons_mappings[KEY_KP_9] = 'KEY_KP_9'
key_buttons_mappings[KEY_KP_ADD] = 'KEY_KP_ADD'
key_buttons_mappings[KEY_KP_DECIMAL] = 'KEY_KP_DECIMAL'
key_buttons_mappings[KEY_KP_DIVIDE] = 'KEY_KP_DIVIDE'
key_buttons_mappings[KEY_KP_ENTER] = 'KEY_KP_ENTER'
key_buttons_mappings[KEY_KP_EQUAL] = 'KEY_KP_EQUAL'
key_buttons_mappings[KEY_KP_MULTIPLY] = 'KEY_KP_MULTIPLY'
key_buttons_mappings[KEY_KP_SUBTRACT] = 'KEY_KP_SUBTRACT'
key_buttons_mappings[KEY_L] = 'KEY_L'
key_buttons_mappings[KEY_LAST] = 'KEY_LAST'
key_buttons_mappings[KEY_LEFT] = 'KEY_LEFT'
key_buttons_mappings[KEY_LEFT_ALT] = 'KEY_LEFT_ALT'
key_buttons_mappings[KEY_LEFT_BRACKET] = 'KEY_LEFT_BRACKET'
key_buttons_mappings[KEY_LEFT_CONTROL] = 'KEY_LEFT_CONTROL'
key_buttons_mappings[KEY_LEFT_SHIFT] = 'KEY_LEFT_SHIFT'
key_buttons_mappings[KEY_LEFT_SUPER] = 'KEY_LEFT_SUPER'
key_buttons_mappings[KEY_M] = 'KEY_M'
key_buttons_mappings[KEY_MENU] = 'KEY_MENU'
key_buttons_mappings[KEY_MINUS] = 'KEY_MINUS'
key_buttons_mappings[KEY_N] = 'KEY_N'
key_buttons_mappings[KEY_NUM_LOCK] = 'KEY_NUM_LOCK'
key_buttons_mappings[KEY_O] = 'KEY_O'
key_buttons_mappings[KEY_P] = 'KEY_P'
key_buttons_mappings[KEY_PAGE_DOWN] = 'KEY_PAGE_DOWN'
key_buttons_mappings[KEY_PAGE_UP] = 'KEY_PAGE_UP'
key_buttons_mappings[KEY_PAUSE] = 'KEY_PAUSE'
key_buttons_mappings[KEY_PERIOD] = 'KEY_PERIOD'
key_buttons_mappings[KEY_PRINT_SCREEN] = 'KEY_PRINT_SCREEN'
key_buttons_mappings[KEY_Q] = 'KEY_Q'
key_buttons_mappings[KEY_R] = 'KEY_R'
key_buttons_mappings[KEY_RIGHT] = 'KEY_RIGHT'
key_buttons_mappings[KEY_RIGHT_ALT] = 'KEY_RIGHT_ALT'
key_buttons_mappings[KEY_RIGHT_BRACKET] = 'KEY_RIGHT_BRACKET'
key_buttons_mappings[KEY_RIGHT_CONTROL] = 'KEY_RIGHT_CONTROL'
key_buttons_mappings[KEY_RIGHT_SHIFT] = 'KEY_RIGHT_SHIFT'
key_buttons_mappings[KEY_RIGHT_SUPER] = 'KEY_RIGHT_SUPER'
key_buttons_mappings[KEY_S] = 'KEY_S'
key_buttons_mappings[KEY_SCROLL_LOCK] = 'KEY_SCROLL_LOCK'
key_buttons_mappings[KEY_SEMICOLON] = 'KEY_SEMICOLON'
key_buttons_mappings[KEY_SLASH] = 'KEY_SLASH'
key_buttons_mappings[KEY_SPACE] = 'KEY_SPACE'
key_buttons_mappings[KEY_T] = 'KEY_T'
key_buttons_mappings[KEY_TAB] = 'KEY_TAB'
key_buttons_mappings[KEY_U] = 'KEY_U'
key_buttons_mappings[KEY_UNKNOWN] = 'KEY_UNKNOWN'
key_buttons_mappings[KEY_UP] = 'KEY_UP'
key_buttons_mappings[KEY_V] = 'KEY_V'
key_buttons_mappings[KEY_W] = 'KEY_W'
key_buttons_mappings[KEY_WORLD_1] = 'KEY_WORLD_1'
key_buttons_mappings[KEY_WORLD_2] = 'KEY_WORLD_2'
key_buttons_mappings[KEY_X] = 'KEY_X'
key_buttons_mappings[KEY_Y] = 'KEY_Y'
key_buttons_mappings[KEY_Z] = 'KEY_Z'
mouse_buttons_mappings[MOUSE_BUTTON_1] = 'MOUSE_BUTTON_1'
mouse_buttons_mappings[MOUSE_BUTTON_2] = 'MOUSE_BUTTON_2'
mouse_buttons_mappings[MOUSE_BUTTON_3] = 'MOUSE_BUTTON_3'
mouse_buttons_mappings[MOUSE_BUTTON_4] = 'MOUSE_BUTTON_4'
mouse_buttons_mappings[MOUSE_BUTTON_5] = 'MOUSE_BUTTON_5'
mouse_buttons_mappings[MOUSE_BUTTON_6] = 'MOUSE_BUTTON_6'
mouse_buttons_mappings[MOUSE_BUTTON_7] = 'MOUSE_BUTTON_7'
mouse_buttons_mappings[MOUSE_BUTTON_8] = 'MOUSE_BUTTON_8'
mouse_buttons_mappings[MOUSE_BUTTON_LAST] = 'MOUSE_BUTTON_LAST'
mouse_buttons_mappings[MOUSE_BUTTON_LEFT] = 'MOUSE_BUTTON_LEFT'
mouse_buttons_mappings[MOUSE_BUTTON_MIDDLE] = 'MOUSE_BUTTON_MIDDLE'
mouse_buttons_mappings[MOUSE_BUTTON_RIGHT] = 'MOUSE_BUTTON_RIGHT'
