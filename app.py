import streamlit as st

st.set_page_config(
    page_title="Simple Calculator",
    page_icon="🧮"
)

st.title("🧮 Simple Calculator")

operator = st.selectbox(
    "Select Operation",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (*)",
        "Division (/)"
    ]
)

if operator == "Addition (+)":

    values = st.text_input(
        "Enter values separated by comma",
        placeholder="Example: 10,20,30,40"
    )

    if st.button("Calculate Addition"):

        try:
            val_list = [float(x.strip()) for x in values.split(",")]
            result = sum(val_list)

            st.success(f"Addition = {result}")

        except ValueError:
            st.error("Please enter valid numbers.")


elif operator == "Subtraction (-)":

    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")

    if st.button("Calculate Subtraction"):

        st.success(f"{num1} - {num2} = {num1 - num2}")
        st.success(f"{num2} - {num1} = {num2 - num1}")


elif operator == "Multiplication (*)":

    values = st.text_input(
        "Enter values separated by comma",
        placeholder="Example: 2,3,4,5"
    )

    if st.button("Calculate Multiplication"):

        try:
            val_list = [float(x.strip()) for x in values.split(",")]

            result = 1

            for value in val_list:
                result = result * value

            st.success(f"Multiplication = {result}")

        except ValueError:
            st.error("Please enter valid numbers.")


elif operator == "Division (/)" :

    num1 = st.number_input("Enter first number")
    num2 = st.number_input("Enter second number")

    if st.button("Calculate Division"):

        if num2 != 0:
            st.success(f"{num1} / {num2} = {num1 / num2}")
        else:
            st.error("You cannot divide by zero.")