
from html.parser import HTMLParser
import re
import urllib.request
 
import xlwt
import time
 

def find_all_citys():
    response = requests.get('http://www.meituan.com/changecity/')
    if response.status_code == 200:
        results = []
        
        soup = BeautifulSoup(response.text,'html.parser')
        links = soup.select('.alphabet-city-area a')
        for link in links:
            temp = {
            'href' : link.get('href'),
            'name' : link.get_text().strip(),
            }
            results.append(temp)
        
        return results
    else:
        return None
for page in range(1,32):
			print("*" *30)
			url = need['url'] + 'pn' + str(page) +'/'
			# url = 'https://jingzhou.meituan.com/jiehun/b16269/pn1/'
			headers = requests_headers()
			print(url+"开始抓取")
			response = requests.get(url, headers=headers, timeout = 10)
			
			# , allow_redirects=False
			# if response.status_code == 302 or response.status_code == 301:
			# 	raise Exception("30*跳转")
 
			pattern = re.compile('"errorMsg":"(\d*?)"',re.S)
			h_code = re.findall(pattern, response.text) 
			
			if len(h_code) != 0 and  h_code[0] == '403':
				raise Exception("403:错误信息:<!-- -->服务器拒绝请求")
			
			pattern = re.compile('"searchResult"\:(.*?),\"recommendResult\"\:',re.S)
			items = re.findall(pattern, response.text) 
			json_text = items[0] + "}"
			# print(json_text)
			json_data = json.loads(json_text)
			# print(len(json_data['searchResult']))
			if len(json_data['searchResult']) == 0:
				print(url+"未匹配到,列表页抓取完毕")
				print("*" *30)
				update_url_to_complete(need['id'])
				break
			for store in json_data['searchResult']:
				# 创建sql 语句，并执行
				sql = 'INSERT INTO `jiehun_detail` (`url`,`poi_id`, `front_img`, `title`, `address`) \
		        VALUES ("%s","%s","%s","%s","%s")' % (url, store['id'],store['imageUrl'],store['title'],store['address'])
				# print(sql)
				cursor.execute(sql)
 
		        # 提交SQL
				connection.commit()
		update_url_to_complete(need['id'])
		print(url+ "抓取完毕")
		print("*" *30
