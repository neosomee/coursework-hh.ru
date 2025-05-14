import pytest
from src.filters import filter_word

def test_filter_word_basic():
    data = {
        "items": [
            {"snippet": {"requirement": "Python, Django"}},
            {"snippet": {"requirement": "Java, Spring"}},
            {"snippet": {"requirement": "Python, Flask"}},
            {"snippet": {"requirement": ""}},
            {}
        ]
    }
    words = ["python"]

    filtered = filter_word(data, words)

    assert len(filtered) == 2
    for vac in filtered:
        assert "python" in vac.get("snippet", {}).get("requirement", "").lower()

def test_filter_word_no_words():
    data = {
        "items": [
            {"snippet": {"requirement": "Любое описание"}},
        ]
    }
    words = []

    filtered = filter_word(data, words)

    assert filtered == data["items"]
