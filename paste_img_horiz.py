# coding: utf-8
# https://gist.github.com/b6c87590a06081175d8f
import Image, photos, dialogs, sys

images = []
number_of_images = int(dialogs.input_alert("# of images?"))

assert 1 <= number_of_images <=36

for i in range(number_of_images):
    images.append(photos.pick_image())

widths, heights = zip(*(j.size for j in images))

total_width = sum(widths)
max_height = max(heights)

new_image = Image.new("RGB", (total_width, max_height))

x_offset = 0
for im in images:
    new_image.paste(im, (x_offset, 0))
    x_offset += im.size[0]
    
try:
    photos.save_image(new_image)
    dialogs.hud_alert("Saved!")
    new_image.show()
except Exception:
    dialogs.hud_alert("could not save file!".title(), "error")
    sys.exit(0)
