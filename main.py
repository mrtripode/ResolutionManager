import pywintypes
import win32api
import win32con

devmode = pywintypes.DEVMODEType()
devmode.PelsWidth = 2880  # 2560
devmode.PelsHeight = 1920  # 1440

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)