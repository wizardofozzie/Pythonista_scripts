# coding: utf-8
## Takes a youtube URL and time code and copies time-coded URL to clipboard
import appex, requests, clipboard, console, dialogs, collections, sys

# Thanks to @cclauss
# from https://github.com/cclauss/Ten-lines-or-less/blob/master/form_dialog_from_fields_dict.py
    
def form_dialog_from_fields_dict(title, fields_dict):
    return dialogs.form_dialog(title, [{'title': k, 'type': v} for k, v in fields_dict.items()])


my_fields_dict1 = collections.OrderedDict((
    ('URL',      'url'), ('Time',     'text')
    ))

my_fields_dict2 = collections.OrderedDict((
                         ('Time',     'text'),
    ))

if appex.is_running_extension():
    url = appex.get_url()
    d = form_dialog_from_fields_dict("Enter timestamp as mm:ss", my_fields_dict2)
    if d is None: sys.exit()
    ts = d['Time']
else:
    d = form_dialog_from_fields_dict("Enter YouTube URL and time (mm:ss)", my_fields_dict1)
    if d is None: sys.exit()
    url = d['URL']
    ts = d['Time']


def main():
    assert any([x in url for x in ("youtube", "youtu.be")]), "{0} is not a YouTube URL!".format(url)
    assert ":" in ts, "timestamp must be written as (hh:)mm:ss"
    
    if ts.count(":") == 1:
        mins, secs = map(int, ts.split(":"))
        hrs = 0
    elif ts.count(":") == 2:
        hrs, mins, secs = map(int, ts.split(":"))
    else:
        sys.stderr.write("Bad timestamp (too many ':')")
        sys.exit(0)
    
    seconds = hrs*(60**2) + mins*(60**1) + secs*(60**0)
    newurl = "{url}?t={seconds}".format(url=url, seconds=seconds)
    
    clipboard.set(newurl)
    dialogs.hud_alert("{0} copied to clipboard".format(newurl))
    return newurl 

main()
