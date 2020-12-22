Requires Python3

Setup
```
$ python3 -m venv venv
$ source venv/bin/activate                 # MacOS, Linux
$ venv\Scripts\activate.bat                # on Windows
$ pip install -r requirements.txt          # install deps
$ python AnlyStreamUrl.py <id> <poll_time> # to run

The `<id>` is part of the pixiv URL, e.g.: `https://sketch.pixiv.net/@<id>/lives/`
The `<poll_time>` is the time in seconds to poll if the stream is live