from fastapi import APIRouter, Request

router = APIRouter()

@router.post("/whatsapp-webhook")
async def whatsapp_webhook(req: Request):
    body = await req.json()
    user_number = body.get("from")
    message = body.get("body")

    if not user_number or not message:
        return {"reply": "Mensagem inválida."}

    # Por enquanto só retorna eco da mensagem
    return {"reply": f"Mensagem recebida de {user_number}: {message}"}
