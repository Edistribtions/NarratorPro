from pypdf import PdfReader

def extract_text(pdf_path:str)->str:
    reader=PdfReader(pdf_path)
    return "\n".join((p.extract_text() or "") for p in reader.pages)
