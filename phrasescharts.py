# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pickle
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import jieba
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
# import codecs

# fin = codecs.open('HotelComments.txt',mode = 'r', encoding = 'utf-8')
# print fin.read()

# 第一次运行程序时将分好的词存入文件
# text = ''
# with open('HotelComments.txt') as fin:
#     for line in fin.readlines():
#         line = line.strip('\n')
#         text += ' '.join(jieba.cut(line))
#         text += ' '
# fout = open('text.txt','wb')
# pickle.dump(text,fout)
# fout.close()

# 直接从文件读取数据
fr = open('responsibility.txt','rb')
responsibility = fr.read()

# 结巴分词
wordlist = jieba.cut(responsibility)
wl = " ".join(wordlist)


#print(wl)#输出分词之后的txt

backgroud_Image = plt.imread('bear.jpg')
wc = WordCloud( #设置字体，不指定就会出现乱码
        font_path='C:/Windows/Fonts/msyh.ttf',
        #font_path=path.join(d,'simsun.ttc'),
        #设置背景色
        background_color='white',
        #词云形状
        mask=backgroud_Image,
        #允许最大词汇
        max_words=200,
        #最大号字体
        max_font_size=200
                )
wc.generate(responsibility)
image_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func = image_colors)
plt.imshow(wc)
plt.axis('off')
plt.show()

