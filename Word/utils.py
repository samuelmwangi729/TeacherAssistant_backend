from docx import Document

def extract_styles(doc_path):
    # Load the document
    doc = Document(doc_path)
    document_data = {"sheets": []}

    # Iterate through paragraphs in the document
    for para in doc.paragraphs:
        paragraph_info = {
            "text": para.text.strip(),
            "style": para.style.name,  # The paragraph's style (e.g., "Normal", "Heading1")
            "runs": []
        }
        
        # Iterate through runs within the paragraph to check for inline styles
        for run in para.runs:
            run_info = {
                "text": run.text.strip(),
                "bold": run.bold,  # Whether the text is bold
                "italic": run.italic,  # Whether the text is italic
                "underline": run.underline,  # Whether the text is underlined
                "font": {
                    "name": run.font.name,  # Font name
                    "size": run.font.size,  # Font size
                }
            }
            paragraph_info["runs"].append(run_info)
        
        document_data["sheets"].append(paragraph_info)

    return document_data