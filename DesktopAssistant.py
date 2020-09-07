import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import webbrowser

def speak(audioString):
print(audioString)
tts = gTTS(text=audioString, lang=&#39;en&#39;)
tts.save(&quot;audio.mp3&quot;)
os.system(&quot;mpg321 audio.mp3&quot;)

def recordAudio():
# Record Audio
r = sr.Recognizer()
with sr.Microphone() as source:
print(&quot;please Say something!&quot;)
audio = r.listen(source)

# Speech recognition using Google Speech Recognition
data = &quot;&quot;
try:
# Uses the default API key
# To use another API key: `r.recognize_google(audio,
key=&quot;GOOGLE_SPEECH_RECOGNITION_API_KEY&quot;)`

data = r.recognize_google(audio)
print(&quot;You said: &quot; + data)
except sr.UnknownValueError:
print(&quot;Google Speech Recognition could not understand audio&quot;)
except sr.RequestError as e:
print(&quot;Could not request results from Google Speech Recognition
service; {0}&quot;.format(e))

return data

def jarvis(data):
if &quot;open facebook&quot; in data:
speak(&quot;Sure Samarth&quot;)
webbrowser.open(&#39;https://www.facebook.com/&#39;)

if &quot;how are you&quot; in data:
speak(&quot;I am fine&quot;)

if &quot;what time is it&quot; in data:
speak(ctime())

if &quot;where is&quot; in data:
data = data.split(&quot; &quot;)
location = data[2]
speak(&quot;Hold on Samarth, I will show you where &quot; + location + &quot;
is.&quot;)
webbrowser.open(&#39;https://www.google.nl/maps/place/&#39; + location +
&#39;/&amp;amp;&#39;)

#initialization
time.sleep(2)
speak(&quot;Hello Samarth, what can I do for you?&quot;)
while 1:
data = recordAudio()
jarvis(data)
