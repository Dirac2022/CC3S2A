## Actividad: Introducción a DevOps
	
### Parte 1

**Objetivo:**  
Comprender los principios fundamentales de DevOps y diferenciar qué es y qué no es DevOps.

### Instrucciones

#### 1. Lectura y reflexión  
Lee el texto proporcionado (*Lectura 1*) y enfócate en los siguientes puntos clave:

- **¿Qué es DevOps?**
> Es una metodología integral que une a los equipos de desarrollo (equipo de desarrollo, equipo de QA y equipo de operaciones) en un proceso colaborativo continuo.  Este enfoque permite acortar los ciclos de entrega, mejorar la calidad y responder de manera ágil a los cambios en el entorno tecnológico y en las necesidades del negocio.

- **Historia y antecedentes de DevOps.**
>Tradicionalmente, el desarrollo se dividía en tres etapas principales: el quipo de desarrollo, el equipo de QA y el de operaciones. Cada grupo trabajaba de forma independiente, lo que provocaba una fragmentación en la comunicación y una tendencia a culpar a otros cuando surgían problemas.


- **Diferencias entre los equipos de desarrollo y operaciones en el pasado.**
> El equipo de desarrollo diseñaba y creaba el software, mientras que el equipo de operaciones se encargaba del despliegue y el mantenimiento. Este flujo secuencial generaba conflictos, retrasos y dificultades en la entrega de software de calidad. 


- **Principios fundamentales de DevOps** (enfoque en el cliente, equipos autónomos y multifuncionales, mejora continua, automatización).
 


- **Qué NO es DevOps.**
> DevOps no es solo un conjunto de herramientas o procesos aislados, sino que engloba un cambio cultural en como se desarrolla software, fomentando la comunicación, transparencia y responsabilidad entre los actores involucrados.
#### 2. Preguntas de reflexión  

Responde en equipo las siguientes preguntas con base en la lectura:

1. **¿Por qué surgió la necesidad de DevOps en el desarrollo de software?** 
> El enfoque convencional donde habían grupos definidos de desarrollo, QA y operaciones y el proceso era secuencial, en donde cada grupo espera a que el anterior termine su tarea, a menudo conduce a grandes "explosiones" de cambios - o lanzamientos mayoritarios - que pueden prolongar considerablemente el ciclo de actualización de software y dificultar la detección temprana de errores.

2. **Explica cómo la falta de comunicación y coordinación entre los equipos de desarrollo y operaciones en el pasado llevó a la creación de DevOps.**  
> La separación de responsabilidades en equipos aislados generaba falta de transparencia y retrasos en la resolución de problemas. Por ejemplo, los ==desarrolladores entregaban código sin considerar la infraestructura==, y los ==equipos de operaciones debían corregir problemas en producción sin haber participado en la fase de desarrollo==. DevOps surgió para integrar ambos equipos, mejorar la comunicación y automatizar procesos clave.

3. **Describe cómo el principio de mejora continua impacta tanto en los aspectos técnicos como en los culturales de una organización.**  
>Técnicamente, la mejora continua impulsa la automatización de pruebas, la detección rápida de errores y la optimización del despliegue de software. Culturalmente, fomenta la colaboración, el aprendizaje constante y la eliminación de barreras entre equipos, promoviendo un ambiente de trabajo más ágil y eficiente.


4. **¿Qué significa que DevOps no se trata solo de herramientas, individuos o procesos?**  
>Uno de los pilares de DevOps es el cambio cultural que impulsa la colaboración y la comunicación entre todos los equipos involucrados en el ciclo de vida del software, es por ello que DevOps es más de un conjunto de herramientas, individuos y procesos.

5. **Según el texto, ¿cómo contribuyen los equipos autónomos y multifuncionales a una implementación exitosa de DevOps?**  
> Los equipos autónomos y multifuncionales permiten reducir la dependencia de otros departamentos, acelerar la entrega de software y mejorar la resolución de problemas. Al trabajar de manera integrada, se evita la fragmentación de tareas y se optimizan los procesos de desarrollo y despliegue.
> La creación de equipos autónomos y multifuncionales fomenta el intercambio de conocimientos y la resolución conjunta de problemas, lo que no solo acelera el proceso de desarrollo, sino que también mejora la calidad del producto final.


---

### Parte 2

**Objetivo:**  
Comprender los conceptos clave y la importancia de **DevSecOps**, **Infraestructura como Código (IaC)**, **Observabilidad**, **Experiencia del desarrollador**, **InnerSource** y **Ingeniería de plataformas** en el contexto de DevOps.

### Instrucciones

#### 1. Lectura y análisis  
Lee atentamente el texto proporcionado (*Lectura 2*) y analiza los siguientes temas:

