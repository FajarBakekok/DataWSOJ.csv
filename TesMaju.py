username = 'fajardebian'
password = 'bratbretbrot'
username_login = str(input('Masukkan Username: '))
pw_login = str(input('Masukkan Password: '))
if (username_login == username) and (pw_login == password):
    print('login berhasil')
else:
    print('login gagal')