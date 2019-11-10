## Program Akun
## Dibuat oleh Sigit L200190171
import random
angka = random.randint(0,1000)

Nama = 'Sigit Her Bilowo'
TanggalLahir = '9 April 2001'
NamaSingkat = Nama[0] + '.' + Nama[6] + '.' + Nama[10:16]
Username = Nama[0] + TanggalLahir[0:1] + TanggalLahir[8:12]
Password = Nama[0:3] + str(angka)
