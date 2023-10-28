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
import threading
import pyttsx3
from alarm import AlarmFunction


# change the timezone
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

    # print(ny_time)
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

    current_timestamp = time.time()

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

        hour = int(ny_time.strftime("%H"))
        minute = int(ny_time.strftime("%M"))
        current_time_show = ny_time.strftime("%I:%M:%S %p")
        Time_block.config(text=f"{current_time_show}")
    else:
        current_local_time = time.localtime(current_timestamp)
        hour = current_local_time.tm_hour
        minute = current_local_time.tm_min
        current_time_show = time.strftime("%I:%M:%S %p", current_local_time)
        Time_block.config(text=f"{current_time_show}")
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


# EN FM
# to get hours
def get_en_hour_filename_en(hr: int, m: int):
    hr, m = update_clock()
    if m == 45:
        h = hr + 1
    if hr > 12:
        h = hr - 12
    elif hr == 0 and m == 0:
        h = "12 midnight"
    elif hr == 12 and m == 0:
        h = "12 noon"
    elif hr == 0:
        h = "12"
    else:
        h = hr

    return "EN_" + gender + "_h" + str(h) + '.wav'


# to get minutes
def get_en_minute_filename_en(m: int):
    hr, m = update_clock()
    if m == 15:
        return 'EN_' + gender + '_qp.wav'
    elif m == 45:
        return 'EN_' + gender + '_qt.wav'
    elif m == 30:
        return 'EN_' + gender + '_hp.wav'
    else:
        return 'EN_' + gender + '_m' + str(m) + ".wav"


# to get am/pm
def get_en_ampm_filename_en(hr: int):
    hr, m = update_clock()
    if hr < 12:
        return "EN_" + gender + "_am.wav"
    else:
        return "EN_" + gender + "_pm.wav"


def en_speak_the_clock():
    global combined_audio
    hour, minute = update_clock()
    audio1 = AudioSegment.from_file(os.path.join('./EN_Recordings/EN_' + gender + '/EN_' + gender + '_its.wav'),
                                    format="wav")
    audio2 = AudioSegment.from_file(
        os.path.join('./EN_Recordings/EN_' + gender + '/' + get_en_minute_filename_en(minute)), format="wav")
    audio3 = AudioSegment.from_file(
        os.path.join('./EN_Recordings/EN_' + gender + '/' + get_en_hour_filename_en(hour, minute)), format="wav")
    audio4 = AudioSegment.from_file(os.path.join('./EN_Recordings/EN_' + gender + '/' + get_en_ampm_filename_en(hour)),
                                    format="wav")
    audio5 = AudioSegment.from_file(os.path.join('./EN_Recordings/EN_' + gender + '/EN_' + gender + '_12n.wav'),
                                    format="wav")
    audio6 = AudioSegment.from_file(os.path.join('./EN_Recordings/EN_' + gender + '/EN_' + gender + '_12n.wav'),
                                    format="wav")

    if minute != 0:
        if minute == 15 or minute == 45 or minute == 30:
            combined_audio = audio1 + audio2 + audio3 + audio4
        else:
            combined_audio = audio1 + audio3 + audio2 + audio4
    else:
        if hour == 12:
            combined_audio = audio1 + audio5
        elif hour == 0:
            combined_audio = audio1 + audio6
        else:
            combined_audio = audio1 + audio3 + audio4

    play_combined_audio()


"""
This file contains code related to the language logic of time in the
Chinese language.

Authors: YanhuaLiao & WeixiLai
"""

# Chinese
def get_cn_hour_filename(hr):
    hr, m = update_clock()
    if hr == 0:
        return '/CN_' + gender + '_pm12.wav'
    elif hr < 12:
        return '/CN_' + gender + f'_am{hr}.wav'
    else:
        return '/CN_' + gender + f'_pm{hr - 12}.wav'


def get_cn_minute_filename(m: int):
    hr, m = update_clock()
    if m != 0:
        return '/CN_' + gender + f'_m{m}.wav'

