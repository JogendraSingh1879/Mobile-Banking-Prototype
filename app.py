import streamlit as st
import qrcode
from PIL import Image
import io
import pandas as pd
from datetime import datetime

# Simulated databases
payee_db = []  # Store payee details
transactions_db = []  # Store transaction history

# Fraud detection function (basic example, can be replaced with an AI model)
def detect_fraud(data, data_type="payee"):
    fraud_patterns = ["dummy", "test"]  # Placeholder patterns
    if data_type == "payee":
        return any(pattern in data["name"].lower() for pattern in fraud_patterns)
    elif data_type == "transaction":
        return any(pattern in data["description"].lower() for pattern in fraud_patterns)
    return False

# Generate QR Code function
def generate_qr(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

# Streamlit UI
st.title("Mobile Banking: Payee Addition and Payment System")

# Section 1: Add Account Payee
st.header("Add Account Payee")
payee_name = st.text_input("Payee Name", "")
account_number = st.text_input("Account Number", "")
ifsc_code = st.text_input("IFSC Code", "")
payee_type = st.selectbox("Payee Type", ["Individual", "Business"])

if st.button("Add Payee"):
    if not payee_name or not account_number or not ifsc_code:
        st.error("Please fill in all the fields.")
    else:
        payee_data = {
            "name": payee_name,
            "account_number": account_number,
            "ifsc_code": ifsc_code,
            "type": payee_type,
            "added_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        if detect_fraud(payee_data, data_type="payee"):
            st.error("Potential fraud detected! Please verify the payee details.")
        else:
            payee_db.append(payee_data)
            st.success("Payee added successfully!")
            st.write("Payee Details:", payee_data)

# Section 2: Generate QR Code for Payment
st.header("Generate QR Code for Due Payment")
if payee_db:
    selected_payee = st.selectbox("Select Payee", [p["name"] for p in payee_db])
    due_amount = st.number_input("Due Amount (INR)", min_value=1.0, value=100.0, step=1.0)
    payment_description = st.text_input("Payment Description", "Payment of dues")

    if st.button("Generate Payment QR Code"):
        payee = next(p for p in payee_db if p["name"] == selected_payee)
        qr_data = f"Payee Name: {payee['name']}, Account Number: {payee['account_number']}, IFSC Code: {payee['ifsc_code']}, Amount: {due_amount}, Description: {payment_description}"
        qr_image = generate_qr(qr_data)
        st.image(qr_image, caption="Scan to Pay", use_column_width=True)

        # Add transaction to history
        transaction = {
            "payee_name": payee["name"],
            "account_number": payee["account_number"],
            "amount": due_amount,
            "description": payment_description,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        transactions_db.append(transaction)
else:
    st.write("No payees available. Please add a payee first.")

# Section 3: View Payee and Transaction History
st.header("View History")
view_choice = st.radio("View", ["Payees", "Transactions"])
if view_choice == "Payees":
    if payee_db:
        st.write(pd.DataFrame(payee_db))
    else:
        st.write("No payees added yet.")
elif view_choice == "Transactions":
    if transactions_db:
        st.write(pd.DataFrame(transactions_db))
    else:
        st.write("No transactions yet.")
