import fitz  # PyMuPDF

def remove_blank_pages(input_pdf, output_pdf):
    # Otwórz dokument PDF
    doc = fitz.open(input_pdf)
    page_numbers = []  # Lista numerów stron do usunięcia

    # Iteruj przez strony i sprawdź, czy są puste
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text().strip()  # Pobierz tekst ze strony i usuń białe znaki

        # Jeśli strona jest pusta, dodaj jej numer do listy
        if not text:
            page_numbers.append(page_num)

    # Usuń strony od końca dokumentu, aby uniknąć błędów indeksowania
    for page_num in reversed(page_numbers):
        doc.delete_page(page_num)

    # Zapisz zmodyfikowany dokument jako nowy plik PDF
    doc.save(output_pdf)
    doc.close()

# Użyj funkcji
input_pdf = r'C:\Users\m.x\Desktop\x\x.pdf'  # Nazwa pliku wejściowego
output_pdf = 'output.pdf'  # Nazwa pliku wyjściowego
remove_blank_pages(input_pdf, output_pdf)
