import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from wikipedia.wikipedia import languages, search
from youtube_search import YoutubeSearch
import pyttsx3

wikipedia.set_lang('vi')       #set từ điển wikipedia thành tiếng việt để tìm những định nghĩa bằng tiếng việt 
language = 'vi'               
#path = ChromeDriverManager().install()  #Khởi tạo trình duyệt Chrome

#chuyển văn bản thành âm thanh 
def speak(text):
    print("Trợ lý ảo: ",text)
    tts = gTTS(text=text,lang=language,slow=False)  #gửi văn bản lên máy chủ google chuyển văn bản thành giọng nói
    tts.save("robot.mp3")   #lưu thành 1 file mp3 có chứa giọng nói của trợ lý ảo 
    playsound.playsound("robot.mp3",True) #chạy file robot.mp3 
    os.remove("robot.mp3")  #chạy xong sẽ xóa file này đi    
    # engine = pyttsx3.init()                 #khởi tạo đối tượng
    # voices = engine.getProperty('voices')   #lấy tất cả mẫu giọng nói có trong máy tính
    # rate = engine.getProperty('rate')       #lấy tốc độ nói
    # volume = engine.getProperty('volume')   #lấy âm lượng

    # engine.setProperty('volumn',volume - 0.0)   #set âm lượng để là âm lượng lớn nhất
    # engine.setProperty('rate',rate-50)          #tốc độ nói bth cho dễ nghe
    # engine.setProperty('voice',voices[1].id)    #chọn giọng nói [1] là giọng của An 
    # engine.say(text)
    # engine.runAndWait()
#speak("Xin chào my friend.")

#chuyển giọng nói thành văn bản
def get_audio():
    print("Trợ lý ảo: Đang nghe |--__--|")
    ear_robot = sr.Recognizer() #Khởi tạo tai nghe 
    with sr.Microphone() as source: #lắng nghe người dùng nói 
        audio = ear_robot.listen(source,phrase_time_limit= 6) #trợ lý ảo sẽ nghe người dùng nói, phrase_time_limit là trợ lý sẽ nghe bạn nói trong bao lâu
        try: 
            text = ear_robot.recognize_google(audio, language='vi-VN')
            print("Tôi: "+text)
            return text
        except:
            print("Trợ lý ảo: Lỗi rồi!...")
            return 0
#get_audio() 

def stop():
    speak("Hẹn gặp lại sau nhé!...")
#stop()

def get_text():
    for i in range(3): #cho nó chạy 3 lần
        text = get_audio()
        if text: 
            return text.lower() #chuyển thành chữ thường cho dễ xử lý 
        elif i < 2: #Nghĩa là lần 1 nó ko nghe đc nó sẽ nghe thêm lần nữa , nếu lần 2 mà ko nghe đc sẽ in ra ở dưới
            speak("Trợ lý ảo không nghe rõ bạn nói. Vui lòng nói lại nha !")
    time.sleep(3) #cho chương trình tạm dừng sau 3 giây
    stop()
    return 0
#print(get_text())

#ham chao
def hello(name):
    day_time = int(strftime("%H")) #lấy giờ 
    if 0 <= day_time < 11:
        speak(f"Chào bạn {name}. Chúc bạn buối sáng tốt lành.")
    elif 11<= day_time < 13:
        speak(f"Chào bạn {name}. Chúc bạn có một buổi trưa vui vẻ.")
    elif 13<=day_time <18:
        speak(f"Chào bạn {name}. Chúc bạn buối chiều tốt lành.")
    elif 18<=day_time<=22: 
        speak(f"Chào bạn {name}. Chúc bạn buối tối tốt lành.")
    elif 22<day_time<24:
        f"Chào bạn {name}. Muộn rồi bạn nên đi ngủ sớm nha."
    else: 
        speak("Thời gian chưa đúng, gặp lỗi. Bạn nên xem lại nha.") 

#ham lay thoi gian
def  get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak(f'Bây giờ là {now.hour} giờ {now.minute} phút {now.second} giây') 
    elif "ngày" in text: 
        speak(f"Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}")
    else:
        speak("Tôi chưa hiểu ý bạn!")
