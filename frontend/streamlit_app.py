import streamlit as st

from backend.rent_predictor import predict_rent
from backend.tenancy_assistant import answer_tenancy_question
from backend.property_advice import get_property_advice


st.set_page_config(
    page_title="Lagos Real Estate Assistant",
    page_icon="🏠",
)


st.title("Lagos Real Estate Assistant")

st.write(
    "A small learning project for exploring rent estimates "
    "and general tenancy information in Lagos."
)


rent_tab, tenancy_tab, advice_tab = st.tabs(
    [
        "Rent Estimate",
        "Tenancy Questions",
        "Property Advice",
    ]
)


with rent_tab:
    st.subheader("Property Details")

    location = st.selectbox(
        "Location",
        [
            "Agege",
            "Ajah",
            "Gbagada",
            "Ikeja",
            "Ikoyi",
            "Lekki",
            "Maryland",
            "Surulere",
            "Victoria Island",
            "Yaba",
        ],
        key="rent_location",
    )

    property_type = st.selectbox(
        "Property type",
        [
            "Mini Flat",
            "Flat",
            "Apartment",
            "Duplex",
        ],
        key="rent_property_type",
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=2,
        key="rent_bedrooms",
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2,
        key="rent_bathrooms",
    )

    if st.button("Estimate Rent", key="estimate_rent_button"):
        estimated_rent = predict_rent(
            location,
            property_type,
            bedrooms,
            bathrooms,
        )

        st.success(
            f"Estimated annual rent: ₦{estimated_rent:,.0f}"
        )


with tenancy_tab:
    st.subheader("Ask About Renting")

    question = st.text_area(
        "Enter a tenancy question",
        placeholder="For example: What should I check before paying rent?",
        key="tenancy_question",
    )

    if st.button("Ask Question", key="ask_tenancy_button"):
        if question.strip():
            answer = answer_tenancy_question(question)
            st.info(answer)
        else:
            st.warning("Please enter a question first.")


with advice_tab:
    st.subheader("Property Advice")

    advice_location = st.selectbox(
        "Location",
        [
            "Agege",
            "Ajah",
            "Gbagada",
            "Ikeja",
            "Ikoyi",
            "Lekki",
            "Maryland",
            "Surulere",
            "Victoria Island",
            "Yaba",
        ],
        key="advice_location",
    )

    advice_property_type = st.selectbox(
        "Property type",
        [
            "Mini Flat",
            "Flat",
            "Apartment",
            "Duplex",
        ],
        key="advice_property_type",
    )

    advice_bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=2,
        key="advice_bedrooms",
    )

    advice_bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2,
        key="advice_bathrooms",
    )

    advice_question = st.text_area(
        "What would you like to know about renting?",
        placeholder="For example: What should I check before paying rent?",
        key="property_advice_question",
    )

    if st.button("Get Property Advice", key="property_advice_button"):
        if advice_question.strip():
            result = get_property_advice(
                advice_location,
                advice_property_type,
                advice_bedrooms,
                advice_bathrooms,
                advice_question,
            )

            st.success(
                f"Estimated annual rent: "
                f"₦{result['estimated_rent']:,.0f}"
            )

            st.info(result["tenancy_advice"])
        else:
            st.warning("Please enter a tenancy question.")


st.caption(
    "This is a learning project. Rent estimates and tenancy "
    "information should not be treated as professional advice."
)