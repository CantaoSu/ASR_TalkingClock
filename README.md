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
- pygame: For playing voice time announcements
- librosa: For audio processing and analysis
- pydub: For audio format conversion and processing
- And other libraries to enhance program functionality

### License
The Talking Clock project is licensed under the MIT License. For more details, please review the [License file](https://github.com/CantaoSu/Talking_Clock/blob/main/LICENSE).

## Before Installation🐲
Before you begin, make sure you have already installed 'Python 3.9' or a higher version, which can be downloaded from the official Python website(https://www.python.org/downloads/).

## Installation🐱

`Step 1`:Click on the green `Code` button at the top of the repository, and then select `Download ZIP`.

`Step 2`:Extract the contents of the downloaded ZIP file to your desired installation location on your computer.

`Step 3`:Open the terminal (or command prompt, depending on your operating system) and navigate to the directory where you extracted the ZIP file（ `cd` ）.

`Step 4`:Execute the command `pip install -r Requirements.txt` to install the necessary dependencies. The requirements.txt file contains a list of libraries and dependencies required for the project.

`Step 5`:Execute the command python basic_clock.py` to run our talking clock! Good luck!


## User Manual🐨

## Supported languages🐇
-English

-Chinese

-Korean

## Lingusitic rules for telling time🐹:
### English
In English, the basic format for telling time is as follows:

`"It's" + "hour" + "minutes" + "am/pm"`

In this format, "hour" represents the current hour, and "minutes" correspond to the current number of minutes. "Am" is used for time from midnight until noon, indicating the morning hours, while "pm" is used for time from noon until midnight, denoting the afternoon and evening.

The time is typically presented in the 12-hour clock format.


**Special cases:**

Midnight: When the clock strikes 12:00 at midnight, it's referred to as "twelve midnight" rather than 12:00 am.

Noon: When the clock strikes 12:00 at noon, it's called "twelve noon" instead of 12:00 pm.

Quarter Past: When the minute count is 15, the expression "quarter past" is used instead of specifying the exact number of minutes past the hour.

Quarter To: When the minute count is 45, the phrase "quarter to" is used, along with the subsequent hour, to indicate that the time is nearing the next hour.

Half Past: When the minute count is 30, "half past" is used, followed by the current hour, to indicate the halfway point in the hour.

### <u>Chinese</u>
In Chinese, the fundamental structure for conveying the time is as follows:

`"Now" + "is" + "morning (6:00-11:59)" / "noon(12:00-12:59)" / "afternoon (1:00-5:59)" / "dusk (6:00-6:59)" / "evening (7:00-24:59)" / "before dawn (1:00-5:59)" + "hours" + "minutes"`


**Special cases:**

When the minute part is 0, the minutes are omitted, and only the hour part is mentioned.


### Korean
In Korean, the format structure is as follows (in Korean, verb always appear at the end of a sentence):

`"Now" + "morning (6:00-11:59)" / "afternoon (12:00-17:59)" / "evening (18:00-23:59)" + "hour" + "minutes" + "is"`


**Special cases:**

When the minute part is 0, the minutes are omitted, and only the hour part is mentioned.

### Team Organization and Member Contributions🐧
`Ziyun Zhang`

Participate in the discussion of the entire program design, and be responsible for the implementation of the alarm clock function and the coding of the layout of the alarm clock in the GUI interface.

`Yinqiu Wang`

Participate in discussion of the overall team project design and architecture.Responsible for the implementation of the time zone conversion function, local time retrieval function, language switching function implementation and corresponding GUI functionality implementation.

`Yanhua Liao`

Participate in discussion of the overall team project design and architecture. First of all, I am mainly responsible for the recording of Chinese and English female voices, and then I am responsible for the code writing of Korean and Chinese language sections, as well as the code writing of the gender change option section.

`Weixi Lai`

Participated in the discussion of the entire program design; responsible for crafting the README.md and requirements.txt files; undertaken the code writing for the English language section, and achieved gender switching for all languages without any code redundancy by implementing gender variable support and function calls.

`Cantao Su`


## GDPR Compliance🐳

This project complies with the General Data Protection Regulation (GDPR) standards for data privacy and protection. We take user data privacy seriously and have implemented measures to ensure that personal data is handled securely and in accordance with GDPR guidelines.

- User data: We only access the current time on the user's computer with their permission. No other user information is collected or stored.
- Transparency: We are committed to providing clear information about data usage and privacy practices.

If you have any concerns about data privacy or would like to request the removal of any specific data, please [contact us](mailto:cantaosu0109@gmail.com) for assistance.

Please note that this project is for educational purposes and may not include advanced GDPR compliance features that would be necessary for production applications. For more information on your rights and GDPR compliance, please refer to the [GDPR official website](https://gdpr.eu/).

