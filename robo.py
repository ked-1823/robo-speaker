import pyttsx3
engine=pyttsx3.init()
engine.setProperty('rate',130)
print("welcome to robo speaker ")

print("Enter the text you want to convert into speech")
while True:
    
    text=input('enter text here: ')
    if text.lower()=="q":
        break
        
    
    engine.say(text)
    engine.runAndWait()
  
   
