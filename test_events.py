from domain.category import Category

# 1️ Criação
cat = Category(name="Drama", description="Filmes dramáticos")
print("Criado:", cat.to_dict())

# 2️ Serialização
data = cat.to_dict()
clone = Category.from_dict(data)
print("Reconstruído:", clone.to_dict())

# 3️ Atualização
cat.update(name="Drama Atualizado", description="Nova descrição")
cat.deactivate()
cat.activate()

# 4️ Eventos
print("\nEventos:")
for e in cat.events:
    print(" -", e)
