# API de Gestión Musical - Cantantes y Álbumes

API REST desarrollada con FastAPI y SQLite para administrar cantantes y sus álbumes.

**Autor:** Dafne Cabrera Sanz

---

## 🗂️ Entidades

### Cantante
- `id`, `nombre`, `edad`, `genero_musical`, `oyentes_mensuales_spotify`, `activo`

### Álbum
- `id`, `nombre`, `cantante_id`, `precio`, `fecha_lanzamiento`, `genero`

Relación: Un cantante → Múltiples álbumes (1:N)

---

## 📁 Estructura del Proyecto

```
CabreraSanz_Dafne_p3.1/
├── main.py                      # Punto de entrada de la aplicación
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este archivo
├── test_api.rest                # Pruebas de endpoints (REST Client)
├── .gitignore                   # Archivos a ignorar en git
├── database/
│   ├── __init__.py
│   ├── database.py              # Configuración de SQLAlchemy y SQLite
│   └── database.db              # Base de datos persistente (generado automáticamente)
├── models/
│   ├── __init__.py
│   ├── cantante.py              # Modelo ORM de Cantante
│   └── album.py                 # Modelo ORM de Álbum
├── schemas/
│   ├── __init__.py
│   ├── cantante.py              # Esquemas Pydantic para Cantante
│   └── album.py                 # Esquemas Pydantic para Álbum
└── routes/
    ├── __init__.py
    ├── cantantes.py             # Endpoints CRUD de Cantantes
    └── albumes.py               # Endpoints CRUD de Álbumes
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

**GET, POST, PUT, DELETE** disponibles para `/cantantes` y `/albumes`

### Base de datos
- SQLite con persistencia en `database/database.db`
- SQLAlchemy ORM con creación automática de tablas
- IDs autogenerados
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

- **FastAPI**: Framework web moderno y rápido
- **SQLAlchemy**: ORM para Python
- **Pydantic**: Validación de datos
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
- Modo ORM habilitado con `orm_mode = True`

### Arquitectura Modular
- Separación clara: database / models / schemas / routes
- Modelos ORM separados de esquemas Pydantic
- Endpoints organizados por recurso

---

## 🎯 Ampliaciones Opcionales

Usa `test_api.rest` con la extensión REST Client de VS Code.

---

## ⚙️ Tecnologías

- FastAPI
- SQLAlchemy
- Pydantic
- SQLite