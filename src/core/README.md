# Capa Core (Capa de Negocio)

## Propósito

Esta capa contiene toda la lógica de negocio de la aplicación. Es el corazón del sistema y no tiene conocimiento de cómo se persisten los datos ni cómo se reciben las solicitudes.

## ¿Por Qué Está Aislada?

1. **Independencia de Infraestructura**: La lógica de negocio no sabe si usas MongoDB, PostgreSQL, o un archivo CSV. Los cambios en la base de datos no afectan esta capa.

2. **Principios SOLID Aplicados**:
   - **S**ingle Responsibility: Cada caso de uso tiene una responsabilidad única
   - **O**pen/Closed: Extiende funcionalidad sin modificar código existente
   - **L**iskov Substitution: Las abstracciones permiten sustitución
   - **I**nterface Segregation: Mínimos métodos necesarios
   - **D**ependency Inversion: Depende de abstracciones, no de concreciones

3. **Testabilidad**: Puedes probar toda la lógica sin mockear base de datos ni servidores HTTP.

## Componentes

```
core/
├── use_cases/    # Casos de uso (extraer texto, validar, checksum)
├── entities/     # Entidades del dominio (PDFDocument, Checksum)
└── services/     # Servicios de negocio (resumen, validación)
```

## Casos de Uso Principales

1. **ExtractTextUseCase**: Extrae texto de un PDF sin almacenamiento temporal
2. **CalculateChecksumUseCase**: Calcula SHA-256 del contenido
3. **ValidatePDFUseCase**: Valida formato y tamaño
4. **CheckDuplicateUseCase**: Control de duplicados por checksum

## Ejemplo de Flujo

```
API Layer → Use Case → Entity (domain logic) → Service → Repository Interface → Infrastructure
```

## Principios

- **Domain-Driven Design**: Las entidades representan el dominio real
- **DRY**: Lógica centralizada, no duplicada
- **Sin dependencias externas**: Solo usa abstracciones (protocolos)