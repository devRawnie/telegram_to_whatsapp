import json

from requests import post
from time import sleep

config = {}
with open("./config.json", "r") as f:
    config = json.load(f).get("whatsapp", {})

WHATSAPP_PHONE_NUMBER_ID = config.get("WHATSAPP_PHONE_NUMBER_ID", None)
WHATSAPP_TARGET_PHONE_NUMBERS = config.get("WHATSAPP_TARGET_PHONE_NUMBERS", [])
WHATSAPP_MESSAGE_TEMPLATE_NAME = config.get("WHATSAPP_MESSAGE_TEMPLATE_NAME", None)
WHATSAPP_AUTHORIZATION_TOKEN = config.get("WHATSAPP_AUTHORIZATION_TOKEN", None)

if any([
    WHATSAPP_PHONE_NUMBER_ID is None,
    WHATSAPP_MESSAGE_TEMPLATE_NAME is None,
    WHATSAPP_AUTHORIZATION_TOKEN is None,
    len(WHATSAPP_TARGET_PHONE_NUMBERS) == 0
    ]):
    exit()

WHATSAPP_MESSAGING_ENDPOINT = config.get("WHATSAPP_MESSAGING_ENDPOINT", "https://graph.facebook.com/v15.0/{phone_number_id}/messages").format(phone_number_id=WHATSAPP_PHONE_NUMBER_ID)

def get_whatsapp_message_body(phone_number, message):
    return  {
        "messaging_product": "whatsapp",
        "to": phone_number,
        "type": "template",
        "template": {
            "name": WHATSAPP_MESSAGE_TEMPLATE_NAME,
            "language": { "code": "en_US" },
            "components": [
                {
                    "type": "body",
                    "parameters": [
                        {
                            "type": "text",
                            "text": message
                        }
                    ]
                }
            ]
        }
    }


def send_message(message="<test-message>"):
    for phone_number in WHATSAPP_TARGET_PHONE_NUMBERS:
        WHATSAPP_BODY = get_whatsapp_message_body(phone_number, message)

        attempts = 5
        while attempts > 0:
            try:
                response = post(
                    url=WHATSAPP_MESSAGING_ENDPOINT,
                    json=WHATSAPP_BODY,
                    headers={
                        "Authorization": f"Bearer {WHATSAPP_AUTHORIZATION_TOKEN}"
                    }
                )
                print(response.json())

                if not response.ok:
                    raise Exception("Response not ok")

                break

            except Exception as e:
                print("Error: ", e)
                attempts -= 1

                sleep(2)
