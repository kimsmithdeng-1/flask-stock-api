from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/get_stock', methods=['GET'])
def get_stock():
    stock_data = {
        "time": "2025-02-05 09:30",
        "stock_name": "AAPL",
        "price": 195.32
    }
    return jsonify(stock_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
