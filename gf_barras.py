import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [2,5,7,1,0]

# título
plt.title("Grafico de barras")

# eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.bar(x,y) # grafico de barras
plt.show()