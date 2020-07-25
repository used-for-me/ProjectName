from PIL import Image

pil_im: Image.Image = Image.open('./02.jpg')
box = (0, 0, 400, 600)
region = pil_im.crop(box)
region = region.transpose(Image.ROTATE_180)
pil_im.paste(region, box)
pil_im.save('02.jpg')
