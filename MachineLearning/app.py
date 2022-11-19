import streamlit as st
import pandas as pd
import joblib

model_path = "/Users/Alysson/Downloads/model.sav"
model = joblib.load(model_path)


def predict(attributes):
    prediction = model.predict(attributes)
    return prediction


def input_scalar(input_dataframe):
    scalar_filepath = "/Users/Alysson/Downloads/standardScaler.sav"
    scalar = joblib.load(scalar_filepath)
    scaled_dataframe = scalar.transform(input_dataframe)
    return scaled_dataframe


# page settings
st.set_page_config(page_title="Cancer de mama",
                   page_icon="A",
                   layout="centered")
# page header
st.title("App de predicao do cancer de mama")
st.subheader("Modelo de Regressao Logistica\n"
             "Desenvolvido por: Alysson Oliveira e Raiza Zardo")

with st.form("Prediction_form"):
    # from header
    st.header("Especificacoes da celula: ")
    # input elements
    Clump_thickness = st.slider(
        label="Clump thickness: ", min_value=0.0, max_value=10.00, step=0.01)
    Uniformity_of_cell_size = st.slider(
        label="Uniformity of cell size: ", min_value=0.0, max_value=10.00, step=0.01)
    Uniformity_of_cell_shape = st.slider(
        label="Uniformity of cell shape: ", min_value=0.0, max_value=10.00, step=0.01)
    Mitoses = st.slider(label="Mitoses: ", min_value=0.0,
                        max_value=9.0, step=0.01)

# Submit values
    submit_values = st.form_submit_button(label="Submit")
    if submit_values:
        # create input dictionary
        input_dict = {
            "Clump_thickness": Clump_thickness,
            "Uniformity_of_cell_size:": Uniformity_of_cell_size,
            "Uniformity_of_cell_shape": Uniformity_of_cell_shape,
            "Mitoses": Mitoses
        }

    # create input dataframe
        input_dataframe = pd.DataFrame(input_dict, index=[1])
    # scale inputs
        input_scaled = input_scalar(input_dataframe)
    # make predictions
        prediction = predict(input_scaled)

        if prediction == 2:
            value = 'Benigno'

        if prediction == 4:
            value = "Maligno"

# output header
    st.header("Resultado: ")

# output results
    st.success("A celula e: {value}")
