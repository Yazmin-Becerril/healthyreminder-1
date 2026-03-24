# Healthy Reminder

Healthy Reminder es un proyecto de Machine Learning enfocado en predecir la inasistencia a citas médicas (**No-show**) utilizando el dataset **Medical Appointment No Shows** de Kaggle.

El proyecto abarca desde el análisis de datos hasta una aplicación web funcional que permite realizar predicciones en tiempo real.

---

## Objetivo del proyecto

El objetivo es identificar pacientes con alta probabilidad de no asistir a su cita médica para poder tomar acciones preventivas como:

- envío de recordatorios
- llamadas de confirmación
- priorización de atención
- optimización de agendas médicas

---

## Dataset

Dataset utilizado: **Medical Appointment No Shows (Kaggle)**

Características principales:

- ~110,000 registros
- Variable objetivo: `No-show`
  - `0` → asistió
  - `1` → no asistió
- Dataset desbalanceado (~80% asistencias, ~20% inasistencias)
- Sin valores nulos

---

## Fases del proyecto

### Fase 2 — Auditoría del dataset
- carga del CSV
- revisión de columnas y tipos
- validación de nulos (no hay)
- validación de duplicados
- análisis de la variable objetivo
- detección de errores (ej. edades negativas)

---

### Fase 3 — Limpieza y preprocesamiento
- conversión de fechas (`ScheduledDay`, `AppointmentDay`)
- eliminación de edades inválidas
- codificación de variables categóricas
- eliminación de columnas irrelevantes (`PatientId`, `AppointmentID`)

Archivo generado:
KaggleV2-May-2016-clean.csv


---

### Fase 4 — Ingeniería de características

Se generaron nuevas variables clave:

- `waiting_days`
- `scheduled_weekday`
- `appointment_weekday`
- `is_same_day`
- `age_group`
- `has_comorbidity`
- `risk_score`
- `is_child_or_senior`
- `appointment_month`
- `schedule_hour`

Archivo generado:
KaggleV2-May-2016-features.csv


---

### Fase 5 — Entrenamiento de modelos

Modelos utilizados:

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- MLPClassifier

Métricas evaluadas:

- accuracy
- precision
- recall
- f1-score
- roc_auc
- matriz de confusión

Resultado:

- buen accuracy (~0.79)
- bajo recall inicial en la clase importante (no-show)

---

### Fase 6 — Manejo de desbalance

Se aplicaron:

- `train_test_split` con `stratify`
- `class_weight='balanced'`
- SMOTE

Resultado final destacado:

- mejora significativa en **recall (~0.84)** para detectar inasistencias
- se priorizó recall sobre accuracy por objetivo de negocio

---

### Fase 8 — Modelo listo para uso

- modelo guardado con `joblib`
- columnas de entrada almacenadas
- script de predicción funcional (`predict.py`)

---

### Fase 9 — Aplicación web

Se desarrolló una aplicación en Flask que permite:

- ingresar datos manualmente
- usar ejemplos predefinidos
- calcular variables automáticamente
- realizar predicción
- mostrar:
  - probabilidad
  - resultado (asiste / no asiste)
  - nivel de riesgo (bajo / medio / alto)

---

## Tecnologías utilizadas

- Python
- Flask
- pandas
- numpy
- scikit-learn
- imbalanced-learn
- matplotlib
- seaborn
- joblib
- Jupyter Notebook

---

## Estructura del proyecto
Healthy Reminder/
│
├── app.py
├── predict.py
├── requirements.txt
├── requerimiento_web.txt
├── README.md
│
├── model/
│ ├── modelo.joblib
│ └── columnas_modelo.joblib
│
├── data/
│ ├── KaggleV2-May-2016.csv
│ ├── KaggleV2-May-2016-clean.csv
│ └── KaggleV2-May-2016-features.csv
│
├── notebooks/
│ ├── auditoria.ipynb
│ ├── limpieza.ipynb
│ ├── features.ipynb
│ ├── entrenamiento.ipynb
│ └── evaluacion.ipynb
│
├── templates/
│ └── index.html
│
└── static/
└── style.css

---

## Instalación

### 1. Crear entorno virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install -r requerimiento_web.txt
```
# Ejecución de la aplicación web
```bash
python app.py
http://127.0.0.1:5000
```
# Uso de la aplicación
La aplicación permite:

- Capturar datos del paciente/cita
- Generar variables automáticamente
- Ejecutar el modelo
- Visualizar resultados de forma clara

# Ejecución por script
```bash
python predict.py
```

# Notas importantes
- Dataset público de Kaggle
- Proyecto con fines académicos y demostrativos
- El modelo no reemplaza decisiones médicas reales
- Se priorizó recall para detectar inasistencias

# Futuras mejoras
- API con FastAPI
- Despliegue en la nube
- Monitoreo del modelo
- Mejora de UI/UX
- MLOps