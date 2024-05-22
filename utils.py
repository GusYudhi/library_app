import fitz  # PyMuPDF

def extract_pdf_cover(pdf_path):
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)  # Halaman pertama
    pix = page.get_pixmap()
    cover_path = pdf_path.replace(".pdf", ".png")
    pix.save(cover_path)
    return cover_path
