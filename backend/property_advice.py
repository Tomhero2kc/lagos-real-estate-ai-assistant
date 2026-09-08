from backend.rent_predictor import predict_rent
from backend.tenancy_assistant import answer_tenancy_question


def get_property_advice(
    location,
    property_type,
    bedrooms,
    bathrooms,
    question,
):
    estimated_rent = predict_rent(
        location,
        property_type,
        bedrooms,
        bathrooms,
    )

    tenancy_advice = answer_tenancy_question(question)

    return {
        "estimated_rent": estimated_rent,
        "tenancy_advice": tenancy_advice,
    }