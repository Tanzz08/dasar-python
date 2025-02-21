import argparse
from datetime import datetime

# Inisialisasi parser argumen
parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan Nama Anda")
parser.add_argument('-t', '--tanggallahir', required=True, help="Masukkan Tanggal Lahir Anda (dd-mm-yyyy)")

# Parsing argumen
args = parser.parse_args()

# Konversi tanggal lahir menjadi objek datetime
try:
    tanggal_lahir = datetime.strptime(args.tanggallahir, "%d-%m-%Y")
except ValueError:
    print("Format tanggal lahir harus dd-mm-yyyy.")
    exit(1)

# Hitung usia berdasarkan tahun saat ini
usia = datetime.now().year - tanggal_lahir.year

# Sesuaikan panggilan berdasarkan usia
if usia < 30:
    panggilan = "Kakak"
else:
    panggilan = "Bapak"

# Cetak hasil
print(f"Terima kasih telah menggunakan panggildicoding.py, {panggilan} {args.nama}.")
