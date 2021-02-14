from flask import Flask, request, jsonify
import sys

app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)


@app.route('/message', methods=['GET'])
def Message():
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    if content == u"신남":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "",
                                    "description": "신나는 오늘 입안에서 톡톡 튀는 빼빼로팝 어떠세요?"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"우울":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "",
                                    "description": "우울한 오늘 부드러 버터링이 당신에게 위로가 될꺼예요."
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"짜증":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "",
                                    "description": "짜증난 오늘 달콤한 딸기웨하스 먹고 기분 푸세요~"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"화남":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type": "basicCard",
                            "items": [
                                {
                                    "title": "",
                                    "description": "화나는 오늘 매콤한 쫄병스낵 먹고 스트레스 날려요!!!"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    else:
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": "저는 과자 추천 봇입니다. 오늘의 기분에 따른 과자를 추천해줍니다.\n"
                                    +"당신의 기분을 알려주세요.(신남, 우울, 짜증, 화남)"
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0')