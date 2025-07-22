from chatterbot import ChatBot

BOT_NAME = "Govbot"
MIN_CONFIDENCE = 0.65

def initialize_bot():
    initialized, bot = False, None

    try:
        bot = ChatBot(BOT_NAME, read_only=True, logic_adapters=[{
            "import_path": "chatterbot.logic.BestMatch"
        }])
        initialized = True
    except Exception as e:
        print(f"Erro inicializando o {BOT_NAME}: {str(e)}")
        
    return initialized, bot

def get_response(bot, message):
    response = bot.get_response(message.lower())
    return response.text, response.confidence

def run_bot(bot):
    print(f"Olá, sou o Govbot, assistente virtual de serviços públicos. Posso ajudar você com informações sobre documentos, benefícios e como acessar serviços do governo. Como posso te ajudar hoje?")

    while True:
        response, confidence = get_response(bot)

        if confidence >= MIN_CONFIDENCE:
            print(f"{response} [confiança: {confidence:.2f}]")
        else:
            print(f"Ainda não sei responder essa pergunta. Para mais informações, acesse o Portal Gov.br em https://www.gov.br [confiança: {confidence:.2f}]")

if __name__ == "__main__":
    initialized, bot = initialize_bot()
    if initialized:
        run_bot(bot)
