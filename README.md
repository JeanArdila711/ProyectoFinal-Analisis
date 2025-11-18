# 📊 Proyecto de Análisis Numérico

Aplicación web desarrollada en Django para la resolución y comparación de métodos numéricos. Incluye métodos de búsqueda de raíces, sistemas lineales e interpolación, con capacidad de generar reportes comparativos en PDF.

## 🎯 Características Principales

### Capítulo 1: Métodos de Búsqueda de Raíces
- **Bisección**: Método de intervalo para encontrar raíces
- **Regla Falsa**: Método de falsa posición
- **Punto Fijo**: Método iterativo de punto fijo
- **Newton-Raphson**: Método con derivadas para convergencia rápida
- **Secante**: Método sin derivadas
- **Raíces Múltiples**: Métodos especializados para raíces múltiples
- **🔍 Comparación**: Compara los 5 métodos principales en una sola ejecución

### Capítulo 2: Métodos Iterativos para Sistemas Lineales
- **Jacobi**: Método iterativo de Jacobi
- **Gauss-Seidel**: Método iterativo de Gauss-Seidel
- **SOR**: Método de Sobrerrelajación Sucesiva
- **🔍 Comparación**: Compara los 3 métodos en una sola ejecución

### Capítulo 3: Métodos de Interpolación
- **Vandermonde**: Interpolación usando matriz de Vandermonde
- **Lagrange**: Interpolación de Lagrange
- **Newton**: Interpolación de Newton (diferencias divididas)
- **Spline Lineal**: Interpolación por splines lineales
- **Spline Cúbico**: Interpolación por splines cúbicos
- **🔍 Comparación**: Compara los 5 métodos en una sola ejecución

