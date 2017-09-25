tam2 = 5
ancho = 1
tam = 1
ancho2 = 1
for b in range(tam):
    print '%s%s' % (' ' * (tam2 - 3), '*' * ancho2)
    print '%s%s' % (' ' * (tam2 - 4), '*' * ancho2), '%s%s' % (' ' * (tam2 - 5), '*' * ancho2)
    print '%s%s' % (' ' * (tam2 - 5), '*' * ancho2), '%s%s' % (' ' * (tam2 - 6), '*' * ancho2), \
            '%s%s' % (' ' * (tam2 - 7), '*' * ancho2)

for a in range(tam2):
    print '%s%s' % (' '*(tam2 - 3), '*'*ancho)
