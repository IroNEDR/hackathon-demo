import pickle
import numpy as np
from PyNomaly import loop
from flask import Flask, request, jsonify


def load_model() -> loop.LocalOutlierProbability:
    return pickle.load(open('model.pkl', 'rb'))

def create_app(model: loop.LocalOutlierProbability) -> Flask:
    app = Flask(__name__)
    @app.route("/v2/classify", methods=["POST"])
    def classify():
        data = request.get_json()
        results = []
        for row in data["data"]:
            data_np = np.array(row, dtype=np.float64)
            results.append(model.stream(data_np))
        return jsonify({"result": results})
    return app


if __name__ == "__main__":
    model = load_model()
    app = create_app(model)
    app.run(host='0.0.0.0',port=5000)
