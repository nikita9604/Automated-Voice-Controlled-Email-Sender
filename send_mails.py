#These libraries needs to be installed - already done here
'''
pip install SpeechRecognition
pip install PyAudio -> pip install pipwin, pipwin install pyaudio
pip install pyttsx3
'''

#Steps to do prior the code - 
'''
1. Open Gmail -> Click on the Profile (right top corner)
2. Click Manage your Google Account -> Security -> Less secure app access (turn ON)
3. Note* = You gmail account should have 2-step verification turned off to see the above option
4. Else turn the off the verification and then follow step 2
'''

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

#Send email (gmail)
def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('from_which_email_to_send@gmail.com', 'password')
    email = EmailMessage()
    email['From'] = 'from_which_email_to_send@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

#This is sending direct mail (without voice command) to a person
'''
def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('from_which_email_to_send@gmail.com', 'password')
    server.sendmail('from_which_email_to_send@gmail.com', 'to_which_email_to_receive@gmail.com', 'Hello mam, Hope you are having a good day today')
'''

#Dictionary of Emails
email_list = {
    'mama': 'mamtarath01@gmail.com',
    'nikita': 'nikitar.study@gmail.com',
    'arpit': 'arpitrath00@gmail.com',
    'dream': 'engineeringmyway@gmail.com'
}

#Get Email info through voice commands
def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    #email-id of the name
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    #Send email
    send_email(receiver, subject, message)
    talk('Your email is sent successfully !!')
    talk('Do you want to send more emails?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

get_email_info()