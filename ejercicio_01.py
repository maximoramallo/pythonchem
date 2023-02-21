'''1) Utilizando el manejo de cadenas, listas, sus métodos internos... Transforma este texto:
un día que el viento soplaba con fuerza#mira como se mueve aquella banderola -dijo un monje#lo que se mueve es el viento -respondió otro monje#ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro

En este otro:

Un día que el viento soplaba con fuerza...
- Mira como se mueve aquella banderola -dijo un monje.
- Lo que se mueve es el viento -respondió otro monje.
- Ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro.'''

#Una forma
caracter = "#"
lista_frases = []
while (caracter in texto) == True:
    linea = texto[:texto.find(caracter)]
    lista_frases.append(linea)
    texto = texto[texto.find(caracter)+1:]
print(texto2[:texto2.find(caracter)].capitalize()+"...")
for f in lista_frases:
    if texto2[:texto2.find(caracter)] != f:
        print("- "+f.capitalize()+".")
print("- "+texto2[texto2.rfind(caracter)+1:].capitalize()+".")
