import keyword

def is_valid_variable_name(text):
    if not text.isidentifier():
        return False

    if keyword.iskeyword(text):
        return False

    return True
