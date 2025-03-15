def highlight_text_in_pdf(self, pdf_path, text_chunk):
    """
    Efficiently finds and highlights a single best-matching paragraph in the PDF.
    """
    doc = fitz.open(pdf_path)
    best_page = None
    best_score = 0
    best_rect = None
    
    # First pass: Find the best matching paragraph across all pages
    for page_num, page in enumerate(doc):
        # Extract text blocks
        blocks = page.get_text("blocks")
        
        # Process blocks to form complete paragraphs
        paragraphs = []
        for block in blocks:
            text = block[4].strip()
            if len(text) > 30:  # Filter out very short blocks
                # Calculate similarity score
                score = fuzz.ratio(text_chunk, text)
                if score > best_score:
                    best_score = score
                    best_page = page_num
                    best_rect = fitz.Rect(block[:4])
    
    # Second pass: Apply highlight only to the best match
    if best_page is not None and best_score > 60:  # Adjust threshold as needed
        page = doc[best_page]
        page.add_highlight_annot(best_rect)
        
        # Save the highlighted PDF
        highlighted_pdf_path = "highlighted_output.pdf"
        doc.save(highlighted_pdf_path)
        doc.close()
        print(f"Highlighted PDF saved as '{highlighted_pdf_path}'")
        return {"highlighted_pdf": highlighted_pdf_path, "similarity_score": best_score}
    else:
        doc.close()
        print("No matching paragraph found for highlighting.")
        return None
