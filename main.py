import streamlit as st
import calculations as cal 
import time 

st.set_page_config(page_title="Unit Converter", page_icon="⚖", layout="wide")

st.subheader("Hey!, 👋")
st.title("Welcome to :red-background[Marjan's Unit Converter]")
st.markdown("##### Convert between different units of measurement.")

units: list[str] = ["Length", "Mass", "Time", "Temperature"]
length_units = ['Kilometers', 'Meters', 'Centimeters', 'Millimeters']
mass_units = ['Kilograms', 'Grams', 'Milligrams']
time_units = ['Seconds', 'Minutes', 'Hours']
temp_units = ['Celsius', 'Fahrenheit', 'Kelvin']

selected_unit = st.selectbox("Select a unit to convert:", units)

with st.form("unit_conversion_form"):
    if selected_unit == "Length":
        from_unit = st.selectbox("Convert from:", length_units)
        to_unit = st.selectbox("Convert to:", length_units)
        value = st.number_input("Enter the value to convert:", min_value=0)

    elif selected_unit == "Mass":
        from_unit = st.selectbox("Convert from:", mass_units)
        to_unit = st.selectbox("Convert to:", mass_units)
        value = st.number_input("Enter the value to convert:", min_value=0)

    elif selected_unit == "Time":
        from_unit = st.selectbox("Convert from:", time_units)
        to_unit = st.selectbox("Convert to:", time_units)
        value = st.number_input("Enter the value to convert:", min_value=0)

    elif selected_unit == "Temperature":
        from_unit = st.selectbox("Convert from:", temp_units)
        to_unit = st.selectbox("Convert to:", temp_units)
        value = st.number_input("Enter the value to convert:", min_value=0)

    submit_button = st.form_submit_button("Convert")

# When the "Convert" button is clicked, perform the conversion
if submit_button:
    if selected_unit == "Length" and from_unit and to_unit and value:
        unit_map = {
            "Kilometers": "km",
            "Meters": "m",
            "Centimeters": "cm",
            "Millimeters": "mm"
        }
        result = cal.length_calc(unit_map[from_unit], unit_map[to_unit], value)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

    elif selected_unit == "Mass" and from_unit and to_unit and value:
        unit_map = {
            "Kilograms": "kg",
            "Grams": "g",
            "Milligrams": "mg",
        }
        result = cal.mass_calc(unit_map[from_unit], unit_map[to_unit], value)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

    elif selected_unit == "Time" and from_unit and to_unit and value:
        unit_map = {
            "Hours": "h",
            "Minutes": "m",
            "Seconds": "s",
        }
        result = cal.time_calc(unit_map[from_unit], unit_map[to_unit], value)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

    elif selected_unit == "Temperature" and from_unit and to_unit and value:
        unit_map = {
            "Kelvin": "K",
            "Fahrenheit": "F",
            "Celsius": "C",
        }
        result = cal.temp_calc(unit_map[from_unit], unit_map[to_unit], value)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

st.markdown(f"<h6 style='text-align: center; color: black;'>© {time.strftime} 2025 Mohammad Marjan Ahmed. All rights reserved.</h6>", unsafe_allow_html=True)
