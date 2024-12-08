This project will launch icecast, it will start ffmpeg to stream to the icecast server.

# main.py
expects icecast binary to reside in
```
main.py
|-icecast
  |-bin
    |-icecast
```
expects icecast binary to reside in
```
main.py
|-ffmpeg
  |-bin
    |-ffmpeg
```
# command examples

list audio devices with ffmpeg on windows
```
ffmpeg -f dshow -list_devices true -i dummy
```

connect ffmpeg to icecast
```
ffmpeg -f dshow -i audio="VoiceMeeter Aux Output (VB-Audio VoiceMeeter AUX VAIO)" -codec libmp3lame -ab 32k -ac 1 -content_type audio/mpeg -f mp3 icecast://source:password@localhost:8000/stream
```