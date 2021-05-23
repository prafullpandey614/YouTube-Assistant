import speech_recognition as sr
import pywhatkit
import pyttsx3

from tkinter import *
root=Tk()
root.geometry('1500x1500')
root.config(bg='black')
def cortana():
    Label(text="Listening.......",font='comicsansms 10 italic').pack()
    import speech_recognition as sc
    import pywhatkit
    import pyttsx3
    assistant = sc.Recognizer()
    speaker = pyttsx3.init()

    def responser(text):
        speaker.say(text)
        speaker.runAndWait()

    def take_cmd():
        with sc.Microphone() as source:
            print("speak now... ,i am listening...")
            voice = assistant.listen(source)
            cmd = assistant.recognize_google(voice)
            print(cmd)
            cmd = cmd.lower()
            if "google" in cmd:
                cmd = cmd.replace('google', '')
                print(cmd)
        return cmd

    def execute_assistant():
        command = take_cmd()
        print(command)
        if "play" in command:
            song = command.replace("play", "")
            responser("playing" + song)
            pywhatkit.playonyt(song)
        else:
            responser("please say clearly i am unable to understand what you say")


    execute_assistant()
Label(text='Youtube Assistant',font="comicsansms 30 bold",fg="white", bg='red').pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()
Label(text="").pack()
but = Button(text='press and speak',bg='black',fg='red',font='comicsansms 20 bold',command = cortana).pack()





root.mainloop()