import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        position_str = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(position_str, end='')
        print('\b' * len(position_str), end='', flush=True)  # Clear previous position
except KeyboardInterrupt:
    print('\nDone.')
