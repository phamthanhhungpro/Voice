import sounddevice as sd
from scipy.io.wavfile import write
import os
import nltk
#nltk.download('punkt')
from tkinter import *
import time
##############################################
path = r"C:\Users\thanh\Desktop\Learning\XLTN\data_wav"
fs = 48000   # Sample rate
seconds = 150  # Max of recording
gui = Tk(className='Recorder Pro - Ahihi') # define tkinter
# set window size
gui.geometry("300x100")
gui.configure(bg="black") #dark theme

to_record_text = open('demo.txt', encoding ="utf-8").read()
text_array = nltk.sent_tokenize(to_record_text)

click = 0 # index of sentence
startTime = 0
# function to record 
def Rec_sentence():
    global click
    click = click + 1
    print(text_array[click])
    global startTime
    startTime = time.time()
    print("start recording ...")
    global myrecording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    return startTime
        
btnStart = Button(gui, text = 'Start', command = Rec_sentence) #start record button
btnStart.pack()
# function to save 
def Stop_rec():
    sd.stop()
    print("finish, press start to next sentence")
    print("######################################################################")
    duration = time.time() - startTime
    frame = int(duration * fs)
    write(path + '/'+str(len(os.listdir(path))) +'.' + 'wav', fs, myrecording[:frame])  # Save as WAV file
btnStop = Button(gui, text = 'Stop', command = Stop_rec) #stop record button
btnStop.pack()
gui.mainloop()
    
