from requests import post

WHATSAPP_TOKEN = ""
WHATSAPP_PHONE_NUMBER_ID = "100999242818609"
WHATSAPP_MESSAGING_ENDPOINT = f"https://graph.facebook.com/v15.0/{WHATSAPP_PHONE_NUMBER_ID}/messages"
WHATSAPP_TARGET_PHONE_NUMBER = "919910795695"
WHATSAPP_MESSAGE_TEMPLATE_NAME = "telegram_message"
WHATSAPP_AUTHORIZATION_TOKEN = "EAAJaEUE8gJ4BABpnGFvc1l5jkPiQOYhZAgZBBz7my8IVEwn3cTq5yfDBbVAnIyJUpbyZBDKPvtuZA0AKfBf40fGD1igAQMA5EuGlZAQhAocPZCTgtaZCfh4PZBZBqWzfu48IgqZB5mZCWHhetGaenvciWB1bD4AEUhoH8BK6EuZANf79fZB65vMsbGnZA1"

WHATSAPP_BODY = {
    "messaging_product": "whatsapp",
    "to": WHATSAPP_TARGET_PHONE_NUMBER,
    "type": "template",
    "template": {
        "name": WHATSAPP_MESSAGE_TEMPLATE_NAME,
        "language": { "code": "en_US" }
    }
}


def send_message(message=""):
    post(url=WHATSAPP_MESSAGING_ENDPOINT, json=WHATSAPP_BODY, headers={"Authorization": f"Bearer {WHATSAPP_AUTHORIZATION_TOKEN}"})
