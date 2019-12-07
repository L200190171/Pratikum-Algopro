import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50004))
s.listen(5)
print "Server Siap"
perintah = ""
si=0

while perintah != "keluar":
    komm, addr = s.accept()
    while perintah != "keluar":
        item = komm.recv(1024).lower().split("=")
        perintah = item [0]
        if perintah == "keluar":
            komm.send("done")
            s.close()
            break
        print "pesan: ", perintah
        if len(item)==2:
            if perintah == "alas":
                a=int(item[1])
                komm.send("alas disimpan")
            elif perintah == "tinggi":
                t=int(item[1])
                komm.send("tinggi disimpan")
            else:
                komm.send("Pesan tidak diketahui")
        elif perintah == "hitung":
            L=float(a*t*0.5)
            response = "Luas segitiga dengan alas {} dan tinggi {} adalah {}".format(a,t,L)
            komm.send(response)
        else:
            komm.send("Pesan tidak diketahui")
