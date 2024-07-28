import pymupdf, subprocess, sys

def install_pymupdf():
    try:
        import pymupdf
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])

def extract_first_page_to_png(pdf_path, output_path):
    install_pymupdf()
    
    document = pymupdf.open(pdf_path)
    if document.page_count < 1: return False
    
    document.load_page(0).get_pixmap().save(output_path)
    return f"{output_path}"
