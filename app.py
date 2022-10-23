import json
import re
import requests

from flask import Flask, request
from whatsapp_handler import send_message

config = {}
with open("./config.json", "r") as f:
    config = json.load(f).get("telegram", {})

TELEGRAM_BOT_TOKEN = config.get("TELEGRAM_BOT_TOKEN", None)
if TELEGRAM_BOT_TOKEN is None:
    exit()

TELEGRAM_WEBHOOK_REGISTRATION_URL = config.get("TELEGRAM_WEBHOOK_REGISTRATION_URL", "https://api.telegram.org/bot{token}/setWebhook?url={url}")

def sanitize_body(text):
    space_regex = re.compile("\s{4, }")
    text = space_regex.sub("", text)
    return text.replace("\n", ",,,,,,,,,,,")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return "Hello World"

    if request.method == "POST":
        response = request.get_json()
        print(response)

        message_body = response.get("message", {}).get("text", None)
        if message_body is not None:
            send_message(sanitize_body(message_body))

    return 'Invalid Request'


@app.route("/set-webhook", methods=['GET'])
def set_webhook():
    endpoint = request.args.get("endpoint", None)
    if endpoint is None:
        return "ERROR: `endpoint` parameter is required"

    # Register webhook
    REQUEST_URL = TELEGRAM_WEBHOOK_REGISTRATION_URL.format(token=TELEGRAM_BOT_TOKEN, url=endpoint)
    response = requests.get(REQUEST_URL)

    if not response.ok:
        return "There was an error registering the URL " +  endpoint +  ": <pre>" + response.json() + "</pre>"

    return "Registered URL: " + endpoint


config = {}
with open("./config.json", "r") as f:
    config = json.load(f).get("flask", {})

PORT = config.get("PORT", 5000)
HOST = config.get("HOST", "0.0.0.0")

if __name__ == '__main__':
   app.run(host=HOST, port=PORT, debug=True)
