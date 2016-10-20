#task1------------------------------------------------------------
"""
Дано два цілих числа. Вивести найменше з них.
"""
a = int(input('Number one'))
b = int(input('Number two'))
if a<b:
    print(a)
else:
    print(b)
#-----------------------------------------------------------------

#task2------------------------------------------------------------
"""
Вивести результат функції sign(x), що визначається наступним чином: 
"""
x = float(input())
if x>0:
    print(1) 
elif x<0:
    print(-1)
else:
    print(0)
#-----------------------------------------------------------------

#task3------------------------------------------------------------
"""
Дано три цілих числа. Вивести найменше з них.
"""
a = int(input())  #Enter first number
b = int(input())  #Enter second number
c = int(input())  #Enter third number
if a<b:
    if a<c:
      print(a)
if b<a:
    if b<c:
        print(b)
if c<a:
    if c<b:
        print(c)
#-----------------------------------------------------------------

#task4------------------------------------------------------------
"""
Дано ціле число, що визначає рік. Визначити, чи є вказаний рік 
високосним. Якщо так, то вивести користувачу "LEAP", в іншому 
випадку – "СOMMON".
"""
year = int(input('Enter year:'))
if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
	print('LEAP')
else:
	print('COMMON')
#-----------------------------------------------------------------

#task5------------------------------------------------------------
"""
Дано три цілих числа. Визначте, скільки з них дорівнюють один 
одному. Програма повинна виводити одне з чисел: 3 (якщо всі числа 
однакові), 2 (якщо два з них дорівнюють один одному, а третє 
відрізняється) або 0 (якщо всі числа різні).
"""
a=int(input())
b=int(input())
c=int(input())
if a == b:
   if a==c:
      if c == b:
          print(3)
if a != b:
    if a == c:
        if b != c:
            print(2)
if a != b:
    if a !=c:
        if b != c:
            print(0)
#-----------------------------------------------------------------

#task6------------------------------------------------------------
"""
Шахова тура переміщається по горизонталі або по вертикалі. Дано 
координати двох клітин шахової дошки. Визначити, чи може тура 
перейти з першої клітини у другу за один хід. Користувач вводить 
чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку 
та стовпчика клітини. Перші два числа - для першої клітини, 
останні два числа – для другої. Програма має вивести "YES", якщо 
тура може виконати переміщення, або "NO" в іншому випадку.
"""
x1 = int(input())    #Enter integer number of column where rook is located
x2 = int(input())    #Enter integer number of row where rook is located
y1 = int(input())    #Enter integer number of column where rook must be moved
y2 = int(input())    #Enter integer number of row where rook must be moved
if x1==y1 or x2==y2:
    print('YES')
else:
    print('NO')
#-----------------------------------------------------------------

#task7------------------------------------------------------------
"""
Дано координати двох клітин шахової дошки. Визначити, чи однакового
вони кольору. Користувач вводить чотири цілих числа від 1 до 8, 
кожне з яких визначає номер рядку та стовпчика клітини. Перші два 
числа - для першої клітини, останні два числа – для другої. Програма
має вивести "YES", якщо колір однаковий, або "NO" в іншому випадку.
"""
if ((cell_ax + cell_ay) % 2) == ((cell_bx + cell_by) % 2):
	print('YES')
else:
	print('NO')
#-----------------------------------------------------------------

#task8------------------------------------------------------------
"""
Шаховий король переміщується по горизонталі, по вертикалі або по 
діагоналі на будь-яку сусідню клітинку. Дано координати двох клітин 
шахової дошки. Визначити, чи може король перейти з першої клітини 
у другу за один хід. Користувач вводить чотири цілих числа від 1 
до 8, кожне з яких визначає номер рядку та стовпчика клітини. Перші
два числа - для першої клітини, останні два числа – для другої. 
Програма має вивести "YES", якщо хід можливий, або "NO" в іншому 
випадку.
"""
x1 = int(input())   #Enter integer number of column where king is located
x2 = int(input())   #Enter integer number of row where king is located
y1 = int(input())   #Enter integer number of column where king must be moved
y2 = int(input())   #Enter integer number of row where king must be moved
if -1<=(x1- y1)<=1 and -1<=(x2- y2)<=1:
   print('YES')
