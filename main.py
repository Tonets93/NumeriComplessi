# Un numero complesso è costituito da una parte reale ed una immaginaria.
complex_num_1 = (3 + -2j)
complex_num_2 = (-1 + 5j)

# Restituiamo il tipo delle variabili dichiarate. In Python tutti i tipi sono oggetti.
print(type(complex_num_1))
print(type(complex_num_2))

# Calcoliamo il prodotto fra due numeri complessi.
complex_product_result = complex_num_1 * complex_num_2
print("Il prodotto fra i due numeri complessi è: ", complex_product_result)

# Accediamo alle proprietà 'real' e 'imag' dell'oggetto contenente il risultato.
print("Parte reale: ", complex_product_result.real)
print("Parte immaginaria: ", complex_product_result.imag)

