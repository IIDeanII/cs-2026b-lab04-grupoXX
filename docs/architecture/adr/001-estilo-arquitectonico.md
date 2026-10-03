# ADR-001: Selección del estilo arquitectónico Monolito Modular

## Estado
Aceptado

## Contexto
Para la plataforma "EcoRecicla AQP" se requiere un sistema que permita a los vecinos solicitar recojo de reciclaje, a los recicladores gestionar sus rutas y puntos, y a la municipalidad consultar reportes. 

Contamos con las siguientes restricciones operativas y de negocio:
- **Equipo:** 1 solo desarrollador.
- **Plazo:** MVP operativo en 1 mes.
- **Infraestructura:** Presupuesto bajo para hosting en un único servidor VPS.
- **Driver crítico:** Modificabilidad (QA-01) para añadir nuevos distritos o cambiar reglas de canje en ≤ 2 días-persona sin afectar otros módulos.

Se evaluaron tres alternativas: Monolito en Capas, Microservicios y Monolito Modular.

## Decisión
Aceptamos adoptar una arquitectura de **Monolito Modular**.

El backend se desplegará como un único artefacto ejecutable en el VPS, pero el código fuente estará organizado internamente en módulos de dominio desacoplados (Usuarios, Solicitudes, Puntos y Reportes) con interfaces públicas bien definidas y comunicación *in-process*.

## Consecuencias

### Positivas
- **Simplicidad de despliegue:** Un único proceso en un solo VPS, manteniendo bajos los costos de hosting y eliminando la complejidad de redes de microservicios.
- **Alta modificabilidad:** Los módulos tienen límites explícitos, permitiendo agregar distritos o modificar el esquema de puntos aisladamente.
- **Velocidad de desarrollo:** Ideal para ser construido por 1 desarrollador en el plazo de 1 mes.

### Negativas / Riesgos
- **Riesgo de acoplamiento paulatino:** Si no se respeta el encapsulamiento de cada módulo, puede terminar convirtiéndose en un "Monolito Big Ball of Mud".
  * *Mitigación:* Definir interfaces/servicios de módulo explícitos y restringir el acceso directo a bases de datos entre módulos.
