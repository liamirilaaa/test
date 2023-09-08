meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "шутка",
            "ЩИЩ": "одобрение или восторг",
            "КРИПОВЫЙ": "страшный, пугающий",
            "АГРИТЬСЯ": "злиться"
}
#start
print('Приветсвуем в словаре странных слов для чайников!!')
#word checking
for i in range (6):
    word = input("Введите непонятное слово (большими буквами!): ")
    if word in meme_dict.keys():
        definition = meme_dict[word]               #NOTE: a way to get definition from the dictionary
        print('Значение слова:', definition)
    else:
        print('Извините, я не знаю такого слова...')
