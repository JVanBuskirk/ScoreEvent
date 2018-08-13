from pyo import *
from pmask import *
from ScoreEvent import ScoreEvent

### Instrument
class Instr1:
    def __init__(self, duration, freq, amp):
        self.env = Fader(0.001, duration-0.005, duration, amp).play()
        self.osc = Sine(freq, mul=self.env).out()
        
s = Server().boot()

### Create the score
score = ScoreEvent(s, globals())

### PMask
frequency = List([220, 330, 440, 550], 'swing')
amp = Range(0.1, 0.4)
density = Range(0.1, 0.3)
duration = 0.5
section = ScoreSection(0, 10, "Instr1", density, duration, frequency, amp)

### Add events to the score ###
score.pmask(section.getScore())

### Play the score ###
score.play()

s.gui(locals())

