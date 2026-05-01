from collections import Counter
import matplotlib.pyplot as plt

dados1 = ["Sim"] * 20 + ["Não"] * 45
print(dados1)

resposta1 = Counter(dados1)
print(resposta1)

labels = list(resposta1.keys())
values = list(resposta1.values())

colors =["skyblue"]
                                                # plt.bar = vertical
plt.bar(labels, values, color=colors)           # para deixar o grafico na horizontal usamos o plt.barh
plt.title("Resposta Entrevista")
plt.legend(labels, loc="upper right")
plt.show()



















































