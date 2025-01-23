import os
import subprocess


def generate_pdf_from_latex(
    latex_content, output_tex_file="output_cv.tex", output_pdf_file="output_cv.pdf"
):
    with open(output_tex_file, "w") as file:
        file.write(latex_content)

    result = subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", output_tex_file],
        check=False,  # Don't raise exceptions if pdflatex fails
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if result.returncode != 0:
        raise RuntimeError(f"PDF generation failed: {result.stderr.decode()}")

    if not os.path.exists(output_pdf_file):
        raise FileNotFoundError(f"PDF file {output_pdf_file} not created.")

    return output_pdf_file
