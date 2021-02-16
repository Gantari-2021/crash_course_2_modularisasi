"""
Program Menghitung Luas Segitiga
Luas_segitiga = alas * tinggi / 2
"""
print('Menghitung luas segitiga 1')
alas = 15
tinggi = 20
luas_segitiga = alas * tinggi / 2

print(f'segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga}')

print('\nMenghitung luas segitiga 2 dengan copy paste')
alas = 30
tinggi = 50
luas_segitiga = alas * tinggi / 2

print(f'segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga}')

print('\nMenghitung fungsi hitung_luas_segitiga')
def hitung_luas_segitiga (alas, tinggi) :
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 20
tinggi = 50
print(f'dengan fungsi, segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {hitung_luas_segitiga (alas, tinggi)}')
alas = 10
tinggi = 20
print(f'dengan fungsi, segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {hitung_luas_segitiga (alas, tinggi)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(30, 50)}')


