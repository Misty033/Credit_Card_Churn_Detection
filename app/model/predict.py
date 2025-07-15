import pandas as pd
from app.core.config import MODEL_PATH, FEATURE_COLUMNS 
import joblib

model = joblib.load(MODEL_PATH)

def predict_from_csv(df: pd.DataFrame):
    try:
        input_df = df[FEATURE_COLUMNS]  
        preds = model.predict(input_df)

        pred_labels = ['Existing' if p == 0 else 'Attrited' for p in preds]
        return pred_labels

    except KeyError as e:
        raise ValueError(f"Missing required feature column: {e}")
