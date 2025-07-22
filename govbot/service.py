from govbot import initialize_bot, get_response, BOT_NAME
from flask import Flask, Response
import json

app = Flask(BOT_NAME)
initialized, bot = initialize_bot()

@app.get("/response/<string:message>")
def answer(message):
    response_text, confidence = get_response(bot, message)
    response = {
        "response": response_text,
        "confidence": confidence
    }
    return Response(json.dumps(response), status=200, mimetype="application/json")

if __name__ == "__main__":
    if initialized:
        app.run(host="0.0.0.0", port=6000, debug=True)
    else:
        print("Govbot falhou.")
