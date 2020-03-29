import jieba
txt = open("PATH","r",encoding="utf-8").read()
excludes = {'我'}#需要排除的词汇
words = jieba.lcut(txt)
counts ={}
for word in words:
    if len(word)==1:
        continue
    elif word =="朕" or word== "本人":
        rword= "关朝峰"
    #可以加任意重名指代
    else:
        rword = word
    counts[rword]=counts.get(rword,0)+1

for word in excludes:
    del counts[word]

items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)

for i in range(10):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word,count))