import json

import requests

from config.config import IMEI_TOKEN, URL
from lexicon.lexicon import LEXICON_USER


async def response_to_imei(imei):
    """Запрос к сервису проверки IMEI"""
    headers = {
        "Authorization": "Bearer " + IMEI_TOKEN,
        "Content-Type": "application/json"
    }
    body = json.dumps({
        "deviceId": str(imei),
        "serviceId": 12
    })

    response = requests.post(URL, headers=headers, data=body)
    if response.status_code == 201:
        return response.json()
    else:
        return


async def check_imei_and_return_info(imei):
    """Проверка IMEI и возврат информацию о IMEI"""
    data = await response_to_imei(imei)

    if data:
        text = ""
        for key, value in data["properties"].items():
            text += f"{key}: {value}\n"
        return text
    else:
        return f"{LEXICON_USER["server_error"]}"
