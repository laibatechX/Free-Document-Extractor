# Free-Document-Extractor
An AI tool that extracts text and named entities from PDF documents using Python, pdfplumber, and spaCy
# 🧠 Free Document Extractor

This is a simple AI-powered tool built using Python that:
- Extracts text from PDF documents
- Identifies useful entities like names, dates, locations, and more using spaCy

## 📄 Features
- Extracts plain text from any `.pdf` file using `pdfplumber`
- Performs Named Entity Recognition (NER) using spaCy's `en_core_web_sm` model
- Outputs both the full text and the named entities to a `.txt` file

## 🛠️ Built With
- Python 3.10+
- pdfplumber
- spaCy

## 💡 How to Run
1. Install dependencies:
   ```bash
   pip install pdfplumber spacy
   python -m spacy download en_core_web_sm
#Run the script
python document_extractor.py
Enter the full path to your PDF file (e.g. C:/Users/Name/Desktop/sample_resume.pdf)
📦 Output
Extracted text saved in extracted_info.txt

Named entities displayed in terminal

📫 Contact
Made with ❤️ by Laiba Azhar
GitHub: laibatechX
