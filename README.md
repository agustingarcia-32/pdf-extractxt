# PDF Text Extractor

## Arquitectura Empresarial con TDD y FastAPI

### Integrantes
- **[GARCIA AGUSTÍN]**
- **[FORQUERA BRIAN]**

---

## Instrucciones para Ejecución
```bash
Para que la aplicación funcione correctamente en su entorno local, siga estos pasos:

### 1. Clonar el repositorio
```bash
git clone <URL_DE_VUESTRO_REPOSITORIO>
cd PDF-TEXT-EXTRACTOR

2. Instalación de dependencias con uv
Utilizamos uv para garantizar que las versiones de las librerías sean idénticas en cualquier computadora.
# Sincroniza el entorno virtual e instala todas las dependencias
uv sync

3. Configuración de Variables de Entorno
El sistema requiere una conexión a MongoDB y claves de configuración.
# Crear el archivo .env a partir de la plantilla
cp .env.example .env  # En Windows: copy .env.example .env

# IMPORTANTE: Abrir el archivo .env y completar los valores de:
# MONGODB_URL (ej: mongodb://localhost:27017)
# DATABASE_NAME

4. Ejecución de la Suite de Tests (TDD)
Antes de iniciar el servidor, puede verificar que todos los requisitos funcionales pasan las pruebas:
uv run pytest

5. Iniciar Servidor de Desarrollo
Una vez configurado el entorno, ejecute el siguiente comando para levantar la API:
uv run uvicorn src.main:app --reload
```
## Arquitectura Elegida
Este proyecto implementa Clean Architecture estructurada en las 3 capas que se observan en nuestro directorio src/:

API (Entrada): Manejo de protocolos HTTP, validación de esquemas (Pydantic) y gestión de errores.

Core (Negocio): Casos de uso y lógica de dominio independiente de herramientas externas.

Infrastructure (Datos): Implementaciones concretas de base de datos NoSQL y cliente de extracción de PDF.

Principios de Ingeniería Aplicados
TDD (Test Driven Development): Estructura de pruebas espejo en la carpeta tests/.

SOLID & Clean Code: Responsabilidad única y código legible.

12-Factor App: Gestión de configuración externa.

Workflow Profesional: Uso de ISSUE_TEMPLATE y pull_request_template en .github/.

## Estructura del Proyecto (VS Code Tree)
```
PDF-TEXT-EXTRACTOR/
├── .github/                # Configuración de GitHub (Templates de PR e Issues)
├── src/                    # Código fuente
│   ├── api/                # Capa de Presentación
│   │   ├── endpoints/      # Rutas de la API
│   │   ├── errors/         # Custom Exception Handlers
│   │   └── schemas/        # DTOs y validaciones
│   ├── core/               # Capa de Dominio
│   │   ├── entities/       # Modelos de negocio
│   │   ├── services/       # Lógica técnica (Checksum)
│   │   └── use_cases/      # Orquestación de procesos
│   ├── infrastructure/     # Capa de Datos
│   │   ├── database/       # Conexión NoSQL
│   │   ├── pdf_client/     # Extractor de texto
│   │   └── repositories/   # Patrón Repositorio
│   └── main.py             # Punto de entrada de la aplicación
├── tests/                  # Suite de pruebas (api, core, infrastructure)
├── .env.example            # Configuración de entorno
├── pyproject.toml          # Dependencias (uv)
└── README.md
```
## Tests con cobertura
uv run pytest --cov=src

## Linter y Formateo
uv run ruff check src/
