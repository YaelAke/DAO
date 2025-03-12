from flask import Flask, render_template, request, jsonify
from dao import UsuarioDAO

app = Flask(__name__)
dao = UsuarioDAO()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(dao.obtener_usuarios())

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    datos = request.json
    dao.crear_usuario(datos)
    return jsonify({"mensaje": "Usuario agregado exitosamente"}), 201

@app.route('/usuarios/<nombre>', methods=['PUT'])
def actualizar_usuario(nombre):
    datos = request.json
    if dao.actualizar_usuario(nombre, datos):
        return jsonify({"mensaje": "Usuario actualizado exitosamente"})
    return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/usuarios/<nombre>', methods=['DELETE'])
def eliminar_usuario(nombre):
    if dao.eliminar_usuario(nombre):
        return jsonify({"mensaje": "Usuario eliminado exitosamente"})
    return jsonify({"error": "Usuario no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
