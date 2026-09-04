def answer_tenancy_question(question):
    question = question.lower().strip()

    if not question:
        return "Please enter a question first."

    if "agreement" in question or "contract" in question:
        return (
            "Read the tenancy agreement carefully before signing. "
            "Check the rent amount, payment dates, tenancy period "
            "and who is responsible for repairs."
        )

    if "receipt" in question or "payment" in question:
        return (
            "Keep a record of every rent payment you make. "
            "Bank transfers, receipts and written confirmations can be useful."
        )

    if "repair" in question or "damage" in question:
        return (
            "Report repair problems early and keep a written record. "
            "Photos can also help show the condition of the property."
        )

    if "before paying" in question or "move" in question:
        return (
            "Before paying, inspect the property, confirm who you are dealing with "
            "and read the tenancy agreement carefully."
        )

    if "landlord" in question:
        return (
            "Keep important communication with your landlord in writing, "
            "especially anything involving payments or repairs."
        )

    return (
        "I do not have a specific answer for that question yet. "
        "For an important legal issue, check an official source "
        "or speak with a qualified professional."
    )