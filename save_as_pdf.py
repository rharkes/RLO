"""
save all pngs as pdf
"""
from PIL import Image
from pathlib import Path

imlist = []
p = Path(Path.cwd(), 'IM')
for i in p.glob('**/*.png'):
    imlist.append(Image.open(i))
imlist[0].save('test.pdf', save_all=True, append_images=imlist[1:])
