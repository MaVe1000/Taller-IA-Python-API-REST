# Conversación con GitHub Copilot

## PROMPT
Crear una API REST con python y flask que tenga las rutas básicas para manejar "tareas" y devuelva respuestas en formato JSON. Las tareas deben tener los datos de nombre y estado. Indicame los pasos a seguir para crear un entorno virtual e instalar las librerias necesarias para ejecutar el proyecto

## RESPUESTA
Para crear una API REST con Python y Flask que maneje "tareas" y devuelva respuestas en formato JSON, sigue estos pasos:

### Paso 1: Crear un entorno virtual
1. Abre una terminal en Visual Studio Code.
2. Navega al directorio donde deseas crear tu proyecto.
3. Ejecuta el siguiente comando para crear un entorno virtual:
    ```sh
    python -m venv venv
    ```
4. Activa el entorno virtual:
    - En Windows:
      ```sh
      .\venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

### Paso 2: Instalar Flask
1. Con el entorno virtual activado, instala Flask ejecutando:
    ```sh
    pip install Flask
    ```

### Paso 3: Crear la estructura del proyecto
1. Crea un archivo llamado [app.py](http://_vscodecontentref_/1) en el directorio de tu proyecto.

### Paso 4: Escribir el código de la API REST
En el archivo [app.py](http://_vscodecontentref_/2), agrega el siguiente código:

```python
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
```

### Paso 5: Ejecutar la aplicación
1. En la terminal, asegúrate de que el entorno virtual esté activado.
2. Ejecuta la aplicación Flask:
   ```sh
   python app.py
   ```
3. La API REST estará disponible en `http://127.0.0.1:5000`.

### Rutas disponibles
- `GET /tareas`: Obtener todas las tareas.
- `GET /tareas/<id>`: Obtener una tarea por ID.
- `POST /tareas`: Crear una nueva tarea.
- `PUT /tareas/<id>`: Actualizar una tarea existente.
- `DELETE /tareas/<id>`: Eliminar una tarea.

¡Listo! Ahora tienes una API REST básica con Flask para manejar tareas.

## PROMPT
Estoy obteniendo el siguiente error @app.route('/tareas/int:tarea_id', methods['PUT']) NameError: name 'methods' is not defined

## RESPUESTA
El error se debe a que hay un error tipográfico en la definición de la ruta. Deberías usar `methods=['PUT']` en lugar de `methods['PUT']`.

Corrige la línea de la siguiente manera:
```python
# Ruta para actualizar una tarea existente
@app.route('/tareas/<int:tarea_id>', methods=['PUT'])
def actualizar_tarea(tarea_id):
    tarea = next((tarea for tarea in tareas if tarea['id'] == tarea_id), None)
    if tarea is None:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    datos = request.get_json()
    tarea.update(datos)
    return jsonify(tarea)
```

Asegúrate de que la línea completa se vea así:
```python
@app.route('/tareas/<int:tarea_id>', methods=['PUT'])
```

Esto debería resolver el error `NameError: name 'methods' is not defined`.

## PROMPT
Agregar validaciones para que el nombre y el estado no sean vacias.

## RESPUESTA
Para agregar validaciones y asegurarte de que el nombre y el estado no sean vacíos al crear una nueva tarea, puedes modificar la función `crear_tarea` de la siguiente manera:

```python
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
```

Con esta modificación, la función `crear_tarea` ahora verifica si los campos `nombre` y `estado` están presentes y no están vacíos. Si alguno de estos campos está vacío, se devuelve un error 400 con un mensaje adecuado.
