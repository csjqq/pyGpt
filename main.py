import json
import os
#import openai
import requests
import telebot

# 从环境变量中读取 OpenAI API 密钥和 Telegram 机器人令牌
#openai.api_key = os.environ.get('OPENAI_API_KEY', '')
bot_token = os.environ.get('TELEGRAM_BOT_TOKEN', '6815406354:AAGJwCJBi5IaIaFdEO0asm_J1KzFth_Sjbc')

# 设置 OpenAI API 基本 URL
#openai.api_base = "https://chimeragpt.adventblocks.cc/api/v1"

# 初始化 Telegram 机器人
bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "你好！我是由 GPT-3.5 Turbo 驱动的助手。发送消息给我，我会回复你的！")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # 获取用户输入
    user_input = message.text
    response = al(user_input)

    # 调用 GPT-3.5 Turbo API 生成回复
    # response = openai.ChatCompletion.create(
    #     model='gpt-3.5-turbo',
    #     messages=[
    #         {'role': 'user', 'content': user_input},
    #     ]
    # )

    # 提取 AI 的回复
    # ai_response = response['choices'][0]['message']['content']

    # 将 AI 的回复发送回给用户
    # bot.reply_to(message, ai_response)
    c = json.loads(response)
    print(c)
    print(c['result'])
    bot.reply_to(message, c['result'])



API_KEY = "i7aQg3oSQhpCShhyIAeOpLYh"
SECRET_KEY = "2sdpdrK3tIKBDgILjsCqmRGe2PclzYWn"


def al(msg):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": msg
            }
        ],
        "disable_search": False,
        "enable_citation": False
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))

if __name__ == "__main__":

    bot.polling()