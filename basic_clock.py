import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time 
import pytz
import datetime
import os
from time import strftime
import numpy as np
from scipy.io import wavfile
from pydub.playback import play
from pydub import AudioSegment
import pygame

#change the timezone
def change_timezone(country): 
    country = time_zones.get()
    now = datetime.datetime.now()
    if country == "America":
        ny_tz = pytz.timezone("America/New_York")
        ny_time = now.astimezone(ny_tz)

    if country == "Netherlands":
        ny_tz = pytz.timezone("Europe/Amsterdam")
        ny_time = now.astimezone(ny_tz)
    if country == "China":
        ny_tz = pytz.timezone("Asia/Shanghai")
        ny_time = now.astimezone(ny_tz)
    if country == "Korea":
        ny_tz = pytz.timezone("Asia/Seoul")
        ny_time = now.astimezone(ny_tz)
        
    #print(ny_time)
    return ny_time

# Function to show the consent form
def show_consent_form():
    global consent_given
    consent_message = """
    In order to provide you with local time and information about DST changes,
    this application may access your computer's system time. 
    By clicking 'yes', you consent to the collection of this information. 
    Your data will not be stored or shared with third parties.
    """
    consent = messagebox.askquestion("Consent Form", consent_message, icon='info')
    if consent == 'yes':
        consent_given = True
    if consent == 'no':
        remind_content = "Daylight Saving Time adjustment reminder has been turned off as you have not consented to access local time."
        remind = messagebox.showinfo('Reminder', remind_content)
    return consent_given

    
def update_clock():
    global current_time_zone
    global current_time
    
    current_timestamp = time.time()
    message = ''

    if current_time_zone != "Local Time":
        now = datetime.datetime.now()
        if current_time_zone == "America":
            ny_tz = pytz.timezone("America/New_York")
        elif current_time_zone == "Netherlands":
            ny_tz = pytz.timezone("Europe/Amsterdam")
        elif current_time_zone == "China":
            ny_tz = pytz.timezone("Asia/Shanghai")
        elif current_time_zone == "Korea":
            ny_tz = pytz.timezone("Asia/Seoul")

        ny_time = now.astimezone(ny_tz)
        current_time = ny_time.strftime("%I:%M:%S %p")
        split_time_list = current_time.split(":")
        hour = int(split_time_list[0])
        minute = int(split_time_list[1])
        Time_block.config(text=f"{current_time}{message}")

    else:
        current_local_time = time.localtime(current_timestamp)
        time_str = time.strftime("%I:%M:%S %p", current_local_time)
        split_time_list = time_str.split(":")
        hour = int(split_time_list[0])
        minute = int(split_time_list[1])
        Time_block.config(text=time_str)
        
    Time_block.after(1000, update_clock)
    return hour, minute

def play_combined_audio():
    try:
        combined_audio.export("combined_audio.wav", format="wav")
        pygame.mixer.init()
        pygame.mixer.music.load("combined_audio.wav")
        pygame.mixer.music.play()
        time.sleep(len(combined_audio) / 1000)
        pygame.mixer.music.unload()
    except PermissionError as e:
        print(f"PermissionError: {e}")

"""
This function contains code related to the language logic of time in the
English.

Authors: YanhuaLiao & WeixiLai
"""
#to get hours
def get_en_hour_filename_en(hr: int,m:int):
    hr,m = update_clock()
    if m == 45:
        h = hr+1
    if hr>12:
        h = hr-12
    elif hr == 0 and m == 0:
        h = "12 midnight"
    elif hr == 12 and m == 0:
        h = "12 noon"  
    elif hr == 0:
        h = "12"
    else:
        h = hr
    return "EN_FM_h" + str(h) + '.wav'

#to get minutes
def get_en_minute_filename_en(m: int):
    hr,m = update_clock()
    if m == 15:
        return 'EN_FM_qp.wav'
    elif m == 45:
        return 'EN_FM_qt.wav'
    elif m == 30:
        return 'EN_FM_hp.wav'
    else:
        return 'EN_FM_m'+str(m)+".wav"

#to get am/pm
def get_en_ampm_filename_en(hr:int):
    hr,m = update_clock()
    if hr <12:
        return "EN_FM_am.wav"
    else:
        return "EN_FM_pm.wav"

# to speak loud in English
def en_fm_speak_the_clock():
    global combined_audio
    hour, minute =  update_clock()
    audio1 = AudioSegment.from_file('./EN_Recordings/EN_FM/EN_FM_its.wav',format ="wav")
    audio2 = AudioSegment.from_file(os.path.join('./EN_Recordings/EN_FM/',get_en_minute_filename_en(minute)),format ="wav")
    audio3 = AudioSegment.from_file(os.path.join('./EN_Recordings/EN_FM/',get_en_hour_filename_en(hour,minute)),format ="wav")
    audio4 = AudioSegment.from_file(os.path.join('./EN_Recordings/EN_FM/',get_en_ampm_filename_en(hour)),format ="wav")
    audio5 = AudioSegment.from_file("./EN_Recordings/EN_FM/EN_FM_12n.wav",format ="wav")
    audio6 = AudioSegment.from_file("./EN_Recordings/EN_FM/EN_FM_12mn.wav",format ="wav")
    
    if minute != 0:
        if minute == 15 or minute == 45 or minute == 30:
            combined_audio = audio1 + audio2 + audio3 +audio4
        else:
            combined_audio = audio1 + audio3 + audio2+ audio4
    else:
        if hour == 12:
            combined_audio = audio1 + audio5
        elif hour == 0:
            combined_audio = audio1 + audio6
        else:
            combined_audio = audio1 + audio3+ audio4

    play_combined_audio()

