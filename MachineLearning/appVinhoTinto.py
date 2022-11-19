import streamlit as st
import pandas as pd
import joblib

model_path = "/Users/raiza/Documents/Python/Linear_Regression/linear_model.sav"
model = joblib.load(model_path)


def predict(attributes):
    prediction = model.predict(attributes)
    return prediction


# page config
st.set_page_config(page_title="Acidez total no vinho tinto ",
                   page_icon="🍷",
                   layout="centered")

# page settings
st.title(f"Predição da acidez total no vinho tinto")
st.subheader(
    "Modelo de Regressão Linear\n" "Desenvolvido por: Alysson Oliveira e Raiza Zardo")
st.write("\nAo entrar em contato com a mucosa da boca, os ácidos do vinho desequilibram o pH local e, para equilibrá-lo, a cavidade bucal é inundada com saliva. Assim, quanto maior a acidez do vinho, maior será a salivação."
"\nA acidez também provoca certo incômodo na mucosa bucal que, às vezes, é confundido com o ardor causado pelo álcool, o qual provoca também uma sensação de calor na boca. "
    "\nÉ normal encontrarmos pessoas que confundem as sensações causadas por ambos, por isso, tome apenas o volume de salivação como indicador do nível de acidez."
)

with st.form("Formulário de predição"):
    st.header("Especificações do vinho:")
    # imput elements
    acido_citrico = st.slider(label="Ácido cítrico: ",
                              min_value=0.0, max_value=1.0, step=0.01)
    sulfatos = st.slider(label="Sulfatos: ", min_value=0.0,
                         max_value=2.0, step=0.01)
    qualidade = st.slider(label="Qualidade: ",
                          min_value=0.0, max_value=8.0, step=0.01)
    acucar_residual = st.slider(
        label="Açucar Residual: ", min_value=0.0, max_value=15.50, step=0.01)

# submit values
    submit_values = st.form_submit_button(label="Submit")
    if submit_values:
        # create input dictionary
        input_dic = {
            "acido_citrico": acido_citrico,
            "sulfatos": sulfatos,
            "qualidade": qualidade,
            "acucar_residual": acucar_residual
        }
    # create input dataframe
        input_dataframe = pd.DataFrame(input_dic, index=[1])
    # make preditions
        prediction = predict(input_dataframe)

    st.header(f"O resultado é: {prediction}")
    # output results
    st.success(f"A acidez total do vinho é igual a: {prediction}")
