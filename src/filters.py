def filter_word(data, words):
    """
    Фильтрация вакансий по ключевым словам в требованиях.
    """
    new_data = []
    if not words:
        return data.get("items", [])
    for item in data.get("items", []):
        try:
            requirement = item.get("snippet", {}).get("requirement", "").lower()
            if any(word.lower() in requirement for word in words):
                new_data.append(item)
        except Exception:
            continue
    return new_data