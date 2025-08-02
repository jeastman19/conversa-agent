from app.chat.ports.rag_gateway import RAGGateway
from app.classification.ports.classifier import AttentionClassifier
from adapters.outbound.rag_stub import dummy_rag_search
from app.chat.domain.message import Message


async def handle_user_message(text: str) -> str:
    message = Message(text=text)

    # Clasificación: ¿requiere humano?
    if AttentionClassifier.requires_human(message):
        return "Derivando a un operador humano... 🚶‍♂️"

    # Búsqueda RAG (stub)
    response = await RAGGateway.query(message)
    return response
