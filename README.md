# note
python学习笔记</br>
github创建文件夹方法 create new file +"/"+一个文件

##正则表达式；
+import re
+str1 = '123第一556，第二，855元。甲方人员和乙方人员,甲1乙,甲a乙甲c乙'
+str2 = 'reerab11ab22abc33bc'
  +a.b a..b a...b a....b,包含前后字符，中间的点代表一个字符。不包含换行符号
  + \d 任意数字 a\db
  + \w 任意字符 a\wb
  +*  修饰前面的字符，出现无数次。>=0次
  ++  修饰前面的字符，>=1次
  +？ 修饰前面的字符，<=1次，0或者1次
  + + ab*?  前面字符最少匹配
  +[1-9][a-z],1到9 a到z。如果需要匹配横线，使用转义字符[a\-z],上尖括号取反[^a-z]
  +  ^ 匹配开头，如'^张'
  + $结尾，从后往前匹配，如'com$'
re.search('<tr>(.*?)</tr>',str3)# 只取括号内容
	^.{3,4}$ 只包含三个字符 花括号次数。3到4次
re.search('^[0-9]{3,4}-[0-9]{7,9}$','135-1234567',re.S)  检测是否电话号
re.search('^http//www\.(.*?)\.com$','http//www.baidu.com')  只取括号部分

