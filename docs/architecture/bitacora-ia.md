# Bitácora de uso de IA: EcoRecicla AQP

| # | Fecha | Herramienta | Prompt (resumen) | Qué propuso la IA | Qué verificamos o corregimos | Decisión |
|---|---|---|---|---|---|---|
| 1 | 2026-10-02 | ChatGPT / Claude / Gemini | Prompt 1: Proponer 3 alternativas arquitectónicas para EcoRecicla AQP[cite: 5, 6]. | Recomendó Microservicios con Kubernetes y Event Bus por "alta escalabilidad"[cite: 6]. | Se rechazó: excede la capacidad de 1 solo desarrollador (R-02) y la restricción de 1 mes (R-01) y VPS de bajo costo (R-03)[cite: 6, 14]. | Rechazada |
| 2 | 2026-10-02 | ChatGPT / Claude / Gemini | Prompt 2: Crítica adversarial contra el Monolito Modular[cite: 6]. | Advirtió riesgo de acoplamiento si los desarrolladores no respetan los límites entre módulos[cite: 10]. | Se aceptó la observación y se decidió añadir reglas de linter/arquitectura en la integración[cite: 10]. | Aceptada |

---

## Anexo: Prompts completos

### Prompt 1 (Generación de alternativas)
> Actúa como arquitecto de software senior. Contexto: plataforma "EcoRecicla AQP" para recojo de residuos reciclables en Arequipa[cite: 5, 14]. Vecinos solicitan recojo, recicladores ven rutas y ganan puntos, municipalidad ve reportes[cite: 14].
> Restricciones: 1 solo desarrollador, plazo de 1 mes (MVP), presupuesto bajo (VPS único)[cite: 6, 14]. Atributo crítico: Modificabilidad (QA-01)[cite: 14].
> Tarea: propón 3 estilos arquitectónicos, analiza sus fortalezas/debilidades y da una matrizEntendido, tomo nota. Adaptaremos todo el desarrollo para que esté enfocado de forma **individual**.

Dime, ¿en qué punto o tema específico de la práctica te gustaría que empecemos a trabajar?