### Funcionalidades Adicionales
- ✅ Generación de gráficas de funciones
- ✅ Exportación de reportes comparativos en PDF
- ✅ Análisis comparativo automático de métodos
- ✅ Interfaz web moderna con Bootstrap 5
- ✅ Validación de entrada en tiempo real

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.10 o superior** ([Descargar Python](https://www.python.org/downloads/))
- **pip** (gestor de paquetes de Python)
- **Git** (opcional, para clonar el repositorio)

### Verificar Instalación

```bash
python --version  # Debe mostrar Python 3.10 o superior
pip --version     # Debe mostrar pip instalado
```

## 🚀 Instalación

### 1. Clonar o Descargar el Proyecto

Si tienes el proyecto en un repositorio Git:

```bash
git clone <url-del-repositorio>
cd "Analisis numerico"
```

O simplemente navega a la carpeta del proyecto si ya la tienes descargada.

### 2. Crear un Entorno Virtual (Recomendado)

Es altamente recomendable usar un entorno virtual para aislar las dependencias del proyecto:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

Una vez activado, verás `(venv)` al inicio de tu línea de comandos.

### 3. Instalar Dependencias

El proyecto tiene tres archivos de requirements según el entorno:

#### Para Desarrollo (Recomendado para empezar):
```bash
pip install -r requirements/development.txt
```

#### Solo Dependencias Base:
```bash
pip install -r requirements/base.txt
```

#### Para Producción:
```bash
pip install -r requirements/production.txt
```

**Nota:** El archivo `development.txt` incluye todas las dependencias base más herramientas de desarrollo.

### 4. Configurar la Base de Datos

El proyecto usa SQLite por defecto, que no requiere configuración adicional. Solo necesitas ejecutar las migraciones:

```bash
python manage.py migrate
```

Esto creará el archivo `db.sqlite3` con las tablas necesarias.

### 5. Crear un Superusuario (Opcional)

Si deseas acceder al panel de administración de Django:

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear un usuario administrador.

## ▶️ Ejecutar el Proyecto

### Modo Desarrollo

Para ejecutar el servidor de desarrollo:

```bash
python manage.py runserver
```

El servidor se iniciará en `http://127.0.0.1:8000/`

Abre tu navegador y visita:
- **Página Principal**: http://127.0.0.1:8000/
- **Panel de Administración**: http://127.0.0.1:8000/admin/

### Ejecutar en un Puerto Específico

```bash
python manage.py runserver 8080
```

Esto iniciará el servidor en `http://127.0.0.1:8080/`

## 📁 Estructura del Proyecto

```
Analisis numerico/
│
├── core/                    # Configuración principal de Django
│   ├── settings.py         # Configuración del proyecto
│   ├── urls.py             # URLs principales
│   └── wsgi.py             # Configuración WSGI
│
├── home/                    # Aplicación de inicio
│   └── views.py            # Vista de la página principal
│
├── numerical/               # Aplicación principal de métodos numéricos
│   ├── services/           # Lógica de negocio (métodos numéricos)
│   │   ├── bisection_service.py
│   │   ├── comparison_service.py
│   │   └── ...
│   ├── views/              # Vistas de la aplicación
│   │   ├── comparison_view.py
│   │   └── ...
│   ├── templates/          # Plantillas HTML
│   │   └── numerical/
│   │       ├── comparison.html
│   │       └── cap1/, cap2/, cap3/
│   └── containers/         # Inyección de dependencias
│
├── shared/                  # Utilidades compartidas
│   └── utils/              # Funciones auxiliares
│       ├── plot_function.py
│       └── ...
│
├── static/                  # Archivos estáticos
│   ├── css/                # Estilos CSS
│   ├── img/                # Imágenes
│   └── reports/            # PDFs generados
│
├── templates/               # Plantillas base
│   └── base.html           # Plantilla principal
│
├── requirements/            # Dependencias del proyecto
│   ├── base.txt            # Dependencias base
│   ├── development.txt     # Dependencias de desarrollo
│   └── production.txt      # Dependencias de producción
│
├── manage.py               # Script de administración de Django
└── db.sqlite3              # Base de datos SQLite (se crea automáticamente)
```

## 🛠️ Comandos Útiles

### Gestión de Base de Datos

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ver estado de migraciones
python manage.py showmigrations
```

### Recopilar Archivos Estáticos

```bash
python manage.py collectstatic
```

### Shell de Django

Para acceder al shell interactivo de Django:

```bash
python manage.py shell
```

### Crear una Nueva Aplicación

```bash
python manage.py startapp nombre_app
```

## 🔧 Configuración

### Variables de Entorno (Opcional)

El proyecto está configurado para funcionar sin variables de entorno. Sin embargo, para producción, se recomienda:

1. Crear un archivo `.env` en la raíz del proyecto
2. Configurar variables sensibles como `SECRET_KEY` y `DEBUG`

### Configuración de Base de Datos

Por defecto, el proyecto usa SQLite. Para cambiar a PostgreSQL u otra base de datos, edita `core/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_db',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## 📖 Uso de la Aplicación

### Acceder a los Métodos

1. **Página Principal**: Visita `http://127.0.0.1:8000/`
2. **Navegación**: Usa el menú superior para acceder a cada capítulo
3. **Métodos Individuales**: Cada capítulo tiene enlaces a métodos específicos
4. **Comparación**: Cada capítulo tiene una opción para comparar todos los métodos

### Ejemplo de Uso - Comparación de Métodos

1. Navega a **Capítulo 1** → **Comparación de Métodos**
2. Ingresa los parámetros:
   - Función f(x): `x**3 - x - 2`
   - Intervalo [a, b]: `1, 2`
   - Punto inicial x₀: `1.5`
   - Tolerancia: `0.0001`
   - Máximo de iteraciones: `100`
3. Selecciona "Generar PDF" si deseas exportar los resultados
4. Haz clic en "Comparar Métodos"
5. Revisa los resultados comparativos y descarga el PDF si lo generaste

## 🐛 Solución de Problemas

### Error: "No module named 'django'"

**Solución**: Asegúrate de haber activado el entorno virtual e instalado las dependencias:

```bash
# Activar entorno virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements/development.txt
```

### Error: "ModuleNotFoundError"

**Solución**: Verifica que todas las dependencias estén instaladas:

```bash
pip install -r requirements/development.txt --upgrade
```

### Error al generar PDFs

**Solución**: Asegúrate de que el directorio `static/reports/` exista:

```bash
# Crear directorio si no existe
mkdir -p static/reports  # Linux/Mac
# O crear manualmente en Windows
```

### El servidor no inicia

**Solución**: Verifica que el puerto 8000 no esté en uso:

```bash
# Usar otro puerto
python manage.py runserver 8080
```

### Error de migraciones

**Solución**: Si hay problemas con las migraciones:

```bash
# Eliminar base de datos (¡CUIDADO! Esto borra todos los datos)
rm db.sqlite3  # Linux/Mac
del db.sqlite3  # Windows

# Recrear migraciones
python manage.py makemigrations
python manage.py migrate
```

## 🧪 Testing

Para ejecutar las pruebas (si están disponibles):

```bash
python manage.py test
```

## 📦 Tecnologías Utilizadas

- **Django 5.2.4**: Framework web
- **Bootstrap 5**: Framework CSS
- **NumPy**: Cálculos numéricos
- **SciPy**: Algoritmos científicos
- **SymPy**: Matemáticas simbólicas
- **Matplotlib**: Visualización de gráficas
- **ReportLab**: Generación de PDFs
- **Dependency Injector**: Inyección de dependencias

## 📝 Notas Importantes

- ⚠️ **Modo Debug**: El proyecto está configurado con `DEBUG = True` por defecto. Para producción, cambia esto a `False` en `core/settings.py`
- 🔒 **Secret Key**: El `SECRET_KEY` en `settings.py` es solo para desarrollo. En producción, usa una clave segura y guárdala en variables de entorno
- 📊 **Base de Datos**: SQLite es suficiente para desarrollo. Para producción, considera usar PostgreSQL
- 📁 **Archivos Estáticos**: En producción, configura un servidor web (Nginx, Apache) para servir archivos estáticos o usa WhiteNoise

## 🤝 Contribuir

Si deseas contribuir al proyecto:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -am 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de uso educativo y académico.

## 👥 Autores

Proyecto desarrollado para el curso de Análisis Numérico.

## 📞 Soporte

Si encuentras algún problema o tienes preguntas:

1. Revisa la sección de [Solución de Problemas](#-solución-de-problemas)
2. Verifica que todas las dependencias estén instaladas correctamente
3. Asegúrate de estar usando Python 3.10 o superior

---

**¡Disfruta usando la aplicación de Análisis Numérico! 🚀**