#get_time("ngày")
#chức năng mở app
def open_application(text):
    if "google" in text:
        speak("Mở google")
        os.system('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"')
        #nếu sử dụng system thì trợ lý ảo sẽ đợi mk tắt ứng dụng đi r mới tiếp tục nghe mk nói
        #nếu dùng os.startfile thì sau khi mở nó sẽ nghe mình nói luôn sẽ gây nên rối loạn 
    elif "word" in text: 
        speak("Mở Microsoft Word")
        os.system('"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"')
    else:
        speak("Ứng dụng chưa cài đặt. Vui lòng cài đặt cho tôi để tôi mở nha")
#open_application("word")
def open_website(text):
    reg_ex= re.search('mở (.+)',text) #xử lý câu nói của cta thành đường dẫn mở web
    if reg_ex:
        domain=reg_ex.group(1) #youtube.com gọi là 1 domain
        url ="http://www."+domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        if input("Nếu muốn tiếp tục thì nhấn q:") == "q": #có thể xóa đi 
            pass
        return True
    else:
        return False
#open_website('mở youtube.com')
def open_google_and_search(text):
    search_for = str(text).split("kiếm",1)[1]
    url = f"https://www.google.com/search?q={search_for}"
    webbrowser.get().open(url)
    speak("Đây là thông tin bạn cần tìm")
#open_google_and_search("tìm kiếm spiderman")
def open_google_and_search2():
    speak("Nói thứ bạn cần tìm kiếm.")
    search= str(get_text()).lower()
    url = f"https://www.google.com/search?q={search}"
    webbrowser.get().open(url)
    speak("Đây là thông tin bạn cần tìm.")
def send_email(text):
    speak("Bạn gửi mail cho ai vậy nhỉ ?")
    recipient = get_text()
    if "minh" in recipient:
        speak("Nói cho tôi nội dung email.")
        content = get_text()
        mail = smtplib.SMTP("smtp.gmail.com",587) #dùng để gửi mail
        mail.ehlo()
        mail.starttls()
        mail.login("superquang09@gmail.com","chimto1909")
        mail.sendmail("superquang09@gmail.com",#người gửi
                        "superquang08@gmail.com",str(content).encode("utf-8"))#mã hóa để bảo mật) #người nhận
        mail.close()
        speak("Email của bạn đã được gửi.Bạn kiểm tra lại giúp")
    else: 
        speak("Tôi không hiểu bạn muốn gửi email cho ai ...") 
        
#send_email("aaaaaaa")
def current_weather():
    # speak("Bạn muốn xem thời tiết ở đâu")
    # ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    # city = get_text()
    # if not city:
    #     pass
    # api_key = "fe8d8c65cf345889139d8e545f57819a"
    # call_url = ow_url + "appid" + api_key + "&q=" + city + "&units=metric" #lấy dữ liệu thời tiết trên trang openweathermap 
    # response = requests.get(call_url) #duyệt web mà ko cần trình duyệt 
    # data = response.json() #lấy giữ liệu dưới dạng json , data này có dạng dictionary
    # if data['cod'] != "404": #nếu ko gặp lỗi
    #     city_res = data["main"] 
    #     print(city_res)
    #     current_temperature =city_res["temp"] #lấy nhiệt độ trung bình
    #     current_pressure = city_res["pressure"]#áp suất ko khí
    #     current_humidity = city_res["humidity"]#độ âm
    #     suntime = data["sys"] #mặt trời mọc
    #     sunrise = datetime.datetime.fromtimestamp(suntime['sunrise']) #thời gian mặt trời mọc
    #     sunset = datetime.datetime.fromtimestamp(suntime['sunset'])   #thời gian mặt trời lặn
    #     wthr = data['weather'] #lấy mô tả thông tin thời tiết
    #     weather_description = wthr[0]["description"] 
    #     now = datetime.datetime.now()
    #     content = f"""Hôm nay là ngày {now.day} tháng {now.month} năm {now.year}
    #                   Mặt trời mọc vào{sunrise.hour} giờ {sunrise.minute} phút
    #                   Mặt trời lặn vào{sunset.hour} giờ {sunset.minute} phút
    #                   Nhiệt độ trung bình là {current_temperature} độ 
    #                   Áp suất không khí là {current_pressure}
    #                   Độ ẩm là {current_humidity}%
    #                """
    #     speak(content)
    # else:
    #     speak("Không tìm thấy địa chỉ của bạn")
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data['cod'] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        speak(content)
        time.sleep(28)
    else:
        speak("Không tìm thấy địa chỉ của bạn")
        time.sleep(2)
