# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_folder='static', template_folder='templates')

# Route untuk halaman utama
@app.route('/')
def index():
    # Jika kamu meletakkan index.html di folder 'templates'
    return render_template('index.html')
    # Jika kamu meletakkan index.html di folder 'static'
    # return app.send_static_file('index.html')

# Contoh API endpoint sederhana
@app.route('/api/transactions', methods=['GET', 'POST'])
def transactions():
    if request.method == 'GET':
        # Nanti di sini akan ambil data dari database
        dummy_transactions = [
            {'id': 1, 'type': 'income', 'amount': 2000000, 'category': 'Gaji', 'date': '2025-06-01', 'description': 'Gaji bulanan'},
            {'id': 2, 'type': 'expense', 'amount': 150000, 'category': 'Makanan', 'date': '2025-06-05', 'description': 'Makan siang'},
        ]
        return jsonify(dummy_transactions)
    elif request.method == 'POST':
        data = request.get_json()
        # Nanti di sini akan simpan data ke database
        print("Data transaksi baru:", data)
        return jsonify({"message": "Transaksi berhasil ditambahkan!", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True) # debug=True akan auto-reload saat ada perubahan kode