import re
def clean(text:str)->str:
    text=re.sub(r"\s+"," ",text)
    return text.strip()
