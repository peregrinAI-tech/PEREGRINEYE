# filename: camera_script.py

import subprocess
i = 1
while True:
    user_input = input("Presiona 'q' para tomar una foto: ")
    if user_input.lower() == 'q':
        subprocess.run(['libcamera-jpeg', '-o', user_input.lower()+f'{i}.jpg', '-t', '2000'])
        print("Foto tomada exitosamente.")
        i = i + 1
    else:
        print("Entrada no reconocida. Por favor, intenta de nuevo.")
