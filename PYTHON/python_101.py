
lista_frutas = ['papaya','toronja','fresa', 'mango', 'platano']
lista_pais = ['Peru','Ecuador','EEUU', 'España', 'Japon']
peru = {
    "idioma": "Español",
    "poblacion": 31000000,
    "flag": True 
}
paises = [
    {
    "pais": "Peru",
    "idioma":"español",
    "poblacion": 31000000
    },
    {
    "pais":"EEUU",
    "idioma":"ingles",
    "poblacion": 331000000
    },
    {
    "pais":"Japon",
    "idioma":"japones",
    "poblacion": 127000000
    }
]

# Enmcagada de agregar valores a N listas
def agregar_a_lista(la_lista, el_objeto):
    la_lista.append(el_objeto)

# Itera cualquier lista
def itera_lista(lista, index=False):
    for n in lista:
        if index == False:
            print(n)
        else:
            print(n[index])
    print('\n')


def run():
    agregar_a_lista(lista_frutas, "Maracumango")
    itera_lista(lista_frutas)

    # agregar_a_lista(lista_pais, "Australia")
    # itera_lista(lista_pais)

    itera_lista(paises, 'pais')


if __name__ == '__main__':
    run()

