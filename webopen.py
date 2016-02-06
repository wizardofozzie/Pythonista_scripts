##Takes URL or clipboard's URL and opens link externally in Safari

import dialogs, clipboard, webbrowser


def webopen(url=None):
    base_url = "safari-{0}"
    cburl = clipboard.get().encode()
    if not cburl.startswith("http"):
        cburl = dialogs.input_alert("URL?")
    url = base_url.format(cburl) if not url else base_url.format(url)
    webbrowser.open(url)
