from app.chat.domain.message import Message


class RAGGateway:
    @staticmethod
    async def query(message: Message) -> str:
        raise NotImplementedError