#current_weather()
def play_youtube():
    speak("Nói nội dung bạn muốn tìm trên Youtube")
    search = get_text()
    url = f"https://www.youtube.com/search?q={search}"
    webbrowser.get().open(url)
    speak("Đây là thứ mà tôi tìm được bạn xem qua nhé")
#play_youtube()
def play_youtube2():
    speak("Nói nội dung bạn muốn tìm trên Youtube")
    search = get_text()
    while True: 
        result = YoutubeSearch(search,max_results=10).to_dict() #max_resutls: lấy tối đa 10 video
        if result:
            break
    url =f"https://www.youtube.com" + result[0]['url_suffix']
    webbrowser.get().open(url)
    speak("Đây là thứ mà tôi tìm được bạn xem qua nhé")
#play_youtube2()
def change_wallpaper():
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
        api_key  # pic from unspalsh.com
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Location where we download the image to.
    urllib2.urlretrieve(photo, "C:\\Users\\dell\\Desktop\\wallpaper\\a.png")
    image=os.path.join("C:\\Users\\dell\\Desktop\\wallpaper\\a.png")
    ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
    speak('Hình nền máy tính vừa được thay đổi')
change_wallpaper()
#change_wallpaper()
def play_music():
    myPATH = r"C:\Users\dell\Desktop\mp3"
    ds = os.listdir(myPATH)
    #print(ds) 1 list
    for i in ds:
        print("Đang phát bài: "+i)
        os.system(myPATH+"\\"+i) 
        print("\nĐã phát xong bài: "+i) 
def tell_me_about():
    try:
        speak("Bạn muốn tìm gì ạ? Hãy nói cho tôi biết.")
        text = get_text()
        contents = wikipedia.summary(text).split('.') #tìm kiếm nội dung mà ng dùng cần tìm kiếm
        speak(contents[0])
        dem=0
        for content in contents[1:]:
            if dem < 2:
                speak("Bạn có muốn biết thêm không?")
                ans = get_text()
                if "có" not in ans:
                    break
            dem += 1
            speak(content)
        speak("Đây là nội dung tôi vừa tìm được!")
    except:
        speak("Không tìm thấy nội dung bạn cần tìm")
#tell_me_about()
def help_me():
    speak("""
    Tôi có thể giúp bạn thực hiện các việc sau đây:
    1. chào hỏi
    2. hiển thị giờ
    3. Mở website, ứng dụng decktop
    4. Tìm kiếm với google
    5. Gửi mail
    6. Dự báo thời tiết
    7. Tìm kiếm video với youtube
    8. Thay đổi hình nền máy tính
    9. Tìm kiếm với wikipedia
    10. Mở nhạc trong máy tính
    """)
#Tao nao cho tro ly ao
def main_brain():
    speak("Xin chào. Bạn tên là gì ?")
    global name
    name = get_text()
    if name:
        speak(f'Xin chào bạn {name}.')
        speak(f"Bạn cần tôi giúp gì?")
        while True:
            text = get_text()
            if not text:
                break
            elif ('tạm biệt' in text) or ('hẹn gặp lại' in text):
                stop()
                break 
            elif ('chào trợ lý' in text):
                hello(name)
            elif ('hiện tại' in text):
                get_time(text)
            elif ('mở' in text):
                if "." in text:
                    open_website(text)
                else:
                    open_application(text)
            elif "tìm kiếm" in text:
                open_google_and_search(text)
            elif("email" in text) or ("mail" in text) or ("gmail" in text):
                send_email(text)
            elif("thời tiết" in text):
                current_weather() 
            elif ("youtube" in text):
                speak("Bạn muốn tìm kiếm đơn giản hay phức tạp")
                yeu_cau = get_text()
                if "đơn giản" in yeu_cau:
                    play_youtube()
                    if input():
                        pass
                elif "phức tạp" in yeu_cau:
                    play_youtube2()
                    if input():
                        pass       
            elif("hình nền" in text):
                change_wallpaper()
            elif("phát nhạc"in text):
                speak("Ok. Tôi bắt đầu mở nhạc nha.")
                play_music()           
            elif("định nghĩa" in text):
                tell_me_about() 
            elif("có thể làm gì" in text):
                help_me()
            else:
                speak(f"Chức năng chưa có. Bạn vui lòng chọn lại chức năng đã có trong menu nha!")
#main_brain()


#Các chức năng có thể thêm 
#đọc thời khóa biểu
#định nghĩa 1 từ tiếng anh 
