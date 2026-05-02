import streamlit as st
from utils.client import train_clients
from utils.server import aggregate_models

st.title("🔐 AI Federated Learning System")

if st.button("Run Federated Learning"):
    client_models = train_clients(num_clients=3)
    global_model = aggregate_models(client_models)

    st.success("✅ Global model updated successfully")
