import sys
import lilybotmodel

def proc_hello(bot, update):
   lily.sendMessage('안녕 나는 릴리봇이야!')

lily = lilybotmodel.BotLily() #봇 객체 선언
lily.add_handler('hello', proc_hello) #hello 명령어 입력되면 proc_hello 함수 실행
lily.start() #봇시작