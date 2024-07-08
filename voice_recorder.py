import sounddevice as sd
import wavio

def record_audio(duration, filename, samplerate=44100):
    
    print(f"Recording for {duration} seconds...")
   
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype='int16')
    sd.wait()  
    
   
    wavio.write(filename, audio, samplerate, sampwidth=2)
    print(f"Audio recorded and saved as {filename}")

if __name__ == "__main__":
    duration = 10  
    filename = "output.wav" 
    record_audio(duration, filename)
