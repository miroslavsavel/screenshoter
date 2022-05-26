https://www.geeksforgeeks.org/how-to-take-screenshots-using-python/
https://pythonguides.com/python-screen-capture/

screenshot specific window
https://stackoverflow.com/questions/40809729/can-python-get-the-screen-shot-of-a-specific-window


problem s nainstalovanim 
pyautogui a PIL

C:\Users\Šavel\PycharmProjects\Screenshoter\venv\Scripts\python.exe -m pip install --proxy http://proxy.int.sk-cert.sk:3128 --upgrade pi


C:\Users\Šavel\PycharmProjects\Screenshoter\venv\Scripts\activate.bat
pip install --proxy http://proxy.int.sk-cert.sk:3128 PIL

ERROR: Could not find a version that satisfies the requirement PIL (from versions: none)
ERROR: No matching distribution found for PIL
https://stackoverflow.com/questions/41326387/get-error-when-try-to-install-pil

skusim ak pyautogui
pip install --proxy http://proxy.int.sk-cert.sk:3128 pyautogui



-----------------------
uz ide 
https://stackoverflow.com/questions/2846947/get-screenshot-on-windows-with-python
odfoi ale iba hlavnu obrazovku

how to screenshot only one window
https://stackoverflow.com/questions/3260559/how-to-get-a-window-or-fullscreen-screenshot-without-pil

C:\Users\Šavel\PycharmProjects\Screenshoter\venv\Scripts\activate.bat
pip install --proxy http://proxy.int.sk-cert.sk:3128 win32gui

pip install win32gui

ModuleNotFoundError: No module named 'win32.distutils.command'
      [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
error: subprocess-exited-with-error

= nainstalujem najnovsiu verziu pythonu


https://stackoverflow.com/questions/52806906/cant-install-win32gui
60

Install pywin32. That gives you win32gui.

pip install pywin32

# toto funguje vyhodi okno do popredia
# https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/
# https://stackoverflow.com/questions/60309475/how-to-install-win32gui-with-pip
Enter this at the command prompt

pip install pywin32==300

Then import win32gui will work with python 3.8.


import win32gui

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "firefox" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break




from PIL import ImageGrab
import win32gui

toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)

firefox = [(hwnd, title) for hwnd, title in winlist if 'firefox' in title.lower()]
# just grab the hwnd for first window matching firefox
firefox = firefox[0]
hwnd = firefox[0]

win32gui.SetForegroundWindow(hwnd)
bbox = win32gui.GetWindowRect(hwnd)
img = ImageGrab.grab(bbox)
img.show()


# toto funguje vyhodi okno do popredia
# https://www.blog.pythonlibrary.org/2014/10/20/pywin32-how-to-bring-a-window-to-front/

import win32gui

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        if "notepad" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break

