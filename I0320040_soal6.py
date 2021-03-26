#Soal 6
a = 4
b = 11

print('nilai :', a, ', binary :', format(a, '03b'))
print('nilai :', b, ', binary :', format(b, '04b'))

#4|11
c = a|b
print('\n', 'Keluaran operator bitwise 4|11')
print('nilai :', c, ', binary :', format(c, '08b'))

#4>>11
c = a>>b
print('\n','Keluaran operator bitwise 4>>11')
print('nilai :', c, ', binary :', format(c, '08b'))

#4^11
c = a^b
print('\n','Keluaran operator bitwise 4^11')
print('nilai :', c, ', binary :', format(c, '08b'))

#~4
c = ~a
print('\n','Keluaran operator bitwise 4~11')
print('nilai :', c, ', binary :', format(c, '08b'))

#11&4
c = b&a
print('\n','Keluaran operator bitwise 11&4')
print('nilai :', c, ', binary :', format(c, '08b'))


