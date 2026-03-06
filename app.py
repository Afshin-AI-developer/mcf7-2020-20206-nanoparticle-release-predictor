# -*- coding: utf-8 -*-
import os
import pickle
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="MCF-7 Nanoparticle-Based Anticancer Drug Release Predictor",
    page_icon="🧪",
    layout="centered"
)

st.title("MCF-7 Nanoparticle-Based Anticancer Drug Release Predictor")
st.markdown(
    """
    This tool predicts **Drug release amount (%)** based on nanoparticle formulation
    and release-condition parameters.
    """
)

MODEL_PATH = "best_drug_release_regression_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

st.subheader("Enter Input Variables")

size_dls = st.number_input("size (DLS) of nanoparticle (nm)-mean", value=150.0, format="%.6f")
pdi = st.number_input("Polydispersity Index (PDI) of nanoparticle-mean", value=0.200000, format="%.6f")
zeta = st.number_input("Zeta potential of nanoparticle (mV)-mean", value=-20.0, format="%.6f")
drug_loading = st.number_input("Drug loading capacity (%)-mean", value=10.0, format="%.6f")
entrapment_eff = st.number_input("Entrapment efficiency of nanoparticle (%)-mean", value=75.0, format="%.6f")
temperature = st.number_input("Temperature °C", value=37.0, format="%.6f")
ph = st.number_input("PH", value=7.4, format="%.6f")
time_release = st.number_input("Time of Drug release (h)", value=24.0, format="%.6f")

if st.button("Predict Drug Release Amount (%)"):
    input_data = np.array([[
        size_dls,
        pdi,
        zeta,
        drug_loading,
        entrapment_eff,
        temperature,
        ph,
        time_release
    ]], dtype=float)

    prediction = model.predict(input_data)[0]

    st.success(f"Predicted Drug Release Amount (%): {prediction:.4f}")