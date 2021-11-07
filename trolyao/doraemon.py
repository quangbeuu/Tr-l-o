import datetime
import urllib.request
import webbrowser
import requests
from requests.api import get
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
from PyDictionary import PyDictionary

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
    
def speak2(text):
    print("D.O.R.A.E.M.O.N: ",text)
    engine = pyttsx3.init()                 #khởi tạo đối tượng
    voices = engine.getProperty('voices')   #lấy tất cả mẫu giọng nói có trong máy tính
    rate = engine.getProperty('rate')       #lấy tốc độ nói
    volume = engine.getProperty('volume')   #lấy âm lượng

    engine.setProperty('volumn',volume - 0.0)   #set âm lượng để là âm lượng lớn nhất
    engine.setProperty('rate',rate-50)          #tốc độ nói bth cho dễ nghe
    engine.setProperty('voice',voices[0].id)    #chọn giọng nói [1] là giọng của An 
    engine.say(text)
    engine.runAndWait()
#speak2("Xin chào my friend.")

#Hàm chuyển âm thanh thành text
def listen():
    print("D.O.R.A.E.M.O.N: Đang nghe ^-^")
    ear = sr.Recognizer() #Khởi tạo tai cho trợ lý ảo(nhận dạng giọng nói)
    with sr.Microphone() as mic: 
        audio = ear.listen(mic,phrase_time_limit=6) 
        #nghe người dùng nói từ microphone, phrase_time_limit 
        #là thời gian đóng mic(),hay còn gọi là thời gian trợ lý ảo sẽ nghe bạn nói
        try:
            text = ear.recognize_google(audio,language='vi_VN') #Sử dụng google để nhận diện giọng nói
            text = text.lower()
            print("User: "+text)
            return text
        except: 
            speak("Oops!")  
            
#listen()

def gettext():
    for i in range(3): #cho nó nghe 3 lần 
        text = listen()
        if text: 
            return text.lower() #chuyển thành chữ thường cho dễ xử lý
        elif i < 2: #Lần 1 nó ko nghe đc nó sẽ in ra dòng dưới 
            speak("Tôi không nghe rõ bạn nói. Vui lòng nói lại nha")
    time.sleep(3) #cho chương trình tạm dừng sau 3 giây
    stop()
        
#Hàm chào tạm biệt 
def stop(): 
    speak("Tạm biệt nhé. See you later")

#Hàm lấy giờ 
def Time():
    time=datetime.datetime.now().strftime("%I:%M:%S:%p")
    speak("Bây giờ là " + time)
#Time()
#Hàm lấy ngày
def Day():
    d=datetime.datetime.now()
    speak(f"Hôm nay là ngày {d.day} tháng {d.month} năm {d.year}")
#Day()
def hello(name):
    h = datetime.datetime.now().hour
    if 0<= h < 11:
        speak(f"Good morning {name}. Chúc bạn một ngày mới vui vẻ.")
    elif 11<= h <15:
        speak(f"Hi {name}. Ăn trưa ngon miệng nha, tôi đi ăn bánh rán đây.")
    elif 15<= h <19:
        speak(f"Good afternoon {name}. Chúc bạn một buổi chiều an lành.")
    elif 19<= h <22: 
        speak(f"Good night {name}. Chúc bạn một buôi tối vui vẻ.")
    elif 22<= h <24:
        speak(f"Chào {name}. Muộn rồi bạn nên đi ngủ đi thôi.") 
#hello("nhím")
def mo_app(text):
    if "google" in text:
        speak("Để tôi mở google cho bạn.")
        os.system('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"')
        #nếu sử dụng system thì trợ lý ảo sẽ đợi mk tắt ứng dụng đi r mới tiếp tục nghe mk nói
        #nếu dùng os.startfile thì sau khi mở nó sẽ nghe mình nói luôn sẽ gây nên rối loạn 
    elif "word" in text:
        speak("Để tôi mở Microsoft Word cho bạn.")
        os.system('"C:\\Program Files (x86)\\Microsoft Office\\root\\Office16\\WINWORD.EXE"')
    else:
        speak("Sorry. Tôi không thể mở được app này.")
