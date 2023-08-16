import streamlit as st
import PyPDF2
from docx import Document
from io import BytesIO

def pdf_to_docx(pdf_file):
    doc = Document()
    
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    for page_number in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_number]
        text = page.extract_text()
        doc.add_paragraph(text)
    
    docx_stream = BytesIO()
    doc.save(docx_stream)
    docx_stream.seek(0)
    return docx_stream

def main():
    st.title("PDF to DOCX Converter")
    
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    
    if uploaded_file is not None:
        st.write("PDF file uploaded successfully!")
        
        convert_button = st.button("Convert to DOCX")
        
        if convert_button:
            st.write("Converting...")
            docx_stream = pdf_to_docx(uploaded_file)
            st.success("Conversion complete!")
            st.download_button("Download DOCX", docx_stream, "Converted.docx")

if __name__ == "__main__":
    main()
