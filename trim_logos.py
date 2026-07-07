from pathlib import Path
from PIL import Image

names = ['logo-miami-oscuro.png', 'logo-miami-claro.png']
for name in names:
    p = Path(name)
    with Image.open(p) as im:
        alpha = im.getchannel('A')
        bbox = alpha.getbbox()
        if bbox:
            cropped = im.crop(bbox)
            out = p.with_name(p.stem + '-trimmed.png')
            cropped.save(out)
            print('saved', out.name, cropped.size, bbox)
        else:
            print('no alpha bbox for', name)
