import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = {
    "income": [5000, 15000, 3000, 25000, 7000, 20000],
    "family_members": [6, 4, 7, 3, 5, 4],
    "employed": [0, 1, 0, 1, 0, 1],
    "poverty": [1, 0, 1, 0, 1, 0]
}

df = pd.DataFrame(data)

X = df[['income', 'family_members', 'employed']]
y = df['poverty']

model = DecisionTreeClassifier()
model.fit(X, y)

st.title("PovertyAI")

income = st.number_input("Monthly Income")
family = st.number_input("Family Members")
employed = st.selectbox("Employed?", ["No", "Yes"])

if st.button("Predict"):
    emp = 1 if employed == "Yes" else 0
    prediction = model.predict([[income, family, emp]])

    if prediction[0] == 1:
        st.error("High Poverty Risk")
    else:
        st.success("Low Poverty Risk")
