# from PyDictionary import PyDictionary

# dic = PyDictionary()
# word="Home"
# meaning = dic.meaning(word)
# for i in meaning:
#     print(f'{i}={meaning[i]}')
#     print("")


from PyDictionary import PyDictionary
dict = PyDictionary()
word = "apple"
mean = dict.meaning(word)
print(mean)