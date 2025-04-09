## **Actividad: Computación en la nube**

Esta actividad se orienta a estudiantes de desarrollo de software que deseen entender los fundamentos de la computación en la nube. 


#### 1. Objetivos de aprendizaje

1. **Comprender las motivaciones** que impulsaron el surgimiento de la computación en la nube y el entorno tecnológico previo (clústeres, data centers, múltiplos núcleos).
2. **Diferenciar y analizar** los beneficios de la elasticidad en la nube, las tecnologías de virtualización y los modelos de servicio (IaaS, PaaS, SaaS, DaaS).
3. **Evaluar** las diversas tipologías de nubes (públicas, privadas, híbridas, multi-cloud) y sus ventajas e inconvenientes, incluyendo el impacto económico y la dependencia del proveedor.
4. **Relacionar** estos conceptos con la práctica del desarrollo de software, analizando cómo las elecciones de arquitectura y servicios en la nube pueden influir en la escalabilidad y competitividad de un proyecto.


#### 2. Instrucciones de la actividad

##### A. Cuestionario

1. **Motivaciones para la nube**  
   - (a) ¿Qué problemas o limitaciones existían antes del surgimiento de la computación en la nube y cómo los solucionó la centralización de servidores en data centers?  
> **Problemas o limitaciones**
> 	- **Altos costos de hardware y mantenimiento**: Las organizaciones necesitaban adquirir servidores, almacenamiento y equipos costosos, además de incurrir en gastos continuos de mantenimiento y actualización.
> 	- **Capacidad limitada y subutilización**: Los servidores locales a menudo operaban por debajo de su capacidad máxima, generando ineficiencia en el uso de recursos.
> 	- **Baja escalabilidad**: Era difícil ampliar la infraestructura, por cuestiones de tiempo, gestión y dinero.
> 	- **Disponibilidad limitada**: La infraestructura local podría fallar, provocando interrupciones en los servicios sin mecanismos de recuperación.
> **Soluciones**
> 	- **Reducción de costos**: La computación en la nube elimina la necesidad de comprar hardware y reduce gastos de mantenimiento.
> 	- **Uso eficiente de recursos**: La centralización en data centers permite compartir recursos entre múltiples usuarios, optimizando su utilización mediante virtualización.
> 	- **Alta escalabilidad**: Las empresas pueden escalar su capacidad de cómputo y almacenamiento rápidamente, de forma automática y bajo demanda.
> 	- **Mayor disponibilidad**: Los data centers están diseñados con redundancia y recuperación antes desastres garantizando alta disponibilidad de los servicios.



   - (b) ¿Por qué se habla de “The Power Wall” y cómo influyó la aparición de procesadores multi-core en la evolución hacia la nube?
> - "The Power Wall" se refiere a la dificultad de escalar el rendimiento de los chips y sistemas informáticos a niveles históricos, debido a las limitaciones fundamentales impuestas por el suministro y la disipación de energía asequibles.  
> - La aparición de procesadores multinúcleo fue una solución directa al problema del *Power Wall*. En lugar de aumentar la frecuencia del reloj, los fabricantes empezaron a integrar múltiples núcleos en un solo chip, permitiendo ejecutar múltiples tareas en paralelo.
> - La computación en la nube se benefició directamente de la aparición de procesadores multi-core ya que los centros de datos modernos usan servidores con procesadores multi-core para manejar grandes volúmenes de datos y ejecutar múltiples aplicaciones simultáneamente.

