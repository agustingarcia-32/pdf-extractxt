# Capa Infrastructure (Capa de Datos)

## Propósito

Esta capa implementa las abstracciones definidas en la capa de-core (repositorios, clientes externos). Maneja la persistencia de datos y la integración con sistemas externos.

## ¿Por Qué Está Aislada?

1. **Separación de la Lógica de Datos**: La lógica de negocio no necesita saber cómo se guardan los datos. Solo conoce las interfaces (protocolos).

2. **Reemplazabilidad**: Puedes cambiar de MongoDB a CouchDB, o de pypdf a pdfplumber sin modificar la lógica de negocio.

3. **Inversión de Dependencias**: La capa core define abstracciones, infrastructure las implementa.

## Componentes

```
infrastructure/
├── database/       # Conexión y configuración MongoDB
├── repositories/   # Implementación del patrón Repository
└── pdf_client/     # Cliente de extracción de PDF
```

## Implementaciones

- **MongoDBRepository**: Persistencia de documentos extraídos
- **PyPDFClient**: Extracción de texto usando pypdf

## Principios

- **Repository Pattern**: Abstrae el acceso a datos
- **Adapter Pattern**: Adapta bibliotecas externas
- **Configuration**: Conexiones configurables via environment