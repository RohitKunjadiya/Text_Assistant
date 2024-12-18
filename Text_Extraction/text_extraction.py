import fitz  # PyMuPDF
import os  # For file operations

# Function to check if a page is blank
def is_blank_page(page):
    text = page.get_text()
    return not text.strip()

# Function to check if a page is an index or table of contents page
def is_index_page(page):
    text = page.get_text()
    lower_text = text.lower()
    keywords = ["index", "contents", "table of contents", "bibliography"]
    return any(keyword in lower_text for keyword in keywords)

# Function to remove unnecessary pages (blank and index pages)
def remove_unnecessary_pages(input_pdf, output_pdf):
    pdf_document = fitz.open(input_pdf)
    new_pdf_document = fitz.open()

    for i in range(len(pdf_document)):
        page = pdf_document.load_page(i)
        if not (is_blank_page(page) or is_index_page(page)):
            new_pdf_document.insert_pdf(pdf_document, from_page=i, to_page=i)

    new_pdf_document.save(output_pdf, deflate=True)
    new_pdf_document.close()
    pdf_document.close()

# Function to extract text from the output PDF
def extract_text_from_pdf(output_pdf):
    doc = fitz.open(output_pdf)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text

# Function to delete the output file after processing
def delete_output_file(output_pdf):
    if os.path.exists(output_pdf):
        os.remove(output_pdf)
        print(f"{output_pdf} has been deleted.")
    else:
        print(f"{output_pdf} does not exist, so no deletion needed.")


def process_pdf(input_pdf):
    output_pdf = f"output_{os.path.basename(input_pdf)}"  # Generate output file name

    # Remove unnecessary pages
    remove_unnecessary_pages(input_pdf, output_pdf)

    # Extract text from the output PDF
    text = extract_text_from_pdf(output_pdf)

    # Delete the output PDF file
    delete_output_file(output_pdf)

    return text