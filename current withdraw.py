import streamlit as st

# Predefined user database with Kuro, Chima, and Saynt
accounts = {
    "1111111111": {"name": "Kuro", "balance": 1500.0},
    "2222222222": {"name": "Chima", "balance": 1200.0},
    "3333333333": {"name": "Saynt", "balance": 800.0}
}

def withdraw(account_number, amount):
    if account_number in accounts:
        if accounts[account_number]["balance"] >= amount:
            accounts[account_number]["balance"] -= amount
            return True, accounts[account_number]["balance"]
        else:
            return False, "Insufficient balance"
    else:
        return False, "Account not found"

# Streamlit App
st.title("🏦 Bank Withdrawal Portal")
st.header("💸 Withdraw Funds")

# User input
account_number = st.text_input("Enter your Account Number:")
amount = st.number_input("Enter amount to withdraw:", min_value=0.01, step=0.01)

# Show balance preview if account already exists
if account_number in accounts:
    user = accounts[account_number]
    st.info(f"Account Holder: {user['name']} | Current Balance: ${user['balance']:.2f}")

if st.button("Withdraw"):
    if account_number.strip() == "" or amount <= 0:
        st.error("Please enter a valid account number and withdrawal amount.")
    else:
        success, result = withdraw(account_number, amount)
        if success:
            st.success(f"Withdrawal successful! New balance: ${result:.2f}")
        else:
            st.error(result)
