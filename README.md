# EcoRecicla AQP — Plataforma de Reciclaje Inclusivo (MVP)

> **Proyecto Universitario:** Arquitectura de Software  
> **Caso de Estudio:** Sistema de recojo y gestión de reciclaje para la ciudad de Arequipa, Perú.  
> **Modalidad:** MVP de 1 mes (Desarrollador Individual).

---

## 📌 Visión General del Proyecto

**EcoRecicla AQP** es una solución digital diseñada para optimizar la cadena de recolección de residuos reciclables en Arequipa. Permite a los vecinos programar solicitudes de recojo, a los recicladores formalizados optimizar sus rutas y pesajes, y a la municipalidad acceder a reportes consolidados sobre toneladas recicladas.

---

## 🏛️ Estilo Arquitectónico

Se ha seleccionado una arquitectura de **Monolito Modular** desplegada en un unico servidor VPS de bajo costo.

* **Drivers Clave:** Velocidad de desarrollo (1 desarrollador en 1 mes) y Modificabilidad (`QA-01`), permitiendo aislar la lógica de cada dominio.
* **Módulos Backend:**
  1. **Usuarios y Autenticación:** Registro, roles y privacidad de datos.
  2. **Solicitudes y Rutas:** Programación e itinerario de recicladores.
  3. **Puntos y Canjes:** Cálculo de beneficios y catálogo de premios.
  4. **Reportes y Métricas:** Indicadores de impacto ambiental por distrito.

---

## 📂 Estructura de Entregables de Arquitectura

Toda la documentación arquitectónica se encuentra organizada dentro de la carpeta `docs/architecture/`:

| Entregable | Ubicación / Archivo | Descripción |
| :--- | :--- | :--- |
| **E1: Drivers de Arquitectura** | [`docs/architecture/drivers.md`](docs/architecture/drivers.md) | Atributos de calidad (QA), restricciones (R) y decisiones de negocio (CON). |
| **E2: Matriz de Decisión** | [`docs/architecture/matriz-decision.md`](docs/architecture/matriz-decision.md) | Evaluación comparativa de alternativas arquitectónicas. |
| **E3: Diagrama de Arquitectura** | [`docs/architecture/diagramas/arquitectura.mmd`](docs/architecture/diagramas/arquitectura.mmd) | Diagrama del Monolito Modular en Mermaid (`.mmd`). |
| **E4: Registros de Decisión (ADRs)** | [`docs/architecture/adr/`](docs/architecture/adr/) | ADR-001 (Monolito Modular), ADR-002 (Ley N° 29733) y ADR-003 (PostgreSQL). |
| **E5: Alternativa Descartada** | [`docs/architecture/diagramas/alternativa.puml`](docs/architecture/diagramas/alternativa.puml) | Diagrama en PlantUML de la alternativa de Microservicios descartada. |
| **E6: Vista de Despliegue** | [`docs/architecture/diagramas/despliegue.py`](docs/architecture/diagramas/despliegue.py) | Script de Python (Diagrams) para la infraestructura VPS. |
| **E7: Bitácora de Inteligencia Artificial** | [`docs/architecture/bitacora-ia.md`](docs/architecture/bitacora-ia.md) | Registro de prompts, iteraciones y validación de diagramas con IA. |
| **E8: README del Repositorio** | [`README.md`](README.md) | Guía principal del repositorio y navegación. |

---

## 🖼️ Diagramas del Sistema

Las imágenes exportadas de los diagramas se encuentran en la carpeta `docs/architecture/img/`:
- **Diagrama de Arquitectura (Mermaid):** `docs/architecture/img/arquitectura.png`
- **Alternativa Descartada (PlantUML):** `docs/architecture/img/alternativa.png`
- **Diagrama de Despliegue (Python Diagrams):** `docs/architecture/img/despliegue.png`

---

## ⚖️ Normativa y Privacidad de Datos

El diseño del sistema cumple con la **Ley N° 29733 (Ley de Protección de Datos Personales en el Perú)** mediante cifrado TLS 1.3, visibilidad restringida de direcciones de vecinos solo durante rutas activas y mecanismos de consentimiento informado (ver [`ADR-002`](docs/architecture/adr/002-estrategia-privacidad-datos.md)).
