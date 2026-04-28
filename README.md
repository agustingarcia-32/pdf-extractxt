# PDF Text Extractor

## Arquitectura Empresarial con TDD y FastAPI

### Integrantes
- **[GARCIA AGUSTÍN]**
- **[FORQUERA BRIAN]**

---

## Quick Start

```bash
# 1. Sincronizar el proyecto (crea el entorno virtual e instala dependencias)
uv sync

# 2. Configurar variables de entorno
cp .env.example .env  # En Windows: copy .env.example .env
# IMPORTANTE: Editar .env con tus credenciales de MongoDB

# 3. Ejecutar tests (Metodología TDD)
uv run pytest

# 4. Iniciar servidor de desarrollo
# (Ajustado a la ubicación de tu main.py en src/)
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
