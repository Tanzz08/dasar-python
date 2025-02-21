import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 8, 10]

# membuat plot garis
plt.plot(x, y)

# menambahkan judul dan label sumbu
plt.title("Contoh Plot Garis")
plt.xlabel("Submbu X")
plt.ylabel("Submbu Y")

# menampilkan plot
plt.show()
