import sys
import lilybotmodel
#pip install requests
#pip install BeautifulSoup4
import requests
from bs4 import BeautifulSoup

def proc_hello(bot, update):
   lily.sendMessage('안녕 나는 릴리봇이야!')


def show_music_rank(bot, update):
   header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
   addr = 'https://www.melon.com/chart/index.htm'
   melon = requests.get(addr, headers=header)
   soup = BeautifulSoup(melon.text, 'html.parser')

   titles = soup.select('* > td > div > div > div.ellipsis.rank01 > span > a')
   artist = soup.select('* > td > div > div > div.ellipsis.rank02 > span')
   lily.sendMessage('실시간 멜론 차트\n'
                   + '1위: ' + titles[1].text + " - " + artist[1].text + '\n'
                   + '2위: ' + titles[2].text + " - " + artist[2].text + '\n'
                   + '3위: ' + titles[3].text + " - " + artist[3].text + '\n'
                   + '4위: ' + titles[4].text + " - " + artist[4].text + '\n'
                   + '5위: ' + titles[5].text + " - " + artist[5].text + '\n'
                   + '6위: ' + titles[6].text + " - " + artist[6].text + '\n'
                   + '7위: ' + titles[7].text + " - " + artist[7].text + '\n'
                   + '8위: ' + titles[8].text + " - " + artist[8].text + '\n'
                   + '9위: ' + titles[9].text + " - " + artist[9].text + '\n'
                   + '10위: ' + titles[10].text + " - " + artist[10].text + '\n'
                   )

lily = lilybotmodel.BotLily() #봇 객체 선언
lily.add_handler('hello', proc_hello) #hello 명령어 입력되면 proc_hello 함수 실행
lily.add_handler('music', show_music_rank)
lily.start() #봇시작