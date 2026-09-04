import streamlit as st
from backend.rent_predictor import predict_rent
from backend.tenancy_assistant import answer_tenancy_question

st.set_page_config(
    page_title="Lagos Real Estate Assistant",
    page_icon="🏠",
)


st.title("Lagos Real Estate Assistant")

st.write(
    "A small learning project for exploring rent estimates "
    "and general tenancy information in Lagos."
)


rent_tab, tenancy_tab = st.tabs(
    ["Rent Estimate", "Tenancy Questions"]
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
    )

    property_type = st.selectbox(
        "Property type",
        [
            "Mini Flat",
            "Flat",
            "Apartment",
            "Duplex",
        ],
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=2,
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2,
    )

if st.button("Estimate Rent"):
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
    )

if st.button("Ask Question"):




    if question.strip():







        
        answer = answer_tenancy_question(question)
        st.info(answer)
    else:
        st.warning("Please enter a question first.")


st.caption(
    "This is a learning project. Rent estimates and tenancy "
    "information should not be treated as professional advice."
)