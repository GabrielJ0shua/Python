from banco import Banco, Conta

c = Conta(0, "Gabriel", 18, {"end": {"rua corumba"}})
b = Banco()

b.addConta(c)

print(c.idade)
print(b.numberAccount)