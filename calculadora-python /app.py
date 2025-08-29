import streamlit as st

st.title("🧮 Python Calculator")

# Histórico de cálculos
if "history" not in st.session_state:
    st.session_state.history = []

# Inputs do usuário
num1 = st.number_input("First Number", value=0.0)
num2 = st.number_input("Second Number", value=0.0)
operation = st.selectbox("Choose Operation", ["Addition (+)", "Subtraction (-)", "Multiplication (*)", "Division (/)"])

# Botão de calcular
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"{num1} + {num2} = {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"{num1} - {num2} = {result}")
    elif operation == "Multiplication (*)":
        result = num1 * num2
        st.success(f"{num1} * {num2} = {result}")
    elif operation == "Division (/)":
        if num2 != 0:
            result = num1 / num2
            st.success(f"{num1} / {num2} = {result}")
        else:
            st.error("Error: Division by zero")
    
    # Adiciona ao histórico
