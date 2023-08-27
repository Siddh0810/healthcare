
# import speech_recognition as sr
# import pyttsx3
# import smtplib
# from email.mime.text import MIMEText
# import mysql.connector
# from mysql.connector import Error
# import os
# from datetime import date

Name=input("enter patient name: ")
email=input("enter patient email:")
r = sr.Recognizer()
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
# with sr.Microphone() as source2:
#     r.adjust_for_ambient_noise(source2,duration=0.2)
# # Record audio from microphone
with sr.Microphone() as source:
    print('Please say the name of the medicine you want to prescribe')
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.listen(source)

# Convert speech to text using Google Speech Recognition
try:
    MyText = r.recognize_google(audio)
    MyText = MyText.lower()
    file_name="speak.txt"
    with open(file_name,"a") as f:
         f.write(MyText)
except sr.UnknownValueError:
    print("Unable to recognize speech")
except sr.RequestError as e:
    print("Error occurred during speech recognition:", str(e))
print("did you say "+MyText)
SpeakText(MyText)
    

    
    
"""FROM HERE SEARCH"""

import mysql.connector

host = "localhost"
user = "root"
password = "root"
database = "project"

host1 = "localhost"
user1 = "root"
password1 = "root"
database1 = "project"
# Establish the connection
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )
    connection1 = mysql.connector.connect(
        host=host1,
        user=user1,
        password=password1,
        database=database1,
    )
    cursor = connection.cursor()
    cursor1 = connection.cursor()
    # Prepare the query
    query = "SELECT * FROM medicines_csv WHERE name = %s"

    values = (MyText,)
    query1 = "INSERT INTO patient_details(name) values(%s)"
    values1 =  (Name,email)
    # Execute the query
    cursor.execute(query, values)
    cursor1.execute(query1, values1)
    cursor.commite()
    cursor1.commite()
    # Fetch and print the results
    results = cursor.fetchall()
    path="./{name}" 
    os.makedir(path)
    file_name="medicine.txt"
    file_path = os.path.join(path, file_name)
    today=date.today()
    with open(file_path,"a") as f:
        f.write("\n")
        if results:
          for row in results:
             f.write(today)
             f.write(row)
             f.write("\n")
             print(row)
    query1 = "SELECT * FROM project WHERE name = %s"
    values1 = (Name,)   
    cursor1.execute(query1, values1)
    cursor1.commite()
    id = cursor1.fetchall()      
    # Close the cursor and the connection
    cursor1.close()
    cursor.close()
    connection.close()
    print(id)
except Error as e:
    
    print("siddh shah has eeror:",e)
# Email configuration

smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'shahsiddh08@gmail.com'    # sender's mail
receiver_email = 'yeshashah9825@gmail.com'   # Receiver's mail (here this mail will be received by pharmacist)
subject = "prescription"
message = MyText
app_password = 'svotnotiieauqvut'

msg = MIMEText(message)
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = receiver_email


try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print('Email sent successfully!')
except Exception as e:
    print('An error occurred:', str(e))
finally:
    server.quit()