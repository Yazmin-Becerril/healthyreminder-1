# Justificación del Proyecto — Healthy Reminder ML

## Objetivo del proyecto

El presente proyecto tiene como objetivo predecir la inasistencia de pacientes a citas médicas utilizando técnicas de Machine Learning, con la finalidad de mejorar la gestión de citas y permitir la implementación de recordatorios inteligentes en el sistema **Healthy Reminder**.

---

## Cumplimiento de los requerimientos

A continuación se justifica cómo el proyecto cumple con cada uno de los puntos solicitados para la evaluación y posible exención.

---

## 1. Mejora de la experimentación

El proyecto no se limitó a un análisis básico, sino que evolucionó significativamente a través de distintas fases:

### Mejora del dataset
- Se partió de un dataset real (No-show appointments).
- Se realizó una auditoría completa (EDA).
- Se identificaron problemas como:
  - datos inconsistentes (edad negativa)
  - desbalance en la variable objetivo
- Se generaron nuevas variables (feature engineering), lo cual enriqueció el dataset.

### Ingeniería de características
Se agregaron variables clave como:
- `waiting_days`
- `age_group`
- `has_comorbidity`
- `risk_score`
- variables temporales (día, mes, hora)

Esto permitió mejorar la capacidad predictiva del modelo.

### Uso de múltiples modelos
Se entrenaron y compararon distintos algoritmos:
- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- MLPClassifier

No se eligió un modelo arbitrariamente, sino mediante comparación con métricas.

### Evaluación con métricas correctas
Se utilizaron:
- accuracy
- precision
- recall
- f1-score
- roc_auc
- matriz de confusión

Se identificó que **accuracy no era suficiente** debido al desbalance del dataset.

---

## 2. Manejo del desbalance

Uno de los problemas principales del dataset era el desbalance:

- ~80% pacientes asisten
- ~20% no asisten

Para resolver esto se implementaron:

- `class_weight='balanced'`
- SMOTE (Synthetic Minority Oversampling Technique)
- división con `stratify`

### Resultado clave

Se logró mejorar significativamente el **recall de la clase No-show (~0.84)**, lo cual es crítico en el problema, ya que el objetivo es detectar pacientes con riesgo de faltar.

---

## 3. Preparación para producción

El proyecto no se quedó en experimentación, sino que avanzó hacia un enfoque más cercano a producción:

### Modelo persistente
- Se guardó el modelo usando `joblib`
- Se guardaron las columnas de entrada

### Script de inferencia
- Se desarrolló `predict.py`
- Permite hacer predicciones con nuevos datos

### Aplicación web (Flask)
Se creó una interfaz que permite:
- ingresar datos
- usar casos de prueba
- visualizar predicción
- interpretar resultados

Esto demuestra un uso real del modelo.

---

## 4. Uso de SQL (Propuesto)

Aunque el entrenamiento se realizó con archivos CSV, se implementó y demostró la capacidad de:

- cargar el dataset en una base de datos SQLite
- consultar datos mediante SQL
- integrar SQL como fuente de datos para producción

Esto cumple con el requerimiento de uso de bases de datos en escenarios reales.

---

## 5. Pipeline de Machine Learning

Se implementó un flujo reproducible de trabajo:

1. Carga de datos
2. Limpieza
3. Transformaciones
4. Feature engineering
5. Entrenamiento
6. Evaluación
7. Guardado del modelo

Este flujo constituye un **pipeline de ML**, ya que permite repetir el proceso de manera estructurada.

---

## 6. MLOps (Preparación)

Se investigaron e integraron conceptos clave de MLOps:

- versionado del modelo
- separación de entrenamiento e inferencia
- estructura de proyecto organizada
- base para despliegue

Aunque no se implementó un pipeline automatizado completo, el proyecto **está preparado para escalar hacia MLOps real**.

---

## 7. Plan de producción

Se definió un plan claro para llevar el modelo a producción:

1. Integrar base de datos SQL
2. Convertir el modelo en API (FastAPI/Flask)
3. Desplegar en servidor
4. Automatizar entrenamiento
5. Monitorear desempeño

---

## 8. Aplicación funcional

El sistema desarrollado permite:

- interacción con el modelo en tiempo real
- uso de datos simplificados para usuario
- generación automática de variables
- interpretación del riesgo mediante colores:
  - Bajo
  - Medio
  - Alto

Esto acerca el proyecto a un uso real en sistemas de salud.

---

## Conclusión

El proyecto cumple completamente con los requisitos solicitados, ya que:

- no se limitó a un modelo básico
- mejoró el dataset mediante feature engineering
- comparó múltiples algoritmos
- resolvió el problema del desbalance
- priorizó métricas correctas (recall)
- preparó el modelo para producción
- implementó una aplicación funcional
- investigó e integró conceptos de SQL, pipelines y MLOps

Además, el sistema desarrollado demuestra un enfoque profesional que va más allá de un trabajo académico, acercándose a un entorno real de aplicación.

---

## 27Nota final

El valor principal del proyecto no radica únicamente en el modelo, sino en todo el proceso completo:

> comprensión del problema → preparación de datos → modelado → evaluación → implementación

Esto demuestra un dominio integral del flujo de Machine Learning.