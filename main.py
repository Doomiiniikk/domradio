from pathlib import Path
import subprocess

class DOMRADIO:
    def __init__(self):
        
        
        self.source : str # The audio source
        self.target : str # The Output target, i.e. the icecast server
        
        self._d_parentDirectory = Path(__file__).parent.absolute()
        
        self._b_ffmpeg : Path = self._d_parentDirectory.joinpath("ffmpeg/bin/ffmpeg.exe") # The path to the ffmpeg binary

        self._d_icecast : Path = self._d_parentDirectory.joinpath("icecast") # icecast root directory
        
        self._b_icecast : Path = self._d_icecast.joinpath("bin/icecast.exe") # The path to the icecast binary
        self._c_icecast : Path = self._d_icecast.joinpath("icecast.xml") # the path to the icecast config file
        self.running : bool = False
    
    def _icecastProcess(self) -> subprocess.Popen[bytes] :
        return subprocess.Popen(f"{self._b_icecast} -c {self._c_icecast}", shell=True, cwd=self._d_icecast)
    
    def _ffmpegProcess(self) -> subprocess.Popen[bytes] :
        return subprocess.Popen(f"{self._b_ffmpeg} -re -ar 48000 -f dshow -i audio=\"CABLE-A Output (VB-Audio Cable A)\" -codec libmp3lame -ar 48000 -ab 256k -content_type audio/mpeg -f mp3 icecast://source:scarce@localhost:8000/stream", shell=True)
    
    def run(self):
        icecastProcess = self._icecastProcess()
        ffmpegProcess = self._ffmpegProcess()
        if icecastProcess.poll() is None and ffmpegProcess.poll() is None:
            self.running = True
            print("Icecast and ffmpeg have started successfully")
        
        while self.running :
            
            if icecastProcess.poll() is not None:
                print("Icecast has stopped")
            if ffmpegProcess.poll() is not None:
                print("ffmpeg has stopped")
            if icecastProcess.poll() is not None or ffmpegProcess.poll() is not None:
                break
                
        print("buhbye")
            
    
domradio = DOMRADIO()
domradio.run()