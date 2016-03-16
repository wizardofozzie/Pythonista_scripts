# coding: utf-8
## Paste chosen/shared images horizontally into a new image, then save and show new image

import Image, photos, dialogs, sys, appex


images = []

if appex.is_running_extension():
    images = appex.get_images()
else:
    while True:
        im = photos.pick_image()
        if im is None:
            break
        images.append(im)


number_of_images = len(images)
assert 1 <= number_of_images <= 50


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
except:
    dialogs.hud_alert("could not save file!".title(), "error")
    sys.exit(0)
