import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'cookie': 'global_cookie=0nan95ys3392ucc8tu2dk1gl810jzo2a3jx; global_wapandm_cookie=ti1sntcn4zpveyr7t2pobsw7g18jzo2chze; Integrateactivity=notincludemc; budgetLayer=1%7Ccd%7C2019-09-09%2018%3A02%3A13; lastscanpage=0; __utma=147393320.1892411794.1566561630.1568023254.1568288818.3; __utmc=147393320; __utmz=147393320.1568288818.3.3.utmcsr=search.fang.com|utmccn=(referral)|utmcmd=referral|utmcct=/captcha-940244c3c190c1b55a/; __utmt_t0=1; __utmt_t1=1; __utmt_t2=1; __utmt_t3=1; logGuid=d478b88c-a347-4ced-ba8a-a4d61795b414; g_sourcepage=ehlist; city=cd; unique_cookie=U_bx5xcz30pyu35zv5hi6hv33gh20k0gmnsom*4; __utmb=147393320.10.10.1568288818'
}
htm = requests.get('https://cd.esf.fang.com/house-a0132/',headers=headers)
# soup = BeautifulSoup(htm.text,'html.parser')
info = {}
# info['标题'] = soup.select('.title h1')[0].text.strip()
# info['总价'] = soup.select('.price_esf i')[0].text
# values = soup.select('div .tt')
# keys = soup.select('.tab-cont-right .clearfix .font14')
# del keys[-1]
# i = 0
# length = len(keys)
# while i < length:
#     info[keys[i].text] = values[i].text 
#     i += 1
print(htm.text)