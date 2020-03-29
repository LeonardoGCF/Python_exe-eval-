import jieba
import wordcloud

# txt = "我叫关朝峰，天秤座理工男，对科技感兴趣, 却写不好代码，时常想做梦，一觉起来什么都会了。" #中文需要字体库文件.ttc
txt = "My name is GUAN CHAO FENG Plesae Be kind to me I just want to be a good guy"

w = wordcloud.WordCloud(width=1000,height=800)
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("词云测试.jpg")
