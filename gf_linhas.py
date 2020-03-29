import matplotlib.pyplot as plt
x = [1,2,5]
y = [2,5,7]

# título
plt.title("Meu primeiro gráfico")

# eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.plot(x,y)
plt.show()