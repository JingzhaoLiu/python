# 引入string模块 string.punction 包含所有标点符号
import string
path = "D:\python3\pratice\Walden.txt"

with open(path, 'r') as text:
    # strip(string.punction 去除所欲标点符号
    # strip(string.punction).lower() 把所有字母大写变成小写
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    # 创建一个无序的set，并且去除重复
    words_index = set(words)
    counts_dict = {index: words.count(index) for index in words_index}
for word in sorted(counts_dict, key=lambda x: counts_dict[x], reversed=True):
    print("{}--{} times".format(word, counts_dict[word]))



# import string
# '''
# 瓦尔登湖文本的词频统计。
# '''
# file = 'Walden.txt'

# with open(file, 'r', encoding='utf-8') as text:
#     words = [
#         word.strip(string.punctuation).lower() for word in text.read().split()
#     ]
#     reset_word = set(words)
#     word_dict = {word: words.count(word) for word in reset_word}

# for word in sorted(word_dict, key=lambda x: word_dict[x], reverse=True):

#     print('{:10} is {:5} times'.format(word, word_dict[word]))
#     # print('%-10s  is %-5d  times' % (word, word_dict[word]))

#     break
