# Matriz de decisión: EcoRecicla AQP

## Alternativas consideradas

**A. Monolito en capas:** Sistema tradicional dividido en presentación, lógica de negocio y acceso a datos[cite: 3]. Un solo despliegue[cite: 3].
**B. Microservicios:** Servicios independientes para Usuarios, Solicitudes, Puntos y Reportes con sus propias bases de datos y API Gateway[cite: 3, 8].
**C. Monolito modular (Elegido):** Un solo despliegue dividido en módulos de dominio desacoplados con interfaces públicas explícitas[cite: 3, 10].

---

## Criterios y pesos (Suma: 100%)

| Criterio | Peso | Justificación (Driver relacionado) |
|---|---|---|
| Modificabilidad | 30% | Atributo crítico (QA-01): agregar distritos o reglas de puntos en ≤ 2 días-persona[cite: 14]. |
| Tiempo de entrega | 25% | Restricción R-01: el MVP debe estar en producción en 1 mes por 1 solo desarrollador[cite: 14]. |
| Simplicidad operativa | 20% | Restricción R-02 y R-03: desarrollo individual y despliegue en VPS de bajo costo[cite: 6, 14]. |
| Costo de hosting | 15% | Restricción R-03: presupuesto reducido[cite: 6, 14]. |
| Escalabilidad | 10% | Carga moderada y predecible en distritos iniciales de Arequipa[cite: 6, 14]. |

---

## Matriz de evaluación (Puntaje de 1: Muy malo a 5: Excelente)

| Criterio (peso) | A. Monolito en Capas | B. Microservicios | C. Monolito Modular |
|---|---|---|---|
| Modificabilidad (30%) | 2 | 5 | 4 |
| Tiempo de entrega (25%) | 5 | 2 | 4 |
| Simplicidad operativa (20%) | 5 | 1 | 4 |
| Costo de hosting (15%) | 5 | 2 | 5 |
| Escalabilidad (10%) | 2 | 5 | 3 |
| **Total ponderado** | **3.80** | **2.85** | **4.15** |

*Cálculo de C (Monolito modular):* $(0.30 \times 4) + (0.25 \times 4) + (0.20 \times 4) + (0.15 \times 5) + (0.10 \times 3) = 1.20 + 1.00 + 0.80 + 0.75 + 0.30 = 4.15$

---

## Conclusión

Se elige el **Monolito Modular** con un puntaje de **4.15**, ya que ofrece el balance perfecto entre alta modificabilidad para agregar distritos/puntos sin romper otros módulos, y la simplicidad operacional requerida para un desarrollador individual en un plazo de 1 mes[cite: 3, 6, 10, 14]. Para más detalles, ver el [ADR-001](adr/001-estilo-arquitectonico.md)[cite: 10, 12].
