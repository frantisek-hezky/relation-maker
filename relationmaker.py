import streamlit as st

# Definice dat
from_application = ["core_keboola"]
from_object_type_key = [
    "member", "project", "user", "branch", "component", "flow", "transformation",
    "configuration", "configuration_row", "version", "job", "bucket", "table", "table_column"
]

to_application = ["cust_btl_snowflake"]
to_object_type_key = [
    "database", "schema", "dynamic_table", "dynamic_table_column", "external_table",
    "external_table_column", "file_format", "function", "pipe", "procedure", "sequence",
    "stage", "stream", "table", "table_column", "task", "view", "view_column"
]

relation_type_key = "core#dataSource"

# Titulek aplikace
st.title("Generátor vazeb objektů")

# Výpis generovaných vazeb
st.subheader("Výstup:")
for to_key in to_object_type_key:
    for from_key in from_object_type_key:
        relation = {
            "fromObjectTypeKey": f"{from_application[0]}#{from_key}",
            "toObjectTypeKey": f"{to_application[0]}#{to_key}",
            "relationTypeKey": relation_type_key
        }
        st.json(relation)
