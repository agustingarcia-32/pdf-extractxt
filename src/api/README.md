# Capa API (Capa de Entrada)

## Propósito

Esta capa actúa como el punto de entrada de la aplicación. Maneja las solicitudes HTTP entrantes, las traduce a llamadas entendibles por la capa de negocio, y formatea las respuestas de vuelta al cliente.

## ¿Por Qué Está Aislada?

1. **Separación de Responsabilidades**: La API no contiene lógica de negocio. Solo se encarga de:
   - Validar entrada (schemas Pydantic)
   - Enrutar solicitudes a los casos de uso apropiados
   - Formatear respuestas HTTP
   - Manejar errores de manera consistente

2. **Acoplamiento Débil**: Si mañana decides cambiar de FastAPI a otro framework (Flask, Django REST), solo necesitas modificar esta capa.

3. **Testabilidad**: Puedes probar la lógica de negocio sin levantar un servidor HTTP.

## Componentes

```
api/
├── endpoints/     # Routers FastAPI (routes, HTTP methods)
├── schemas/       # Modelos Pydantic (request/response DTOs)
└── errors/        # Manejo centralizado de errores
```

## Ejemplo de Flujo

```
HTTP Request → Endpoint → Schema (validation) → Use Case → Response → HTTP Response
```

## Principios

- **Single Responsibility**: Cada endpoint hace UNA cosa
- **DRY**: Esquemas reutilizados cuando es posible
- **Sin lógica de negocio**: Toda la lógica va en `core/`