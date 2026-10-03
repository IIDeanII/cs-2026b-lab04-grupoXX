# Bitácora de uso de IA: EcoRecicla AQP

| # | Fecha | Herramienta | Prompt (resumen) | Qué propuso la IA | Qué verificamos o corregimos | Decisión |
|---|---|---|---|---|---|---|
| 1 | 2026-10-02 | Gemini / ChatGPT | Prompt 1: Proponer 3 alternativas arquitectónicas para EcoRecicla AQP. | Recomendó Microservicios con Kubernetes y Event Bus por "alta escalabilidad". | Se rechazó: excede la capacidad de 1 solo desarrollador (R-02) y las restricciones de 1 mes (R-01) y VPS de bajo costo (R-03). | Rechazada |
| 2 | 2026-10-02 | Gemini / ChatGPT | Prompt 2: Crítica adversarial contra el Monolito Modular. | Advirtió riesgo de acoplamiento si no se respetan los límites de dominio entre módulos. | Se aceptó la observación: se aplicará encapsulamiento estricto por carpetas de dominio e interfaces públicas explícitas. | Aceptada |
| 3 | 2026-10-02 | Gemini / ChatGPT | Prompt 3: Generar escenarios de calidad en formato 6 partes. | Generó métricas vagas como "el sistema responderá rápido y cambiará fácil". | Se corrigió: se asignaron métricas numéricas concretas (p95 ≤ 2s, modificabilidad ≤ 2 días-persona). | Corregida |
| 4 | 2026-10-02 | Gemini / ChatGPT | Prompt 4: Proponer motor de base de datos. | Sugirió MongoDB por flexibilidad en los esquemas de recolección. | Se rechazó: las relaciones entre usuarios, puntos, distritos y rutas requieren integridad referencial estricta (PostgreSQL / MySQL). | Rechazada |
| 5 | 2026-10-02 | Gemini / ChatGPT | Prompt 5: Diagramación en Mermaid y PlantUML. | Generó sintaxis básica de diagramas de bloques. | Se corrigió: se ajustó la sintaxis para reflejar correctamente los límites del Monolito Modular y la notación de contenedores C4. | Corregida |

---

## Anexo: Prompts completos utilizados

### Prompt 1 (Generación de alternativas)
> Dame 3 opciones de arquitectura de software para un sistema llamado EcoRecicla AQP en Arequipa. Trata sobre vecinos que piden recojo de reciclaje, recicladores que ven sus rutas y ganan puntos, y la municipalidad que ve reportes. Ojo: soy un solo desarrollador, tengo 1 mes para el MVP y un servidor VPS barato. Prioriza la modificabilidad para agregar distritos fácil.

### Prompt 2 (Crítica adversarial)
> Dame todas las desventajas, riesgos y cosas malas de usar un Monolito Modular para este proyecto de reciclaje. Actúa como un revisor bien estricto y dime en qué puede fallar la arquitectura a futuro si la elijo.

### Prompt 3 (Escenarios de calidad)
> Ayúdame a armar un escenario de calidad para el atributo de modificabilidad en EcoRecicla AQP usando las 6 partes (fuente, estímulo, entorno, artefacto, respuesta y medida). La medida tiene que ser un número concreto en días-persona.

### Prompt 4 (Selección de Base de Datos)
> ¿Qué base de datos me conviene más para EcoRecicla AQP entre MongoDB y PostgreSQL? Considera que el sistema es un monolito modular con usuarios, puntos de canje, rutas y distritos.

### Prompt 5 (Diagram as Code)
> Genera el código en Mermaid para representar un Monolito Modular con los módulos de Usuarios, Solicitudes/Rutas, Puntos/Canjes y Reportes Municipales.
