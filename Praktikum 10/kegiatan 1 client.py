import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50008))
print "program komunikasi tentang data diri"

while pesan.lower()!= "q":
    pesan = raw_input("perintah: ")
    s.send(pesan)
    if pesan.lower() == "keluar":
        response = s.recv(1024)
        print "Jawab: ", response
        s.close()
        break
    elif pesan.lower() != "q":
        response = s.recv(1024)
        print "Jawab: ", response
s.close()
