# Práctica: API REST con FastAPI y base de datos persistente

**API de Gestión Musical - Cantantes y Álbumes**

**Autor:** Dafne Cabrera Sanz 

---

## 📋 Temática Elegida

He elegido desarrollar un **sistema de gestión musical** que permite administrar información sobre cantantes y sus álbumes. Este sistema podría servir como backend para una plataforma de música, tienda online de discos o aplicación de streaming.

---

## 🗂️ Entidades Creadas

El sistema gestiona **dos entidades relacionadas**:

### 1. **Cantante** (Tabla: `cantantes`)

Representa a los artistas musicales.

**Campos (6):**
- `id` (Integer, Primary Key, autoincremental): Identificador único
- `nombre` (String, único, no nulo): Nombre del cantante
- `edad` (Integer, no nulo): Edad del artista
- `genero_musical` (String, no nulo): Género musical principal
- `oyentes_mensuales_spotify` (Integer, no nulo): Número de oyentes mensuales
- `activo` (Boolean, no nulo, default=True): Estado de actividad del artista

### 2. **Álbum** (Tabla: `albumes`)

Representa las producciones musicales.

**Campos (6):**
- `id` (Integer, Primary Key, autoincremental): Identificador único
- `nombre` (String, único, no nulo): Título del álbum
- `cantante_id` (Integer, Foreign Key, no nulo): ID del cantante asociado
- `precio` (Float, no nulo): Precio del álbum
- `fecha_lanzamiento` (DateTime, no nulo, default=datetime.utcnow): Fecha de publicación
- `genero` (String, no nulo): Género musical del álbum

**Relación:** Un cantante puede tener múltiples álbumes (1:N). La relación se implementa mediante Foreign Key (`cantante_id`) y `relationship()` de SQLAlchemy con `back_populates`.

---

## 📁 Estructura del Proyecto

```
CabreraSanz_Dafne_p3.1/
├── main.py                      # Punto de entrada de la aplicación
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este archivo
├── test_api.rest               # Pruebas de endpoints (REST Client)
├── database/
│   ├── __init__.py
│   ├── database.py             # Configuración de SQLAlchemy y SQLite
│   └── database.db             # Base de datos persistente (generado automáticamente)
├── models/
│   ├── __init__.py
│   ├── cantante.py             # Modelo ORM de Cantante
│   └── album.py                # Modelo ORM de Álbum
├── schemas/
│   ├── __init__.py
│   ├── cantante.py             # Esquemas Pydantic para Cantante
│   └── album.py                # Esquemas Pydantic para Álbum
└── routes/
    ├── __init__.py
    ├── cantantes.py            # Endpoints CRUD de Cantantes
    └── albumes.py              # Endpoints CRUD de Álbumes
```

---

## ✅ Requisitos Implementados

### 1. Recursos (tablas)

✅ **Dos entidades distintas**: Cantante y Álbum  
✅ **Mínimo 5 campos** cada una: Ambas tienen 6 campos incluyendo el ID  
✅ **Tipos de datos variados**: Integer, String, Float, Boolean, DateTime  
✅ **Relación entre tablas**: Foreign Key de Álbum hacia Cantante

### 2. Operaciones CRUD

Se han implementado las **5 operaciones CRUD** para cada recurso:

#### **Cantantes** (`/cantantes`)
- `GET /cantantes/` - Obtener todos los cantantes
- `GET /cantantes/{id}` - Obtener un cantante por ID
- `POST /cantantes/` - Crear nuevo cantante
- `PUT /cantantes/{id}` - Actualizar cantante
- `DELETE /cantantes/{id}` - Eliminar cantante

#### **Álbumes** (`/albumes`)
- `GET /albumes/` - Obtener todos los álbumes
- `GET /albumes/{id}` - Obtener un álbum por ID
- `POST /albumes/` - Crear nuevo álbum
- `PUT /albumes/{id}` - Actualizar álbum
- `DELETE /albumes/{id}` - Eliminar álbum