def cn_speak_the_clock():
    global combined_audio
    hour, minute = update_clock()
    audio1 = AudioSegment.from_file(os.path.join('./CN_Recordings/CN_' + gender + get_cn_hour_filename(hour)),
                                    format="wav")
    if minute != 0:
        audio2 = AudioSegment.from_file(os.path.join('./CN_Recordings/CN_' + gender + get_cn_minute_filename(minute)),
                                        format="wav")
        combined_audio = audio1 + audio2
    else:
        combined_audio = audio1
    play_combined_audio()


# korean
def get_kn_hour_filename(hr):
    hr, m = update_clock()
    if hr == 0:
        return '/KN_' + gender + '_h12.wav'
    elif hr < 12:
        return '/KN_' + gender + f'_h{hr}.wav'
    else:
        return '/KN_' + gender + f'_h{hr - 12}.wav'

def get_kn_other_filename(hr):
    hr, m = update_clock()
    if 6 <= hr < 12:
        return "/KN_" + gender + '_morning.wav'
    elif 12 <= hr < 18:
        return "/KN_" + gender + "_afternoon.wav"
    else:
        return "/KN_" + gender + "_evening.wav"

def get_kn_minute_filename(m: int):
    hr, m = update_clock()
    return '/KN_' + gender + f'_m{m}.wav'

def kn_speak_the_clock():
    global combined_audio
    hour, minute = update_clock()

    audio1 = AudioSegment.from_file(os.path.join('./KN_Recordings/KN_' + gender + '/KN_' + gender + '_now.wav'),
                                    format="wav")
    audio2 = AudioSegment.from_file(os.path.join('./KN_Recordings/KN_' + gender + get_kn_other_filename(hour)),
                                    format="wav")
    audio3 = AudioSegment.from_file(os.path.join('./KN_Recordings/KN_' + gender + get_kn_hour_filename(hour)),
                                    format="wav")
    audio4 = AudioSegment.from_file(os.path.join('./KN_Recordings/KN_' + gender + get_kn_minute_filename(minute)),
                                    format="wav")
    audio5 = AudioSegment.from_file(os.path.join('./KN_Recordings/KN_' + gender + '/KN_' + gender + '_is.wav'),
                                    format="wav")
    combined_audio = audio1 + audio2 + audio3 + audio4 + audio5
    play_combined_audio()


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


def scale_changed(value):
    global current_speed
    current_speed = value


# Initialize pygame for playing audio
pygame.mixer.init()


def play_audio_for_language(selected_language):
    global gender
    selected_gender = gender_var.get()

    if selected_language == "English":
        if selected_gender == "Male":
            gender = "M"
            en_speak_the_clock()
        elif selected_gender == "Female":
            gender = "FM"
            en_speak_the_clock()
    if selected_language == "中文/Chinese":
        if selected_gender == "Male":
            gender = "M"
            cn_speak_the_clock()
        elif selected_gender == "Female":
            gender = "FM"
            cn_speak_the_clock()
    if selected_language == "한국어/Korean":
        if selected_gender == "Male":
            gender = "M"
            kn_speak_the_clock()
        elif selected_gender == "Female":
            gender = "FM"
            kn_speak_the_clock()


time_zones = ttk.Combobox(root, values=("Local Time", "America", "Korea", "China", "Netherlands"),
                          font=("Time New Roman", 10), width=25)
time_zones.set("Local Time")
time_zones.bind("<<ComboboxSelected>>", change_timezone)
time_zones.pack()

consent_given = False
consent_given = show_consent_form()

language_label = tk.Label(root, text="Select Language:", font=("Times New Roman", 15, "bold"), background="black",
                          foreground="white")
language_label.pack()
language_var = tk.StringVar()
language_dropdown = ttk.Combobox(root, textvariable=language_var, values=("English", "中文/Chinese", "한국어/Korean"),
                                 font=("Times New Roman", 12))
language_dropdown.pack(pady=5)

