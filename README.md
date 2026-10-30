# Laboratorio 6: API REST con Django REST Framework 🍽️

Proyecto colaborativo desarrollado para el **Laboratorio 6**, enfocado en la construcción de servicios web tipo REST utilizando Django y Django REST Framework (DRF). En esta etapa, los endpoints están construidos mediante **vistas basadas en funciones (FBV)** con el decorador `@api_view` y `Response`, trabajando sobre estructuras de datos en memoria (listas de diccionarios en Python).

---

## 🎯 Temática: Sistema de Gestión de Restaurante / Cafetería

El proyecto modela el catálogo y la operación básica de un restaurante o cafetería, distribuyendo las responsabilidades en recursos independientes asignados a cada integrante del equipo.

### Distribución de Recursos por Integrante

| Integrante | Rol | Recurso Asignado | Campos del Recurso | Endpoints |
| :--- | :--- | :--- | :--- | :--- |
| **Joaquín Michea** | Anfitrión | **Plato** | `id`, `nombre`, `precio`, `categoria` | `GET /api/platos/`<br>`POST /api/platos/` |
| **Integrante 2** | Desarrollador | **Chef** | `id`, `nombre`, `especialidad`, `experiencia_anios` | `GET /api/chefs/`<br>`POST /api/chefs/` |
| **Integrante 3** | Desarrolladora/or | **Categoría** | `id`, `nombre`, `descripcion` | `GET /api/categorias/`<br>`POST /api/categorias/` |

---

## 🛠️ Tecnologías y Requisitos

* **Python:** 3.10+ (probado en Python 3.13)
* **Django:** 6.1+
* **Django REST Framework:** 3.18+

---

## 🚀 Instalación y Ejecución Local

Para levantar el proyecto en tu entorno local, sigue estos pasos:

### 1. Clonar el repositorio
```bash
git clone https://github.com/jimm-96/lab6_APIRestDjango.git
cd lab6_APIRestDjango
```

### 2. Crear y activar el entorno virtual

* **En Windows (PowerShell):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
* **En Linux / macOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

El servidor estará accesible en: `http://127.0.0.1:8000/`

---

## 📡 Documentación de Endpoints

### 1. Recurso: Platos (`/api/platos/`)
* **GET `/api/platos/`**: Retorna la lista completa de platos disponibles.
* **POST `/api/platos/`**: Registra un nuevo plato en la lista.
  * **Payload esperado (JSON):**
    ```json
    {
      "nombre": "Pastel de Choclo",
      "precio": 8500,
      "categoria": "Fondos"
    }
    ```

### 2. Recurso: Chefs (`/api/chefs/`)
* **GET `/api/chefs/`**: Retorna la lista del equipo de cocina.
* **POST `/api/chefs/`**: Agrega un nuevo chef al equipo.
  * **Payload esperado (JSON):**
    ```json
    {
      "nombre": "Auguste Escoffier",
      "especialidad": "Cocina Clásica Francesa",
      "experiencia_anios": 15
    }
    ```

### 3. Recurso: Categorías (`/api/categorias/`)
* **GET `/api/categorias/`**: Retorna las categorías del menú.
* **POST `/api/categorias/`**: Registra una nueva categoría.
  * **Payload esperado (JSON):**
    ```json
    {
      "nombre": "Postres",
      "descripcion": "Dulces tradicionales y repostería artesanal"
    }
    ```

---

## 🌿 Flujo de Trabajo Git y Commits Incrementales

El equipo sigue una metodología de trabajo colaborativo basada en ramas individuales y Pull Requests hacia `main`:

1. Crear y cambiarse a una rama propia:
   ```bash
   git checkout -b feature/recurso-<nombre-recurso>
   ```
2. Cada integrante realiza al menos **4 commits incrementales** para su recurso:
   * **Commit 1:** Definición de la lista de datos de ejemplo en memoria.
   * **Commit 2:** Implementación del endpoint `GET` con `@api_view(['GET'])` y `Response`.
   * **Commit 3:** Implementación del endpoint `POST` con `@api_view(['POST'])` para agregar registros.
   * **Commit 4:** Conexión de rutas en `urls.py` y verificación en la interfaz navegable de DRF.
3. Subir la rama a GitHub y abrir un **Pull Request** para revisión y posterior integración a `main`.

