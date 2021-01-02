# PixivStreamRecord
An Python3 script to record Pixiv live stream. This has been modified from the original by kanami1990 to incorporate streamlink usage.

Credit to kanami1990 for this project: https://github.com/kanami1990/PixivStreamRecord

Requires Python3.8

Setup
```

# Windows-Users wanting to use Linux
```
$ wsl --list                               # List all installed builds in Windows
$ Choose a Distro on the Microsft Store
$ Open whichever distro you installed (i.e. type Ubuntu if you installed it)
$ Terminal will open, and it will prompt you for a password and user (root user priv)
$ update and upgrade your current Distro
$ sudo apt-get install python3
$ sudo apt-get install python3-pip
$ sudo apt-get install ffmpeg
$ sudo apt-get install streamlink

# Virtual Env Setup (OPTIONAL)
```
$ python3 -m venv venv                     # Do not use with the Windows Linux Subsystem
$ source venv/bin/activate                 # MacOS, Linux (Do not use the Windows Linux Subsystem)
$ venv\Scripts\activate.bat                # on Windows

# Installing dependencies
```
$ pip3 install -r requirements.txt         # Install dependencies

# Virtual Env Usage (OPTIONAL)
```
$ source venv/bin/activate                  # MacOS, Linux (Do not use the Windows subsystem)
$ venv\Scripts\activate.bat                 # on Windows

# Running the program with PowerShell, Bash, Mac Terminals, or Linux Terminals (Debian etc.)
```
$ python3 AnlyStreamUrl.py <id> <session_id> <device_token> <poll_time> # to run

The `<id>` is part of the pixiv URL, e.g.: `https://sketch.pixiv.net/@<id>/lives/`
The `<session_id>` is the value specified in PHPSESSID of your pixiv cookies
The `<device_token>` is the value specified in device_token of your pixiv cookies
The `<poll_time>` is the time in seconds to poll if the stream is live