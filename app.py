from pathlib import Path
from flask import Flask, render_template, request, send_file
import markdown
import pandas as pd

from src.predict import predict_no_show

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
REPORTS_DIR = BASE_DIR / "reports"
NOTEBOOKS_DIR = BASE_DIR / "notebooks"
MODELS_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"


def get_neighbourhoods():
    csv_path = DATA_DIR / "KaggleV2-May-2016-features.csv"

    if not csv_path.exists():
        return []

    df = pd.read_csv(csv_path, usecols=["Neighbourhood"])
    neighbourhoods = sorted(df["Neighbourhood"].dropna().unique().tolist())
    return neighbourhoods


def categorize_age(age: int) -> str:
    if age <= 12:
        return "child"
    elif age <= 17:
        return "teen"
    elif age <= 35:
        return "young_adult"
    elif age <= 59:
        return "adult"
    return "senior"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/investigacion")
def investigacion():
    md_path = REPORTS_DIR / "mlops_sql_pipeline_produccion.md"

    if not md_path.exists():
        html_content = "<p>No se encontró el archivo de investigación.</p>"
    else:
        content = md_path.read_text(encoding="utf-8")
        html_content = markdown.markdown(
            content,
            extensions=["fenced_code", "tables"]
        )

    return render_template("investigacion.html", content=html_content)

@app.route("/justificacion")
def justificacion():
    md_path = REPORTS_DIR / "justificacion_proyecto.md"

    if not md_path.exists():
        html_content = "<p>No se encontró el archivo de justificación.</p>"
    else:
        content = md_path.read_text(encoding="utf-8")
        html_content = markdown.markdown(
            content,
            extensions=["fenced_code", "tables"]
        )

    return render_template("investigacion.html", content=html_content)


@app.route("/resultados")
def resultados():
    metrics = {
        "accuracy": 0.5774,
        "precision": 0.3036,
        "recall": 0.8441,
        "f1": 0.4465,
        "roc_auc": 0.7223,
    }

    fase5 = [
        {"model": "Decision Tree", "accuracy": 0.7323, "precision": 0.3338, "recall": 0.3271, "f1": 0.3304, "roc_auc": 0.5823},
        {"model": "MLPClassifier", "accuracy": 0.7579, "precision": 0.3614, "recall": 0.2590, "f1": 0.3017, "roc_auc": 0.6993},
        {"model": "Random Forest", "accuracy": 0.7972, "precision": 0.4931, "recall": 0.1530, "f1": 0.2335, "roc_auc": 0.7411},
        {"model": "Logistic Regression", "accuracy": 0.7977, "precision": 0.4524, "recall": 0.0085, "f1": 0.0167, "roc_auc": 0.7234},
        {"model": "Gradient Boosting", "accuracy": 0.7980, "precision": 0.4706, "recall": 0.0036, "f1": 0.0071, "roc_auc": 0.7343},
    ]

    fase6 = [
        {"model": "Logistic Regression Balanced", "accuracy": 0.5774, "precision": 0.3036, "recall": 0.8441, "f1": 0.4465, "roc_auc": 0.7223},
        {"model": "Decision Tree Balanced", "accuracy": 0.7177, "precision": 0.3235, "recall": 0.3645, "f1": 0.3427, "roc_auc": 0.5858},
        {"model": "Random Forest Balanced", "accuracy": 0.7967, "precision": 0.4893, "recall": 0.1530, "f1": 0.2331, "roc_auc": 0.7412},
        {"model": "Logistic Regression + SMOTE", "accuracy": 0.5762, "precision": 0.3027, "recall": 0.8430, "f1": 0.4455, "roc_auc": 0.7203},
    ]

    return render_template(
        "resultados.html",
        metrics=metrics,
        fase5=fase5,
        fase6=fase6
    )


