# ADR-002: Estrategia de privacidad de datos y cumplimiento de la Ley N° 29733

## Estado
Aceptado

## Contexto
El sistema gestiona información sensible de los ciudadanos de Arequipa, incluyendo nombres, números telefónicos, direcciones exactas de residencia y geolocalización. 

En el Perú rige la **Ley N° 29733 (Ley de Protección de Datos Personales)**, la cual exige garantizar el consentimiento informado, la confidencialidad, la seguridad en el tratamiento de datos y el ejercicio de derechos ARCO (Acceso, Rectificación, Cancelación y Oposición).

## Decisión
Aceptamos implementar los siguientes mecanismos dentro de la arquitectura:
1. **Cifrado en tránsito y reposo:** Comunicaciones protegidas estrictamente mediante HTTPS (TLS 1.3) via Nginx y contraseñas/tokens hasheados con algoritmos robustos (Argon2 / bcrypt).
2. **Aislamiento de la ubicación:** Las direcciones y ubicaciones GPS de los vecinos solo serán visibles para el reciclador cuando la solicitud de recojo esté asignada y activa en su ruta del día.
3. **Consentimiento explícito:** Registro formal del consentimiento en la PWA durante el registro de usuarios.
4. **Módulo de borrado/anonimización:** Mecanismo en el modulo de Usuarios para anonimizar los datos históricos de un vecino cuando ejerza su derecho de cancelación.

## Consecuencias

### Positivas
- Cumplimiento estricto con la normativa peruana vigente, evitando multas o sanciones legales para el proyecto municipal.
- Aumento de la confianza de los vecinos al compartir su ubicación para el recojo de reciclaje.

### Negativas / Riesgos
- Ligero incremento en el tiempo de desarrollo inicial para implementar el consentimiento y las rutinas de anonimización de datos.
