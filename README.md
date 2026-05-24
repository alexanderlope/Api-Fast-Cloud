# 🚀 API FastAPI en Google Cloud Run

API de ejemplo para desplegar en **Google Cloud Run** usando **GitHub** y **Cloud Build** con CI/CD automático.

---

## 📁 Estructura del proyecto

```
.
├── main.py            # Código principal de la API (FastAPI)
├── requirements.txt   # Dependencias de Python
├── Dockerfile         # Instrucciones para construir el contenedor
├── .gcloudignore      # Archivos a ignorar al subir a Cloud Build
├── .gitignore         # Archivos a ignorar en Git
└── README.md          # Este archivo
```

---

## ▶️ Ejecutar localmente

```bash
# 1. Crear entorno virtual
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Correr el servidor
uvicorn main:app --reload
```

La API estará disponible en: `http://localhost:8000`  
Documentación automática en: `http://localhost:8000/docs`

---

## 🐳 Ejecutar con Docker

```bash
# Construir la imagen
docker build -t mi-api .

# Correr el contenedor
docker run -p 8080:8080 mi-api
```

---

## ☁️ Desplegar en Cloud Run (manual)

```bash
# 1. Autenticarse en Google Cloud
gcloud auth login

# 2. Establecer tu proyecto
gcloud config set project TU_PROJECT_ID

# 3. Desplegar directamente desde el código fuente
gcloud run deploy mi-api \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```

---

## 🔄 CI/CD con Cloud Build y GitHub

1. Ve a **Cloud Run** en Google Cloud Console
2. Haz clic en **"Configurar con Cloud Build"**
3. Autoriza GitHub y selecciona tu repositorio
4. En **Configuración de compilación**, elige:
   - Rama: `main` (o `master`)
   - Tipo de compilación: `Dockerfile`
5. ¡Listo! Cada `git push` desplegará automáticamente

---

## 🔗 Endpoints disponibles

| Método | Ruta           | Descripción                  |
|--------|----------------|------------------------------|
| GET    | `/`            | Mensaje de bienvenida        |
