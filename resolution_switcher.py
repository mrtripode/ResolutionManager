from calendar import c
from itertools import count
from typing import Tuple
import pystray
import pywintypes
import win32api
import win32con
import config as cfg
from PIL import Image as img
from pystray import Menu as menu
from pystray import MenuItem as item


def set_resolution(width:int, height:int):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = width
    devmode.PelsHeight = height
    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

    win32api.ChangeDisplaySettings(devmode, 0)

def setup(icon):
    icon.visible = True

def on_exit():
    icon.visible = False
    icon.stop()
  
def show_notification(text):
    icon.notify(text,"My test notification sub title")

if __name__ == "__main__":
    img_icon = img.open("icon.png")
    SEPARATOR = item('- - - -', None)

    menu = []

    counter = 0

    for resolution in cfg.RESOLUTION_LIST:
        #w = (lambda w=w: i.width)
        #h=i.height
        menu.append(item(f'{resolution.width},{resolution.height}', lambda resolution=resolution: set_resolution(resolution.width, resolution.height)))
        #menu.append(item(f'{i.width},{i.height}', lambda i=i: set_resolution(i.width, i.height)))

    menu.append(item(SEPARATOR, None))
    #menu.append(item('Restore', set_resolution(cfg.RESOLUTION_LIST[0].width, cfg.RESOLUTION_LIST[0].height)))
    menu.append(item('Exit', on_exit))
        
    print('total: ', len(menu))

    icon = pystray.Icon(cfg.APP_TITLE, img_icon, cfg.APP_TITLE, menu)
    icon.run(setup)