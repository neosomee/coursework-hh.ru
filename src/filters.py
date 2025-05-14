def filter_word(data, words):
    new_data = []
    if not words:
        return data.get("items", [])
    for i in data.get("items", []):
        try:
            requirement = i.get("snippet", {}).get("requirement", "").lower()
            if any(word.lower() in requirement for word in words):
                new_data.append(i)
        except Exception:
            continue
    return new_data
