import requests

TOKEN = "f9LHodD0cOJYH8sP72m2pFJE_o24qmn2XStQ0cbFAhOO_6xjZ0bR3H-whqxJYNT8tEGc6o8YfnIQC06tYyRM"
BASE_URL = "https://platform-api.max.ru"

async def on_message(data):
    print(f"Получен вебхук: {data}")
    
    update_type = data.get('update_type')
    
    if update_type == 'message_created':
        msg = data.get('message', {})
        chat_id = msg.get('recipient', {}).get('chat_id')
        text = msg.get('body', {}).get('text', '')
        
        if chat_id and text:
            send_message(chat_id, f"✅ Ты написал: {text}")
    
    elif update_type == 'bot_started':
        chat_id = data.get('chat_id')
        if chat_id:
            send_message(chat_id, "👋 Привет! Я бот!")

def send_message(chat_id, text):
    url = f"{BASE_URL}/messages?chat_id={chat_id}"
    headers = {
        "Authorization": TOKEN,
        "Content-Type": "application/json"
    }
    data = {"text": text}
    
    try:
        r = requests.post(url, json=data, headers=headers)
        print(f"Ответ MAX: {r.status_code} - {r.text}")
        return r.status_code == 200
    except Exception as e:
        print(f"Ошибка: {e}")
        return False