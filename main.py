import pygetwindow  #https://pypi.org/project/PyGetWindow/
import time
import os
import pyautogui
import PIL

# get screensize
x,y = pyautogui.size()
print(f"width={x}\theight={y}")

x2,y2 = pyautogui.size()
x2,y2=int(str(x2)),int(str(y2))
print(x2//2)
print(y2//2)

# find new window title
z1 = pygetwindow.getAllTitles()
time.sleep(1)
print(len(z1))
# test with pictures folder
os.startfile("C:\\Users\\yourname\\Pictures")
time.sleep(1)
z2 = pygetwindow.getAllTitles()
print(len(z2))
time.sleep(1)
z3 = [x for x in z2 if x not in z1]
z3 = ''.join(z3)
time.sleep(3)

# also able to edit z3 to specified window-title string like: "Sublime Text (UNREGISTERED)"
my = pygetwindow.getWindowsWithTitle(z3)[0]
# quarter of screen screensize
x3 = x2 // 2
y3 = y2 // 2
my.resizeTo(x3,y3)
# top-left
my.moveTo(0, 0)
time.sleep(3)
my.activate()
time.sleep(1)

# save screenshot
p = pyautogui.screenshot()
p.save(r'C:\\Users\\yourname\\Pictures\\\\p.png')

# edit screenshot