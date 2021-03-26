#Soal 4
print('Spesifikasi calon siswa kursus online')

#Input usia
print('Berapa usia kamu?')
usia = int(input('Usia : '))

#Input ujian kualifikasi
print ('Apakah Anda sudah lulus ujian kualifikasi?')
ujian_kualifikasi = input('(Y / T) :')

#Program
if usia >= 21:
    if ujian_kualifikasi == 'Y' :
        print('Anda dapat mendaftar di kursus')
    else:
        print('Anda tidak dapat mendaftar di kursus')
else :
    print('Anda tidak dapat mendaftar di kursus')
