import fitz

def remove_blank_pages(input_pdf, output_pdf):
    
    doc = fitz.open(input_pdf)
    page_numbers = []  
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text().strip()  #
        
        if not text:
            page_numbers.append(page_num)

    for page_num in reversed(page_numbers):
        doc.delete_page(page_num)
        
    doc.save(output_pdf)
    doc.close()

input_pdf = r'C:\Users\m.x\Desktop\x\x.pdf' 
output_pdf = 'output.pdf'
remove_blank_pages(input_pdf, output_pdf)
