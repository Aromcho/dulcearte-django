
# DulceArte

**DulceArte** es una aplicación web desarrollada con Django que permite a los usuarios crear, compartir, comentar y dar "me gusta" a recetas de repostería.

## Cómo Probar el Proyecto

### 1. Clonar el Repositorio
```bash
git clone https://github.com/Aromcho/dulcearte-django.git
cd dulcearte
```

### 2. Crear y Activar el Entorno Virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 4. Aplicar Migraciones y Crear un Superusuario
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Ejecutar el Servidor de Desarrollo
```bash
python manage.py runserver
```

Accede a la aplicación en `http://127.0.0.1:8000` y al panel de administración en `http://127.0.0.1:8000/admin`.

## Progreso del Desarrollo

- **Modelos personalizados:** Se creó un modelo de usuario personalizado (`Usuario`) con campos adicionales como `bio` y `avatar`.
- **Modelos principales:** Implementación de los modelos `Receta`, `Publicación`, `Comentario` y `MeGusta` para gestionar las recetas y la interacción de los usuarios.
- **Autenticación:** Se configuró el sistema de registro, inicio y cierre de sesión para los usuarios.
- **Vistas y URLs:** Se configuraron rutas y vistas básicas para el manejo de recetas y autenticación.
- **Interfaz de usuario:** Se aplicó Bootstrap en la plantilla `home.html` para mejorar la apariencia y la navegación.
- **Panel de administración:** Configuración del panel de administración de Django para gestionar los usuarios y el contenido generado.

