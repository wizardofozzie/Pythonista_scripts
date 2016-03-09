# coding: utf-8
## Takes a youtube URL and time code and copies time-coded URL to clipboard
import appex, requests, clipboard, console, editor, dialogs

def main():
    if appex.is_running_extension():
        url = appex.get_url()
    else:
        url = clipboard.get()
        url = url if url.startswith("http") else dialogs.input_alert("Youtube Time URL Generator", "Enter URL")

    assert any([x in url for x in ("youtube", "youtu.be")]), "{0} is not a YouTube URL!".format(url)
    ts = dialogs.input_alert("Enter time", "hh:mm:ss")
    if ts.count(":") == 1:
        mins, secs = map(int, ts.split(":"))
        hrs = 0
    elif ts.count(":") == 2:
        hrs, mins, secs = map(int, ts.split(":"))
    newurl = "{url}?t={seconds}".format(url=url, seconds=3600*hrs + 60*mins + secs)
    
    clipboard.set(newurl)
    dialogs.hud_alert("{0} copied to clipboard".format(newurl))
    return newurl 
