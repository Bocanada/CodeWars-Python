def alphabet_position(text: str):
    return ' '.join(list(str(ord(c) - 96) for c in text.lower()))