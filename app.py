from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos iniciales de ejemplo
tareas = [
    {'id': 1, 'nombre': 'Tarea 1', 'estado': 'pendiente'},
    {'id': 2, 'nombre': 'Tarea 2', 'estado': 'completada'}
]

# Ruta para obtener todas las tareas
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    return jsonify(tareas)

# Ruta para obtener una tarea por ID
@app.route('/tareas/<int:tarea_id>', methods=['GET'])
def obtener_tarea(tarea_id):
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if tarea is None:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    return jsonify(tarea)

# Ruta para crear una nueva tarea
@app.route('/tareas', methods=['POST'])
def crear_tarea():
    nueva_tarea = request.get_json()
    if not nueva_tarea.get('nombre') or not nueva_tarea.get('estado'):
        return jsonify({'error': 'El nombre y el estado son obligatorios'}), 400
    nueva_tarea['id'] = len(tareas) + 1
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

# Ruta para actualizar una tarea existente
@app.route('/tareas/<int:tarea_id>', methods=['PUT'])
def actualizar_tarea(tarea_id):
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if tarea is None:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    datos = request.get_json()
    tarea.update(datos)
    return jsonify(tarea)

# Ruta para eliminar una tarea
@app.route('/tareas/<int:tarea_id>', methods=['DELETE'])
def eliminar_tarea(tarea_id):
    global tareas
    tareas = [tarea for tarea in tareas if tarea['id'] != tarea_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)