from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='keras')

modelo = load_model('modelo_mnist.h5')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_img():
    file = request.files['file']
    
    img = Image.open(file)
    img = img.resize((28, 28))
    img = img.convert('L')
    img = np.array(img) / 255.0  
    img = img.reshape(1, 28, 28, 1) 


    predict = modelo.predict(img)
    predict = np.argmax(predict, axis=1)[0] 

    return jsonify({'predict': int(predict)})

if __name__ == '__main__':
    app.run(debug=True)