- [Muro de energía | SpringerLink](https://link.springer.com/referenceworkentry/10.1007/978-0-387-09766-4_499#:~:text=Definition,affordable%20power%20delivery%20and%20dissipation.)
- [¿Qué es la computación en la nube? Visión general de la nube | Atlassian](https://www.atlassian.com/es/microservices/cloud-computing)


2. **Clusters y load balancing**  
   - (a) Explica cómo la necesidad de atender grandes volúmenes de tráfico en sitios web condujo a la adopción de clústeres y balanceadores de carga.  
>El crecimiento exponencial del tráfico web generó problemas críticos en servidores individuales:
>- **Sobrecargas y caídas**: Servidores únicos colapsaban ante picos de demanda, afectando la disponibilidad
>- **Escalabilidad limitada**: Añadir servidores manualmente era complejo y poco eficiente
>
>La solución fue implementar clústeres de servidores combinados con balanceadores de carga:
>- **Distribución inteligente de tráfico**: Los balanceadores (como HAProxy o Nginx) asignan solicitudes a servidores según algoritmos como **Round Robin (RR)** o **Least Connections (LC)**
>- **Alta disponibilidad**: Si un servidor falla, el tráfico se redirige automáticamente a nodos activos, evitando interrupciones
>- **Escalabilidad horizontal** Permite agregar servidores al clúster bajo demanda, gestionando tráfico creciente sin reiniciar servicios.


   - (b) Describe un ejemplo práctico de cómo un desarrollador de software puede beneficiarse del uso de load balancers para una aplicación web.
   > Por ejemplo, un desarrollador lanza una aplicación web para reserva de paquetes turísticos tipo *Despegar.com*. Al crecer el número de usuarios el servidor se satura y comienza a fallar. El *load balancer* ayudaría en
   1. Organizar y distribuir el tráfico entre servicios y peticiones
 >  2.  Posibilidad de escalar servicios individualmente
 >  3. Las solicitudes entrantes pueden enrutarse a los contenedores correctos según el path 

4. **Elastic computing**  
   - (a) Define con tus propias palabras el concepto de Elastic Computing.  
> Es la capacidad que tiene una infraestructura de adaptarse a la demanda que recibe, es decir, ajusta sus recursos dependiendo de la carga de trabajo. Es una característica de la computación en la nube.

   - (b) ¿Por qué la virtualización es una pieza clave para la elasticidad en la nube?  
> 




   - (c) Menciona un escenario donde, desde la perspectiva de desarrollo, sería muy difícil escalar la infraestructura sin un entorno elástico.
>


4. **Modelos de servicio (IaaS, PaaS, SaaS, DaaS)**  
   - (a) Diferencia cada uno de estos modelos. ¿En qué casos un desarrollador optaría por PaaS en lugar de IaaS?  
   - (b) Enumera tres ejemplos concretos de proveedores o herramientas que correspondan a cada tipo de servicio.

5. **Tipos de nubes (Pública, Privada, Híbrida, Multi-Cloud)**  
   - (a) ¿Cuáles son las ventajas de implementar una nube privada para una organización grande?  
   - (b) ¿Por qué una empresa podría verse afectada por el “provider lock-in”?  
   - (c) ¿Qué rol juegan los “hyperscalers” en el ecosistema de la nube?


##### B. Actividades de investigación y aplicación

1. **Estudio de casos**  
   - Busca dos o tres casos de empresas (startups o grandes organizaciones) que hayan migrado parte de su infraestructura a la nube. Describe:
     1. Sus motivaciones para la migración.  
     2. Los beneficios obtenidos (por ejemplo, reducción de costos, escalabilidad, flexibilidad).  
     3. Los desafíos o dificultades enfrentadas (ej. seguridad, cumplimiento normativo).

2. **Comparativa de modelos de servicio**  
   - Realiza un cuadro comparativo en el que muestres las **responsabilidades** del desarrollador, del proveedor y del equipo de operaciones en los distintos modelos (IaaS, PaaS, SaaS).  
   - Incluye aspectos como: instalación de S.O., despliegue de aplicaciones, escalado automático, parches de seguridad, etc.

3. **Armar una estrategia multi-cloud o híbrida**  
   - Imagina que trabajas en una empresa mediana que tiene una parte de su infraestructura en un data center propio y otra parte en un proveedor de nube pública.  
   - Diseña una estrategia (de forma teórica) para migrar el 50% de tus cargas de trabajo a un segundo proveedor de nube, con el fin de no depender exclusivamente de uno.  
   - Explica dónde iría la base de datos, cómo manejarías la configuración de red y cuál sería el plan de contingencia si un proveedor falla.

4. **Debate sobre costos**  
   - Prepara un breve análisis de los pros y contras de cada tipo de nube (pública, privada, híbrida, multi-cloud) considerando:
     1. Costos iniciales (CAPEX vs. OPEX).  
     2. Flexibilidad y escalabilidad a mediano y largo plazo.  
     3. Cumplimiento con normativas (p.ej. GDPR, HIPAA).  
     4. Barreras o complejidades al cambiar de proveedor.


#### C. Ejercicio de presentación de "mini-proyecto"

Como parte del **aprendizaje práctico**, forma equipos y presenten un **"Mini-proyecto de arquitectura en la Nube"**:

1. **Objetivo del sistema**: Cada equipo define brevemente la aplicación o servicio (por ejemplo, un e-commerce, un sistema de reservas, una plataforma de contenido).  
2. **Selección de modelo de servicio**: Explica si se utilizará IaaS, PaaS o SaaS, y justifica por qué.  
3. **Tipo de nube**: Decide si vas a desplegar la aplicación en una nube pública, privada, híbrida o multi-cloud. Argumenta con un análisis de ventajas y desventajas.  
4. **Esquema de escalabilidad**: Describe cómo la aplicación escalaría en caso de aumento de demanda.  
5. **Costos y riesgos**: Menciona los principales costos (directos o indirectos) y los riesgos asociados a tu elección (p.ej., dependencia del proveedor, requerimientos de seguridad).  
6. **Presentación final**: Prepara un diagrama de alto nivel (físico o lógico) donde se visualice la infraestructura básica y los componentes en la nube.
