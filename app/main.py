import os
import httpx

from fastapi import FastAPI, Request

app = FastAPI()


# WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")  # Token do Meta
# PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")
PHONE_NUMBER_ID = 701219823084846
WHATSAPP_TOKEN = "EAAVLngcZCnwEBPdOf9nKKlOmv9sHglKSQpeWdZBFY03uwwUP45AYU0J1iH9ZBP4Y9zsykWGl6IvjpqGjSMSGhTvAa195SH37K5AlmsJtZCBH9Fe2zcxeaV5l6xFB5iIVaRqhccFGbS3sdCi5XzZAxejOOuGDCAkvOhUCgDCXti2W5F3vZAwJEwMrVjQjsU8tkYYAlsPElqEe9Ac9pjkw8MQuZCYyDh7ZCkP1f6cFoZAdJmEUZCoDB2uZB6pzVKZAyHcZD"
VERIFY_TOKEN ="f@#$%kjkh4857485"

@app.get("/")
async def verify_webhook(request: Request):
    data = request.query_params._dict
    hub_mode = data.get('hub.mode')
    hub_challenge = data.get('hub.challenge')
    hub_verify_token = data.get('hub.verify_token')
    if hub_mode == "subscribe" and hub_verify_token == VERIFY_TOKEN:
        return int(hub_challenge)
    return {"status": "erro", "message": "Token inválido"}

@app.post("/")
async def receive_message(request: Request):
    data = await request.json()
    print("Mensagem recebida:", data)

    try:
        # Pega o texto enviado pelo usuário
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]
        sender = message["from"]
        text = message["text"]["body"]

        print(f"Mensagem de {sender}: {text}")

        # Resposta do chatbot (aqui podemos chamar GPT, regras, etc.)
        reply = f"Você disse: {text}"

        # Enviar resposta de volta
        url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"
        headers = {
            "Authorization": f"Bearer {WHATSAPP_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": sender,
            "type": "text",
            "text": {"body": reply}
        }

        async with httpx.AsyncClient() as client:
            await client.post(url, headers=headers, json=payload)

    except Exception as e:
        print("Erro ao processar mensagem:", e)

    return {"status": "success"}
