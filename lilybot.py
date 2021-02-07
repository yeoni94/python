'''
* 탤래그램 챗봇 만들기
1. 텔레그램 가입
https://web.telegram.org
2. @BotFather 찾아 추가
텔레그램에서 챗봇의 기본적인 설정을 도와주는 텔레그램 봇
3. /newbot 채팅창에 입력
4. 봇 이름 채팅창에 입력: lily94_bot
5. 내 봇에 대한 http api token 제공해줌
1566291523:AAHs8dH53uVRc8TmIOokhCaLEypzrM2QS5Q
6. 터미널에서 pip install python-telegram-bot --upgrade 설치
7. 핸드폰에서 lilybot에게 ‘테스트메시지’ 입력
8. lilybot.py 실행
{'message_id': 4, 'date': 1612610967, 'chat': {'id': 1661004061, 'type': 'private', 'first_name': 'Gayeon', 'last_name': 'Kim'}, 'text': '테스트메시지', 'entities': [], 'caption_entities': [], 'photo': [], 'new_chat_members': [], 'new_chat_photo': [], 'delete_chat_photo': False, 'group_chat_created': False, 'supergroup_chat_created': False, 'channel_chat_created': False, 'from': {'id': 1661004061, 'first_name': 'Gayeon', 'is_bot': False, 'last_name': 'Kim', 'language_code': 'ko'}}
-> 대화 아이디 1661004061 확인
9. 봇기능 만들어주기 : lilybotmodel.py 참고
10. 기능 추가 및 실행 : lilybot_hello.py 참고
'''
import telegram

lily_token = '1566291523:AAHs8dH53uVRc8TmIOokhCaLEypzrM2QS5Q'
lily = telegram.Bot(token = lily_token)
updates = lily.get_updates()
for u in updates:
    print(u.message)