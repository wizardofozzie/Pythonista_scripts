# coding: utf-8
## Resize an image (either from  external apps' share-sheet, or via photo-roll)
import photos, appex, sys, console


if appex.is_running_extension():
    im = appex.get_image()
else:
    im = photos.pick_image()

if im is None:
    console.hud_alert("No image chosen", "error", 1.0)
    sys.exit(0)
else:
    assert repr(type(im))[8:-2] in ("PIL.JpegImagePlugin.JpegImageFile", )
    
    width, height = im.size
    percentage = int(console.input_alert("Resize image to _%", "Enter number"))
    fraction = percentage / 100.0
    new_width = int(round(width*float(fraction)))
    new_height = int(round(height*float(fraction)))
    im2 = im.resize((new_width, new_height))
    saved = photos.save_image(im2)
    
    
    if saved:
        console.hud_alert("Successfully saved resized image ({0}%)".format(int(percentage)))
    else:
        console.hud_alert("Unsuccessfully saved resized image ({0}%)".format(int(percentage)), "error")
