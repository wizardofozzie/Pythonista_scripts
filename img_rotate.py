# coding: utf-8
## Rotate an image (either from  external apps' share-sheet, or via photo-roll)
import photos, appex, sys, console, Image


if appex.is_running_extension():
    im = appex.get_image()
else:
    im = photos.pick_image()

if im is None:
    console.hud_alert("No image chosen", "error", 1.0)
    sys.exit(0)
else:
    assert str(type(im))[8:-2][4:].partition("ImagePlugin")[0] in ("Bmp", "Gif", "Jpeg", "Png", "Ppm", "Tiff")
    keep_original = console.alert("Rotate original image?", "Rotate & copy?", \
                                  "Rotate Original", "Rotate Copy", hide_cancel_button=True)
    if keep_original == 2:
        im2 = im.copy()
    else:
        im2 = im
    
    degrees = int(console.input_alert("Rotate image __ degrees", "Use multiples of 90"))
    
    assert divmod(abs(degrees), 360)[1] in (0, 90, 180, 270)
    
    deg = (degrees % 360) if not (0 < degrees < 360) else degrees
    img = im2.rotate(deg)
    
    saved = photos.save_image(img)
    
    if saved:
        console.hud_alert("Successfully saved rotated image")
        img.show()
    else:
        console.hud_alert("Successfully saved rotated image", "error")
