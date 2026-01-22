from flask import Flask, render_template, request, send_file
from PyPDF2 import PdfMerger
import os

app = Flask(__name__, template_folder="templates")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/merge', methods=['POST'])
def merge():
    files = request.files.getlist('pdfs')

    if not files:
        return "No files uploaded", 400

    merger = PdfMerger()

    for file in files:
        merger.append(file)

    output = "merged.pdf"
    merger.write(output)
    merger.close()

    return send_file(output, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


