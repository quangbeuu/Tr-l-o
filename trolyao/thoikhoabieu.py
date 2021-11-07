import datetime
import urllib.request
import webbrowser
import requests
import wikipedia
from gtts import gTTS
import os 
import playsound
import pyttsx3
import speech_recognition as sr
import time
import re
import json 
import ctypes

wikipedia.set_lang('vi') # set từ điển wikipedia tìm kiếm bằng tiếng việt 
language = 'vi' 
#Hàm chuyển text thành âm thanh 
def speak(text):
#dùng thư viện gtts
    print("D.O.R.A.E.M.O.N: ",text)
    tts = gTTS(text=text,lang=language,slow=False)#slow: tốc độ đọc chậm(True),nhanh(False) #chuyển văn bản thành giọng nói
    tts.save("doraemon.mp3") #Lưu thành 1 file mp3 có chứa giọng nói của mk
    playsound.playsound("doraemon.mp3",True) #chạy file doraemon.mp3
    os.remove("doraemon.mp3") #chạy xong xóa file này đi 
#speak("Xin chào my friend.")
def listen():
    print("D.O.R.A.E.M.O.N: Đang nghe ^-^")
    ear = sr.Recognizer() #Khởi tạo tai cho trợ lý ảo(nhận dạng giọng nói)
    with sr.Microphone() as source: 
        audio = ear.listen(source,phrase_time_limit=6) #nghe người dùng nói từ microphone, phrase_time_limit là thời gian đóng mic(), thời gian trợ lý ảo sẽ nghe bạn nói
        try:
            text = ear.recognize_google(audio,language='vi_VN') #Sử dụng google để nhận diện giọng nói
            text = text.lower()
            print("User: "+text)
            return text
        except: 
            speak("Oops! Lỗi mất rồi :(")  
def gettext():
    for i in range(3): #cho nó nghe 3 lần 
        text = listen()
        if text: 
            return text.lower() #chuyển thành chữ thường cho dễ xử lý
        elif i < 2: #Lần 1 nó ko nghe đc nó sẽ in ra dòng dưới 
            speak("Oops! Tôi không nghe rõ bạn nói. Vui lòng nói lại nha")
        time.sleep(3) #cho chương trình tạm dừng sau 3 giây
        stop()
        
#Hàm chào tạm biệt 
def stop(): 
    speak("Tạm biệt nhé. See you later")

def nhaptkb():
    while True:
        tkb = {
            "Thứ 2":"",
            "Thứ 3":"",
            "Thứ 4":"",
            "Thứ 5":"",
            "Thứ 6":"",
            "Thứ 7":"",
            "Chủ nhật":""
        }
        thu = '2'
        for i in range (2,9):
            if str(i) in thu: 
                tkb[f'Thứ {i}'] = str(input(f"Mời nhập thời khóa biểu của ngày thứ {i}:")).split(" ")
            
    



    