@app.route("/prediccion", methods=["GET", "POST"])
def prediccion():
    result = None
    error = None
    neighbourhoods = get_neighbourhoods()

    casos_ejemplo = {
        "riesgo_bajo": {
            "Gender": 0,
            "Age": 25,
            "Neighbourhood": "JARDIM DA PENHA",
            "Scholarship": 0,
            "Hipertension": 0,
            "Diabetes": 0,
            "Alcoholism": 0,
            "Handcap": 0,
            "SMS_received": 1,
            "waiting_days": 1,
            "scheduled_weekday": 1,
            "appointment_weekday": 2,
            "appointment_month": 5,
            "schedule_hour": 9
        },
        "riesgo_medio": {
            "Gender": 1,
            "Age": 48,
            "Neighbourhood": "CENTRO",
            "Scholarship": 0,
            "Hipertension": 1,
            "Diabetes": 0,
            "Alcoholism": 0,
            "Handcap": 0,
            "SMS_received": 0,
            "waiting_days": 12,
            "scheduled_weekday": 2,
            "appointment_weekday": 4,
            "appointment_month": 5,
            "schedule_hour": 11
        },
        "riesgo_alto": {
            "Gender": 0,
            "Age": 67,
            "Neighbourhood": "ITARARÉ",
            "Scholarship": 1,
            "Hipertension": 1,
            "Diabetes": 1,
            "Alcoholism": 0,
            "Handcap": 1,
            "SMS_received": 0,
            "waiting_days": 25,
            "scheduled_weekday": 0,
            "appointment_weekday": 5,
            "appointment_month": 6,
            "schedule_hour": 15
        }
    }

    if request.method == "POST":
        try:
            gender = int(request.form["Gender"])
            age = int(request.form["Age"])
            neighbourhood = request.form["Neighbourhood"]
            scholarship = int(request.form["Scholarship"])
            hipertension = int(request.form["Hipertension"])
            diabetes = int(request.form["Diabetes"])
            alcoholism = int(request.form["Alcoholism"])
            handcap = int(request.form["Handcap"])
            sms_received = int(request.form["SMS_received"])
            waiting_days = int(request.form["waiting_days"])
            scheduled_weekday = int(request.form["scheduled_weekday"])
            appointment_weekday = int(request.form["appointment_weekday"])
            appointment_month = int(request.form["appointment_month"])
            schedule_hour = int(request.form["schedule_hour"])

            age_group = categorize_age(age)
            has_comorbidity = int(
                hipertension == 1 or
                diabetes == 1 or
                alcoholism == 1 or
                handcap > 0
            )
            risk_score = (
                hipertension +
                diabetes +
                alcoholism +
                (1 if handcap > 0 else 0) +
                scholarship
            )
            is_child_or_senior = int(age <= 12 or age >= 60)
            is_same_day = int(waiting_days == 0)

            input_data = {
                "Gender": gender,
                "Age": age,
                "Neighbourhood": neighbourhood,
                "Scholarship": scholarship,
                "Hipertension": hipertension,
                "Diabetes": diabetes,
                "Alcoholism": alcoholism,
                "Handcap": handcap,
                "SMS_received": sms_received,
                "waiting_days": waiting_days,
                "scheduled_weekday": scheduled_weekday,
                "appointment_weekday": appointment_weekday,
                "is_same_day": is_same_day,
                "age_group": age_group,
                "has_comorbidity": has_comorbidity,
                "risk_score": risk_score,
                "is_child_or_senior": is_child_or_senior,
                "appointment_month": appointment_month,
                "schedule_hour": schedule_hour,
            }

            result = predict_no_show(input_data)
            prob = float(result.get("probability_no_show", 0.0))

            if prob < 0.30:
                risk_label = "Riesgo bajo"
                risk_color = "low"
            elif prob < 0.60:
                risk_label = "Riesgo medio"
                risk_color = "medium"
            else:
                risk_label = "Riesgo alto"
                risk_color = "high"

            result["risk_label"] = risk_label
            result["risk_color"] = risk_color
            result["age_group"] = age_group
            result["has_comorbidity"] = has_comorbidity
            result["risk_score"] = risk_score
            result["is_child_or_senior"] = is_child_or_senior
            result["is_same_day"] = is_same_day

        except Exception as exc:
            error = f"Ocurrió un error al procesar la predicción: {exc}"

    return render_template(
        "prediccion.html",
        result=result,
        error=error,
        neighbourhoods=neighbourhoods,
        casos_ejemplo=casos_ejemplo
    )


@app.route("/descargas")
def descargas():
    files = {
        "investigacion": REPORTS_DIR / "mlops_sql_pipeline_produccion.md",
        "modelo": MODELS_DIR / "no_show_model.joblib",
        "columnas": MODELS_DIR / "feature_columns.joblib",
        "eda": NOTEBOOKS_DIR / "01_eda_auditoria.ipynb",
        "preprocesamiento": NOTEBOOKS_DIR / "02_preprocesamiento.ipynb",
        "features": NOTEBOOKS_DIR / "03_feature_engineering.ipynb",
        "modelos": NOTEBOOKS_DIR / "04_modelos.ipynb",
        "balanceo": NOTEBOOKS_DIR / "05_balanceo.ipynb",
        "modelo_final": NOTEBOOKS_DIR / "06_modelo_final.ipynb",
    }

    return render_template("descargas.html", files=files)


@app.route("/download/<name>")
def download_file(name: str):
    allowed = {
        "investigacion": REPORTS_DIR / "mlops_sql_pipeline_produccion.md",
        "modelo": MODELS_DIR / "no_show_model.joblib",
        "columnas": MODELS_DIR / "feature_columns.joblib",
        "eda": NOTEBOOKS_DIR / "01_eda_auditoria.ipynb",
        "preprocesamiento": NOTEBOOKS_DIR / "02_preprocesamiento.ipynb",
        "features": NOTEBOOKS_DIR / "03_feature_engineering.ipynb",
        "modelos": NOTEBOOKS_DIR / "04_modelos.ipynb",
        "balanceo": NOTEBOOKS_DIR / "05_balanceo.ipynb",
        "modelo_final": NOTEBOOKS_DIR / "06_modelo_final.ipynb",
    }

    file_path = allowed.get(name)

    if file_path is None or not file_path.exists():
        return "Archivo no encontrado", 404

    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)