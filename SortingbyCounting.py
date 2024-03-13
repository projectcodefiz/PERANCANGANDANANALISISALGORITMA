# Nama : Abdul Hafiz
# NIM : 22343017

def hitung_jumlah_elemen_sama(data, nilai):
  jumlah_elemen_sama = 0
  for elemen in data:
    if elemen == nilai:
      jumlah_elemen_sama += 1
  return jumlah_elemen_sama

def penyortiran_penukaran_ruang_waktu(data):
  n = len(data)
  
  # Menghitung jumlah maksimum elemen yang sama
  max_jumlah_elemen_sama = 0
  for nilai in data:
    jumlah_elemen_sama = hitung_jumlah_elemen_sama(data, nilai)
    if jumlah_elemen_sama > max_jumlah_elemen_sama:
      max_jumlah_elemen_sama = jumlah_elemen_sama

  # Membuat daftar untuk menyimpan elemen yang telah dihitung
  data_terhitung = [[] for _ in range(max_jumlah_elemen_sama + 1)]

  # Mendistribusikan elemen ke dalam daftar berdasarkan jumlah kemunculannya
  for nilai in data:
    jumlah_elemen_sama = hitung_jumlah_elemen_sama(data, nilai)
    data_terhitung[jumlah_elemen_sama].append(nilai)

  # Menggabungkan daftar elemen yang telah dihitung
  data_terhitung = [elemen for daftar in data_terhitung for elemen in daftar]

  return data_terhitung

# Mengambil input data dari pengguna
data = []
while True:
  try:
    nilai = int(input("Masukkan nilai: "))
    data.append(nilai)
  except ValueError:
    break

print("Data awal:", data)

data_terurut = penyortiran_penukaran_ruang_waktu(data)
print("Data setelah disortir:", data_terurut)
