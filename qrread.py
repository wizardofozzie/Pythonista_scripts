# coding: utf-8
## Decode QR Code from an image using goqr.me api (from a screenshot, cropped or uncropped)
## 

import sys, os 
import requests, photos, editor, console, dialogs, clipboard, appex
from urllib import quote

from io import BytesIO
from urlparse import urljoin

GOQRME_BASEURL = "http://api.qrserver.com/v1/"

BYTES_PER_KB = 1<<20

def get_image_bytes(index=None):
    '''Pick photo from camera roll (or specify by by index number) and return its bytes in a io.BytesIO object'''
    #assert isinstance(index, (int, None)) or (isinstance(index, basestring) and str(index).isdigit())
    if index is None:
        im = photos.pick_image(show_albums=False, include_metadata=False, \
                               original=True, raw_data=True, multi=False)
    else:
        im = photos.get_image(int(index), original=True, raw_data=True)
    # check image size < 1Mb
    filesizeb = len(im)
    filesizekb = round(float(filesizeb) / (BYTES_PER_KB), 3)
    if filesizeb > 1000:
        raise ValueError("Image size exceeds 1Mb limit by {} bytes".format(round(filesizekb-1000.0, 2)))
    b = BytesIO()
    b.write(im)
    return b



def main():
    # TODO
    if appex.is_running_extension():
        if appex.get_text():
            # check if it's an image file, pass bytes
            pass
        elif appex.get_image_data():
            # check len(imgdata)>0 and PNG
            
        elif appex.get_url():
            # check url works and it's to an img
            pass
    read_qrcode_file_url = urljoin(GOQRME_BASEURL, "/v1/read-qr-code/").rstrip("/") + "/"
    filebytes = get_image_bytes().getvalue() #if not appex.is_running_extension() else appex.get_image_data()
    
    r = requests.post(read_qrcode_file_url, files={"file": filebytes })
    
    r.raise_for_status()
    
    result = r.json()
    symbol = result[0]["symbol"]
    error_reason = symbol[0]["error"]
    if error_reason is not None:
        sys.stderr.write("QR code reading error: {0}".format(error_reason))
        return None
    else:
        data = symbol[0]["data"]
        return data

if __name__ == "__main__":
    main()




### creating a qr code

#baseurl = "https://api.qrserver.com/v1/create-qr-code/?data={}&size={}&charset-source={}&charset_target={}&ecc={}&color={}&bgcolor={}&margin={}&qzone={}&format={}"

# kwargz = {
#     'size': '200x200',
#     'charset_source': 'UTF-8',
#     'charset_target': 'UTF-8',
#     'ecc': 'L',
#     'color': '0-0-0', 
#     'bgcolor': '255-255-255',
#     'margin': '1',
#     'qzone': '0',
#     'fmt': 'png'
# }
