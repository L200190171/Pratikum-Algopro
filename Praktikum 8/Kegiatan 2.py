def konversisuhu(C = 'n', F = 'n'):
    if C == 'n' and F == 'n':
        print('suhu 0 celcius setara dengan 32 fahrenheit')
    elif F == 'n':
        C1 = C * 9 / 5 + 32
        C2 = int(C1)
        print('suhu', C, 'celcius setara dengan', C1, 'fahrenheit')
    elif C == 'n':
        F1 = (F - 32) * 5 / 9
        F2 = int(F1)
        print('suhu', F, 'fahrenheit setara dengan', F1, 'celcius')
