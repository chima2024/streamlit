import streamlit as st

# Predefined user database with Kuro, Chima, and Saynt
accounts = {
    "1111111111": {"name": "Kuro", "balance": 1500.0},
    "2222222222": {"name": "Chima", "balance": 1200.0},
    "3333333333": {"name": "Saynt", "balance": 800.0}
}

def deposit(account_number, amount, name="Guest"):
    if account_number in accounts:
        accounts[account_number]["balance"] += amount
    else:
        # Create a new account if it doesn't exist
        accounts[account_number] = {"name": name, "balance": amount}
    return accounts[account_number]["balance"]

# Streamlit App
st.title("🏦 Bank Deposit Portal")
st.header("💰 Deposit Funds")

# User input
account_number = st.text_input("Enter your Account Number:")
name = st.text_input("Enter your Name (for new accounts):")
amount = st.number_input("Enter amount to deposit:", min_value=0.01, step=0.01)

# Show balance preview if account already exists
if account_number in accounts:
    user = accounts[account_number]
    st.info(f"Account Holder: {user['name']} | Current Balance: ${user['balance']:.2f}")

if st.button("Deposit"):
    if account_number.strip() == "" or name.strip() == "" or amount <= 0:
        st.error("Please enter valid account number, name, and deposit amount.")
    else:
        new_balance = deposit(account_number, amount, name)
        st.success(f"Deposit successful for {accounts[account_number]['name']}! New balance: ${new_balance:.2f}")
