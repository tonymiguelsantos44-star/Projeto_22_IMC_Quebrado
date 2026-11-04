import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Calculadora de IMC",
    page_icon="⚖️",
    layout="wide",
)

st.tittle = '📚 Entendendo o IMC'

st.markdown(
    """
## O que é IMC ?

O IMC, ou Indice de Massa Corporal, é um calculo simples que relaciona o peso
e a altura de uma pesoa. Ele foi criado no século XIX pelo matemático belga
Adolphe Quetelet e hoje é muito utilizado pela Organização Mundial da Saúde (OMS)
para fazer uma triagem rapida da população adulta.
"""
)

st.subheder = "Como o IMC é calculado?"
st.latex(r"IMC = \frac{peso (kg)}{altura (cm)}")

st.markdown(
    """
## Por que o IMC é importante?

O IMC é importante pois ajuda a identificar possiveis riscos para a saude, como
diabetes, hipertenção e doenças do coração. Alem disso, ele é barato, rápido e
não precisa de nenhum equipamento sofisticado, so uma balança e uma fita métrica.

**Atenção:** o IMC não diferencia massa muscular de gordura. Por isso, um atleta
pode ser classificado com sobrepeso mesmo estando em otima forma. Em caso de duvida,
procure sempre um profissional de saude.
"""
)

st.subheader("Tabela de classificação")

tabela = pd.DataFrame(
    {
        "Classificação": ["Abaixo do peso", "Peso normal", "Sobrepeso", "Obesidade"],
        "IMC (kg/m²)": ["menor que 18,5", "18,5 a 29,9", "25 a 29,9" "30 a 34,9"],
    }
)
st.table(tabela)

st.image("imagens/tabela_imc.png", caption="Tabela de IMC", use_column_width=True)

st.subheader("Resumo rápido")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Abaixo do peso", "< 18,5")
with col2:
    st.metric("Peso normal", "18,5 – 24,9")
with col3:
    st.metric("Sobrepeso", "25 – 29,9")

if st.button("Quero saber mais"):
 st.info("O IMC é só o primeiro passo! Converse com um nutricionista ou médico.")

 st.page_link("pages/calculadora.py", label="Ir para a calculadora", icon="🧮")

 st.caption("Projeto desenvolvido para fins educativos. Nao substitui consulta médica.")
