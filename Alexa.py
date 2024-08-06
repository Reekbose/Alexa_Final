#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install SpeechRecognition


# In[2]:


pip install pyttsx3


# In[9]:


conda install -c anaconda pyaudio


# In[10]:


pip install pywhatkit


# In[11]:


pip install wikipedia


# In[1]:


pip install pyjokes


# In[8]:


import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
alexa = pyttsx3.init()

voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[0].id)

def talk(text):
    alexa.say(text)
    alexa.runAndWait()

def take_command():
    
    try:
        with sr.Microphone() as source:
            print('Alexa is listening, please speak...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        pass
    return command

def run_alexa():
    
    command = take_command()
    
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time) 
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        wiki = command.replace('tell me about', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry I did not get your question, I can search it from google')
        pywhatkit.search(command)
             
        
run_alexa()
     


# In[ ]:





# In[ ]:




