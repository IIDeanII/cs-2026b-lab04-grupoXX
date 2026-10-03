# ADR-003: Selección del motor de base de datos relacional (PostgreSQL)

## Estado
Aceptado

## Contexto
El sistema "EcoRecicla AQP" gestiona relaciones complejas entre entidades: usuarios (vecinos, recicladores y administradores), solicitudes de recojo, rutas asignadas por distrito, registro de pesajes y saldo de puntos para canjes.

Se requiere garantizar la consistencia de los datos, especialmente en la asignación de puntos por reciclaje y el catálogo de premios, así como la posibilidad de realizar consultas agregadas para los reportes municipales.

Se evaluaron dos alternativas:
- **NoSQL (MongoDB):** Proporciona esquemas flexibles pero carece de soporte nativo simple para transacciones complejas entre colecciones.
- **Relacional (PostgreSQL / MySQL):** Ofrece integridad referencial estricta, cumplimiento ACID y consultas relacionales complejas via SQL/ORM.

## Decisión
Aceptamos utilizar un motor de base de datos relacional (**PostgreSQL**).

El Monolito Modular utilizará esquemas o tablas con relaciones explícitas (claves foráneas y restricciones) para garantizar la integridad de las transacciones de puntos y la consistencia de las solicitudes de recojo.

## Consecuencias

### Positivas
- **Integridad de datos:** Garantía ACID en transacciones críticas como el canje de puntos y el registro de pesaje de residuos.
- **Facilidad de consultas agregadas:** Las métricas y reportes para la municipalidad (toneladas recicladas por distrito) se calculan de forma eficiente con SQL.
- **Soporte de ORM:** Excelente integración con ORMs populares (Prisma, TypeORM, SQLAlchemy) que agilizan el desarrollo de 1 solo programador.

### Negativas / Riesgos
- **Rigidez en cambios de esquema:** Modificar la estructura de tablas requiere migraciones formales de base de datos.
  * *Mitigación:* Utilizar herramientas de migración automatizadas integradas en el framework elegido.
