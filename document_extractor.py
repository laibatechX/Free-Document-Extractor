import pdfplumber
import spacy
import os

def extract_text_from_pdf(pdf_path):
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ''
            for page in pdf.pages:
                text += page.extract_text() + '\n'
        return text
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        return None

def extract_entities(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    return doc.ents

def save_entities_to_file(entities, filename="extracted_entities.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for ent in entities:
                f.write(f"{ent.text} --> {ent.label_}\n")
        print(f"\n✅ Entities saved to '{filename}'\n")
    except Exception as e:
        print(f"❌ Could not save to file: {e}")

# ---------------------------
# MAIN
# ---------------------------
print("📄 Welcome to the Document Extractor!")

file_path = input("Enter the full path to your PDF file: ").strip()

if not os.path.isfile(file_path):
    print(f"❌ File not found at: {file_path}")
    print("⚠️ Unable to extract text. Please check the file path again.")
else:
    text = extract_text_from_pdf(file_path)
    if text:
        print("\n🔍 Extracting named entities...")
        entities = extract_entities(text)
        for ent in entities:
            print(f"{ent.text} --> {ent.label_}")
        save_entities_to_file(entities)
    else:
        print("⚠️ No text could be extracted from the PDF.")
