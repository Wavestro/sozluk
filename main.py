kelimeler = {
    "piton": "zehirsiz bir yılan türü",
    "laboratuvar": "deney yapılan bir yer",
    "sefa": "keyif"
    "tebeşir"
}

while True:
    kelime = input("Bir Kelime Girin:")
    if kelime in list(kelimeler.keys()):
        print(kelimeler[kelime])
    else:
        anlami = input("Anlamını Girin:")
        kelimeler[kelime] = anlami
        print(kelime, " Sözlüğe Eklendi")


