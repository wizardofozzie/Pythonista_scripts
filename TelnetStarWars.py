 #!/usr/bin/env python
 '''
 STARWARS!
 '''
 import telnetlib
 import ui
 
 HOST = "towel.blinkenlights.nl"
 playing = False
 
 def button_pressed(sender):
     global playing
     if sender.title == "Play":
         sender.title = 'Pause'
         playing = True
     else:
         sender.title = 'Play'
         playing = False
         
 tn = telnetlib.Telnet(HOST)
 #view
 view = ui.View()
 view.background_color = (0,0,0)
 view.frame = (0,0,800,800)
 #textview
 tv = ui.TextView()
 tv.font = ('Courier',17)
 tv.flex = 'LRTB'
 tv.text_color = (1,1,1)
 tv.name = 'textview1'
 tv.frame = (0, 60, 800, 400)
 tv.background_color = (0,0,0)
 view.add_subview(tv)
 #button
 btn = ui.Button()
 btn.name = 'button1'
 btn.title = 'Play'
 btn.action = button_pressed
 btn.tint_color = (1,1,1)
 btn.flex = 'LR'
 btn.frame = (359, 6, 80, 32)
 view.add_subview(btn)
 
 view.present('fullscreen')
 tn.read_until('\r\n')
 while True:
     if playing:
         txt = ''
         lines = tn.read_until('[H').replace('[H','')
         view['textview1'].text = lines
