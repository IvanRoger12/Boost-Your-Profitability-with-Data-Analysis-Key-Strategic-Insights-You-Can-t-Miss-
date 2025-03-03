import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données
file_path = "Sample - Superstore.csv"
df = pd.read_csv(file_path, encoding="latin1")

# Exploration des données
print(df.info())
print(df.head())

# Graphique des ventes par région et par catégorie
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x="Region", y="Sales", hue="Category", estimator=sum, ci=None, palette=["#72A7D9", "#5A9BD5", "#4178A7"])
plt.title("Total des ventes par région et catégorie de produit", fontsize=14, fontweight="bold")
plt.xlabel("Région", fontsize=12)
plt.ylabel("Total des ventes ($)", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Catégorie")
plt.show()

# Scatter plot des remises vs profit
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Discount", y="Profit", alpha=0.6, color="#72A7D9", edgecolor="black")
plt.title("Impact des remises sur le profit", fontsize=14, fontweight="bold")
plt.xlabel("Remise (%)", fontsize=12)
plt.ylabel("Profit ($)", fontsize=12)
plt.axhline(0, color="red", linestyle="dashed", linewidth=1.2)
plt.show()

# Scatter plot des ventes vs profit
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Sales", y="Profit", alpha=0.6, color="#72A7D9", edgecolor="black")
plt.title("Relation entre les ventes et le profit", fontsize=14, fontweight="bold")
plt.xlabel("Ventes ($)", fontsize=12)
plt.ylabel("Profit ($)", fontsize=12)
plt.xscale("log")
plt.axhline(0, color="red", linestyle="dashed", linewidth=1.2)
plt.show()

# Matrice de corrélation (Heatmap)
plt.figure(figsize=(8, 6))
correlation_matrix = df[["Sales", "Quantity", "Discount", "Profit"]].corr()
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Matrice de corrélation entre les variables numériques", fontsize=14, fontweight="bold")
plt.show()

# Boxplot des profits par catégorie de produit
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="Category", y="Profit", color="#72A7D9")
plt.title("Distribution des profits par catégorie de produit", fontsize=14, fontweight="bold")
plt.xlabel("Catégorie de produit", fontsize=12)
plt.ylabel("Profit ($)", fontsize=12)
plt.xticks(rotation=45)
plt.show()

# Tableau croisé dynamique des ventes et profits par région et segment
pivot_table = df.pivot_table(values=["Sales", "Profit"], index="Region", columns="Segment", aggfunc="sum")
print(pivot_table)
