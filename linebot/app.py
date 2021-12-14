from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage,)
import os 
import botfunction

app = Flask(__name__)

line_bot_api = LineBotApi('fPIHhYO21ITsCUcijGC2LR3BIgSLDAC+bIxusN4quYwqFHtOTemOtfToOPICRBuyQUhpB+MiKqq0bQ4qI5vgR984FhfQRIpTKUke7WYukLDUIHOvSuRvs015AAYeOAbKwwJGBL+hu+MRjTM2MUQLRQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('e55cae005f0c55862dd9dcf8d879929f')
line_bot_api.push_message('Ub7cedf008ee4f256313d7100c0b37919', TextSendMessage(text='你可以開始了'))

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message= text=event.message.text
    if message[0]=='!':
        mesinfo=botfunction.blogadvise(message[1:])
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=mesinfo))
    elif message[0:4] in ['help','Help','HELP']:
        mesinfo=botfunction.helpmes()
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=mesinfo))
    else:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(message))





if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



