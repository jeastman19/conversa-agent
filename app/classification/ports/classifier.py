from app.chat.domain.message import Message

class AttentionClassifier:
    @staticmethod
    def requires_human(message: Message) -> bool:
        raise NotImplementedError
