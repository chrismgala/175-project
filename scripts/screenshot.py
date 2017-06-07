import pyscreenshot as ImageGrab
import time

# fullscreen
time.sleep(1)
im=ImageGrab.grab()
# im=ImageGrab.grab(bbox=(290,215,1250,500))
im.show()
# save image file
im.save('screenshot.png')
