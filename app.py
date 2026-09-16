import requests
import random
import json
import os

# funcao de recomendacao de musicas - posso melhorar..
def recomendar_musica():
    pasta_do_projeto = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta_do_projeto, "musicas.json")
    with open(caminho, "r", encoding="utf-8") as arquivo:
        musicas = json.load(arquivo)
    escolhida = random.choice(musicas)
    return f"Música do dia: {escolhida}"

# funcao de buscar o clima
def buscar_clima():
    latitude = -22.91
    longitude = -43.17
    cidade = "Rio de Janeiro"

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    #requisicao
    resposta = requests.get(url)

    # transformar em json
    dados = resposta.json()

    temperatura = dados["current_weather"]["temperature"]
    if temperatura > 27:
        return f"Hoje vai rolar uma praia! {cidade}: {temperatura}°C"
    else:
        return f"Clima no {cidade}: {temperatura}°C"


# funcao do preco do bitcoin
def buscar_bitcoin():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,brl"

    resposta = requests.get(url)
    dados = resposta.json()

    preco_usd = dados["bitcoin"]["usd"]
    preco_brl = dados["bitcoin"]["brl"]

    return f"₿ Bitcoin: US$ {preco_usd:,.2f} | R$ {preco_brl:,.2f}"


# funcao para juntar todos os valores
def main():
    print("=" * 40)
    print("  Bom dia Pedro, Vamos para mais um dia.:")
    print("=" * 40)
    print()
    print(buscar_clima())
    print(buscar_bitcoin())
    print(recomendar_musica())
    print()
    print("=" * 40)


if __name__ == "__main__":
    main()