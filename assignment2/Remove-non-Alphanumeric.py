def remove_non_alphanumeric(text):
    result="" 
    for ch in text:
        if text.isalnum() or ch==" ":
            result+=ch
    return result
