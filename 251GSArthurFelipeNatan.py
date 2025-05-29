
tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_afetados = []
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

def coletar_dados():
    print("\n Registrar Desastre ")
    tipo = input("Tipo de desastre (incêndio, enchente, tempestade, ciclone): ").strip().lower()
    pais = input("País: ").strip()
    cidade = input("Cidade: ").strip()
    bairro = input("Bairro: ").strip()
    rua = input("Rua: ").strip()


    total = int(input("Quantidade total de pessoas afetadas: "))


    contagem_criancas = int(input("Quantidade de crianças afetadas: "))
    contagem_adultos = int(input("Quantidade de adultos afetados: "))
    contagem_idosos = int(input("Quantidade de idosos afetados: "))
    contagem_mobilidade = int(input("Quantidade de pessoas com mobilidade reduzida afetadas: "))
    contagem_feridos = int(input("Quantidade de feridos: "))


    if total != (contagem_criancas + contagem_adultos + contagem_idosos + contagem_mobilidade + contagem_feridos):
        print("Erro: A soma das categorias não corresponde ao total de pessoas afetadas.")
        return False



