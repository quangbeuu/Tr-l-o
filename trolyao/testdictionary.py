# def add():
#     a = open("mydictionary.txt",'r+',encoding='utf-8')
#     dic ={}
#     while True:
#         word = input("Từ mới:")
#         mean = input("Nghĩa là:")
#         dic[word] = mean
#         if (input("Bạn có muốn nhập thêm từ mới không (nếu không nhập k): ")) == "k":
#             break
#     dic.save("mydictionary.txt")
# add()
    
# # while True:
# #     word = input("Từ mới: ")
# #     mean = input("Nghĩa là: ")
# #     database[word] = mean 
# #     print(database) 


# #Import the module
# import wikipedia 

# #Setting language to Vietnamese
# wikipedia.set_lang('vi')

# #printing the sumary
# print(wikipedia.summary("việt nam",sentences=2))

# import os
     
# # Get the current working
# # directory (CWD)
# cwd = os.getcwd()
     
# # Print the current working
# # directory (CWD)
# print("Current working directory:", cwd)

# print(os.listdir())

# print(os.name)

#import os module
# import os

# #Get the list of all files and directories
# #in the roor directory
# filenhac = r"C:\Users\dell\Desktop\mp3"
# ds = os.listdir(filenhac) 

# #Tệp và thư mục trong filenhac
# print(ds)


# import os 
# os.system('"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"')

# Python program to explain os.path.join() method
   
# # importing os module
# import os
    
# # Path
# path = "/home"
 
# #Nối các thành phần đường dẫn khác nhau
# print(os.path.join(path, "User/Public/", "Documents", ""))
 
# # Trong ví dụ trên, cuối cùng
# # thành phần đường dẫn trống
# # nên một dấu phân tách thư mục ('/')
# # sẽ được đặt ở cuối 
# # cùng với giá trị được nối






# import speech_recognition as sr

# ear = sr.Recognizer() 
# with sr.Microphone() as mic: 
#     audio = ear.listen(mic,phrase_time_limit=6) 
#     text = ear.recognize_google(audio,language='vi_VN') 






from gtts import gTTS
import playsound 

text = "Chào cô và các bạn ạ"
sound = gTTS(text=text,lang="vi",slow=False)

sound.save("hi.mp3")

playsound.playsound("hi.mp3")













