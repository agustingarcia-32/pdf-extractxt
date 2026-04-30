---
name: "Estructura Inicial"
about: "Boilerplate inicial del proyecto"
title: "[Setup]: Estructura Inicial"
labels: ["setup"]
assignees: ""

---

## Objetivo

Crear el boilerplate inicial del proyecto siguiendo:

- Arquitectura Empresarial (3 capas): API / Core / Infrastructure
- TDD: Estructura de tests espejada
- 12-Factor App: Configuración via environment
- Clean Architecture con principios SOLID

## Especificaciones

- [ ] Stack: Python + FastAPI + uv
- [ ] Persistencia: MongoDB (NoSQL)
- [ ] Funcionalidad: Extracción texto PDF (sin almacenamiento temporal)
- [ ] Validación: Formato y tamaño
- [ ] Control duplicados: Checksum SHA-256

## Estructura de Carpetas

```
src/
├── api/           # Capa de Entrada
├── core/          # Capa de Negocio
└── infrastructure/# Capa de Datos

tests/
├── api/
├── core/
└── infrastructure/
```

## Entregables

- [ ] pyproject.toml con uv
- [ ] .env.example (12-Factor Config)
- [ ] README.md raíz
- [ ] READMEs por capa
- [ ] Código base de cada capa
- [ ] Tests estructura