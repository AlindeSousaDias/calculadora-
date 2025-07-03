
def calcular_valores(venda, custo):
    try:
        # Trata entradas com vírgulas e sem pontos
        venda = float(str(venda).replace(",", "."))
        custo = float(str(custo).replace(",", "."))

        # Calcula markup
        markup = (venda / custo) if custo != 0 else 0

        # Calcula margem
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

    except ValueError:
        return {"Erro": "Por favor, insira números válidos para venda e custo."}

# Testando o código
venda_input = input("Digite o valor de venda: ")
custo_input = input("Digite o custo total: ")

resultado = calcular_valores(venda_input, custo_input)

for chave, valor in resultado.items():
    print(f"{chave}: {valor}")
