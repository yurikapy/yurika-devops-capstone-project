from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS  # Import CORS

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Membuat instance Talisman dan memasangnya pada aplikasi Flask
talisman = Talisman(app)

# Menambahkan CORS untuk mengizinkan permintaan lintas domain
CORS(app)

# Route aplikasi
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Menjalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)
