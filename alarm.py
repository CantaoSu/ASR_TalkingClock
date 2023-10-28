# Alarm clock module

import pyttsx3
import datetime
import time

class AlarmFunction:
    def __init__(self):
        # Initialize Engine
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Victoria')
        self.engine.setProperty('rate', 150)

    def sound_alarm(self, message):
        # play sound
        self.engine.say(message)
        self.engine.runAndWait()

    def set_absolute_trigger(self, user_hour, user_minute, todo_message=None):
        #set Alarm Trigger Mechanism
        current_datetime = datetime.datetime.now()
        trigger_datetime = current_datetime.replace(hour=user_hour, minute=user_minute, second=0, microsecond=0)

        if trigger_datetime < current_datetime:
            trigger_datetime = trigger_datetime + datetime.timedelta(days=1)

        while True:
            current_datetime = datetime.datetime.now()
            if current_datetime >= trigger_datetime:
                break
            time.sleep(10)

        if todo_message:
            self.sound_alarm(todo_message)
        else:
            self.sound_alarm("Your set time has arrived.")
