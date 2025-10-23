from weasyprint import HTML, CSS

# Caminhos absolutos (altere se estiver em outra pasta)
html_path = r"C:\Users\Victoriano\Desktop\Curriculo online\Index.html"
css_path = r"C:\Users\Victoriano\Desktop\Curriculo online\style.css"
output_pdf = r"C:\Users\Victoriano\Desktop\Curriculo online\EnzoVictorianoLeodriguez.pdf"

# Gera o PDF fiel ao layout do navegador
HTML(html_path).write_pdf(
    output_pdf,
    stylesheets=[CSS(css_path)]
)

print(" [OK] PDF gerado com sucesso:", output_pdf)
''