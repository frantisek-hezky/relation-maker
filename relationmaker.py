
import streamlit as st
import json

st.title("Generátor vazeb objektů")

# Definice dat
from_application = st.text_input ("Zadej jméno jedné aplikace, ze které chceš vytvořit 'from' vazby.", placeholder="core_business_glossary")
from_object_type_raw = st.text_input ("Zadej jméno objektových typů, ze kterých chceš vytvořit vazby.", placeholder="business_term, business_indicator, business_rule")

to_application = st.text_input ("Zadej jméno jedné aplikace, do které chceš vytvořit 'to' vazby.", placeholder="core_snowflake")
to_object_type_raw = st.text_input ("Zadej jméno objektových typů, do kterých chceš vytvořit vazby.", placeholder="database, table, column")

relation_type_key = st.text_input ("Zadej klíč relace.", placeholder="core#related")

# Titulek aplikace


from_object_type_key = [item.strip() for item in from_object_type_raw.split(",") if item.strip()]
to_object_type_key = [item.strip() for item in to_object_type_raw.split(",") if item.strip()]

# Výpis generovaných vazeb

relations = []
def relace_maker ():
    for to_key in to_object_type_key:
        for from_key in from_object_type_key:
            relation = {
                "fromObjectTypeKey": f"{from_application}#{from_key}",
                "toObjectTypeKey": f"{to_application}#{to_key}",
                "relationTypeKey": f"{relation_type_key}"
            }
            relations.append(relation)
            
    st.markdown("Vygenerované relace (kopírovatelné JSON pole):")
    st.code(json.dumps(relations, indent=2), language="json")


if st.button("Vytvoř relace"):
    if not all([from_application,from_object_type_raw,to_application,to_object_type_raw,relation_type_key ]):
        st.error("Vyplň prosím všechna pole před vytvořením relací.")

    elif '"' in from_application or '"' in to_application or '"' in relation_type_key \
        or '"' in from_object_type_raw or '"' in to_object_type_raw:
        st.error('Pole nesmí obsahovat uvozovky (").')
            
    elif ',' in from_application:
        st.error ('Pole "from_application" může obsahovat pouze jednu hodnotu.')

    elif ',' in to_application:
        st.error ('Pole "to_application" může obsahovat pouze jednu hodnotu.')

    elif ',' in relation_type_key:
        st.error ('Pole "relation" může obsahovat pouze jednu hodnotu.')

    else:
        relace_maker()


