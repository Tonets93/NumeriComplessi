# Un numero complesso è costituito da una parte reale ed una immaginaria.
complexNum1 = (3 + -2j)
complexNum2 = (-1 + 5j)

# Restituiamo il tipo delle variabili dichiarate. In Python tutti i tipi sono oggetti.
print(type(complexNum1))
print(type(complexNum2))

# Calcoliamo il prodotto fra due numeri complessi.
complexProductResult = complexNum1 * complexNum2
print("Il prodotto fra i due numeri complessi è: ", complexProductResult)

# Accediamo alle proprietà 'real' e 'imag' dell'oggetto contenente il risultato.
print("Parte reale: ", complexProductResult.real)
print("Parte immaginaria: ", complexProductResult.imag)