"""
This file contains code related to the language logic of time in the
Chinese.

Authors: YanhuaLiao & WeixiLai
"""

#to get hours
def get_cn_hour_filename(hr):
    hour, minute = update_clock()
    if hr == 0:
        return 'CN_FM_pm12.wav'
    elif hr < 12:
        return f'CN_FM_am{hr}.wav'
    else:
        return f'CN_FM_pm{hr-12}.wav'

#to get minutes   
def get_cn_minute_filename(m: int):
    if m != 0:
        return f'CN_FM_m{m}.wav'

from pydub import AudioSegment

# to speak loud in Chinese
def cn_fm_speak_the_clock():
    global combined_audio
    hour, minute = update_clock()
    audio1 = AudioSegment.from_file(os.path.join('./CN_Recordings/female',get_cn_hour_filename(hour)), format="wav")
    if minute != 0:

        audio2 = AudioSegment.from_file(os.path.join('./CN_Recordings/female',get_cn_minute_filename(minute)), format="wav")

# to combine the final audio
        combined_audio = audio1 + audio2
    else:
        combined_audio = audio1
    play_combined_audio()
    

"""
This file contains code related to the language logic of time in the
Korean.

Authors: YanhuaLiao & WeixiLai
"""
#to get hours
def get_kn_hour_filename(hr):
    if hr == 0:
        return 'KN_FM_h12.wav'
    elif hr < 12:
        return f'KN_FM_h{hr}.wav'
    else:
        return f'KN_FM_h{hr-12}.wav'

# to get other filenames
def get_kn_other_filename(hr):
    if 6 <= hr < 12:
        return "KN_FM_morning.wav"
    elif 12 <= hr < 18:
        return "KN_FM_afternoon.wav"
    else:
        return "KN_FM_evening.wav"

#to get minutes
def get_kn_minute_filename(m: int):
    return f'KN_FM_m{m}.wav'

# to speak loud in Korean
def kn_fm_speak_the_clock():
    global combined_audio
    hour, minute = update_clock()

    audio1 = AudioSegment.from_file('./KN_Recordings/KN_FM/KN_FM_now.wav', format="wav")
    audio2 = AudioSegment.from_file(os.path.join('./KN_Recordings/KN_FM', get_kn_other_filename(hour)), format="wav")
    audio3 = AudioSegment.from_file(os.path.join('./KN_Recordings/KN_FM',get_kn_hour_filename(hour)), format="wav")
    audio4 = AudioSegment.from_file(os.path.join('./KN_Recordings/KN_FM',get_kn_minute_filename(minute)), format="wav")
    audio5 = AudioSegment.from_file('./KN_Recordings/KN_FM/KN_FM_is.wav', format="wav")
    combined_audio = audio1 + audio2 + audio3 + audio4 + audio5 
    play_combined_audio()

"""
The following is the interface 
"""
root = tk.Tk()
root.title("Talking Clock")
root.configure(bg="black")
root.geometry("1280x720")

current_time_zone = "Local Time"

Time_block = tk.Label(root, font=("Times New Roman", 80, "bold"), background="black", foreground="white")
Time_block.pack(side=tk.TOP, padx=20, pady=20)

def show_consent_form():
    global consent_given
    consent_message = """
    In order to provide you with local time and information about DST changes,
    this application may access your computer's system time. 
    By clicking 'yes', you consent to the collection of this information. 
    Your data will not be stored or shared with third parties.
    """
    consent = messagebox.askquestion("Consent Form", consent_message, icon='info')
    if consent == 'yes':
        consent_given = True
    if consent == 'no':
        remind_content = "Daylight Saving Time adjustment reminder has been turned off as you have not consented to access local time."
        remind = messagebox.showinfo('Reminder', remind_content)
    return consent_given

def change_timezone(event):
    global current_time_zone
    current_time_zone = time_zones.get()
    update_clock()
    
def play_audio_for_language(language):
    global current_speed
    selected_language = language
    if language == "America":
        en_fm_speak_the_clock()
    elif language == "China":
        cn_fm_speak_the_clock()  
    elif language == "Korea":
        kn_fm_speak_the_clock()  
    else:
        print("Invalid language selected.")

time_zones = ttk.Combobox(root, values=("Local Time", "America", "Korea", "China", "Netherlands"),
                          font=("Time New Roman", 10), width=25)
time_zones.set("Local Time")
time_zones.bind("<<ComboboxSelected>>", change_timezone)
time_zones.pack()

consent_given = False
consent_given = show_consent_form()

america_button = tk.Button(root, text="America", command=lambda: play_audio_for_language("America"), bg="black", fg="grey", font=("Times New Roman", 15, "bold")) 
america_button.pack(pady=10) 
china_button = tk.Button(root, text="China", command=lambda: play_audio_for_language("China"), bg="black", fg="grey", font=("Times New Roman", 15, "bold")) 
china_button.pack(pady=10) 
korea_button = tk.Button(root, text="Korea", command=lambda: play_audio_for_language("Korea"), bg="black", fg="grey", font=("Times New Roman", 15, "bold")) 
korea_button.pack(pady=10)

update_clock()

root.mainloop()

