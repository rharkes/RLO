"""
Grab images from screen
A4 = 210 x 297 mm
"""
from PIL import ImageGrab
from pathlib import Path

wh = (1201, 1700)
corners = [[1085, 139],
           [223, 139],
           [1425, 139]]

rois = [(corners[0][0], corners[0][1], corners[0][0] + wh[0], corners[0][1] + wh[1]),
        (corners[1][0], corners[1][1], corners[1][0] + wh[0], corners[1][1] + wh[1]),
        (corners[2][0], corners[2][1], corners[2][0] + wh[0], corners[2][1] + wh[1])]
im = ImageGrab.grab(bbox=rois[2])
im.show()
print(im.size)
im.save(Path('IM', '05.png'))
