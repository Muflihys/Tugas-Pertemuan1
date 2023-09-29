# Kegiatan 1

# Fungsi untuk penjumlahan
def plus(a, b):
    return a + b

# Fungsi untuk pengurangan
def minus(a, b):
    return a - b

# Fungsi untuk perkalian
def mult(a, b):
    return a * b

# Fungsi untuk pembagian
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa melakukan pembagian oleh 0"

# Fungsi tree yang dapat mengoperasikan pohon ekspresi
def tree(expression):
    if isinstance(expression, tuple):
        left, operator, right = expression
        
        
        if operator == '+':
            return plus(tree(left), tree(right))
        elif operator == '-':
            return minus(tree(left), tree(right))
        elif operator == '*':
            return mult(tree(left), tree(right))
        elif operator == '/':
            return div(tree(left), tree(right))
    else:
        return expression

# Contoh pohon ekspresi: ((2, '+', 3), '*', (5, '-', 1))
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi pohon ekspresi dengan fungsi pada paradigma fungsional
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:", result)
print("================================")

# =======================================
# Kegiatan 2
random_list = [105, 3.1, "hello", 737, "python", 2.7, "world", 412, 5.5, "AI"]

# Inisialisasi struktur data untuk hasil pemisahan
float_tuple = ()
string_list = []
int_dict = { "ratusan" : [], "puluhan" : [], "satuan": []}



# Iterasi melalui elemen-elemen dalam random_list
for item in random_list:
    if isinstance(item, float):
        # Jika item adalah float, tambahkan ke dalam tuple float_tuple
        float_tuple += (item,)
    elif isinstance(item, str):
        # Jika item adalah string, tambahkan ke dalam list string_list
        string_list.append(item)
    elif isinstance(item, int):
        # Jika item adalah int, pisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = (item // 100) % 10
        
        # Tambahkan ke dalam dictionary int_dict
        int_dict["satuan"].append(satuan)
        int_dict["puluhan"].append(puluhan)
        int_dict["ratusan"].append(ratusan) 

# Hasil pemisahan
print("Tuple float:", float_tuple)
print("List string:", string_list)
print("Dictionary int:", int_dict)
print("================================")


# =================================
#Kegiatan 3

# Sistem Penilaian Akhir Mahasiswa

# Fungsi untuk menghitung nilai akhir mahasiswa
def menghitung_nilai_akhir(nilai_uts, nilai_uas):
    return (nilai_uts + nilai_uas) / 2

# Fungsi Menghitung Nilai akhir semua mahasiswa
def nilai_akhir(data_mahasiswa) :
    data_nilai_akhir = {}
    for nama, (uts, uas) in data_mahasiswa.items():
        nilai_akhir = menghitung_nilai_akhir(uts, uas)
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir

# Fungsi untuk menampilkan nilai akhir mahasiswa
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("Hasil Nilai Akhir Mahasiswa:")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print(f"Nama: {nama}\tNilai Akhir: {nilai_akhir:.2f}")

def main():
    data_mahasiswa = {
        "brizqu" : (80, 90),
        "danu" : (80, 70),
        "muflih" : (90, 90),
    }

    # Menghitung nilai akhir semua mahasiswa
    data_nilai_akhir = nilai_akhir(data_mahasiswa)

    # Menampilkan nilai akhir mahasiswa
    tampilkan_nilai_akhir(data_nilai_akhir)

if __name__ == "__main__":
    main()
