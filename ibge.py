import requests

def lista_estados():
    return {"AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas", "BA": "Bahia",
        "CE": "Ceará", "DF": "Distrito Federal", "ES": "Espírito Santo", "GO": "Goiás",
        "MA": "Maranhão", "MT": "Mato Grosso", "MS": "Mato Grosso do Sul", "MG": "Minas Gerais",
        "PA": "Pará", "PB": "Paraíba", "PR": "Paraná", "PE": "Pernambuco", "PI": "Piauí",
        "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte", "RS": "Rio Grande do Sul", "RO": "Rondônia",
        "RR": "Roraima", "SC": "Santa Catarina", "SP": "São Paulo", "SE": "Sergipe", "TO": "Tocantins"}

def estados():
    estados = lista_estados()
    uf =[]
    for sigla, nome in estados.items():
        uf.append(nome)
    return uf

def cidades(estado):
    estados = lista_estados()

    sigla = ""
    for uf, nome in estados.items():
        if estado in nome:
            sigla = uf

    # Busca cidades da API do IBGE
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{sigla}/municipios"
    response = requests.get(url)
    if response.status_code == 200:
        cidades = [cidade['nome'] for cidade in response.json()]
        cidades.sort()
    else:
        cidades = []
    return cidades


