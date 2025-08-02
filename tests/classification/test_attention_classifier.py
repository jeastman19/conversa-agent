import pytest
from app.chat.domain.message import Message
from app.classification.ports.classifier import AttentionClassifier


@pytest.mark.parametrize(
    "text,expected",
    [
        ("Quiero hablar con un asesor", True),
        ("Necesito atención urgente", True),
        ("Hola, cómo están?", False),
        ("Me ayudan con un producto?", False),
    ]
)
def test_attention_classifier_basic_rule(text: str, expected: bool):
    message = Message(text=text)
    result = AttentionClassifier.requires_human(message)
    assert result == expected
