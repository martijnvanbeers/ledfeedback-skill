import time
from pixel_ring import pixel_ring
from gpiozero import LED

from mycroft import MycroftSkill, intent_file_handler


class Ledfeedback(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.power = LED(5)
        self.power.on()

        pixel_ring.set_brightness(10)

    def shutdown(self):
        self.power.off()

    def initialize(self):
        self.log.info("initalising led handler")
        self.add_event('recognizer_loop:wakeword', self.handler_wakeword)
        self.add_event('recognizer_loop:record_begin', self.handler_record_begin)
        self.add_event('recognizer_loop:record_end', self.handler_record_end)
        self.add_event('recognizer_loop:audio_output_start', self.handler_audio_output_start)
        self.add_event('recognizer_loop:audio_output_end', self.handler_audio_output_end)

    def handler_wakeword(self, message):
        # code to excecute when recognizer_loop:wakeword message detected...
        self.log.info("waking up")
        pixel_ring.wakeup()

    def handler_record_begin(self, message):
        # code to excecute when recognizer_loop:record_begin message detected...
        self.log.info("listening")
        pixel_ring.listen()

    def handler_record_end(self, message):
        # code to excecute when recognizer_loop:record_end message detected...
        self.log.info("done listening")
        pixel_ring.off()


    def handler_audio_output_start(self, message):
        # code to excecute when recognizer_loop:audio_output_start message detected...
        self.log.info("speaking")
        pixel_ring.speak()


    def handler_audio_output_end(self, message):
        # code to excecute when recognizer_loop:audio_output_end message detected..
        self.log.info("done speaking")
        pixel_ring.off()

def create_skill():
    return Ledfeedback()

