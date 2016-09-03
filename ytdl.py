import youtubedl as ytdl
import clipboard

with ytdl.YoutubeDL({}) as ydl:
    ydl.download([clipboard.get()])

try:
    from move_vids import move_vids
    move_vids()
    print("Done!")
except ImportError:
    pass
