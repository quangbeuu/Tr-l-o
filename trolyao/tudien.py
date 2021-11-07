import numpy as np 
import os
import json 
database = {
    'home': 'ngôi nhà',
    'baby': 'em bé'
}

def show_menu():
    print("CHƯƠNG TRÌNH TỪ ĐIỂN")
    print("1. Thêm từ")
    print("2. Tìm từ")
    print("3. Xóa từ")
    print("4. Xem tất cả từ điển")
    print("0. Thoát chương trình")
#show_menu()
#Hàm thêm từ: 
def addword():
    word = input("Từ mới: ")
    mean = input("Nghĩa là: ")
    database[word] = mean 
    print("Từ mới đã được thêm")
#Hàm tìm từ
def findword():
    word = input("Từ gì")
    if word in database:
        print(f"Tìm thấy: {word}:{database[word]}")
    else:
        print(f"Không tìm thấy từ: {word}")
def delete():
    word = input("Từ gì: ")
    if word in database:
        del database[word]
        print(f"Từ {word} đã bị xóa")
    else:
        print(f"Không tìm thấy từ: {word}")
def viewall():
    lst=[]
    for word,mean in database.items():
         lst.append(word)
    print(lst)
viewall()
# def savedic():
    # np.save("mydictionary.npy",database)
    # with open("mydictionary.txt",'w',encoding='utf-8') as file:
    #      file.write(json.dumps(database))
    
#     a = open("mydictionary.txt",'w+',encoding='utf-8')
#     a.write(str(database))
#     a.close()
# def loadic():
#     a = open("mydictionary.txt",'r+',encoding='utf-8')
#     b=a.read()
#     print(b)
#     a.close()
#show_menu()
choice = int(input("Bạn chọn option nào:"))
while choice != 0: 
    if choice == 0: 
        break
    elif choice == 1:
        addword()
    elif choice == 2:
        findword()
    elif choice == 3:
        delete()
    # elif choice == 4:
    #     savedic()
    # elif choice == 5:
    #     loadic()
    else: 
        print("Không có lựa chọn này.")
    choice = int(input("Bạn chọn option nào:"))
#show_menu()
# new_dic= np.load("mydictionary.npy",allow_pickle=True).item()
# print(new_dic)
