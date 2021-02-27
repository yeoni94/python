from flask import Flask, request, jsonify
import sys

app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
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
    elif content == u"편의점":
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
                                    "description": "편의점별 대표 과자를 알려드릴께요. \n어떤 편의점이 궁금하세요?(GS,CU,세븐일레븐)"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"GS":
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
                                    "description": "GS편의점 대표 과자는 다음과 같습니다. \n* GS25 초코렛타 \n* GS25 버터갈릭팝콘 \n* GS25 초코써니볼 \n* GS25 쌀로 만든 고소한 인절미"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"CU":
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
                                    "description": "CU편의점 대표 과자는 다음과 같습니다. \n* CU 초코바나나콘 \n* CU 콘소메맛 팝콘 \n* CU 까르보나라스낵 \n* CU 꼬불이 라면스낵"
                                }
                            ]
                        }
                    }
                ]
            }
        }
    elif content == u"세븐일레븐":
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
                                    "description": "세븐일레븐 대표 과자는 다음과 같습니다. \n* 세븐일레븐 트위스트 \n* 세븐일레븐 씨앗호떡뻥"
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
                            "text": "저는 과자 추천 봇입니다. 오늘의 기분에 따른 과자를 추천해줍니다.\n당신의 기분을 알려주세요.(신남, 우울, 짜증, 화남)"
                        }
                    }
                ]
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0')