import glfw

content = ""
content += "from glfw import PRESS, REPEAT, RELEASE\n"
names = [
    name
    for name in dir(glfw)
    if name.startswith("KEY_")
    or name.startswith("MOUSE_BUTTON_")
    or name.startswith("MOD_")
]

for name in names:
    content += f"from glfw import {name}\n"

content += "action_mappings = {}\n"
content += "key_buttons_mappings = {}\n"
content += "mouse_buttons_mappings = {}\n"

for name in ["PRESS", "REPEAT", "RELEASE"]:
    content += f"action_mappings[{name}] = {name!r}\n"
for name in names:
    if name.startswith("KEY_"):
        content += f"key_buttons_mappings[{name}] = {name!r}\n"
    elif name.startswith("MOUSE_BUTTON_"):
        content += f"mouse_buttons_mappings[{name}] = {name!r}\n"


with open("ui_enum.py", "w", encoding="utf-8") as f:
    f.write(content)
