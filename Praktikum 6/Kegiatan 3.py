Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Nama = 'Sigit Her Bilowo'
>>> NIM = 'L200190171'
>>> X = '1' + NIM[7:]
>>> a = int(X)
>>> b = len(Nama)
>>> type(a)
<class 'int'>
>>> # Varibel a adalah data yang berbentuk integer karena variabel a telah diubah dari data tipe string menjadi data tipe integer.
>>> type(b)
<class 'int'>
>>> # Variabel b adalah data yang bertipe integer karena data dari variabel b mengandung intruksi intruksi len yang berarti jumlah anggota dari suatu objek.
>>> a / b
73.1875
>>> # Data tersebut bertipe float karena variabel bernilai 1171 dibagi dengan variabel b yang bernilai 16 dan menghasilkan nilai 73.1875 yang merupakan bilangan float.
>>> a // b
73
>>> # Data tersebut bertipe integer karena variabel bernilai 1171 dibagi dengan variabel b yang bernilai 16 dan menghasilkan nilai 73.1875 dan dibulatkan menjadi 73 yang merupakan data yang bertipe integer.
>>> 10 * (a - 999)
1720
>>> # Data tersebut bertipe integer karena data dari variabel a yang bernilai 1171 dikurang dengan nilai 999 menghasilkan nilai 172 dan kemudian dikalikan dengan nilai 10 menghasilkan data 1720.
>>> b ** 2
256
>>> # Data tersebut bertipe integer karena data dari variabel b dipangkatkan 2 yang menghasilkan data 256.
>>> a % b
3
>>> # Data tersebut bertipe integer karena simbol % merupakan sisa hasil bagi dari data variabel a dibagi data variabel b yaitu 3.
>>> c = 12.5
>>> # data 12.5 disimpan dalam variabel c
>>> type(c)
<class 'float'>
>>> # variabel c merupakan data float karena mengandung nilai desimal.
>>> a / c
93.68
>>> # Data tersebut bertipe float karena data variabel a dibagi dengan data variabel c sama dengan 93.68 atau 1171 dibagi 12.5 menghasilkan data 93.68 yang bertipe float atau bernilai desimal.
>>> a // c
93.0
>>> # Data tersebut bertipe float karena dalam variabel c mengandung data bertipe float maka hasil pembagian dibulatkan kebawah dari variabel data bertipe integer dibagi variabel data bertipe float adalah data bertipe float (1171 dibagi 12.5 dan dibulatkan ke bawah menghasilkan data 93.0).
>>> a % c
8.5
>>> # Data tersebut bertipe float karena sisa hasil bagi(%) antara data variabel a(1171) dengan data variabel c(12.5) menghasilkan 8.5 yang mengandung nilai desimal.
>>> c > b
False
>>> # Merupakan data yang bertipe boolean yang bernilai atau berkondisi False karena data variabel c (12.5) lebih kecil dari data variabel b (16) sedangkan dalam program ditulis data variabel c lebih besar dari pada data variabel b maka menghasilkan kondisi atau nilai False.
>>> type(c > b)
<class 'bool'>
>>> # Merupakan data yang bertipe boolean yang memiliki 2 kondisi atau nilai yaitu True dan False , merupakan operator logika.
>>> a > b and b > c
True
>>> # Data tersebut bertipe boolean yang berkondisi atau bernilai True karena a > b bernilai True dan b > c bernilai True juga , dalam operator 'and' apabila kedua data memiliki nilai True maka menghasilkan data bernilai True.
>>> a > 1100 or b < 10
True
>>> # Merupakan data yang bertipe boolean yang berkondisi atau bernilai True karena a > 1100 bernilai True dan b < 10 bernilai False , dalam operator 'or' apabila salah satu memiliki nilai True maka menghasilkan data bernilai True juga.
