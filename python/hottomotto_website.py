from urllib import request
from bs4 import BeautifulSoup

response = request.urlopen('https://www.hottomotto.com/menu_list/index/13')
soup = BeautifulSoup(response)
response.close()

jstab_wrap = soup.find('div', class_='js-tab__wrap')

cmenu__picts = jstab_wrap.find_all('img', class_="c-menu__pict")
cmenu__titles = jstab_wrap.find_all('p', class_="c-menu__title")

for j in range(len(cmenu__titles)):
	cmenu__titles[j] = cmenu__titles[j].text.rstrip('\n')

cmenu__prices = jstab_wrap.find_all('span', class_="c-menu__price")


f = open('hottomotto_out.txt', mode='w')

for i in range(len(cmenu__titles)):
	f.write('		<div class="contents-item">\n'\
	'			<img src="https://www.hottomotto.com' + cmenu__picts[i].get("src") + '" width="auto" height="200px">\n'\
	'			<p class="product-name">' + cmenu__titles[i] + '</p>\n'\
	'			<p class="place-price">ほっともっと 東大正門前店: ' + cmenu__prices[i].text + '円(税込)</p>\n'\
	'		</div>\n')
f.close()