def greet(name):
    print(f"Hello {name}, Ini aplikasi cli untuk hitung gaji karyawan")


def hitung_gaji(pokok, tunjangan):
    gaji_bersih = pokok + tunjangan
    print(f"Gaji Bersih Anda adalah: {gaji_bersih}")


def kategori_karyawan():
    try:
        print("Kategori Karyawan:")
        kasir, tunjangan = 5000000, 3000000
        pelayan, tunjangan = 3500000, 1500000
        spv, tunjangan = 6000000, 1000000
        input_kategori = input("Masukkan kategori karyawan (A/B/C): ").upper()

        if input_kategori == "A":
            print(f"Kategori A - Kasir: Gaji Pokok = {kasir}, tunajangan = {tunjangan}")
            hitung_gaji(kasir, tunjangan)
        elif input_kategori == "B":
            print(
                f"Kategori B - Pelayan: Gaji Pokok = {pelayan}, tunajangan = {tunjangan}"
            )
            hitung_gaji(pelayan, tunjangan)
        elif input_kategori == "C":
            print(
                f"Kategori C - Supervisor: Gaji Pokok = {spv}, tunajangan = {tunjangan}"
            )
            hitung_gaji(spv, tunjangan)
        else:
            print("Kategori tidak valid. Silakan masukkan A, B, atau C.")
            return kategori_karyawan()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return kategori_karyawan()


def welcome():
    print("Selamat datang di aplikasi hitung gaji karyawan!")
    name = input("Masukkan nama Anda: ")
    greet(name)
    kategori_karyawan()


if __name__ == "__main__":
    welcome()