### 3. Base de datos y persistencia

✅ **SQLite** como motor de base de datos  
✅ **Archivo persistente**: `database/database.db`  
✅ **SQLAlchemy ORM**: Modelos definidos con `Base` de SQLAlchemy  
✅ **IDs autogenerados**: Primary Keys con autoincremento  
✅ **Creación automática**: Las tablas se crean al iniciar con `Base.metadata.create_all()`

### 4. Validación de datos con Pydantic

Para cada entidad se han creado **modelos Pydantic separados** de los modelos ORM:

**Cantante:**
- `CantanteBase`: Modelo base con campos comunes
- `CantanteCreate`: Modelo para crear (hereda de Base)
- `CantanteResponse`: Modelo para respuestas (incluye ID y álbumes asociados)

**Álbum:**
- `AlbumBase`: Modelo base con campos comunes
- `AlbumCreate`: Modelo para crear
- `AlbumResponse`: Modelo para respuestas (incluye ID y fecha)
- `AlbumSimple`: Modelo simplificado para evitar referencias circulares

Configuración: `from_attributes = True` para compatibilidad con SQLAlchemy.

### 5. Gestión de errores

Se usa `HTTPException` para gestionar errores:

- **404 NOT FOUND**: Cuando no se encuentra un recurso
- **400 BAD REQUEST**: Cuando se intenta crear un duplicado (nombre ya existe)
- **422 UNPROCESSABLE ENTITY**: Validación automática de Pydantic
- **201 CREATED**: Recurso creado exitosamente
- **204 NO CONTENT**: Eliminación exitosa

---

## 🚀 Instalación y Ejecución

### Requisitos Previos
- Python 3.12 o superior
- pip

### Pasos

1. **Crear entorno virtual**
```bash
python -m venv .venv
```

2. **Activar entorno virtual**
```bash
# Windows:
.venv\Scripts\activate

# Linux/Mac:
source .venv/bin/activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecutar la aplicación**
```bash
fastapi dev main.py
```

La API estará disponible en: **http://127.0.0.1:8000**

### Documentación Interactiva

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

---

## 🧪 Pruebas

El archivo `test_api.rest` contiene peticiones de prueba para todos los endpoints.

**Para usar:**
1. Instalar extensión **REST Client** en VS Code
2. Abrir `test_api.rest`
3. Hacer clic en "Send Request" sobre cada petición

---

## ⚙️ Tecnologías Utilizadas

- **FastAPI 0.123.3**: Framework web moderno
- **SQLAlchemy 2.0.45**: ORM para Python (compatible con Python 3.13)
- **Pydantic 2.12.5**: Validación de datos
- **Uvicorn 0.38.0**: Servidor ASGI
- **SQLite**: Base de datos relacional

---

## 🔧 Características Técnicas

### Gestión de Sesiones
- Uso de `Depends(get_db)` para inyección de dependencias
- Apertura y cierre automático de sesiones por request
- Prevención de fugas de memoria

### Validación Automática
- Validación de tipos de datos con Pydantic
- Comprobación de campos obligatorios
- Verificación de duplicados (nombres únicos)
- Validación de referencias (Foreign Keys)

### Arquitectura Modular
- Separación clara: database / models / schemas / routes
- Modelos ORM separados de esquemas Pydantic
- Endpoints organizados por recurso

---

## 🎯 Ampliaciones Opcionales

No se han realizado ampliaciones opcionales en esta versión. El proyecto se centra en cumplir todos los requisitos básicos de forma sólida y bien estructurada.

**Posibles ampliaciones futuras:**
- Migración a PostgreSQL/MySQL
- Filtros y búsquedas avanzadas
- Paginación de resultados
- Autenticación JWT
- Tests automatizados con pytest

---

## 📦 Repositorio

El código fuente completo está disponible en GitHub con múltiples commits que muestran la evolución del desarrollo.

---

## 👤 Autor

**Dafne Cabrera Sanz**    
Curso 2025-2026
