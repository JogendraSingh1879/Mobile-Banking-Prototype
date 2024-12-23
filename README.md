# Check out the streamlit links for web application- 

# https://mobile-banking-prototype-j2dlbjqo8ybrcmx6satw6p.streamlit.app/

# Mobile Banking: Account Payee Addition and Payment System
This project showcases a Mobile Banking Application prototype built using AI and modern web technologies. The system enables users to add account payees, generate QR codes for due payments, and simulate transaction processing with fraud detection capabilities.

# Features
1. Account Payee Management
Add account payees with details such as name, account number, IFSC code, and payee type.
Validate account details with AI-powered fraud detection.
2. QR Code Payment Generation
Generate secure QR codes for payment to payees.
Include details like payee name, account number, due amount, and payment description in the QR code.
3. Transaction History
Maintain a detailed log of transactions.
View payee and transaction history in a tabular format.
4. AI Integration
Fraud detection for payee addition and transactions.
Placeholder for predictive analytics, such as reminders for due payments or suspicious activity detection.

# Technology Stack
Backend and Logic
Python: For building the backend logic.
Pandas: For managing and displaying data in tabular form.

# Web Interface
Streamlit: A framework for creating a user-friendly, interactive web interface.
QR Code Functionality
QRCode: For generating QR codes.
Pillow: For handling and processing QR code images.

# AI Capabilities
Rule-based fraud detection with placeholders for AI model integration.

# How It Works
Add Account Payees:

Enter payee details such as name, account number, and IFSC code.
Fraud detection validates the payee details to prevent errors or malicious entries.
Generate Payment QR Code:

Select a payee and specify the due amount.
A secure QR code is generated, ready for scanning and payment.
Transaction History:

Log all transactions in a database for easy reference and monitoring.

# AI Features:

Fraud detection based on predefined patterns (expandable with AI models).
Predictive analytics for payment reminders and suspicious activity.

# Installation and Setup

# Prerequisites
Python 3.8 or higher
Pip (Python package manager)

# Future Enhancements

AI-Driven Features:

Implement machine learning models for predictive analytics.
Advanced fraud detection for transactions and payee addition.

Real-Time QR Code Scanning: Integrate with hardware or camera for live QR code scanning.
Payment Gateway Integration: Connect to banking APIs for real-time payment processing.
Enhanced User Experience: Add features like user authentication, notification systems, and mobile-first design.
