from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Mengambil data yang dikirimkan oleh aplikasi Android
    data = request.json

    # Membuat permintaan POST ke TensorFlow Serving
    response = requests.post('http://<tensorflow_serving_endpoint>/v1/models/<model_name>:predict', json=data)

    # Mengekstrak hasil dari respon TensorFlow Serving
    predictions = response.json()['predictions']

    # Mengembalikan hasil prediksi ke aplikasi Android
    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
