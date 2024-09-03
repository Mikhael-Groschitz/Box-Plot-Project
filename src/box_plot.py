import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar o dataset de despesas
df = pd.read_csv('../data/despesas_1000.csv')

# Configurar o estilo dos gráficos
sns.set(style="whitegrid")

# Criar o box plot
plt.figure(figsize=(12, 8))
ax = sns.boxplot(x='loja', y='despesa', data=df, palette="Set2")

# Adicionar título e labels
plt.title('Distribuição das Despesas Mensais por Tipo de Loja', fontsize=16)
plt.xlabel('Tipo de Loja', fontsize=14)
plt.ylabel('Despesa (R$)', fontsize=14)

# Adicionar etiquetas aos valores do box plot
for i, artist in enumerate(ax.artists):
    artist.set_edgecolor('black')
    artist.set_linewidth(1.2)
    for j in range(len(ax.lines)):
        line = ax.lines[j]
        if j % 6 == 0:
            x = line.get_xdata()[1]
            y = line.get_ydata()[1]
            ax.text(x, y, f'{y:.2f}', horizontalalignment='center', size=10, color='black', weight='semibold')

# Ajustar o layout e exibir o gráfico
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
