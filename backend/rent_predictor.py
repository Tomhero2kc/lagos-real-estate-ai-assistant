from pathlib import Path

import joblib
import pandas as pd


project_folder = Path(__file__).resolve().parent.parent
model_file = project_folder / "model" / "rent_model.joblib"


def predict_rent(location, property_type, bedrooms, bathrooms):
    model = joblib.load(model_file)

    property_details = pd.DataFrame(
        [
            {
                "location": location,
                "property_type": property_type,
                "bedrooms": bedrooms,
                "bathrooms": bathrooms,
            }
        ]
    )

    prediction = model.predict(property_details)[0]

    return round(prediction)