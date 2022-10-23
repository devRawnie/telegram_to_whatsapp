from requests import post
from time import sleep

WHATSAPP_PHONE_NUMBER_ID = "100999242818609"
WHATSAPP_MESSAGING_ENDPOINT = f"https://graph.facebook.com/v15.0/{WHATSAPP_PHONE_NUMBER_ID}/messages"
# WHATSAPP_TARGET_PHONE_NUMBER = "919910795695"
WHATSAPP_TARGET_PHONE_NUMBER = "918700486627"
WHATSAPP_MESSAGE_TEMPLATE_NAME = "telegram_message"
WHATSAPP_AUTHORIZATION_TOKEN = "EAAJaEUE8gJ4BAFjRbACzxQoSZBWM5jAS2SCz2MuKnwDm0YdsJYSoNYzjX1V7M1IOhcliG9oTIChrycccruusdqNkq7WgXBdTFblnIrZAWpSeC1bZBp49qlgrxiQGZCchETzKchGdZBGt1fi0VgnmbbvNKmLEtjUWZCQR63tlbde6FSKyAaLMdc"

def get_whatsapp_message_body(message):
    return  {
        "messaging_product": "whatsapp",
        "to": WHATSAPP_TARGET_PHONE_NUMBER,
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
    WHATSAPP_BODY = get_whatsapp_message_body(message)

    attempts = 5
    while attempts > 0:
        try:
            response = post(url=WHATSAPP_MESSAGING_ENDPOINT, json=WHATSAPP_BODY, headers={"Authorization": f"Bearer {WHATSAPP_AUTHORIZATION_TOKEN}"})
            print(response.json())

            if not response.ok:
                raise Exception("Response not ok")

            break

        except Exception as e:
            print("Error: ", e)
            attempts -= 1

            sleep(2)
