import joblib
import pandas as pd

MODEL_PATH = r"C:\Users\PC\Downloads\Recoleccion_Datos_PI\Recoleccion_Datos_PI\models\no_show_model.joblib"

def predict_no_show(input_data: dict) -> dict:
    """
    Realiza una predicción de no asistencia a partir de un diccionario
    con las variables esperadas por el modelo.
    """
    model = joblib.load(MODEL_PATH)

    df = pd.DataFrame([input_data])

    pred_class = int(model.predict(df)[0])
    pred_prob = float(model.predict_proba(df)[0, 1])

    return {
        "prediction": pred_class,  # 0 = asiste, 1 = no asiste
        "probability_no_show": round(pred_prob, 4)
    }


if __name__ == "__main__":
    sample_input = {
        'Gender': 0,
        'Age': 45,
        'Neighbourhood': 'JARDIM DA PENHA',
        'Scholarship': 0,
        'Hipertension': 1,
        'Diabetes': 0,
        'Alcoholism': 0,
        'Handcap': 0,
        'SMS_received': 1,
        'waiting_days': 12,
        'scheduled_weekday': 1,
        'appointment_weekday': 3,
        'is_same_day': 0,
        'age_group': 'adult',
        'has_comorbidity': 1,
        'risk_score': 1,
        'is_child_or_senior': 0,
        'appointment_month': 5,
        'schedule_hour': 10
    }

    result = predict_no_show(sample_input)
    print(result)