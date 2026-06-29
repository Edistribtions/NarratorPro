import re
PATTERN=re.compile(r"(?=\b(?:CHAPTER|Chapter|PART|PROLOGUE|EPILOGUE|APPENDIX)\b)")
def split(text:str):
    parts=[p.strip() for p in PATTERN.split(text) if p.strip()]
    return parts or [text]
