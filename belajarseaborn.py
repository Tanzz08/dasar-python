import seaborn as sns
import matplotlib.pyplot as plt

# contoh data 
tips = sns.load_dataset('tips') # memuat dataset tips dari seaborn

# contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogtam Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()