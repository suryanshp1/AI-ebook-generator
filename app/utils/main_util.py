from fpdf import FPDF

def generate_pdf(topic, chapters_content, chapters):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Cover Page
    pdf.add_page()
    pdf.set_font(family='Times', size=30)
    pdf.set_text_color(r=255, g=0, b=0)
    pdf.set_y(pdf.h / 2 - 15)
    pdf.cell(w=pdf.w - 50, txt=f"{topic}", align="C")

    # Table of Contents
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Table of Contents", ln=True)
    for i, chapter_title in enumerate(chapters):
        pdf.cell(200, 10, txt=f"Chapter {i+1}: {chapter_title}", ln=True)

    # Chapters
    for i, content in enumerate(chapters_content):
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(200, 10, txt=f"Chapter {i+1}: {chapters[i]}", ln=True)
        pdf.set_font("Arial", '', 12)
        pdf.multi_cell(0, 10, txt=content, markdown=True)

    pdf_file_path = f"{topic.replace(' ', '_')}.pdf"
    pdf.output(pdf_file_path)
    
    return pdf_file_path