else:
   print('NO')
#-----------------------------------------------------------------

#task9------------------------------------------------------------
"""
Шаховий слон рухається по діагоналі на будь-яку кількість клітин. 
Дано координати двох клітин шахової дошки. Визначити, чи може слон 
перейти з першої клітини у другу за один хід. Користувач вводить 
чотири цілих числа від 1 до 8, кожне з яких визначає номер рядку 
та стовпчика клітини. Перші два числа - для першої клітини, 
останні два числа – для другої. Програма має вивести "YES", 
якщо хід можливий, або "NO" в іншому випадку.
"""
x1 = int(input())   #Enter integer number of column where bishop is located
x2 = int(input())   #Enter integer number of row where bishop is located
y1 = int(input())   #Enter integer number of column where bishop must be moved
y2 = int(input())   #Enter integer number of row where bishop must be moved
if (x1/y1)==(x2/y2):
    print('YES')
elif (x1+x2)==(y1+y2):
    print('YES')
else:
    print('NO')
#-----------------------------------------------------------------

#task10------------------------------------------------------------
"""
Шахова королева рухається по горизонталі, по вертикалі або по 
діагоналі на будь-яку кількість клітин. Дано координати двох 
клітин шахової дошки. Визначити, чи може королева перейти з 
першої клітини у другу за один хід. Користувач вводить чотири 
цілих числа від 1 до 8, кожне з яких визначає номер рядку та 
стовпчика клітини. Перші два числа - для першої клітини, останні 
два числа – для другої. Програма має вивести "YES", якщо хід 
можливий, або "NO" в іншому випадку.
"""
x1 = int(input())   #Enter integer number of column where queen is located
x2 = int(input())   #Enter integer number of row where queen is located
y1 = int(input())   #Enter integer number of column where queen must be moved
y2 = int(input())   #Enter integer number of row where queen must be moved
if x1==y1 or x2==y2:
       print('YES')
elif (x1/y1)==(x2/y2):
    print('YES')
elif (x1+x2)==(y1+y2) or (x1-x2)==(y1- y2):
    print('YES')
else:
    print('NO')

#-----------------------------------------------------------------

#task11------------------------------------------------------------
"""
Шаховий кінь рухається як літера L. Він може переміщатись на дві 
клітинки по горизонталі і одну клітинку по вертикалі або на дві 
клітинки по вертикалі і одну по горизонталі. Дано координати двох 
клітин шахової дошки. Визначити, чи може кінь перейти з першої 
клітини у другу за один хід. Користувач вводить чотири цілих 
числа від 1 до 8, кожне з яких визначає номер рядку та стовпчика
клітини. Перші два числа - для першої клітини, останні два числа 
– для другої. Програма має вивести "YES", якщо хід можливий, 
або "NO" в іншому випадку.
"""
x1 = int(input())   #Enter integer number of column where knight is located
x2 = int(input())   #Enter integer number of row where knight is located
y1 = int(input())   #Enter integer number of column where knight must be moved
y2 = int(input())   #Enter integer number of row where knight must be moved
if abs(x1-y1)==2 and abs(x2-y2)==1:
    print('YES')
elif abs(x1-y1)==1 and abs(x2-y2)==2:
    print('YES')
else:
    print('NO')
#-----------------------------------------------------------------

#task12------------------------------------------------------------
"""
Шоколад має форму прямокутника, розділеного на n×m клітин. Шоколад
може бути розділений на дві частини тільки по горизонталі або по 
вертикалі, при цьому клітини мають бути цілими. Визначити, чи можна
розділити шоколад за один крок таким чином, щоб одна з частин 
матиме точно k клітин. Програма має вивести "YES", якщо шоколад 
можна поділити, або "NO" в іншому випадку.
"""
n = int(input())    #length of the bar
m = int(input())    #width of the bar
k = int(input())    #quantity of bars 
if n*m-k==a or n*m-k==b and n*m>k and k!=1:
    print('YES')
elif (n*m-k)%2==0 and n*m>k and k!=1:
    print('YES')
else:
    print('NO')
#-----------------------------------------------------------------