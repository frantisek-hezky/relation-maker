import streamlit as st

st.title("🎛️ Generátor vazeb objektů")

# --- VSTUPY ---
st.header("🔧 Vstupní parametry")

from_application = st.text_input("From Application", "core_keboola")
from_object_type_key = st.text_area(
    "From Object Type Keys (oddělené čárkou)", 
    "member,project,user,branch,component,flow,transformation,configuration,configuration_row,version,job,bucket,table,table_column"
)

to_application = st.text_input("To Application", "cust_btl_snowflake")
to_object_type_key = st.text_area(
    "To Object Type Keys (oddělené čárkou)", 
    "database,schema,dynamic_table,dynamic_table_column,external_table,external_table_column,file_format,function,pipe,procedure,sequence,stage,stream,table,table_column,task,view,view_column"
)

relation_type_key = st.text_input("Relation Type Key", "core#dataSource")

# --- TLAČÍTKO ---
if st.button("🔄 Generovat vazby"):
    st.subheader("🧾 Výstup:")
    
    # Převod vstupních stringů na listy
    from_object_type_key_list = [item.strip() for item in from_object_type_key.split(",") if item.strip()]
    to_object_type_key_list = [item.strip() for item in to_object_type_key.split(",") if item.strip()]
    
    # Generování výstupu
    for to_key in to_object_type_key_list:
        for from_key in from_object_type_key_list:
            relation = {
                "fromObjectTypeKey": f"{from_application}#{from_key}",
                "toObjectTypeKey": f"{to_application}#{to_key}",
                "relationTypeKey": relation_type_key
            }
            st.json(relation)
