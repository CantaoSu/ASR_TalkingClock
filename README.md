# Multi-lingual Talking Clock & Alarm 🐣🐻
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/release/python-31013/)
## Description🐕:

Welcome to the Talking Clock project! This is a multi-functional voice-based timekeeping system built using Python. It provides round-the-clock time services, featuring voice time announcements in English, Chinese, and Korean, with options for both male and female voices. It also includes timezone selection, automatic detection and reminder for daylight saving time adjustment, multiple alarm management, and to-do list capabilities.

### Key Features
- Three languages: English, Chinese, and Korean
- Two voice genders: Male and Female
- Timezone selection: Switch between three timezones worldwide (the Netherlands, China and the USA)
- Daylight Saving Time: Automatical detection and reminder one day before DST transitions
- Multiple alarms: Manage important reminders and schedules
- To-Do List: Easily add and manage tasks and to-dos

### Tech Stack
Talking Clock leverages several Python libraries and frameworks, including:
- tkinter: For creating a user-friendly graphical user interface
- pygame: For playing voice-time announcements
- librosa: For audio processing and analysis
- pydub: For audio format conversion and processing
- And other libraries to enhance programme functionality

### License
The Talking Clock project is licensed under the MIT License. For more details, please review the [License file](https://github.com/CantaoSu/Talking_Clock/blob/main/LICENSE).

## Before Installation🐲
Before you begin, make sure you have already installed `Python 3.9` or a higher version, which can be downloaded from the official Python website(https://www.python.org/downloads/).

## Installation🐱

First, click on the green `Code` button at the top of the repository, and then select `Download ZIP`.

Then, xtract the contents of the downloaded ZIP file to your desired installation location on your computer.

**If you want to run it in terminal:**

`Step 1`:Open the terminal (or command prompt, depending on your operating system) and navigate to the directory where you extracted the ZIP file（ `cd` ）.

`Step 2`:Execute the command `pip install -r Requirements.txt` to install the necessary dependencies. The requirements.txt file contains a list of libraries and dependencies required for the project.

`Step 3`:Execute the command `python basic_clock.py` to run our talking clock! 

**If you want to run it in Jupyter:**

Open Anaconda, run Jupyter Notebook, and then locate `basic_clock.ipynb` and execute it.


## User Manual🐨

### Table of Contents
- [Getting Started](#getting-started)
- [Daylight Saving Time Reminder](#daylight-saving-time-reminder)
- [Time Zone Adjustment](#time-zone-adjustment)
- [Voice Time Announcement](#voice-time-announcement)
- [Clock Functionality](#clock-functionality)
- [Alarms and To-Do List](#alarms-and-to-do-list)

### Getting Started
1. Ensure that all extracted files and folders are in the same directory.
2. Make sure you have installed the required Python resource packages.

### Daylight Saving Time Reminder
- When you run the `basic_clock.py` (or `basic_clock.ipynb`) file, a popup window will appear, asking for your computer's time (to provide the daylight saving time reminder). You can choose "Yes" or "No" to indicate your consent.
- In the main interface, you'll see the Time Window displaying the current time in your location.
- Below the Time Window is the Daylight Saving Time Reminder Window, which will display text reminders only one day before the transition to daylight saving time.

### Time Zone Adjustment
- Below the Daylight Saving Time Reminder Window, you can find the Time Zone Adjustment Window.
- You can choose from five time zones: "Local Time," "US Time," "China Time," "Korean Time," and "Dutch Time."

### Voice Time Announcement
- Under the Time Zone Adjustment Window, there are two windows to adjust the language and gender for voice time announcements.
- You have three language options: English, Chinese, and Korean, and you can select either a male or female voice.
- After making your selections, click the "Play" button, and the application will announce the current time based on your chosen time zone, language, and gender.

### Clock Functionality
- The Clock Functionality displays the current time in your selected time zone.
- Below the clock, you will find the Alarms and To-Do List sections.

### Alarms and To-Do List
- You can add and delete multiple alarms and receive voice reminders when they go off.
- In addition, you can set to-do items by selecting "set as to-do," providing a "To-Do Message," and the application will convert your to-do items into voice announcements when the scheduled time arrives.

That's it! You're all set to make the most of our Talking Clock application. Enjoy managing your time and staying organized with ease.

## Linguistic Rules for Telling Time🐹:
### English
In English, the basic format for telling time is as follows:

`"It's" + "hour" + "minutes" + "am/pm"`

In this format, "hour" represents the current hour, and "minutes" corresponds to the current number of minutes. "Am" is used for the time from midnight until noon, indicating the morning hours, while "pm" is used for the time from noon until midnight, denoting the afternoon and evening.

The time is typically presented in the 12-hour clock format.


**Special cases:**

 `Midnight `: When the clock strikes 12:00 at midnight, it's referred to as "twelve midnight" rather than 12:00 am.

 `Noon `: When the clock strikes 12:00 at noon, it's called "twelve noon" instead of 12:00 pm.

 `Quarter Past `: When the minute count is 15, the expression "one quarter past" is used instead of specifying the exact number of minutes past the hour.

 `Quarter To `: When the minute count is 45, the expression "one quarter to" is used, along with the subsequent hour, to indicate that the time is nearing the next hour.

 `Half Past `: When the minute count is 30, "half past" is used, followed by the current hour, to indicate the halfway point in the hour.

### <u>Chinese</u>
In Chinese, the fundamental structure for conveying time is as follows:

`"Now" + "is" + "morning (6:00-11:59)" / "noon(12:00-12:59)" / "afternoon (1:00-5:59)" / "dusk (6:00-6:59)" / "evening (7:00-24:59)" / "before dawn (1:00-5:59)" + "hours" + "minutes"`


**Special cases:**

When the minute part is 0, the minutes are omitted, and only the hour part is mentioned.


### Korean
In Korean, the format structure is as follows (in Korean, verbs always appear at the end of a sentence):

`"Now" + "morning (6:00-11:59)" / "afternoon (12:00-17:59)" / "evening (18:00-23:59)" + "hour" + "minutes" + "is"`


**Special cases:**

When the minute part is 0, the minutes are omitted, and only the hour part is mentioned.

## Team Organization and Member Contributions🐧

`Cantao Su`

Participated in the overall application framework design; was responsible for the daylight saving time advance reminder feature; the popup for obtaining the user's computer time; recorded audio files for the voice time announcement feature in English (male), Korean (male), and Korean (female); and adhered to Python writing conventions to refactor all code.

`Weixi Lai`

Participated in the discussion of the entire programme design; was responsible for crafting the README.md and requirements.txt files; undertook the code writing for the English language section, and achieved gender switching for all languages without any code redundancy by implementing gender variable support and function calls.

`Yanhua Liao`

Participated in discussion of the overall team project design and architecture; responsible for the recording of Chinese and English female voices; responsible for the code writing of Korean and Chinese language sections, as well as the code writing of the gender change option section.

`Yinqiu Wang`

Participated in discussion of the overall team project design and architecture; responsible for the implementation of the time zone conversion function, local time retrieval function, language switching function implementation, and corresponding GUI functionality implementation.

`Ziyun Zhang`

Participated in the discussion of the entire program design; responsible for the implementation of the alarm clock function and the coding of the layout of the alarm clock in the GUI interface.

## Technical Challenges🐰

### Integration of Functionalities and Language Implementations
- **Challenge:** The project had separate development tracks for functionality and language implementation. During the final integration, multiple issues were encountered, and significant portions of code needed to be rewritten.
- **Solution:** Close collaboration and communication between teams were essential to overcome this challenge.

### Timezone Updates
- **Challenge:** Connecting user interface choices to timezone updates proved to be difficult. The application struggled to update the timezone based on the user's selection in the interface.
- **Solution:** Resolving this issue required a comprehensive review of the code responsible for managing timezone selection and updates.


### Alarm Clock Development
- **Challenge 1:** After implementing the alarm clock feature, the system experienced limitations in multitasking. The alarm clock would cause the entire system to wait, preventing other tasks, such as time updates or alarm list management, from running simultaneously.
- **Solution:** Leveraging the "threading" library to run the alarm clock in the background without blocking other operations helped address this challenge.

- **Challenge 2:** Debugging the code revealed situations where alarms were successfully set and added to the list in the GUI. However, when the alarm time arrived, it did not trigger the announcement. The problem was traced to a variable being restricted to a local scope.
- **Solution:** Changing the variable to a global scope resolved this issue, allowing alarms to trigger correctly.

- **Challenge 3:** The addition of a "to-do" feature alongside alarm creation was complex. Issues occurred where users could input text, but the "Confirm" button disappeared or the system played default tones instead of the user's input.
- **Solution:** Enabling and disabling the text input box based on the user's selection was a solution to ensure smoother operation.

These challenges, while demanding, were effectively addressed through teamwork, thorough code inspection, and the use of Python libraries and modules to enhance the application's functionality. 

However, there are still issues unsolved due to time limit:
### Language Announcements
- **Language Announcement Path Logic:** The designed function logic suggests that calling the corresponding audio file should be straightforward by specifying the file path. However, in practice, the system cycles through all audio files before locating and playing the intended one, despite the absence of a loop in the code.

- **Language Announcement Playback:** The project encountered challenges related to the division of responsibilities between the time announcement and playback modules. This misalignment led to significant problems, particularly concerning different parameters. Initially, the "play()" function was used for playback, but it exhibited compatibility issues on Windows systems after a Python update. Subsequent attempts to switch to "pygame" allowed only one-time playback, with permission denied issues when attempting additional plays.

- **Language Announcement and GUI Interaction:**  According to design principles, the user interface should provide visual feedback by turning white when the user presses a button, indicating a successful operation before initiating the time announcement. However, during the announcement, pressing other buttons does not provide feedback on the interface. Still, the system continues to receive play instructions, resulting in sequential announcements.


## GDPR Compliance🐳

This project complies with the General Data Protection Regulation (GDPR) standards for data privacy and protection. We take user data privacy seriously and have implemented measures to ensure that personal data is handled securely and in accordance with GDPR guidelines.

- User data: We only access the current time on the user's computer with their permission. No other user information is collected or stored.
- Transparency: We are committed to providing clear information about data usage and privacy practices.

If you have any concerns about data privacy or would like to request the removal of any specific data, please [contact us](mailto:cantaosu0109@gmail.com) for assistance.

Please note that this project is for educational purposes and may not include advanced GDPR compliance features that would be necessary for production applications. For more information on your rights and GDPR compliance, please refer to the [GDPR official website](https://gdpr.eu/).

## Reflection on FAIR data 🐷
In developing the Python-based Talking Clock program, adherence to FAIR data principles (Findable, Accessible, Interoperable, Reusable) is vital for data sharing and reusability.

- Findable: The project incorporates comprehensive metadata, unique identifiers, and structured documentation for enhanced discoverability.
- Accessible: Open access on GitHub under an MIT license ensures that resources are freely available and accessible through stable and reliable URLs.

In addition to being Findable and Accessible, the program is designed for Interoperability and Reusability. It uses standard Python libraries, follows best practices, and provides thorough documentation, fostering collaboration and knowledge sharing in the voice technology field.

