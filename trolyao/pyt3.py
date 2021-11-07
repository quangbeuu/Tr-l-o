# # import pyttsx3

# # engine = pyttsx3.init()                 #khởi tạo đối tượng
# # voices = engine.getProperty('voices')   #lấy tất cả mẫu giọng nói có trong máy tính
# # rate = engine.getProperty('rate')       #lấy tốc độ nói
# # volume = engine.getProperty('volume')   #lấy âm lượng

# # for i in voices:                        #in ra tất cả mẫu giọng nói trong window
# #     print(i)

# # engine.setProperty('volumn',volume - 0.0)   #set âm lượng để là âm lượng lớn nhất
# # engine.setProperty('rate',rate-50)          #tốc độ nói bth cho dễ nghe
# # engine.setProperty('voice',voices[1].id)    #chọn giọng nói [1] là giọng của An 
# # engine.say("1 2 3 4 5 6 7 8 ")
# # engine.runAndWait()

# def current_weather():
#     speak("Bạn muốn xem thời tiết ở đâu ạ.")
#     time.sleep(3)
#     ow_url = "http://api.openweathermap.org/data/2.5/weather?"
#     city = get_text()
#     if not city:
#         pass
#     api_key = "fe8d8c65cf345889139d8e545f57819a"
#     call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
#     response = requests.get(call_url)
#     data = response.json()
#     if data['cod'] != "404":
#         city_res = data["main"]
#         current_temperature = city_res["temp"]
#         current_pressure = city_res["pressure"]
#         current_humidity = city_res["humidity"]
#         suntime = data["sys"]
#         sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
#         sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
#         wthr = data["weather"]
#         weather_description = wthr[0]["description"]
#         now = datetime.datetime.now()
#         content = """
#         Hôm nay là ngày {day} tháng {month} năm {year}
#         Mặt trời mọc vào {hourrise} giờ {minrise} phút
#         Mặt trời lặn vào {hourset} giờ {minset} phút
#         Nhiệt độ trung bình là {temp} độ C
#         Áp suất không khí là {pressure} héc tơ Pascal
#         Độ ẩm là {humidity}%
#         Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
#                                                                            hourset = sunset.hour, minset = sunset.minute, 
#                                                                            temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
#         speak(content)
#         time.sleep(28)
#     else:
#         speak("Không tìm thấy địa chỉ của bạn")
#         time.sleep(2)

# import os 
# myPATH = r"C:\Users\dell\Desktop\mp3"
# ds = os.listdir(myPATH)
# #print(ds) 1 list
# for i in ds:
#     print("Đang phát bài: "+i)
#     os.system(myPATH+"\\"+i) 
#     print("\nĐã phát xong bài: "+i) 

# import re 
# str = "Hôm nay tôi ngủ"
# result = re.search("ngủ",str)
# print(result.group())
# import urllib.request as urllib2
# import json
# import os

# api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
# url = 'https://api.unsplash.com/photos/random?client_id=' + \
# api_key  # pic from unspalsh.com
# f = urllib2.urlopen(url)
# data_json = f.read()
# # print(data_json)
# # print('____________________________________________')
# f.close()
# data_python = json.loads(data_json)
# # print(data_python)
# photo = data_python['urls']['full']
# urllib2.urlretrieve(photo, "C:\\Users\\dell\\Desktop\\wallpaper\\a.png")
# image=os.path.join("C:\\Users\\dell\\Desktop\\wallpaper\\a.png")
# print(image)

import numpy as np 
# Save
dictionary = {
    "Thứ 2": "toán",
    "Thứ 3": "anh"
    }
np.save('my_file.npy', dictionary) 

# Load
read_dictionary = np.load('my_file.npy',allow_pickle='TRUE').item()
print(read_dictionary) # displays "world"