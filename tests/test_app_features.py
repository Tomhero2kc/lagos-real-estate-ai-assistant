from backend.rent_predictor import predict_rent
from backend.tenancy_assistant import answer_tenancy_question
from backend.property_advice import get_property_advice


def test_rent_prediction():
    result = predict_rent(
        "Yaba",
        "Flat",
        2,
        2,
    )

    assert result > 0


def test_tenancy_question():
    answer = answer_tenancy_question(
        "What should I check before paying rent?"
    )

    assert "before paying" in answer.lower()


def test_empty_tenancy_question():
    answer = answer_tenancy_question("")

    assert answer == "Please enter a question first."


def test_combined_property_advice():
    result = get_property_advice(
        "Yaba",
        "Flat",
        2,
        2,
        "Should I keep my rent receipts?",
    )

    assert result["estimated_rent"] > 0
    assert result["tenancy_advice"]