gender_label = tk.Label(root, text="Select Gender:", font=("Times New Roman", 15, "bold"), background="black",
                        foreground="white")
gender_label.pack()
gender_var = tk.StringVar()
gender_dropdown = ttk.Combobox(root, textvariable=gender_var, values=("Male", "Female"), font=("Times New Roman", 12))
gender_dropdown.pack(pady=5)

language_button = tk.Button(root, text="Play", command=lambda: play_audio_for_language(language_var.get()), bg="black",
                            fg="grey", font=("Times New Roman", 15, "bold"))
language_button.pack(pady=10)

update_clock()


# Alarm Clock Interface Display
def open_alarm_window():
    global alarm_window
    alarm_window = tk.Toplevel(root)
    alarm_window.title("Alarm Clock")
    alarm_window.geometry("400x300")

    create_button = tk.Button(alarm_window, text="Create New Alarm", command=create_new_alarm)
    create_button.pack()


alarms = []
alarm_function = AlarmFunction()


def create_new_alarm():
    new_alarm_window = tk.Toplevel(alarm_window)
    new_alarm_window.title("New Alarm")
    new_alarm_window.geometry("400x300")

    title_label = tk.Label(new_alarm_window, text="Please choose your alarm time:")
    title_label.pack()

    hours = list(range(24))
    minutes = list(range(60))

    hour_label = tk.Label(new_alarm_window, text="Hour:")
    hour_label.pack()
    hour_combo = ttk.Combobox(new_alarm_window, values=hours)
    hour_combo.pack()

    minute_label = tk.Label(new_alarm_window, text="Minute:")
    minute_label.pack()
    minute_combo = ttk.Combobox(new_alarm_window, values=minutes)
    minute_combo.pack()

    is_todo_var = tk.BooleanVar()
    is_todo_checkbox = tk.Checkbutton(new_alarm_window, text="Set as To-Do", variable=is_todo_var)
    is_todo_checkbox.pack()

    todo_entry_label = tk.Label(new_alarm_window, text="To-Do Message:")
    todo_entry_label.pack()
    todo_entry = tk.Entry(new_alarm_window, state="disabled")
    todo_entry.pack()

    def toggle_todo_text():
        if is_todo_var.get():
            todo_entry.configure(state="normal")
        else:
            todo_entry.configure(state="disabled")

    is_todo_checkbox.configure(command=toggle_todo_text)

    def confirm_alarm():
        hour = int(hour_combo.get())
        minute = int(minute_combo.get())

        if is_todo_var.get():
            todo_message = todo_entry.get()
        else:
            todo_message = None

        alarm_time = f"{hour:02d}:{minute:02d}"

        alarm_thread = threading.Thread(target=alarm_function.set_absolute_trigger, args=(hour, minute),
                                        kwargs={"todo_message": todo_message})
        alarm_thread.start()

        list_thread = threading.Thread(target=add_to_alarm_list, args=(alarm_time,))
        list_thread.start()

        new_alarm_window.destroy()

    confirm_button = tk.Button(new_alarm_window, text="Confirm", command=confirm_alarm)
    confirm_button.pack()


def add_to_alarm_list(alarm_time):
    alarms.append(alarm_time)
    update_alarm_list()


def update_alarm_list():
    for widget in alarm_window.winfo_children():
        widget.destroy()

    create_button = tk.Button(alarm_window, text="Create New Alarm", command=create_new_alarm)
    create_button.pack()

    for i, alarm_time in enumerate(alarms):
        label_text = f"Alarm {i + 1}: {alarm_time}"
        label = tk.Label(alarm_window, text=label_text)
        label.pack()

    close_button = tk.Button(alarm_window, text="Delete", command=lambda i=i: close_alarm(i))
    close_button.pack()

    def close_alarm(index):
        alarms.pop(index)
        update_alarm_list()


set_alarm_button = tk.Button(root, text="Set Alarm", command=open_alarm_window, bg="grey", fg="black",
                             font=("Times New Roman", 15, "bold"))
set_alarm_button.pack()

root.mainloop()
