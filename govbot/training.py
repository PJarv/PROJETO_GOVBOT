from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json

BOT_NAME = "Govbot"

TRAINING_FILES = [
    "./conversas/saudacoes.json",
    "./conversas/servicos_publicos.json",
    "./conversas/informacoes_basicas.json"
]

def initialize_bot():
    try:
        bot = ChatBot(BOT_NAME)
        trainer = ListTrainer(bot)
        return True, trainer
    except Exception as e:
        print(f"Error initializing trainer: {str(e)}")
        return False, None

def load_conversations():
    conversations = []
    try:
        for file_path in TRAINING_FILES:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                conversations.append(data["conversas"])
        return True, conversations
    except Exception as e:
        print(f"Error loading conversations: {str(e)}")
        return False, []

def train_bot(trainer, conversations):
    for topic in conversations:
        for item in topic:
            for question in item["mensagens"]:
                print(f"Training: {question} -> {item['resposta']}")
                trainer.train([question.lower(), item["resposta"]])

if __name__ == "__main__":
    initialized, trainer = initialize_bot()
    if initialized and trainer:
        loaded, data = load_conversations()
        if loaded:
            train_bot(trainer, data)
