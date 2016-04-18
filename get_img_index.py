# coding: utf-8
## get index of image for filename ____.jpg
## see https://forum.omz-software.com/topic/3035/pick_image-index-of-picked-image

import photos

def get_img_index(filename):
    c = photos.get_count()
    for i in range(c):
        m = photos.get_metadata(i)
        if m.get('filename') == filename:
            return i

img = photos.pick_image(
                        show_albums=True, 
                        include_metadata=True, 
                        original=True, 
                        raw_data=False, 
                        multi=False
                        )

filename = img[1].get('filename')
i = get_img_index(filename)
print filename + ' = ' + str(i)
