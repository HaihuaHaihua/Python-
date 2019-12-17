'''
Match对象的属性
    .string 待匹配的文本
    .re 匹配时使用的pattern对象（正则表达式）
    .pos 正则表达式搜索文本的开始位置
    .endpos 正则表达式搜索文本的结束位置

Match对象的方法
    .group()   0获取匹配后的字符串
    .start() 匹配字符串的原始字符串的开始位置
    .end() 匹配字符串的原始字符串的结束位置
    .span() 返回(.start(), .end())  开始和结束两个位置

贪婪匹配：返回最大匹配 （r'PY.*N','PYANBNCNDN'）
最小匹配： (r'PY.*?N','PYANBNCNDN')   *？ +？ ？？ {m,n}?  4种方法都可以获得最小匹配
'''
import re
m = re.search(r'[1-9]\d{5}','BIT100081 TUS100084')
print(m.string)
print(m.re) #compile后的字符串组才是正则表达式
print(m.pos)
print(m.endpos)
print(m.group(0)) #match对象 返回第一次匹配的结果
print(m.start())
print(m.end())
print(m.span())

match =re.search(r'PY.*N','PYANBNCNDN')
if match:
    print(match.group(0))

match2 =re.search(r'PY.*?N','PYANBNCNDN')
if match2:
    print(match2.group(0))
