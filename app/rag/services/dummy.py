from app.chat.domain.message import Message
from app.rag.ports.gateway import RAGGateway


class DummyRAGSearch:
    @staticmethod
    async def query(message: Message) -> str:
        return f"🔍 Respuesta automática a: '{message.text}' (RAG simulado)"


# Inyectamos la implementación dummy al gateway
RAGGateway.query = DummyRAGSearch.query
