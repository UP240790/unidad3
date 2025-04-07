lista = tuple()

hermano = ("Victor", "Daniel")
hermana = ("Wendy", "Dennis")
hermanos = hermano + hermana
print(hermanos)

print(f"yo tengo {len(hermanos)} hermanos")

familia = hermanos + ("victor","Wendy")
print(familia)

sibling = familia[:len(hermanos)]
padres = familia[-2:]
print(familia, padres)

fruta = ("Mango", "uva", "sandia")
verduras = ("lechuga", "champiñon", "papa")
producto_animal = ("huevo", "jamon", "carne")

comida_completa = fruta + verduras + producto_animal
print(comida_completa)

comida_completalista = list(comida_completa)
print(comida_completalista)

mid = int(len(comida_completalista)/2)
comidast = comida_completalista[:mid]
print(comidast)

del comidast

paisesnordicos = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in paisesnordicos)
print("Iceland" in paisesnordicos)
