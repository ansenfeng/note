# note
python学习笔记</br>
github创建文件夹方法 create new file +"/"+一个文件

# 正则表达式
+ import re
+ str1 = '123第一556，第二，855元。甲方人员和乙方人员,甲1乙,甲a乙甲c乙'
+ str2 = 'reerab11ab22abc33bc'
	+a.b a..b a...b a....b,包含前后字符，点代表一个字符。不包含换行符号
	+ \d 任意数字 a\db
	+ \w 任意字符 a\wb
	+ \s
	+ (*)修饰前面的字符，出现无数次。>=0次
	+ (+)修饰前面的字符，>=1次
	+ (?)修饰前面的字符，<=1次，0或者1次
	+ ab*?  前面字符最少匹配
	+ [1-9][a-z],1到9 a到z。如果需要匹配横线，使用转义字符[a\-z],上尖括号取反[^a-z]
	+  ^ 匹配开头，如'^张'
	+ $结尾，从后往前匹配，如'com$'
	+ re.search('<tr>(.*?)</tr>',str3)# 只取括号内容
	+ ^.{3,4}$ 只包含三个字符 花括号次数。3到4次
	+ re.search('^[0-9]{3,4}-[0-9]{7,9}$','135-1234567',re.S)  检测是否电话号
	+ re.search('^http//www\.(.*?)\.com$','http//www.baidu.com')  只取括号部分
	+ print(r.group()) 结果例子
	
# python

+ format
	+ print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
	+ print("网站名：{}, 地址 {}".format("菜鸟教程", "www.runoob.com"))
	+ 等价 
	+ format 还可以使用字典和列表。
	+ 列出目录列表
	+ import os
	+ print(os.listdir(r'/Library/WebServer/Documents/07'))
	
+ print
	+ print两个参数 sep 间隔，end结尾 
	+ print(a,b,c,sep='......')
	+ print(x,y,z,end='\n')
+ 数据切片
	+ str = ‘0123456789’
	+ print str[0:3] #截取第一位到第三位的字符
	+ print str[:] #截取字符串的全部字符
	+ print str[6:] #截取第七个字符到结尾
	+ print str[:-3] #截取从头开始到倒数第三个字符之前
	+ print str[2] #截取第三个字符
	+ print str[-1] #截取倒数第一个字符
	+ print str[::-1] #创造一个与原字符串顺序相反的字符串
	+ print str[-3:-1] #截取倒数第三位与倒数第一位之前的字符
	+ print str[-3:] #截取倒数第三位到结尾
	+ print str[:-5:-3] #逆序截取，具体啥意思没搞明白？
	
+ if __name__ == '__main__':#判断是否自己，自己文件是运行，被引入时不执行。
	
	+ print(locals()) 局部变量
	+ print(globals()) 全局变量
