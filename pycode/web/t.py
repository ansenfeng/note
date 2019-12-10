#-*- coding: utf-8 -*-
from flask import Flask, render_template, jsonify,request
import pymysql
import requests 
from lxml import etree
app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():
    return render_template('table.html')

@app.route('/tieba/',methods=['GET','POST'])
def tieba():
    return render_template('tieba.html',results=get('历史'),key='历史',key2='')
@app.route('/tieba3/',methods=['GET','POST'])
def tieba3():
    key1 = request.form.get("key1")
    print(key1)
    return render_template('tieba.html',results=get(key1),key=key1,key2=key1)
@app.route('/tieba/<key>', methods=['GET'])
def tieba2(key):
    print (key)
    return render_template('tieba.html',results=get(key),key=key)
@app.route('/test')
def test():
    return render_template('tb2.html')

@app.route('/xiaoqu')
def beike_xiaoqu():
    return render_template('beike_xiaoqu.html')

@app.route('/index_get_data')
def stuff():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql3 = """ select * from test"""
    cursor.execute(sql3)
    resp = cursor.fetchall()
    data={'test1':"1",'test2':'nihao','data':resp}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/index_get_data2')
def stuff2():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql3 = """ select * from beike_1_15 where name not like '%车%';"""
    cursor.execute(sql3)
    resp = cursor.fetchall()
    data={'test1':"1",'test2':'nihao','data':resp}
    cursor.close()
    conn.close()
    return jsonify(data)

@app.route('/index_get_data3')
def stuff3():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql3 = """ select * from fang_xiaoqu_10 """
    cursor.execute(sql3)
    resp = cursor.fetchall()
    data={'test1':"1",'test2':'nihao','data':resp}
    cursor.close()
    conn.close()
    return jsonify(data)

def get(key):
    for  i in range(0,150,50):
        tlist=[]
        jieguo=[]
        url='https://tieba.baidu.com/f?kw={}&ie=utf-8&pn='.format(key)
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }
        tlist.clear()
        response = requests.get(url+str(i))
        responsed =response.text
        htm = etree.HTML(responsed)
        title = htm.xpath('//*[@id="thread_list"]/li/div/div/div/div/a/text()')
        hot = htm.xpath('//*[@id="thread_list"]/li/div/div/span/text()')
        urli = htm.xpath('//*[@id="thread_list"]/li/div/div/div/div/a/@href')
        if len(hot)!=len(title):#减去多余长度
            for x in range(1,len(hot)-len(title)+1):
                hot.pop()

        for i in  urli:#拼接url
            urlq = "https://tieba.baidu.com"+i
            tlist.append(urlq)     
        for re,re2,re3 in zip(title,hot,urli):
            a1=[]
            a1.append(re)
            a1.append(re2)
            a1.append("https://tieba.baidu.com"+re3)
            print(re,re2,re3)
            jieguo.append(a1)
        return jieguo

if __name__ == '__main__':
    app.run(debug=True)