from win32api import GetSystemMetrics

def position(size): return (round(GetSystemMetrics(0) / 2 - size[0] / 2), round(GetSystemMetrics(1) / 2 - size[1] / 2))
