import streamlit as st

# Definice dat
from_application = st.text_input ("Zadej jméno aplikace, ze které chceš vytvořit from vazby.")
from_object_type_key = st.text_input ("Zadej jméno objektových typů, ze kterých chceš vytvořit vazby.")

to_application = st.text_input ("Zadej jméno aplikace, do které chceš vytvořit to vazby.")
to_object_type_key = st.text_input ("Zadej jméno objektových typů, do kterých chceš vytvořit vazby.")

relation_type_key = st.text_input ("Zadej klíče relace.")

# Titulek aplikace
st.title("Generátor vazeb objektů")

# Výpis generovaných vazeb

def relace_maker ():
    for to_key in to_object_type_key:
        for from_key in from_object_type_key:
            relation = {
                "fromObjectTypeKey": f"{from_application[0]}#{from_key}",
                "toObjectTypeKey": f"{to_application[0]}#{to_key}",
                "relationTypeKey": relation_type_key
            }
            st.json(relation)
if st.button("Vytvoř relace"):
    relace_maker()
