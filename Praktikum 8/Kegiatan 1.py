Data = {"NIM":"L200190171", "Nama":"Sigit Her Bilowo", "Tanggal Lahir":"9 Aril 2001", "Alamat":"Jln. Abimanyu Desa Sidorejo Kec. Rimbo Ilir Kab. Tebo Prov. Jambi", "Agama":"Islam", "Pekerjaan":"Pelajar/Mahasiswa", "Golongan Darah":"A"}
def TampilNIM():
    print(Data["NIM"])
def TampilNama():
    print(Data["Nama"])
def TampilTL():
    print(Data["Tanggal Lahir"])
def TampilAlamat():
    print(Data["Alamat"])
def TampilAgama():
    print(Data["Agama"])
def TampilPekerjaan():
    print(Data["Pekerjaan"])
def TampilGD():
    print(Data["Golongan Darah"])

print("Pilihan Yang Tersedia:")
print("a menampilkan bantuan ini")
print("b menampilkan NIM")
print("c menampilkan Nama")
print("d menampilkan Tanggal Lahir")
print("e menampilkan Alamat")
print("f menampilkan Agama")
print("g menampilkan Pekerjaan")
print("h menampilkan Golongan Darah")
print("i untuk keluar")
print(" ")

j ="""Pilihan Yang Tersedia:
a menampilkan bantuan ini
b menampilkan NIM
c menampilkan Nama
d menampilkan Tanggal Lahir
e menampilkan Alamat
f menampilkan Agama
g menampilkan Pekerjaan
h menampilkan Golongan Darah
i untuk keluar"""


i = "Terimakasih"
l = input("Masukkan huruf: ")
while l != "i":
    if l == "a":
        print(j)
        print(" ")
        l = input("Masukkan Huruf: ")
    elif l == "b":
        TampilNIM()
        print(" ")
        l = input("Masukkan Huruf: ")
    elif l == "c":
        TampilNama()
        print(" ")
        l = input("Masukkan Huruf: ")
    elif l == "d":
        TampilTL()
        print(" ")
        l = input("Masukkan Huruf: ")
    elif l == "e":
        TampilAlamat()
        print(" ")
        l = input("Masukkan Huruf: ")
    elif l == "f":
        TampilAgama()
        print(" ")
        l = input("Masukkan Huruf: ")
    elif l == "g":
        TampilPekerjaan()
        print(" ")
        l = input("Masukkan Huruf: ")
    elif l == "h":
        TampilGD()
        print(" ")
        l = input("Masukkan Huruf: ")
print(i)
