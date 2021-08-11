from horarios import sabado, domingo, lunes, martes, miercoles, jueves, viernes
from teams import teams
from flask import Flask, json, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def index():
    return jsonify({"status": 200, "data": "Api Radio"})


@app.route('/teams')
def getTeams():
    return jsonify({"status": 200, "teams": teams})


@app.route('/Horario/<int:dia>')
def getHorarios(dia):
    if dia == 1:
        return jsonify({"status": 200, "Horario": sabado})
    if dia == 2:
        return jsonify({"status": 200, "Horario": domingo})
    if dia == 3:
        return jsonify({"status": 200, "Horario": lunes})
    if dia == 4:
        return jsonify({"status": 200, "Horario": martes})
    if dia == 5:
        return jsonify({"status": 200, "Horario": miercoles})
    if dia == 6:
        return jsonify({"status": 200, "Horario": jueves})
    if dia == 7:
        return jsonify({"status": 200, "Horario": viernes})
    else:
        return jsonify({"status": 404, "msg": "Error"})


@app.route('/Horario/<string:dato>')
def getHorariosE(dato):
    return jsonify({"status": 404, "msg": "Error"})


if __name__ == '__main__':
    app.run(debug=True, port=4000)
