import re
from collections import Counter
def summ(n1,n2):
    c= sum(range(n1,n2))
    print(str(n1)+'→'+str(n2-1)+'累加等于：'+str(c))
def sumxx(n1,n2):
    s = []
    for i in range(n1,n2):
        s.append(i)
    r= re.findall('\d',str(s))
    # print(len(r))
    a=0
    for s in range(0,len(r)):
        a += int(r[s])
        # print(r[s],a,sep='/',end=' ')
    print (str(n1)+'→'+str(n2-1)+"单个数字相加等于："+str(a),'共有'+str(len(r))+'个数字')
    result = Counter(r)
    # print(result)
    print('其中1有'+str(result['1'])+'个','2有'+str(result['2'])+'个','3有'+str(result['3'])+'个','4有'+str(result['4'])+'个','5有'+str(result['5'])+'个','6有'+str(result['6'])+'个','7有'+str(result['7'])+'个','8有'+str(result['8'])+'个','9有'+str(result['9'])+'个','0有'+str(result['0'])+'个',)
summ(1,101)
sumxx(1,201)
for x in range(0,11):
	print(x,end='/')
print('')
