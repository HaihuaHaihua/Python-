'''
正则表达式 用一小段字符串表示一个字符串组 

re.search(pattern,string,flags=0)
  在一个字符串中搜索匹配正则表达式的第一个位置 返回 match对象
  pattern 正则表达式的表示 string或者raw string（raw string 不表示转义符的字符串类型）
  string 需要匹配的对象
  flags 正则表达式使用时的控制标记
      re.I 忽略大小写标记
      re.M 使得正则表达式中的 ^ 操作符 能够从字符串对象的每一行开始匹配
      re.S  使得正则表达式中的 .  操作符  能够匹配所有字符 不调时 不能匹配换行符

re.match(pattern,string,flags=0)
    从一个字符串的开始位置起匹配正则表达式，返回match对象
    pattern 正则表达式的表示 string或者raw string（raw string 不表示转义符的字符串类型）
    string 需要匹配的对象
    flags 正则表达式使用时的控制标记
      re.I 忽略大小写标记
      re.M 使得正则表达式中的 ^ 操作符 能够从字符串对象的每一行开始匹配
      re.S  使得正则表达式中的 .  操作符  能够匹配所有字符 不调时 不能匹配换行符

re.findall(pattren,string,flags=0)
    搜索字符串，以列表类型返回全部能匹配的子串
    pattern 正则表达式的表示 string或者raw string（raw string 不表示转义符的字符串类型）
    string 需要匹配的对象
    flags 正则表达式使用时的控制标记

re.split(pattren,string,maxsplit=0,flags=0)
    将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
    pattern 正则表达式的表示 string或者raw string（raw string 不表示转义符的字符串类型）
    string 需要匹配的对象
    maxsplit 最大分割数，剩余部分作为最后一个元素输出
    flags 正则表达式使用时的控制标记

re.finditer(pattern,string,flags=0)
    搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素都是match对象
    pattern 正则表达式的表示 string或者raw string（raw string 不表示转义符的字符串类型）
    string 需要匹配的对象
    flags 正则表达式使用时的控制标记

re.sub(pattern,repl,string,count=0,flags=0)
    在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
    pattern 正则表达式的表示 string或者raw string（raw string 不表示转义符的字符串类型）
    repl 替换的匹配字符串的字符串
    string 需要匹配的对象
    count 匹配的最大替换次数
    flags 正则表达式使用时的控制标记

regex = re.compile(pattern,flags=0)
    将正则表达式的字符串形式编译成正则表达式对象regex (这里regex表示正则表达式，表示一组字符串)

Re库的多次使用等价用法：面向对象的用法，编译后多次操作
    pat = re.compile(r'[1-9]\d{5}') #编译pattern对象
    rst = pat.search('BIT 100081') #对象调用函数
'''
import re
match = re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))
'''
match1=re.match(r'[1-9]\d{5}','BIT 100081')  #match从字符串起始位置才是搜索 但目标字符串的起始位置不是1-9的数组 返回match为空
if match:
    print(match1.group(0))
'''

match1=re.match(r'[1-9]\d{5}','100081 BIT')
if match1:
    print(match1.group(0))

ls = re.findall(r'[1-9]\d{5}','BIT 100081 TUS 100084')
print(ls)

ls1 = re.split(r'[1-9]\d{5}','BIT 100081 TUS 100084')
print(ls1)
#增加maxsplit 只进行一次分割
ls2 = re.split(r'[1-9]\d{5}','BIT 100081 TUS 100084',maxsplit=1)
print(ls2)

#迭代的获得每一次匹配结果并进行单独处理
for m in re.finditer(r'[1-9]\d{5}','BIT100081 TUS100084'):
    if m:
        print(m.group(0))

string1=re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TUS100084')
if string1:
    print(string1)

print("\n面向对象的使用方法")
pat = re.compile(r'[1-9]\d{5}')

match2 = pat.search('BIT100081')
if match2:
    print(match2.group(0))

match3 = pat.match('100084TUS')
if match3:
    print(match3.group(0))

ls3 = pat.findall('BIT100081 100084TUS')
print(ls3)

ls4 = pat.split('BIT100081 100084TUS',maxsplit=1)
print(ls4)

for m in pat.finditer('BIT100081 100084TUS'):
    if m:
        print(m.group(0))

string2 = pat.sub(':zipcode','BIT100081 100084TUS',count=1)
print(string2)
