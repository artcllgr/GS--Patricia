#Arthur Callegari - 565476
#Felipe Franca - 566393
#Natan Mestre - 565552

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

    tipos_desastres.append(tipo)
    paises.append(pais)
    cidades.append(cidade)
    bairros.append(bairro)
    ruas.append(rua)
    total_afetados.append(total)
    criancas.append(contagem_criancas)
    adultos.append(contagem_adultos)
    idosos.append(contagem_idosos)
    mobilidade_reduzida.append(contagem_mobilidade)
    feridos.append(contagem_feridos)

    return True


def gerar_relatorio():
    total_geral = sum(total_afetados)
    total_criancas = sum(criancas)
    total_adultos = sum(adultos)
    total_idosos = sum(idosos)
    total_mobilidade = sum(mobilidade_reduzida)
    total_feridos = sum(feridos)

    categorias = {
        "Crianças": total_criancas,
        "Adultos": total_adultos,
        "Idosos": total_idosos,
        "Mobilidade reduzida": total_mobilidade,
        "Feridos": total_feridos
    }

    categoria_mais_afetada = max(categorias, key=categorias.get)
    desastre_mais_grave_index = total_afetados.index(max(total_afetados))
    local_mais_afetado = f"{ruas[desastre_mais_grave_index]}, {bairros[desastre_mais_grave_index]}, {cidades[desastre_mais_grave_index]}, {paises[desastre_mais_grave_index]}"

    print("\nRelatório Final")
    print(f"Quantidade total de desastres registrados: {len(tipos_desastres)}")
    print(f"Total de pessoas afetadas em cada categoria:")
    print(f"Crianças: {total_criancas} | Adultos: {total_adultos} | Idosos: {total_idosos} | Mobilidade reduzida: {total_mobilidade} | Feridos: {total_feridos}")
    print(f"Categoria mais afetada: {categoria_mais_afetada}")
    print(f"Total geral de pessoas afetadas: {total_geral}")
    print(f"Local do desastre mais grave: {local_mais_afetado}")


def main():
    while True:
        if coletar_dados():
            continuar = input("\nDeseja registrar outro desastre? (s/n): ").strip().lower()
            if continuar != 's':
                break
        else:
            print("Tente novamente.")

    gerar_relatorio()

if __name__ == "__main__":
    main()


