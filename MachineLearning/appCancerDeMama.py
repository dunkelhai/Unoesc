import streamlit as st
import pandas as pd
import joblib

model_path = "/Users/raiza/Documents/Python/Logistic_Regression/model.sav"
model = joblib.load(model_path)


def predict(attributes):
    prediction = model.predict(attributes)
    return prediction


def input_scalar(input_dataframe):
    scalar_filepath = "/Users/raiza/Documents/Python/Logistic_Regression/standard_scaler.sav"
    scalar = joblib.load(scalar_filepath)
    scaled_dataframe = scalar.transform(input_dataframe)
    return scaled_dataframe


# page settings
st.set_page_config(page_title="Cancer de mama",
                   page_icon="🔬",
                   layout="centered")
# page header
st.title(f"App de predição do câncer de mama")
st.subheader("Modelo de Regressão Logística\n"
             "Desenvolvido por: Alysson Oliveira e Raiza Zardo")
st.write("\nQuando o tumor se dá por crescimento do número de células, ele é chamado neoplasia - que pode ser benigna ou maligna. "
         "\nAo contrário do câncer, que é neoplasia maligna, as neoplasias benignas têm seu crescimento de forma organizada, em geral lento, e apresenta limites bem nítidos. "
         "\nElas tampouco invadem os tecidos vizinhos ou desenvolvem metástases. O lipoma e o mioma são exemplos de tumores benignos.")

with st.form("Prediction_form"):
    # from header
    st.header("Especificações da célula: ")
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
    st.success(f"A célula é: {value}")
