import telegram
from telegram.ext import Updater, CommandHandler

#기초 클래스 생성
class TelegramBot:
    #초기화 함수
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 1661004061
        self.name = name
    #메세지 보내는 함수
    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)
    #종료 함수
    def stop(self):
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

#기초 클래스를 기반으로 시작 함수를 포함한 내 챗봇 작성
class BotLily(TelegramBot):
    def __init__(self):
        self.token = '1566291523:AAHs8dH53uVRc8TmIOokhCaLEypzrM2QS5Q'
        TelegramBot.__init__(self, 'lily', self.token)
        self.updater.stop()

    def add_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def start(self):
        self.sendMessage('릴리 봇이 시작됩니다.')
        self.updater.start_polling()
        self.updater.idle()

