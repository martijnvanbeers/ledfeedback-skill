from mycroft import MycroftSkill, intent_file_handler


class Ledfeedback(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ledfeedback.intent')
    def handle_ledfeedback(self, message):
        self.speak_dialog('ledfeedback')


def create_skill():
    return Ledfeedback()

