from pypinyin import pinyin
#print 汉字, the characters in Chinese
def 汉语拼音(user_input):
    汉字 = pinyin(user_input, heteronym=True)
    for i in range(len(汉字)):
        print(汉字[i])  # print the pinyin characters one by one
    return(汉字)  # the entire word