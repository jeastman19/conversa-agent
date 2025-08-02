from app.chat.domain.message import Message

class HumanAttentionClassifier:
    @staticmethod
    def requires_human(message: Message) -> bool:
        # Clasificación rudimentaria (se mejorará luego)
        keywords = ["quiero hablar", "asesor", "humano"]
        return any(kw in message.text.lower() for kw in keywords)
