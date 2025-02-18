import streamlit as st

def main():
    st.title("MSME Budgeting System")
    
    income = st.number_input("Enter your monthly income:", min_value=0.0, step=100.0)
    
    st.subheader("Add Expenses")
    expense_name = st.text_input("Expense Name")
    expense_amount = st.number_input("Expense Amount", min_value=0.0, step=50.0)
    
    if "expenses" not in st.session_state:
        st.session_state.expenses = []
    
    if st.button("Add Expense"):
        if expense_name and expense_amount:
            st.session_state.expenses.append({"name": expense_name, "amount": expense_amount})
    
    st.subheader("Expenses")
    total_expenses = sum(exp["amount"] for exp in st.session_state.expenses)
    remaining_budget = income - total_expenses
    
    for exp in st.session_state.expenses:
        st.write(f"{exp['name']}: ₱{exp['amount']:.2f}")
    
    st.subheader("Summary")
    st.write(f"**Total Expenses:** ₱{total_expenses:.2f}")
    st.write(f"**Remaining Budget:** ₱{remaining_budget:.2f}")
    
    if remaining_budget < 0:
        st.error("Warning: You are over budget!")
    else:
        st.success("You are within budget.")
    
if __name__ == "__main__":
    main()
