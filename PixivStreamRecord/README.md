Requires Python3.8

Setup
```

# Windows-Users
```
$ wsl --list                               # List all installed builds in Windows
$ Choose a Distro on the Microsft Store
$ Open whichever distro you installed (i.e. type Ubuntu if you installed it)
$ Terminal will open, and it will prompt you for a password and user (root user priv)
$ update and upgrade your current Distro

# First time only
```
$ python3 -m venv venv                     # Do not use with the Windows Linux Subsystem
$ source venv/bin/activate                 # MacOS, Linux (Do not use the Windows Linux Subsystem)
$ venv\Scripts\activate.bat                # on Windows
$ pip install -r requirements.txt          # install deps

# Any other time
```
$ source venv/bin/activate                 # MacOS, Linux (Do not use the Windows subsystem)
$ venv\Scripts\activate.bat                # on Windows
$ python AnlyStreamUrl.py <id> <poll_time> # to run

The `<id>` is part of the pixiv URL, e.g.: `https://sketch.pixiv.net/@<id>/lives/`
The `<poll_time>` is the time in seconds to poll if the stream is live
