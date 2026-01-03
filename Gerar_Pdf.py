from weasyprint import HTML, CSS

# Caminhos absolutos (altere se estiver em outra pasta)
html_path = r"C:\Users\Victoriano\Documents\Projetos em geral\Organização-FrontEnd\Curriculo online\Index.html"
css_path = r"C:\Users\Victoriano\Documents\Projetos em geral\Organização-FrontEnd\Curriculo online\style.css"
output_pdf = r"C:\Users\Victoriano\Documents\EnzoVictorianoLeodriguez.pdf"

# Gera o PDF fiel ao layout do navegador
HTML(html_path).write_pdf(
    output_pdf,
    stylesheets=[CSS(css_path)]
)

print(" [OK] PDF gerado com sucesso:", output_pdf)
''