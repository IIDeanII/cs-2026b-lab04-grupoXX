# Drivers arquitectónicos: EcoRecicla AQP

## 1. Requisitos funcionales clave

| ID    | Requisito                                                                                                                          | Actor         | Prioridad |
|-------|------------------------------------------------------------------------------------------------------------------------------------|---------------|-----------|
| RF-01 | Solicitar recojo de residuos reciclables indicando tipo de material, ubicación y horario.                                          | Vecino        | Alta      |
| RF-02 | Visualizar la ruta de recojo asignada para el día y actualizar el estado de las solicitudes.                                       | Reciclador    | Alta      |
| RF-03 | Consultar y canjear puntos acumulados por kilogramo de material reciclado entregado.                                               | Vecino        | Alta      |
| RF-04 | Generar reportes agregados de toneladas recicladas por distrito y tipo de material.                                                | Municipalidad | Media     |
| RF-05 | Registrar y gestionar distritos participantes, recicladores formalizados y catálogo de materiales con sus equivalencias en puntos. | Municipalidad | Alta      |

---

## 2. Atributos de calidad (ordenados por prioridad)

1. **Modificabilidad (Atributo Crítico):** Es fundamental adaptar el sistema para incorporar rápidamente nuevos distritos de Arequipa o modificar el esquema de asignación de puntos sin afectar el núcleo del sistema ni romper otros módulos operacionales.
2. **Capacidad de interacción / Usabilidad (Usability):** Los recicladores realizan sus tareas en campo usando dispositivos móviles; la interfaz debe ser simple e intuitiva para minimizar errores durante la recolección.
3. **Disponibilidad (Availability):** Las solicitudes de recojo y la consulta de rutas deben estar operativas durante las horas de trabajo municipal y de recolección (6:00 a. m. a 8:00 p. m.).
4. **Seguridad (Security):** Garantizar la privacidad y protección de los datos de localización e identidad de los vecinos y recicladores según la normativa vigente.

---

## 3. Restricciones

| ID   | Tipo        | Restricción                                                                                 |
|------|-------------|---------------------------------------------------------------------------------------------|
| R-01 | Plazo       | El MVP debe estar en producción en un plazo máximo de 1 mes.                                |
| R-02 | Equipo      | Equipo reducido de 1 desarrollador con dominio en tecnologías web/móviles estándar.         |
| R-03 | Presupuesto | Presupuesto bajo; infraestructura desplegada en un único servidor VPS de costo reducido.    |
| R-04 | Normativa   | Cumplimiento estricto de la Ley N° 29733 de Protección de Datos Personales en el Perú.      |

---

## 4. Escenarios de atributos de calidad

| ID | Atributo | Fuente | Estímulo | Entorno | Artefacto | Respuesta | Medida |
|---|---|---|---|---|---|---|---|
| QA-01 | Modificabilidad | Administrador municipal | Solicita agregar un nuevo distrito o cambiar la regla de canje de puntos | Fase de mantenimiento / desarrollo | Módulo de Puntos y Módulo de Distritos | El desarrollador implementa e integra el cambio mediante reglas/configuración aislada | Tiempo de desarrollo e integración ≤ 2 días-persona, con 0 modificaciones en los demás módulos. |
| QA-02 | Capacidad de interacción | Reciclador formalizado | Registra el peso recolectado y confirma la entrega | Operativo en campo (dispositivo móvil de gama baja) | Aplicación Móvil / PWA | La aplicación registra la transacción y actualiza los puntos del vecino | Proceso completado en ≤ 3 toques en la pantalla de la aplicación. |
| QA-03 | Disponibilidad | Vecinos de Arequipa | Realizan 500 solicitudes de recojo concurrentes | Hora pico (7:00 a. m. - 9:00 a. m.) | Módulo de Solicitudes | El sistema procesa la solicitud y asigna el turno correspondiente | Tiempo de respuesta p95 ≤ 2 segundos y disponibilidad del servicio ≥ 99.5%. |
