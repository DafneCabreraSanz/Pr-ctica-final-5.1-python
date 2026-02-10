# API de Gestión Musical - Cantantes y Álbumes

API REST desarrollada con FastAPI y PostgreSQL (Docker) para administrar cantantes y sus álbumes.

**Autor:** Dafne Cabrera Sanz

**GitHub:** https://github.com/DafneCabreraSanz/Pr-ctica-final-5.1-python.git

**Documentación Swagger:** https://api-cantantes.onrender.com/docs

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
CabreraSanz_Dafne_Practica_final_5.1/
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Este archivo
├── test_api.rest                # Pruebas de endpoints (REST Client)
├── .gitignore                   # Archivos a ignorar en git
├── docker-compose.yml           # Orquestacion de servicios
├── Dockerfile                   # Imagen de la API
└── app/
    ├── main.py                  # Punto de entrada de la aplicacion
    ├── database/
    │   ├── __init__.py
    │   └── database.py          # Configuracion de SQLAlchemy
    ├── models/
    │   ├── __init__.py
    │   ├── cantante.py          # Modelo ORM de Cantante
    │   └── album.py             # Modelo ORM de Album
    ├── schemas/
    │   ├── __init__.py
    │   ├── cantante.py          # Esquemas Pydantic para Cantante
    │   └── album.py             # Esquemas Pydantic para Album
    └── routes/
        ├── __init__.py
        ├── cantantes.py         # Endpoints CRUD de Cantantes
        └── albumes.py           # Endpoints CRUD de Albumes
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
- PostgreSQL via Docker Compose (recomendado)
- SQLAlchemy ORM con creacion automatica de tablas
- IDs autogenerados
- Variable `DATABASE_URL` para elegir motor (por defecto usa SQLite)

### Pasos (Docker)

1. **Levantar servicios**
```bash
docker compose up -d
```

La API estara disponible en: **http://127.0.0.1:8000**

### Pasos (local sin Docker)

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

4. **Ejecutar la aplicacion**
```bash
fastapi run app/main.py --port 8000
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
- **PostgreSQL**: Base de datos relacional (Docker)

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
- PostgreSQL

---

## 📸 Capturas de Pantalla

### Desarrollo y Configuración

![Imagen 1](imagenes/WhatsApp%20Image%202026-02-10%20at%2009.29.49.jpeg)

![Imagen 2](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.02.30.jpeg)

![Imagen 3](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.46.37.jpeg)

![Imagen 4](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.47.40.jpeg)

![Imagen 5](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.48.06.jpeg)

![Imagen 6](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.49.23.jpeg)

![Imagen 7](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.49.46.jpeg)

![Imagen 8](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.50.14.jpeg)

![Imagen 9](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.50.36.jpeg)

![Imagen 10](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.51.00.jpeg)

![Imagen 11](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.51.24.jpeg)

![Imagen 12](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.53.21.jpeg)

![Imagen 13](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.55.21.jpeg)

![Imagen 14](imagenes/WhatsApp%20Image%202026-02-10%20at%2010.58.02.jpeg)

![Imagen 15](imagenes/WhatsApp%20Image%202026-02-10%20at%2011.34.21.jpeg)

![Imagen 16](imagenes/WhatsApp%20Image%202026-02-10%20at%2011.47.19.jpeg)

![Imagen 17](imagenes/WhatsApp%20Image%202026-02-10%20at%2011.53.40.jpeg)