#mo_app("lululu")


def mo_website(text):
    find=re.search("mở (.+)",text) #Thực hiện tìm kiếm chuỗi "mở (.+)" trong text)
    if find: #nếu tìm thấy
        domain = find.group(1) #in ra chữ sau chữ mở(ko in chữ mở)
        url ="http://www." + domain
        webbrowser.open(url)
        speak(f"Tôi đã mở {domain} rồi nha")
        if input("Nếu bạn muốn tiếp tục thì nhấn phím bất kỳ:") :
            pass
#mo_website("mở instagram.com")
def search_information_with_google():
    speak("Tôi có thể tìm kiếm gì cho bạn?")
    infor = str(gettext()).lower()
    url = f"https://www.google.com/search?q={infor}"
    webbrowser.get().open(url)
    speak(f"Đây là thông tin về {infor} trên google nha.")
    if input("Nếu muốn tiếp tục nhấn phím bất kỳ: ") :
        pass
#search_information_with_google()

def weather():
    speak("Bạn muốn xem thời tiết ở thành phố nào thế ?")
    w_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = gettext()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    info_w = w_url + "appid=" + api_key + "&q=" + city +"&units=metric"
    response = requests.get(info_w) #gửi một yêu cầu để lấy thông tin về thời tiết 
    data = response.json() #mã hóa thành json
    #https://api.openweathermap.org/data/2.5/weather?appid=fe8d8c65cf345889139d8e545f57819a&q=H%C3%A0%20N%E1%BB%99i&units=metric
    if data['cod'] != "404":
        city_key = data['main']
        nhietdo = city_key["temp"]
        apsuat = city_key["pressure"]
        doam = city_key["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        now = datetime.datetime.now()
        weatherforecast =  """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {giomoc} giờ {phutmoc} phút
        Mặt trời lặn vào {giolan} giờ {phutlan} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        """.format(day = now.day,month = now.month, year= now.year, giomoc = sunrise.hour, phutmoc = sunrise.minute,
                                                                           giolan = sunset.hour, phutlan = sunset.minute, 
                                                                           temp = nhietdo, pressure = apsuat, humidity = doam)
        speak(weatherforecast)
    else:
        speak("Sorry. Tôi không tìm thấy thông tin về thời tiết của thành phố này.")
#weather()
def search_youtube():
    speak("Bạn muốn xem gì trên youtube?")
    search = gettext()
    url = f"https://www.youtube.com/search?q={search}"
    webbrowser.get().open(url)
    speak(f"Đây là các video về {search} trên youtube.")
    if input("Nếu muốn tiếp tục nhấn phím bất kỳ: "):
        pass
#search_youtube()
#Làm hàm search vào trực tiếp video => làm sau 
def phatnhac():
    filenhac = r"C:\Users\dell\Desktop\mp3"
    ds = os.listdir(filenhac) #in ra danh sách tên file các bài hát
    for i in ds:
        print("Đang phát bài: "+i)
        os.system(filenhac+"\\"+i)
        print("\nĐã phát xong bài: "+i)
    if input("Nếu muốn tiếp tục nhấn phím bất kỳ: "):
        pass
#phatnhac()

def bachkhoatoanthu():
    try:
        speak("Hãy nói cho tôi biết bạn muốn tìm kiếm gì nào ?")
        text = gettext()
        thongtins = wikipedia.summary(text).split(".") #cắt theo từng câu
        speak(thongtins[0])
        for thongtin in thongtins[1:]:
            speak(f"Bạn có muốn biết thêm thông tin về {text} không?")
            ans = gettext()
            if "có" not in ans:
                break
            speak(thongtin)
        speak("Cảm ơn bạn đã sử dụng bách khoa toàn thư :)")
    except:
        speak("Sorry. Tôi không tìm thấy thông tin bạn cần tìm :(")
def wallpaper():
    #https://api.unsplash.com/photos/random?client_id=RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + api_key #link chứa hình ảnh để lấy về 
    f = urllib.request.urlopen(url) #truy cập và dữ liệu hoặc mã nguồn của trang
    data_json = f.read()
    f.close()
    data_python = json.loads(data_json) # chuyển từ json type sang python type (ở đây là chuyển từ object sang dạng dict trong python)
    photo = data_python['urls']['full']
    urllib.request.urlretrieve(photo,"C:\\Users\\dell\\Desktop\\wallpaper\\a.png")
    #Lưu ảnh vào thư mục này
    image=os.path.join("C:\\Users\\dell\\Desktop\\wallpaper\\a.png")
    #trả về đường dẫn ảnh
    ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
    speak("Hình nền máy tính được thay đổi rồi đó!")
#wallpaper()
def dictAnh():
    dict = PyDictionary()
    speak2("What's word you want to find the meaning?")
    word = gettext()
    mean = dict.meaning(word)
    if mean:
        speak2("This is the meaning of your word!!")
        for key in mean:
            speak2(f"Kind of word: {key}")
            speak2(f"Meaning of this word: {mean[key]}")
    else:
        speak2("Sorry. I can't find the meaning of this word")
    if input("Nếu muốn tiếp tục nhấn phím bất kỳ: "):
        pass
#dictAnh()

def supportuser():
    speak("""
    Trong túi thần kỳ của tôi có những bảo bối thần kỳ sau:
    1. Cỗ máy thời gian(cho biết thời gian hiện tại)
    2. Lịch vạn năng (cho biết ngày hôm nay là ngày bao nhiêu)
    3. Cỗ máy chào hỏi (chào bạn mỗi khi bạn chào tôi)
    4. Ứng dụng thần kỳ (mở các ứng dụng có trong laptop)
    5. Website tự động (mở các website)
    6. Google, youtube thông minh (Tìm kiếm thông tin, video với google và youtube)
    7. Dự báo thời tiết (cho biết thời tiết của ngày hôm nay)
    8. Máy phát nhạc diệu kỳ (phát nhạc trong máy tính)
    9. Bách khoa toàn thư (Tìm kiếm thông tin với wikipedia)
    10. Wallpaper ngẫu nhiên (Thay ảnh nền máy tính bằng một hình ảnh ngẫu nhiên)
    11. Từ điển Anh-Anh
    """)
#supportuser()

#Hàm main
def main():
    speak("Xin chào. Bạn tên là gì ?")
    name = gettext()
    if name: 
        speak(f"Chào bạn {name} của tôi!.")
        speak("Để tôi giúp bạn xả stress nhé!")
        speak("Bạn cần tôi giúp gì nào!")
        while True: 
            text = gettext()
            if not text: 
                break
            elif ("tạm biệt" in text) or ("bye bye" in text) or ("hẹn gặp lại" in text):
                stop()
                break
            elif ("giờ" in text):
                Time()
            elif ("ngày"in text):
                Day()
            elif ("chào doraemon" in text) or ("chào bạn" in text):
                hello(name)
            elif ("mở" in text) or ("open" in text):
                if "." in text:
                    mo_website(text)
                else:
                    mo_app(text)
            elif ("tìm kiếm" in text):
                search_information_with_google()
            elif ("thời tiết" in text):
                weather()
            elif ("youtube" in text):
                search_youtube()
            elif ("phát nhạc" in text):
                speak("Tôi bắt đầu mở nhạc nha.")
                phatnhac()
            elif ("định nghĩa" in text) or ("là gì" in text):
                bachkhoatoanthu()
            elif ("help me" in text) or ("có thể là gì" in text) or ("hỗ chợ người dùng" in text):
                supportuser()
            elif ("hình nền" in text) or ("wallpaper" in text):
                wallpaper()
            elif ("từ điển" in text) or ("tra từ" in text) or ("nghĩa của từ" in text):
                dictAnh()
            else:
                speak("Sorry. Tôi vẫn chưa thể làm được việc này, mong bạn thông cảm, tôi sẽ cố gắng khắc phục trong thời gian sớm nhất")
main()

#Ý tưởng 
# -Tạo một thời khóa biẻu
# -Tạo một chương trình học từ vựng 
# -Tạo một app nghe lời bài hát mà ra tên bài hát (Shazam)
# -Tạo từ điển Anh-Việt            