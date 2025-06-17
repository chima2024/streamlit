import streamlit as st

# Initialize session state for balances
if 'savings_balance' not in st.session_state:
    st.session_state.savings_balance = 0.0
if 'current_balance' not in st.session_state:
    st.session_state.current_balance = 0.0

st.title("Bank Account Interface")

# Sidebar for account selection and actions
st.sidebar.header("Account Operations")
account_type = st.sidebar.radio(
    "Select Account Type",
    ('Savings Account', 'Current Account')
)

operation = st.sidebar.selectbox(
    "Operation",
    ('Deposit', 'Withdraw', 'Check Balance')
)

amount = None
if operation in ['Deposit', 'Withdraw']:
    amount = st.sidebar.number_input(
        "Amount", min_value=0.0, step=0.01, format="%.2f"
    )

# Button to execute operation
if st.sidebar.button("Execute"):
    if account_type == 'Savings Account':
        if operation == 'Deposit':
            st.session_state.savings_balance += amount
            st.success(f"Deposited ₦{amount:.2f} to Savings Account.")
        elif operation == 'Withdraw':
            if amount <= st.session_state.savings_balance:
                st.session_state.savings_balance -= amount
                st.success(f"Withdrew ₦{amount:.2f} from Savings Account.")
            else:
                st.error("Insufficient funds in Savings Account.")
        else:
            st.info(f"Savings Account Balance: ₦{st.session_state.savings_balance:.2f}")
    else:
        if operation == 'Deposit':
            st.session_state.current_balance += amount
            st.success(f"Deposited ₦{amount:.2f} to Current Account.")
        elif operation == 'Withdraw':
            if amount <= st.session_state.current_balance:
                st.session_state.current_balance -= amount
                st.success(f"Withdrew ₦{amount:.2f} from Current Account.")
            else:
                st.error("Insufficient funds in Current Account.")
        else:
            st.info(f"Current Account Balance: ₦{st.session_state.current_balance:.2f}")

# Main dashboard view
st.header("Account Dashboard")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Savings Account")
    st.metric(label="Balance", value=f"₦{st.session_state.savings_balance:.2f}")
with col2:
    st.subheader("Current Account")
    st.metric(label="Balance", value=f"₦{st.session_state.current_balance:.2f}")

st.markdown("---")
st.write("Use the sidebar to manage your accounts.")

























































































































































































































