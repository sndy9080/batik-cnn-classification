from flask import Flask, render_template, request, jsonify
# from tensorflow.keras.models import load_model
# from keras.models import load_model  # ✅ Keras 3+ untuk format .keras ZIP
import tf_keras as keras
from tf_keras.models import load_model
from keras.preprocessing import image

from PIL import Image
import numpy as np
from datetime import datetime
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# === KONFIGURASI DASAR ===
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'tiff', 'webp', 'jfif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# === LOAD MODEL CNN DAN XCEPTION UNTUK BATIK ===
# === PERBAIKAN ===
# === GANTI DENGAN KODE INI ===


model_cnn = load_model(os.path.join(BASE_DIR, "scratchCNN.keras"))
model_xception = load_model(os.path.join(BASE_DIR, "Xception.keras"))



# === KELAS KLASIFIKASI BATIK ===
class_names = ['Kawung', 'Mega_Mendung', 'Parang', 'Truntum']

# === CEK FILE YANG DIIJINKAN ===
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def main():
    return render_template("cnn.html")

@app.route("/classification", methods=["GET", "POST"])
def classification():
    return render_template("classifications.html")

@app.route("/submit", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({'message': 'No image uploaded'}), 400

    file = request.files['file']
    if not (file and allowed_file(file.filename)):
        return jsonify({'message': 'Invalid file type'}), 400

    # Pastikan folder uploads ada
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Simpan gambar upload
    filename = datetime.now().strftime("%d%m%y-%H%M%S") + ".png"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    img = Image.open(file).convert('RGB')
    img.save(file_path)
    img.close()

    # Preprocessing untuk prediksi
    def preprocess(img_path):
        img = image.load_img(img_path, target_size=(224, 224))  # Pastikan sama dengan input model
        x = image.img_to_array(img)
        x = x / 127.5 - 1  # Jika model kamu pakai normalisasi ini
        return np.expand_dims(x, axis=0)

    input_img = preprocess(file_path)

    # Ubah path file lokal menjadi path web (untuk <img src=""> di HTML)
    web_img_path = '/static/uploads/' + filename

    # === PREDIKSI DENGAN SEMUA MODEL ===
    pred_cnn = model_cnn.predict(input_img)
    pred_xception = model_xception.predict(input_img)

    result = {
        'img_path': web_img_path,
        'predictioncnn': class_names[np.argmax(pred_cnn)],
        'confidencecnn': '{:2.0f}%'.format(100 * np.max(pred_cnn)),
        'predictionxception': class_names[np.argmax(pred_xception)],
        'confidencexception': '{:2.0f}%'.format(100 * np.max(pred_xception)),
    }

    return render_template("classifications.html", **result)

if __name__ == "__main__":
    app.run(debug=True)
