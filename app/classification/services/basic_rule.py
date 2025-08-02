from app.chat.domain.message import Message
from app.classification.ports.classifier import AttentionClassifier

class BasicRuleClassifier:
    @staticmethod
    def requires_human(message: Message) -> bool:
        keywords = ["humano", "asesor", "quiero hablar", "atención"]
        return any(kw in message.text.lower() for kw in keywords)


# Inyectamos la implementación al clasificador
AttentionClassifier.requires_human = BasicRuleClassifier.requires_human
