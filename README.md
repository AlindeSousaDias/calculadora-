import streamlit as st

st.title("Calculadora de Lucro e Markup")

st.markdown("Insira os valores abaixo. A margem de lucro mínima deve ser de **15%**.")

# Entradas
venda_input = st.text_input("Valor de Venda (R$)", "")
custo_input = st.text_input("Custo Total (R$)", "")

def calcular_valores(venda, custo):
    try:
        venda = float(str(venda).replace(",", "."))
        custo = float(str(custo).replace(",", "."))

        markup = (venda / custo) if custo != 0 else 0
        margem = (venda - custo) / venda if venda != 0 else 0

        mensagem = ""
        if margem < 0.15:
            mensagem = "Atenção: Margem de lucro abaixo de 15%!"
        else:
            mensagem = "Margem de lucro dentro do ideal."

        return {
            "Valor de Venda (R$)": round(venda, 2),
            "Custo Total (R$)": round(custo, 2),
            "Markup": round(markup, 2),
            "Margem de Lucro (%)": f"{margem * 100:.2f}%",
            "Mensagem": mensagem
        }

    except:
        return {"Erro": "Por favor, insira valores válidos."}

if st.button("Calcular"):
    resultado = calcular_valores(venda_input, custo_input)
    for chave, valor in resultado.items():
        st.write(f"**{chave}**: {valor}")
