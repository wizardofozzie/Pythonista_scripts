import ui
import hashlib
import clipboard

## see https://forum.omz-software.com/topic/3186/entropy-builder-finger-dragging-ui


class TouchHash(ui.View):
    def __init__(self):
        self.flex = 'WH'
        self.name = 'Swipe/Touch around to generate a hash'
        self.hash = hashlib.sha256()
        self.count = 0
        self.textview = ui.TextView()
        self.textview.touch_enabled = False
        self.textview.editable = False
        self.textview.flex = 'WH'
        self.add_subview(self.textview)
        self.present()

    def do_hash_generation(self, location, prev_location, timestamp):
        if self.count < 999:
            self.hash.update('{}{}{}{:15f}'.format(location[0],location[1],prev_location,timestamp))
            self.count += 3
            self.name = str(
                            float(self.count)/10
                            ) + '% complete'
            self.textview.text = 'Hash: ' + self.hash.hexdigest() #show the text in the textview
        elif self.count == 999:
            self.name = str(100.0) + '% complete'
            print self.hash.hexdigest()
            clipboard.set(self.hash.hexdigest())
            self.close() #close the view

    def touch_began(self, touch):
        self.do_hash_generation(touch.location, touch.prev_location, touch.timestamp)

    def touch_moved(self, touch):
        self.do_hash_generation(touch.location, touch.prev_location, touch.timestamp)

    def touch_ended(self, touch):
        #do nothing so that user can touch random spots
        pass

hash = TouchHash()
