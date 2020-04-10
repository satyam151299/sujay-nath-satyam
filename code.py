import speech_recognition as sr
import win32com.client as wincl
import operator
speak = wincl.Dispatch("SAPI.SpVoice")
r = sr.Recognizer()                 
with sr.Microphone() as source:     
    speak.speak("hi how can i help you")
    audio = r.listen(source) 
    print(audio)
try:
    text = r.recognize_google(audio)        
    speak.speak(text)
except:
        speak.speak("sorry")        
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
import os
from gtts import gTTS
if text=="play song" or text=="playsong":
    FLIST = open("jun.txt", "r").read().replace("\n", " ")

    print("please wait...processing")
    TTS = gTTS(text=str(FLIST), lang='en-uk')
    TTS.save("voice.mp3"+input())
    os.system("start voice.mp3")
elif text=="calculate":    
        import operator        
        import speech_recognition as s_r
        print("Your speech_recognition version is: "+s_r.__version__)
        r = s_r.Recognizer()
        my_mic_device = s_r.Microphone(device_index=1)
        with my_mic_device as source:
            print("Say what you want to calculate, example: 3 plus 3")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        my_string=r.recognize_google(audio)
        print(my_string)
        def get_operator_fn(op):
            return {
                '+' : operator.add,
                '-' : operator.sub,
                'x' : operator.mul,
                'divided' :operator.__truediv__,
                'Mod' : operator.mod,
                'mod' : operator.mod,
                '^' : operator.xor,
                }[op]
        def eval_binary_expr(op1, oper, op2):
            op1,op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)
        import win32com.client as wincl
        speak = wincl.Dispatch("SAPI.SpVoice")
        #print(eval_binary_expr(*(my_string.split())))
        try:
            speak.Speak(eval_binary_expr(*(my_string.split())))
        except:
            speak.speak("sorry wrong input")
elif text=="play YouTube" or text=="YouTube":
    import webbrowser
    url="https://www.youtube.com/"
    new=2
    webbrowser.open(url,new=new)
elif text==" open fb" or text=="open facebook" or text=="fb":
    webbrowserrowser.open("https://www.fb.com/")
elif text=="hi" or text=="hello":
    speak.speak("hello how are you")
