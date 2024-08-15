import os
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    """Upload files"""
    if 'files' not in request.files:
        return jsonify({"error": "No file part"}), 400

    files = request.files.getlist('files')

    if not files or files[0].filename == '':
        return jsonify({"error": "No selected file"}), 400
    upload_dir = "./uploads"

    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)

    # Save the file to source
    uploaded_files = []
    for file in files:
        save_path = f"./uploads/{file.filename}"
        file.save(save_path)
        uploaded_files.append(file.filename)
    return jsonify({"message": "Files successfully uploaded", "filenames": uploaded_files}), 200


if __name__ == '__main__':
    app.run(debug=True)
