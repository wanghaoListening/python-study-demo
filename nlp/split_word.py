import jieba

with open('/Users/didi/paper_code/天龙八部.txt', errors='ignore', encoding='utf-8') as fp:
   lines = fp.readlines()
   for line in lines:
       seg_list = jieba.cut(line)
       with open('/Users/didi/paper_code/分词后的天龙八部.txt', 'a', encoding='utf-8') as ff:
           ff.write(' '.join(seg_list)) # 词汇用空格分开

