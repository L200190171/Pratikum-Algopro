Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Sigit Her Bilowo'
>>> NIM = 171
>>> Tinggi = 1.58
>>> Berat = 49
>>> TahunLahir = 2001
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> Data = [TahunLahir, Berat, Tinggi, NIM, Nama]
>>> type(Aku)
<class 'tuple'>
>>> # Data tersebut merupakan tipe tuple yang berisi sejumlah data yang memuat TahunLahir, Berat, Tinggi, NIM, dan Nama dan tipe data tuple tetap atau tidak dapat diubah.
>>> Aku[0]
2001
>>> # Data tersebut menampilkan elemen tuple indeks ke-0 yaitu TahunLahir.
>>> a = NIM % 4; Aku[a]
171
>>> # Data tersebut menampilkan hasil sisa bagi dari variabel NIM dengan 4 adalah 3 dan disimpan dalam variabel a kemudian Aku[a] akan menjadi Aku[3] dimana akan menampilkan elemen tuple Aku indeks ke-3 atau NIM.
>>> type(Aku[a])
<class 'int'>
>>> # Data tersebut merupakan elemen tuple Aku indeks ke 3(3 merupakan data dari variabel a) atau NIM adalah 171 dan merupakan data bertipe integer atau bilangan bulat.
>>> Aku[a:4]
(171,)
>>> # Data tersebut menampilkan elemen dari tuple Aku mulai dari indeks ke-3 hingga sebelum indeks ke-4 yang berisi NIM.
>>> type(Aku[4])
<class 'str'>
>>> # Data tersebut merupakan elemen tuple Aku indeks ke-4 dan merupakan data bertipe string karena berisi Nama.
>>> Aku[0] = 'ok'
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> # Pada data tersebut terjadi tipe eror karena data bertipe tuple tidak dapat diubah sedangkan program ingin mengubah elemen tuple indeks ke-0 dari TanggalLahir menjadi 'ok' sehingga terjadi tipe error.
>>> type(Data)
<class 'list'>
>>> # Menampilkan variabel Data yang bertipe list karena berisi sekumpulan data atau karakter dan data dalam list dapat diubah.
>>> type(Data[4])
<class 'str'>
>>> # Menampilkan elemen list indeks ke-4 atau yang berisi Nama merupakan data yang bertipe string karena mengandung karakter.
>>> Data[4][5]
' '
>>> # Menampilkan elemen list indeks ke-4 atau yang berisi Nama kemudian program akan menjadi Nama[5] atau indeks ke-5 dari data yang telah disimpan dalam variabel Nama yaitu sepasi.
>>> Data[4][a:6]
'it '
>>> # Menampilkan elemen list Data indeks ke-4 yang berisi Nama kemudian program akan menjadi Nama[a:6] dimana a berisi data 3 sehingga akan menjadi Nama[3:6] yang akan meampilkan elemen list indeks ke-3 hingga sebelum indeks ke-6 yaitu 'it '.
>>> Data[0] = 'ok'; Data
['ok', 49, 1.58, 171, 'Sigit Her Bilowo']
>>> # Menampilkan elemen list Data indeks ke-0 diubah dari TanggalLahir menjadi 'ok' dan kemudian program menampilkan data yang ada di list Data.
>>> Data[-a]
1.58
>>> # Menampilkan variabel a berisi data 3 maka program menjadi Data[-3] yang akan menampilkan elemen list Data indeks ke 3 dari sebelah kanan.
>>> range(a)
range(0, 3)
>>> # Menampilkan varibel a berisi data 3 sehingga program akan menjadi range(3) dan program akan menampilkan range dari 0 hingga 3.
