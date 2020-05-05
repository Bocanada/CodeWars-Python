def alphabet_position(text: str):
    try:
        return ' '.join(list(str(ord(c) - 96) for c in text.lower().replace(' ', '')))
    except ValueError and AttributeError:
        return 'Only alphabet letters are allowed.'