- **DevSecOps**: Integración de la seguridad en el ciclo de vida del desarrollo.  
>DevSecOps propone integrar herramientas y prácticas de seguridad desde el inicio, realizando análisis de vulnerabilidades, pruebas de penetración y revisiones de código de forma automatizada en cada fase del pipeline de CI/CD

- **Infraestructura como Código (IaC)**: Automatización y gestión de infraestructura mediante código.  
>Se basa en la idea que toda la infraestructura debe poder reproducirse de forma consistente en distintos entornos (desarrollo, pruebas, producción). Los principios fundamentales son
>- Reproducibilidad: Recrear un entorno idéntico en distintos contextos
>- Idempotencia: Ejecutar múltiples veces el mismo código no genera cambios adicionales
>- Composabilidad: Módulos o componentes reutilizables para crear arquitecturas más complejas
>- Evolución controlada: Versionar cada cambio en los archivos de configuración, facilitando rollbacks y auditorías.

- **Observabilidad**: Un enfoque avanzado para monitorear y comprender el estado de los sistemas.  
> La observabilidad combina tres pilares principales:
	- Monitoreo: recolección de métricas (CPU, memoria, latencia, tasa de errores) para evaluar el estado de la aplicación.
	- Logging: Para identificar anomalías y comportamientos inesperados
	- Trazabilidad: Tener un rastro de una petición a través de distintos microservicios o componentes,


- **Experiencia del desarrollador**: Cómo mejorar la satisfacción y productividad de los desarrolladores dentro de un equipo DevOps. 
> DevOps fomenta un ecosistema de colaboración entre desarrolladores. Esta integración no solo optimiza los procesos técnicos sino que también impulsa una cultura de responsabilidad compartida y mejora continua en las organizaciones.


- **InnerSource**: Adopción de prácticas de código abierto dentro de una organización.  
>

- **Ingeniería de plataformas**: Creación de plataformas internas para facilitar el desarrollo y la operación.
>
#### 2. Preguntas de reflexión  

Responde en equipo las siguientes preguntas con base en la lectura:

1. **¿Qué significa "desplazar a la izquierda" en el contexto de DevSecOps y por qué es importante?**  
> Desplazar a la izquierda en DevSecOps significa integrar la seguridad desde el inicio del ciclo de desarrollo en lugar de añadirla al final, para así descartar vulnerabilidades tempranas

	
1. **Explica cómo IaC mejora la consistencia y escalabilidad en la gestión de infraestructuras.**
> Los principios de reproducibilidad e idempotencia mejoran la consistencia, la composabilidad y evaluación controlada mejoran la escalabilidad en la gestión de infraestructuras.

3. **¿Cuál es la diferencia entre monitoreo y observabilidad? ¿Por qué es crucial la observabilidad en sistemas complejos?**  
> El monitoreo recopila métricas del sistema (uso de CPU, memoria, latencia de respuestas, tasa de errores), mientras que la observabilidad cuenta con un enfoque completo de monitoreo, registro de logs y trazabilidad.


4. **¿Cómo puede la experiencia del desarrollador impactar el éxito de DevOps en una organización?**  
> Desarrolladores experimentados podrían detectar tareas repetitivas y vulnerables al error, estas tareas podrían optimizarlas mediante la adopción de DevOps como marco de trabajo. 


5. **Describe cómo InnerSource puede ayudar a reducir silos dentro de una organización.**
> InnerSource -al ser una metodología que aplica las mejores prácticas usadas en el desarrollo de código abierto- promueve la transparencia y colaboración entre diferentes equipos, permitiendo la reutilización de código y fomentando la innovación.  

6. **¿Qué rol juega la ingeniería de plataformas en mejorar la eficiencia y la experiencia del desarrollador?**  
> La ingeniería de plataformas facilitan el desarrollo y despliegue de software, esto reduce la complejidad de tareas y hace que los desarrolladores sean más eficientes, ya que elimina el error en tareas repetitivas.
---

### Indicaciones para trabajo grupal

1. **Formación de equipos:**  
   Formen grupos de hasta **3 integrantes**. Lean las lecturas asignadas y analicen los conceptos clave de DevOps y DevSecOps.  

2. **Distribución del trabajo:**  
   - Un integrante lidera la lectura.  
   - Otro toma notas y sintetiza la información.  
   - El tercero formula respuestas y coordina la discusión.  

3. **Discusión en grupo:**  
   Reflexionen juntos sobre cada pregunta, asegurando que todos comprendan los principios y su impacto en la industria. Analicen cómo estos conceptos pueden aplicarse en entornos reales, destacando mejoras en colaboración, automatización y seguridad dentro de DevOps.  

4. **Presentación y conclusiones:**  
   Reúnanse con otros grupos y compartan sus reflexiones. Debatan cómo la implementación de estas prácticas puede transformar un entorno de desarrollo y operaciones.  

---

**Consejo:** No se trata solo de responder las preguntas, sino de comprender cómo DevOps impacta la cultura, las herramientas y los procesos dentro de una organización.
