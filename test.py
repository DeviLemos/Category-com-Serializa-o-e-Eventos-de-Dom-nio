from domain.category import Category


c1 = Category(name="Drama")
c2 = Category(name="Ação", description="Filmes de Ação")
c3 = Category(name="Comédia", description="Filmes de Comédia", is_active=False)

print("\n--- Testes básicos ---")
print(c1.description)
print(c2)
print(c3)
c3.activate()
print(c3)

"""
Saída esperada:
Drama |  (True)
Ação | Filmes de Ação (True)
Comédia | Filmes de Comédia (False)
Comédia | Filmes de Comédia (True)
"""

print("\n--- Serialização ---")
dict_c2 = c2.to_dict()
print("to_dict:", dict_c2)

c2_clone = Category.from_dict(dict_c2)
print("from_dict:", c2_clone.to_dict())


print("\n--- Eventos ---")

c2.update(name="Ação Atualizada", description="Nova descrição de ação")
c2.deactivate()
c2.activate()

for e in c2.events:
    print(" -", e)
