import streamlit as st

def calculate_bmi(weight,hieght):
    return weight / ((hieght/100) ** 2)


def find_bmi_category(bmi):
    if bmi < 18.5:
        return "Under Weight","assests/bmi1.jpg"
    
    elif 18.5 <= bmi < 25:
        return "Normal Weight", "assests/bmi2.jpg"
    
    elif 25 <= bmi < 30:
        return "Over Weight", "assests/bmi3.jpg"
    
    else: 
        return "Obesity", "assests/bmi4.jpg"
    
st.title("BMI Calculater")

weight = st.number_input("Enter your weight(kg): ")
hieght = st.number_input("Enter your hieght(cm): ")

if st.button("Calculate BMI"):
    bmi = calculate_bmi(weight,hieght)

    category , image = find_bmi_category(bmi)

    st.write(f"Your BMI:{bmi:.3f}")
    
    st.image(image,caption=category)


