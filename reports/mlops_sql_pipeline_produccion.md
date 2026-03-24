# Investigación: SQL, Pipelines y MLOps en Healthy Reminder

## 1. Uso de bases de datos SQL como dataset para producción

En un entorno de desarrollo académico, es común trabajar con datasets en formato CSV; sin embargo, en un entorno real de producción, los datos provienen generalmente de bases de datos relacionales como MySQL o PostgreSQL. Estas bases contienen información operativa del sistema, como pacientes, citas, tratamientos y comportamiento histórico.

En el contexto del proyecto Healthy Reminder, el uso de SQL como fuente de datos permite que el modelo de machine learning trabaje con información actualizada y real, en lugar de depender de archivos estáticos. Esto es fundamental para mantener la relevancia del modelo en el tiempo.

El flujo típico para usar SQL como dataset es el siguiente:

1. Extracción de datos mediante consultas SQL.
2. Transformación de los datos (limpieza, manejo de nulos, creación de variables derivadas).
3. Carga de los datos en herramientas de análisis como Python (pandas).
4. Entrenamiento del modelo con los datos obtenidos.

Una buena práctica es crear una vista en la base de datos que centralice el dataset necesario para el modelo. Por ejemplo:

- edad del paciente
- sexo
- fecha de agendado
- fecha de cita
- días de espera
- número de recordatorios enviados
- historial de inasistencias
- asistencia (variable objetivo)

Esto permite desacoplar el modelo de la estructura interna de la base de datos y facilita su mantenimiento.

Ventajas de usar SQL como dataset:
- datos actualizados en tiempo real;
- integración directa con el sistema principal;
- eliminación de procesos manuales de carga;
- mayor escalabilidad.

Por lo tanto, el uso de bases de datos SQL es un paso clave para llevar un modelo de machine learning de un entorno experimental a uno productivo.

---

## 2. ¿Qué es un pipeline y cómo implementarlo en el proyecto?

Un pipeline en machine learning es una secuencia estructurada de pasos que automatiza el flujo completo de trabajo, desde la preparación de datos hasta la generación de predicciones. Su principal objetivo es garantizar reproducibilidad, orden y facilidad de mantenimiento.

Un pipeline típico incluye:
1. carga de datos;
2. limpieza de datos;
3. transformación de variables;
4. ingeniería de características;
5. entrenamiento del modelo;
6. evaluación;
7. generación de predicciones.

En el proyecto Healthy Reminder, un pipeline permitiría automatizar el proceso de predicción de asistencia a citas médicas. Por ejemplo:

- extraer datos desde la base SQL;
- calcular variables como días de espera o historial del paciente;
- transformar variables categóricas;
- entrenar el modelo;
- generar una probabilidad de inasistencia para cada cita.

En Python, utilizando la librería sklearn, es posible implementar pipelines mediante las clases `Pipeline` y `ColumnTransformer`. Esto permite encadenar transformaciones y modelos en una sola estructura.

Ejemplo conceptual de pipeline:
- transformación de datos numéricos;
- codificación de variables categóricas;
- entrenamiento de modelo (por ejemplo, Random Forest o regresión logística).

Ventajas del uso de pipelines:
- evita errores humanos en el flujo de trabajo;
- permite repetir el proceso fácilmente;
- facilita pruebas y validación;
- simplifica el paso a producción.

En este proyecto, implementar un pipeline es fundamental para pasar de un notebook experimental a un sistema estructurado y reutilizable.

---

## 3. ¿Qué es MLOps?

MLOps (Machine Learning Operations) es un conjunto de prácticas que busca integrar el desarrollo de modelos de machine learning con su despliegue y mantenimiento en producción. Es una extensión de los principios de DevOps aplicada al ciclo de vida de los modelos.

Mientras que en un entorno académico el modelo se entrena una sola vez, en producción es necesario mantenerlo actualizado, monitoreado y versionado.

MLOps incluye los siguientes elementos:

- versionado de datos y modelos;
- automatización del entrenamiento;
- pruebas y validación del modelo;
- despliegue en producción;
- monitoreo del rendimiento;
- reentrenamiento continuo.

En el contexto de Healthy Reminder, MLOps permitiría que el modelo de predicción de inasistencia no sea un experimento aislado, sino un componente activo del sistema.

Ejemplo aplicado:
- el sistema registra nuevas citas diariamente;
- el modelo se reentrena cada cierto tiempo con datos recientes;
- se compara el rendimiento del modelo actual con el anterior;
- si el nuevo modelo es mejor, se despliega automáticamente;
- se monitorea si el modelo pierde precisión con el tiempo.

Beneficios de MLOps:
- mejora continua del modelo;
- mayor confiabilidad;
- integración real con el sistema;
- escalabilidad.

Implementar MLOps, aunque sea a nivel básico, eleva significativamente el nivel del proyecto hacia estándares profesionales.

---

## 4. Plan de acción para llevar el modelo a producción en Healthy Reminder

Para llevar el modelo de predicción de asistencia a un entorno de producción dentro del sistema Healthy Reminder, se propone el siguiente plan de acción dividido en fases:

### Fase 1: Mejora del dataset
- integrar datos reales desde la base de datos SQL;
- agregar variables relevantes como historial del paciente, número de recordatorios y tiempo de anticipación;
- limpiar y validar los datos.

### Fase 2: Ingeniería de características
- crear variables derivadas como días de espera;
- agrupar variables clínicas en indicadores de riesgo;
- generar variables temporales (día de la semana, mes, etc.).

### Fase 3: Entrenamiento y selección de modelo
- probar múltiples modelos (regresión logística, random forest, redes neuronales);
- evaluar con métricas adecuadas (recall, f1-score, roc-auc);
- seleccionar el modelo más eficiente para el problema.

### Fase 4: Implementación de pipeline
- automatizar el flujo completo de datos y entrenamiento;
- asegurar reproducibilidad;
- preparar el pipeline para producción.

### Fase 5: Integración con el sistema
- generar predicciones antes de cada cita;
- asignar un nivel de riesgo a cada paciente;
- activar recordatorios adicionales para pacientes con alto riesgo de inasistencia.

### Fase 6: Despliegue
- guardar el modelo entrenado;
- integrarlo mediante una API o módulo interno;
- permitir consultas en tiempo real.

### Fase 7: MLOps básico
- monitorear el rendimiento del modelo;
- registrar predicciones vs resultados reales;
- reentrenar el modelo periódicamente;
- mantener versiones del modelo.

Este plan permite evolucionar el modelo desde un entorno experimental hasta una solución funcional integrada al sistema Healthy Reminder, aportando valor real en la reducción de inasistencias.

---

## Conclusiones

El desarrollo de modelos de machine learning no debe limitarse a la experimentación en notebooks, sino que debe orientarse a su implementación en entornos reales. En este proyecto, se identificó la importancia de utilizar bases de datos SQL como fuente de datos en producción, implementar pipelines para estructurar el flujo de trabajo y aplicar principios de MLOps para asegurar la continuidad y mejora del modelo.

Además, se propuso un plan de acción concreto para integrar el modelo dentro del sistema Healthy Reminder, permitiendo predecir la inasistencia de pacientes y mejorar la gestión de citas médicas.

Estas prácticas elevan el proyecto de un nivel académico básico a uno con enfoque profesional, alineado con necesidades reales de sistemas de salud y software empresarial.