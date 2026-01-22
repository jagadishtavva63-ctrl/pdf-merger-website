from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfMerger

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge():
    files = request.files.getlist('pdfs')
    merger = PdfMerger()

    for file in files:
        merger.append(file)

    output = "merged.pdf"
    merger.write(output)
    merger.close()

    return send_file(output, as_attachment=True)

if __name__ == "__main__":
    app.run()
