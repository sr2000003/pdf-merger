from PyPDF2 import PdfMerger
import os

def merge_pdfs(folder_path, output_name):
    merger = PdfMerger()
    for filename in sorted(os.listdir(folder_path)):
        if filename.endswith(".pdf"):
            merger.append(os.path.join(folder_path, filename))
    merger.write(output_name)
    merger.close()
    print(f"✅ Merged PDF saved as: {output_name}")

merge_pdfs("your_pdf_folder", "merged_output.pdf")
