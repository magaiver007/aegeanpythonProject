import matplotlib.pyplot as plt
import seaborn as sns

tips_dataset = sns.load_dataset("tips")
print(tips_dataset)

sns.displot(tips_dataset["total_bill"], bins=30, kde=False)
plt.show()
sns.relplot(x="total_bill", y="tip", data=tips_dataset)
plt.show()
sns.relplot(x="total_bill", y="tip", hue="sex", data=tips_dataset)
plt.show()
sns.pairplot(tips_dataset, hue="sex", palette="flare")
plt.show()
