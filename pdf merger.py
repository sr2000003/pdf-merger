from PyPDF2 import PdfMerger
import os

def merge_pdfs(folder_path, output_name):
    files = [f for f in sorted(os.listdir(folder_path)) if f.endswith(".pdf")]
    if not files:
        print("❌ No PDF files found in the selected folder.")
        return

    # ✅ List available PDFs
    print("\nAvailable PDFs in this folder:\n")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")

    # ✅ Ask user for input
    selected = input("\nEnter the numbers of PDFs you want to merge (comma separated): ").split(",")
    selected = [int(x.strip()) for x in selected if x.strip().isdigit()]
    selected_files = [files[i-1] for i in selected if 1 <= i <= len(files)]

    if not selected_files:
        print("❌ No valid files selected.")
        return

    # ✅ Perform the merging
    merger = PdfMerger()
    for filename in selected_files:
        merger.append(os.path.join(folder_path, filename))
    merger.write(output_name)
    merger.close()

    print(f"\n✅ Done! Merged PDFs saved as: {output_name}")

# 👇 Edit the path accordingly
merge_pdfs(r"C:\Users\sr200\OneDrive\Desktop\Coding\Project 7\pdfs", "merged_output.pdf")
