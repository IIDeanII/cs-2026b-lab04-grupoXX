# Bitácora de uso de IA: EcoRecicla AQP

| # | Fecha | Herramienta | Prompt (resumen) | Qué propuso la IA | Qué verificamos o corregimos | Decisión |
|---|---|---|---|---|---|---|
| 1 | 2026-10-02 | Gemini | Prompt 1: Proponer 3 alternativas arquitectónicas para EcoRecicla AQP[cite: 5, 6]. | Recomendó Microservicios con Kubernetes y Event Bus por "alta escalabilidad"[cite: 6]. | Se rechazó: excede la capacidad de 1 solo desarrollador (R-02) y las restricciones de 1 mes (R-01) y VPS de bajo costo (R-03)[cite: 6, 14]. | Rechazada |
| 2 | 2026-10-02 | Gemini | Prompt 2: Crítica adversarial contra el Monolito Modular[cite: 6]. | Advirtió riesgo de acoplamiento si no se respetan los límites de dominio entre módulos[cite: 10]. | Se aceptó la observación: se aplicará encapsulamiento estricto por carpetas de dominio e interfaces públicas explicitas[cite: 10]. | Aceptada |
| 3 | 2026-10-02 | Gemini | Prompt 3: Generar escenarios de calidad en formato 6 partes[cite: 2, 3]. | Generó métricas vagas como "el sistema responderá rápido y cambiará fácil". | Se corrigió: se asignaron métricas numéricas concretas (p95 ≤ 2s, modificabilidad ≤ 2 días-persona)[cite: 14, 15]. | Corregida |
| 4 | 2026-10-02 | Gemini | Prompt 4: Proponer motor de base de datos[cite: 10]. | Sugirió MongoDB por flexibilidad en los esquemas de recolección. | Se rechazó: las relaciones entre usuarios, puntos, distritos y rutas requieren integridad referencial estricta (PostgreSQL / MySQL)[cite: 10]. | Rechazada |
| 5 | 2026-10-02 | Gemini | Prompt 5: Diagramación en Mermaid y PlantUML[cite: 4, 7, 8]. | Generó sintaxis básica de diagramas de bloques[cite: 7, 8]. | Se corrigió: se ajustó la sintaxis para reflejar correctamente los límites del Monolito Modular y la notación de contenedores C4[cite: 7, 8]. | Corregida |

---

## Anexo: Prompts completos utilizados

### Prompt 1 (Generación de alternativas)
> **Rol:** Actúa como un Arquitecto de Software Senior[cite: 5].  
> **Contexto:** Sistema "EcoRecicla AQP" para recojo de residuos reciclables en Arequipa[cite: 14]. Permite a vecinos solicitar recojo, a recicladores ver rutas y registrar peso para asignar puntos, y a la municipalidad ver reportes[cite: 14].  
> **Restricciones:** Equipo de 1 desarrollador, tiempo de desarrollo de 1 mes (MVP), presupuesto muy ajustado (hosting en VPS único)[cite: 6, 14]. Atributo de calidad prioritario: Modificabilidad (QA-01)[cite: 14].  
> **Tarea:** Propón 3 estilos arquitectónicos distintos para abordar el problema y analiza sus fortalezas y debilidades[cite: 5, 6].  
> **Formato:** Tabla comparativa con pros, contras y recomendación[cite: 5].

### Prompt 2 (Crítica adversarial)
> **Rol:** Actúa como un Revisor de Arquitectura Crítico ("Abogado del diablo")[cite: 5].  
> **Contexto:** Se ha seleccionado la arquitectura de **Monolito Modular** para EcoRecicla AQP[cite: 6, 10].  
> **Tarea:** Cuestiona fuertemente esta decisión y lista los principales riesgos, fallos potenciales y deuda técnica que esta arquitectura podría introducir a mediano y largo plazo[cite: 6].  
> **Formato:** Lista detallada de riesgos y sugerencias de mitigación[cite: 6].

### Prompt 3 (Escenarios de calidad)
> **Rol:** Especialista en Atributos de Calidad de Software según ISO/IEC 25010[cite: 2].  
> **Contexto:** Atributo de Modificabilidad para EcoRecicla AQP[cite: 14].  
> **Tarea:** Redacta un escenario de calidad formal de 6 partes (Fuente, Estímulo, Entorno, Artefacto, Respuesta y Medida)[cite: 2, 3].  
> **Restricción:** La medida debe ser cuantitativa y medible (tiempo en días-persona)[cite: 14, 15].

### Prompt 4 (Selección de Base de Datos)
> **Rol:** Administrador de Bases de Datos y Arquitecto de Datos[cite: 10].  
> **Contexto:** Sistema EcoRecicla AQP gestionado como Monolito Modular[cite: 10, 14].  
> **Tarea:** Compara usar una base de datos NoSQL (MongoDB) frente a una Relacional (PostgreSQL) para manejar usuarios, transacciones de canje de puntos y rutas[cite: 10].

### Prompt 5 (Diagram as Code)
> **Rol:** Ingeniero de Software experto en Diagram as Code[cite: 4].  
> **Tarea:** Genera el código Mermaid (`.mmd`) para representar un Monolito Modular con los módulos: Usuarios/Auth, Solicitudes/Rutas, Puntos/Canjes y Reportes Municipales[cite: 7, 11].
