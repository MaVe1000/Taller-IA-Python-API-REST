## **📌 Proyecto: API REST de Gestión de Tareas con Flask**
🚀 **Descripción**  
Este proyecto es una **API REST** sencilla desarrollada con **Flask** para gestionar tareas. Permite **crear, editar, obtener y eliminar tareas**, implementado diccionarios con python.

✅ **Características principales:**  
- Implementación de **Pair Programming con IA** (GitHub Copilot y ChatGPT).  
- Uso de un **entorno virtual** para facilitar la instalación de dependencias.  
- Archivos adicionales:  
  - 📄 `requirements.txt`: Dependencias del proyecto.  
  - 📄 `.gitignore`: Archivos a excluir en Git.  
  - 📄 `conversacion-copilot.md`: Historial de interacción con Copilot.  

---

### **🔧 Requisitos**
Antes de comenzar, asegúrate de tener instalado:  
- **Python 3.8+**  
- **pip** (gestor de paquetes de Python)  
- **Git** (para clonar el repositorio)  

---

### **📂 Instalación y Configuración**
Sigue estos pasos para clonar y ejecutar el proyecto en tu máquina local.

1️⃣ **Clona el repositorio**  
```bash
git clone https://github.com/broko-de/proyecto-taller-ia.git
cd proyecto-taller-ia
```

2️⃣ **Crea y activa un entorno virtual**  
```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Instala las dependencias**  
```bash
pip install -r requirements.txt
```

4️⃣ **Ejecuta la aplicación**  
```bash
python app.py
```

5️⃣ **Prueba la API**  
Abre tu navegador o usa herramientas como **Postman** o **cURL** para probar los endpoints:  
- **Obtener todas las tareas**: `GET http://127.0.0.1:5000/tareas`  
- **Crear una tarea**: `POST http://127.0.0.1:5000/tareas` (enviar JSON con `tarea` y `estado`)  

---

### **🎯 Estructura del Proyecto**
```
/proyecto-taller-ia
│── /venv           # Entorno virtual (excluido en .gitignore)
│── app.py          # Código principal de la API
│── requirements.txt # Dependencias
│── .gitignore      # Archivos a ignorar por Git
│── conversacion-copilot.md # Conversación con Copilot
│── README.md       # Documentación del proyecto
```

---

### **📜 Notas y Recomendaciones**
- **Pair Programming con IA**: Puedes revisar el archivo `conversacion-copilot.md` para ver cómo la IA ayudó en el desarrollo.  
- **Extensibilidad**: Si deseas mejorar la API, puedes agregar autenticación, más rutas o migrar a un framework como **FastAPI**.  

---

