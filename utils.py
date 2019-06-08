from kivy import platform
from kivy.core.window import Window

def strip_whitespace(value):
    return value.replace('\n', '').replace('\r', '').strip()

def is_windows():
    return True if platform == 'win' else False

def pct_h(pct):
    return Window.height * pct

def pct_w(pct):
    return Window.width * pct