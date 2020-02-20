
import math
import sys
import random
import turtle


# funkcja struktura_obszaru_roboczego sluzy tylo do zubdowania struktury (potem kopia do obszaru roboczego)
# wejscie - wstepna ilosc list i zadan w kazej z list.
# wyjscie - slownik "listy_liczba_zadan" + struktura
# slownik bedzie aktualizowany podczas wykonywania zadan (bo nie w kazdej liscie jest tyle samo zadan)
# po przejsciu calego zakresu i aktualizacji slownika otrzymamy prawidlowa ilosc zadan


def struktura_obszaru_roboczego():
    # zeby nie klepac slownika recznie, to zbudujmy go na podstawie zdanej ilosci list i wstepnej liczby zadan w kazdej liscie
    slownik_listy_liczba_zadan = {}

    liczba_list = 13
    zadania = 10  # ilosc zadan w kazdej lisicie

    i=1
    while i < liczba_list:
        tytul_listy= 'lista' + str(i)
        slownik_listy_liczba_zadan[tytul_listy] = zadania
        #print('def {}():'.format(tytul_listy))
        for nr_zadania in list(range(1, zadania)):
            print('\ndef {}_zadanie{}():'.format(tytul_listy, nr_zadania))
            print("\t'''\n")
            print("\t'''")
            print('\n{}_zadanie{}()'.format(tytul_listy, nr_zadania))
            print('#zadanie ukonczone? wpisz 1 jesli tak')
            print('ukonczenie_zadania += 0')
            print('#szacunkowy poziom znajomosci zagadnienia od 1 do 10')
            print('szac_poziom_znajomosci_zadania += 0')
        i += 1
    print(slownik_listy_liczba_zadan)
#struktura_obszaru_roboczego()






slownik_listy_liczba_zadan = {'lista1': 5, 'lista2': 8, 'lista3': 5, 'lista4': 6, 'lista5': 6, 'lista6': 3, 'lista7': 5, 'lista8': 5, 'lista9': 2, 'lista10': 5, 'lista11': 4, 'lista12': 10}
# wyjsciowy poziom znajomosci zagadnien i ilosci wykonanych zadan
szac_poziom_znajomosci_zadania = 0
ukonczenie_zadania = 0

# wykonywanie zadan

def lista1_zadanie1():
    '''

    :return:
    '''
#lista1_zadanie1()


# zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
# szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 10


def lista1_zadanie2():
    '''

    :return:
    '''

#lista1_zadanie2()


# zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
# szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 10


def lista1_zadanie3():
    '''

    :return:
    '''
    #

#lista1_zadanie3()


# zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
# szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 10


def lista1_zadanie4():
    '''

    :return:
    '''
    #
#lista1_zadanie4()


# zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
# szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 10


def lista1_zadanie5():
    '''

    :return:
    '''
    #
#lista1_zadanie5()


# zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
# szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 10


def lista2_zadanie1():
    '''


    Stwórz krotkę (tuple) zawierającą pięć cyfr: 0, 1, 2, 3, 4 oraz pięć literałów słownych: "piec", "szesc", "siedem", "osiem", "dziewiec".

    Wydrukuj na ekranie trzy pierwsze elementy.

    Wydrukuj na ekranie 2 ostatnie elementy.

    Wydrukuj co drugi element (zaczynając od drugiego).

    Korzystając z funkcji len sprawdź ilość elementów w krotce oraz długość przedostatniego elementu.

    Niech x oznacza nazwę krotki. Wykonaj:
        x[:5] + (5, 6) + x[-3:]
        x[:5], (5, 6), x[-3:]
        porównaj otrzymane wyniki

    Dodaj pusty literał słowny na koniec krotki. Czy możesz skorzystać z funkcji append?

    '''

    krotka = (0, 1, 2, 3, 4, 5, 'piec', 'szesc', 'siedem', 'osiem', 'dziewiec')
    print(krotka[:3])
    print(krotka[-2:])
    print(krotka[1::2])
    print(len(krotka))
    x = krotka
    e= x[:5] + (5, 6) + x[-3:] # jedna krotka
    g =x[:5], (5, 6), x[-3:] # krotka  w krotce
    print(e)
    print(g)
    x.append('literal') # krotka jest nie mutowalna
    print(x)
#lista2_zadanie1()


# zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
# szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 7


def lista2_zadanie2():
    '''


    Stwórz listę studentów: Kasia, Basia, Marek, Darek.

    Korzystając z funkcji append dodaj do listy Józka.

    Korzystając z funkcji extend dodaj do listy Anię i Basię.

    Posortuj alfabetycznie studentów.

    Wypisz na ekranie:
        czwartego studenta na liście
        dwóch pierwszych studentów na liście
        dwóch ostatnich studentów na liście

    Korzystając z funkcji remove usuń wszystkie Basie.

    Korzystając z funkcji len sprawdź ilość studentów.

    Z ostatecznej listy studentów utwórz krotkę.

    '''

    studenci = ['Kasia', 'Basia', 'Marek', 'Darek']
    studenci.append('Jozek') # append i okragle nawiasy
    studenci.extend(['Ania', 'Basia'])
    print(studenci)
    studenci.sort()
    print(studenci)
    print(studenci[3])
    print(studenci[:2]) # wpisuje 2 bo chce printowac zerowego i pierwszego (czyli pierwsze dwa)
    print(studenci[-2:])
    studenci.remove('Basia')
    studenci.remove('Basia')
    print(studenci)
    print(len(studenci))
    krotka = tuple(studenci)
    print(krotka)


#lista2_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 7

def lista2_zadanie3():
    '''


Zad 3.

    Korzystając z range utwórz listę zawierającą wszystkie wielokrotności liczby 3 mniejsze od 100.

    Korzystając z del usuń co trzeci element (zaczynając od piątego).

    Sprawdź definicję funkcji wbudowanej sum (help(sum)). Wykorzystaj ją oraz funkcję len, aby wyliczyć średnią arytmetyczną otrzymanej listy.

    '''

    lista = list(range(0,100,3))
    print(lista)
    del lista[5::3]
    print(lista)
    srednia_arytmetyczna = sum(lista)/len(lista)
    print(srednia_arytmetyczna)


#lista2_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 5

def lista2_zadanie4():
    '''
Zad 4.

    Stwórz krotkę: ('a', 'b', 'c', 'd').

    Zapoznaj się z dokumentacją funkcji str.join.

    Wykonaj następujące polecenia (gdzie x to zmienna wskazująca na krotkę):

"".join(x)
" ".join(x)
", ".join(x)

    Wydrukuj na ekranie 100 zer oddzielonych tabulacjami (spróbuj wykonać to komendą jednolinijkową).

    '''
    x = ('a', 'b', 'c', 'd')
    print(x)
    e = "".join(x)
    print(e)
    e = " ".join(x)
    print(e)
    e = ", ".join(x)
    print(e)

    print(100*"\t0")
#lista2_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 6

def lista2_zadanie5():
    '''
Zad 5.

    Stwórz obiekt typu str, który przechowuje tekst ślubowania studenta:

slubowanie = """
wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
- zdobywać wiedzę i umiejętności,
- postępować zgodnie z prawem, tradycją i dobrymi obyczajami akademickimi,
- dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.
"""

    W interpreterze sprawdź wynik:

>>> print(slubowanie)
>>> slubowanie
>>> slubowanie[0]

    Popraw zmienną slubowanie, aby tekst zaczynał się wielką literą.

    Korzystając z funkcji count sprawdź, ile razy występuje spójnik "i".

    Korzystając z funkcji count sprawdź, ile razy występuje litera "i".

    Korzystając z in sprawdź, czy słowo "Uniwersytet" występuje w tekście.

    Korzystając z funkcji str.split:
        stwórz listę wyrazów występujących w tekście (30 słów => 30 elementów)
        stwórz listę, której każdy element odpowiada jednej linijce tekstu

    '''
    slubowanie = """
    wstępując do wspólnoty akademickiej Uniwersytetu Wrocławskiego, ślubuję uroczyście:
    - zdobywać wiedzę i umiejętności,
    - postępować zgodnie z prawem, tradycją i dobrymi obyczajami akademickimi,
    - dbać o dobre imię Uniwersytetu Wrocławskiego i godność studenta.
    """
    slubowanie_capitalW = slubowanie.replace(slubowanie[5], 'W')
    print(slubowanie_capitalW)
    i = slubowanie.count(' i ')
    #print(i)
    i = slubowanie.count('i')
    #print(i)
    #if "Uniwersytet" in slubowanie:
        #print('tak, wystepuje')


    lista = slubowanie.split()
    print(lista)
    #print(*lista, sep = ', ') # drukuje tylko elementy listy i zadany separator
    #print(len(lista))
    #print(*lista, sep ='\n')




#lista2_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 6

def lista2_zadanie6():
    '''
Zad 6.

    Korzystając z funkcji sys.getsizeof sprawdź, ile pamięci zajmuje:
        0
        2**100
        2**1000

    Sprawdź, ile pamięci zajmują: True i False. Czy jest to wynik, którego się spodziewałeś?

    Zapoznaj się z dokumentacją funkcji isinstance.

    Wykonaj następujące polecenia:

isinstance(0, int)
isinstance(0, float)
isinstance(0.0, float)
isinstance(True, bool)
isinstance(True, int)

    Wyjaśnij rozmiar True i False.

    '''
    a = 0
    b = 2**100
    c = 2**1000
    print(sys.getsizeof(a), sys.getsizeof(b), sys.getsizeof(c))

    print(sys.getsizeof(True), sys.getsizeof(False))
    print(isinstance(0, int))
    print(isinstance(0, float))
    print(isinstance(0.0, float))


#lista2_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 3



def lista2_zadanie7():
        '''
        Zad 7.

    Zapoznaj się z dokumentacją funkcji id.

    Wykonaj następujące polecenia:

x = 2
y = x
print(x, y, id(x), id(y))
y = 3
print(x, y, id(x), id(y))

    Wykonaj następujące polecenia:

x = [1,2]
y = x
print(x, y, id(x), id(y))
y[1] = 3
print(x, y, id(x), id(y))

    Wyjaśnij, dlaczego modyfikacja listy y zmienia wartość listy x, ale nie dzieje się tak w przypadku int.


        '''

        x = 2
        y = x
        print(x, y, id(x), id(y))
        y = 3
        print(x, y, id(x), id(y))

        x = [1,2]
        y = x
        print(x, y, id(x), id(y))
        y[1] = 3
        print(x, y, id(x), id(y))

#lista2_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 7

def lista2_zadanie8():


    '''
    zad 8.

        Niech x = (a, b, c) = (1, 2, 3). Sprawdź wartości zmiennych x, a, b i c.

        Niech x = a, b, c = 1, 2, 3. Sprawdź wartości zmiennych x, a, b i c.

        Niech a = 1 oraz b = "jeden". Podmień wartości zmiennych a i b.

    '''
    x = (a, b, c) = (1, 2, 3)
    print(x,a,b,c)
    x = a, b, c = 1, 2, 3
    print(x,a,b,c)
    a, b = 1, 'jeden'
    a, b = b, a
    print(x, a, b, c)


#lista2_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 7


def lista3_zadanie1():
    '''
    Zad 1

    Wykorzystaj listę składaną (list comprehension), aby stworzyć sekwencję kwadratów liczb naturalnych mniejszych od 100. Następnie (korzystając z enumerate) wydrukuj na ekranie:

    1 -> 1
    2 -> 4
    3 -> 9
    .
    .
    '''
    lista = [(i**2) for i in range(1,100)]

    print(lista)
    for pozycja, element in enumerate(lista):
        print(pozycja, '->', element)



#lista3_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 4

def lista3_zadanie2():

    '''


    Zad 2.

    Przeanalizuj poniższy kod:

    #!/usr/bin/env python

    i = 0

    # drukujemy wszystkie liczby parzyste mniejsze od 10
    while i < 10:
    if i % 2:    # reszta z dzielenia != 0 -> True
        continue # pomiń liczby nieparzyste
    else:
        print(i) # drukuj liczby parzyste

    i += 1 # zwiększ i o jeden

    Czy skrypt będzie działał zgodnie z założeniami? Jeśli nie, to napraw go.


    '''
    #!/usr/bin/env python #question - znalazlem taki opis ale daje nie jest to dla mnie jasne
    '''
    You are specifying the location to the python executable in your machine, that rest of the script needs to be interpreted with.
    You are pointing to python is located at /usr/local/bin/python
    
    Consider the possiblities that in a different machine, python may be installed at /usr/bin/python or /bin/python in those cases, the above #! will fail.
    For those cases, we get to call the env executable with argument which will determine the arguments path by searching in the $PATH and use it correctly.
    
    Thus,
    #/usr/bin/env python
    Will figure out the correct location of python ( /usr/bin/python or /bin/python from $PATH) and make that as the interpreter for rest of the script.
    - ( env is almost always located in /usr/bin/ so one need not worry what is env is not present at /usr/bin)'''

    i = 0
    while i < 10:
        if i % 2 == 0:
            print(i)
        i += 1  # zwiększ i o jeden


#lista3_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 8

def lista3_zadanie3():
    '''
    Uzupełnij skrypt o brakujące fragmenty:

    #!/usr/bin/env python

    # lista zakupów
    grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']
    # ilość sztuk
    n_items = {}
    # zakazane produkty
    prohibited = ['wódka', 'piwo', 'wino']

    # w pętli pytamy użytkownika, ile sztuk danego produktu chce kupić
    for product in grocery:
    # wydrukuj na ekranie komunikat: "Produkt [nazwa produktu]: sztuk = "
    # pobierz liczbę od użytkownika i zapisz w n_items dla danego produktu
    # pomiń produkty zakazane (i automatycznie przyjmij ilość = 0)

    # w pętli wydrukuj: [lp]. [nazwa produktu]: [ilość]
    # czyli np.: 1. jajka: 5 itd.

    '''
    grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']
    n_items = {}
    prohibited = ['wodka', 'piwo', 'wino']

    print('ile potrzeba kolejnych produktow')
    for produkt in grocery:
        ilosc = 0
        if produkt not in prohibited:
            ilosc = input('{}: sztuk:'.format(produkt))
        n_items.update({produkt: ilosc})# nie umialem tego zapisu dalem znak rowna sie po update...
    for i, (produkt, ilosc) in enumerate(n_items.items()): # tego zapisu w dalszym ciagu nie znam
        print('{}. {}: {}'.format(i+1, produkt, ilosc))

#lista3_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 3

def lista3_zadanie4():
    '''
    Zad 4.

    Napisz skrypt, który:

    losuje liczbę całkowitą mniejszą od 100 (help(random.randint))
    pyta użytkownika o odgadnięcie liczby
    informuje użytkownika, czy podana przez niego liczba jest:
        dużo mniejsza (różnica > 50)
        mniejsza (różnica > 10)
        trochę mniejsza
        trochę większa
        większa (różnica > 10)
        dużo większa (różnica > 50)
    program się kończy, gdy użytkownik odgadnie wylosowaną liczbę

    '''

    x = random.randint(0, 100)
    print(x)
    # iterowanie w celu sprawdzenia zgadywanej liczby
    iteracja = True
    while iteracja == True:
        y = int(input('zgadnij liczbe w zakresie 0-100:\n'))
        roznica = abs(y - x)
        if y == x:
            print('Odgadles liczbe')
            iteracja = False
        elif y > x:
            if roznica in range(50, 100):
                print('Twoja liczba jest duzo wieksza niz zgadywana liczba')
            elif roznica in range(10, 50):
                print('Twoja liczba jest wieksza niz zgadywana liczba')
            else:
                print('Twoja liczba jest troche wieksza niz zgadywana liczba')
        elif y < x:
            if roznica in range(50, 100):
                print('Twoja liczba jest duzo mniejsza niz zgadywana liczba')
            elif roznica in range(10, 50):
                print('Twoja liczba jest mniejsza niz zgadywana liczba')
            else:
                print('Twoja liczba jest troche mniejsza niz zgadywana liczba')





#lista3_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 4

def lista3_zadanie5():
    '''
    Zad 5.

    Poniższy skrypt narysuje kwadrat:

    #!/usr/bin/env python

    import turtle

    length = eval(input("Podaj dł\lugosc boku: "))
    n_sides = 4 # ilosc boków

    turtle.speed(20) # ustal predkosc zolwia

    # powtorz n_sides razy
    for i in range(n_sides):
        turtle.forward(length) # narysuj linie o danej dlugosci
        turtle.right(90)       # obroc sie w prawo o dany kat

    turtle.mainloop() # nie zamykaj okna po narysowaniu

    5.1 zmodyfikuj go tak, aby narysował trójkąt równoboczny
    5.2 zmodyfikuj go tak, aby narysował sześciokąt foremny
    5.3 zmodyfikuj go tak, aby narysował wielokąt foremny, którego liczba boków podana jest przez użytkownika
                '''
    # 5.1
    ''' 
     length = eval(input('podaj dlugosc boku:'))  # nie znalem metody eval

    n_sides = 3
    turtle.speed(2)

    for i in range(n_sides):
        turtle.forward(length)
        turtle.right(120)
    turtle.mainloop()
    
    

    '''

    '''
    5.2
    length = eval(input('podaj dlugosc boku:'))  # nie znalem metody eval
    n_sides = 6
    turtle.speed(2)

    for i in range(n_sides):
        turtle.forward(length)
        turtle.right(60)
    turtle.mainloop()
    '''

    #5.3
    liczba_bokow = eval(input('podaj ilosc bokow: '))
    length = eval(input('podaj dlugosc boku:'))  # nie znalem metody eval

    turtle.speed(2)
    kat = 360/liczba_bokow

    for i in range(liczba_bokow):
        turtle.forward(length)
        turtle.right(kat)
    turtle.mainloop()


#lista3_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10 # zrozumiane dobrze ale nie mam w pamieci tych funkcji
szac_poziom_znajomosci_zadania += 7

def lista4_zadanie1():
    '''
    Zad 1.

    Stwórz słownik, który przyporządkuje pięciu różnym produktom ich cenę. Następnie:

    w pętli wydrukuj na ekranie listę produktów z ceną
    policz średnią cenę produktu
    dodaj nowy produkt
    jak się zmieniła średnia cena?
    napisz funkcję, która liczy średnią cenę
    usuń produkt
    policz średnią cenę
        '''


    cena_produktow = {'maslo':10, 'cukier':5, 'sol':3}
    # cena_produktow.items() - lista utworzona z par klucz i wartosc
    # enumerate - drukuje index i kolejny element listy

    for i, (produkt, cena) in enumerate(cena_produktow.items()):
        print('{} produkt: {} -> cena: {} '.format(i, produkt, cena)) # zrozumialem zapis, nie bardzo plynne uzycie

    ilosc_produktow = len(cena_produktow)
    suma_cen = sum(cena_produktow.values())
    srednia_cena = suma_cen/ilosc_produktow
    print('srednia cena: {}'.format(srednia_cena))

    cena_produktow['orzechy'] = 70
    cena_produktow.update(banany=11)

    ilosc_produktow = len(cena_produktow)
    suma_cen = sum(cena_produktow.values())
    srednia_cena = suma_cen / ilosc_produktow
    print('srednia cena: {}'.format(srednia_cena))


    def sr_cena():
        x = suma_cen / ilosc_produktow
        print(x)
    sr_cena()

    del cena_produktow['banany']
    print(cena_produktow)



    '''
    srednia_cena = (sum(cena_produktow.values))/(len(cena_produktow))
    print('srednia cena: {}'.format(srednia_cena))
    '''


    #pytania_weryfikujace
    # jak zbudowany jest slownik
    # sposoby budowania slownika (rowniez przez konstruktor - 4 sposoby
    # dostep do wartosc - 2 sposoby
    # modyfikowanie kluczy
    # dostep do kluczy, do wartosci, do pary klucze wartosci
    # usuwanie kluczy - 2 sposoby
    # dodawnia kluczy  - 3 sposoby
    # petla po slowniku (po kluczach , po wartosciach, z enumerate)


#lista4_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 6

def lista4_zadanie2():
    '''
    Zad 2.

    Napisz funkcję, która znajduje mniejszą liczbę z dwóch podanych.

    '''

    def porownaj(a,b):
        if a < b:
            return a
        else:
            return b
    wynik = porownaj(4,8)
    print(wynik)

    # pytania_weryfikujace:
    # jak uzyjesz petli if do porownania dwoch wartosci?
    # argumenty funkcji podawane w funkcji
    # zmienna = funkcja = wyjasnij


#lista4_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 3

def lista4_zadanie3():
    '''
    Zad 3.

    Napisz funkcję, która z podanych liczb (ilość dowolna) znajduje najmniejszą.

    Uwaga: Możesz wykorzystać funkcję z zadania 2.
    '''

    def porownaj(*args):
        #return min(args) # najszybszy sposob
        min = args[0]
        for i in args:
            if i < min:
                min = i
        print(min)


    wynik = porownaj(4,8,3,4)
    print(wynik)

#lista4_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 3

def lista4_zadanie4():
    '''
    Zad 4.

    Napisz funkcję, która wypisze na ekranie n pierwszych wyrazów ciągu Fibonacciego.

    Definicja ciągu Fibonacciego: Ciąg Fibonacciego

    Zad 5.
    '''

    def fibonacci(n):
        print('Fibonacci sequance:')
        n1, n2 = 0, 1
        count = 0
        while count < n:
            print(n1)
            n1, n2 = n2, n1 + n2
            count += 1

    fibonacci()


#lista4_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 5

def lista4_zadanie5():
        '''
Zad 5.

Napisz program, który pobiera od użytkownika współczynniki trójmianu kwadratowego, a następnie podaje jego rozwiązania.

Uwaga: Rozłóż program na mniejsze funkcje.

Definicja trójmianu kwadratowego: Trójmian Kwadratowy
        '''

lista4_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista4_zadanie6():
        '''
Zad 6.

    Napisz funkcję, która przyjmuje dowolną liczbę argumentów pozycyjnych oraz kluczowych.
    Niech funkcja drukuje argumenty pozycyjne w formie listy:

1 -> wartość pierwszego argumentu
2 -> wartość drugiego argumentu
.
.
.

    Niech funkcja drukuje argumenty kluczowe w formie listy:

nazwa (klucz) -> wartość
.
.
.

        '''

lista4_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0


def lista5_zadanie1():
        '''
Zad 1.

Stwórz moduł ciag_arytmetyczny.py zawierający funkcje, które dla podanych a1 (pierwszy wyraz ciągu), r (różnica) oraz n zwracają:

    n-ty wyraz ciągu
    sumę pierwszych n wyrazów ciągu

Wzór na ciąg arytmetyczny: an = a1 + (n - 1) * r
Przykład: 1,3,5,7,9 gdzie a1 = 1, r = 2, n = [1,5]
        '''

lista5_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie2():
        '''
Zad 2.

Napisz skrypt, który zaimportuje moduł z pierwszego zadania. Następnie:

    spyta użytkownika o a1, r i n
    wydrukuje na ekranie n-ty wyraz ciągu
    wydrukuje na ekranie sumę pierwszych n wyrazów ciągu

Zad 3.
        '''

lista5_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie3():
        '''
Zad 3.

Napisz funkcję, która dla podanego n i c0 wyznacza n-ty wyraz ciągu Collatza.

Definicja problemu Collatza: Problem Collatza


        '''

lista5_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie4():
        '''
Zad 4.

Napisz funkcję, która dla podanego n i c0 wyznacza pierwsze wystąpienie liczby 1 w ciągu Collatza.
        '''

lista5_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie5():
        '''
Zad 5 - Zadanie domowe.

Przeanalizuj rozwiązanie zadania 5 w Przykładowych Rozwiązaniach, które dokonuje konwersji między kolorami opisanymi w RGB i HEX.

Wyciągnij wnioski i przedstaw je na kolejnych zajęciach.


        '''

lista5_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie6():
        '''
Zad 6 - Pierwszy Projekt

Zapoznaj się z opisem projektu Gra - Krowy i Byki, który będzie Twoim pierwszym samodzielnym projektem.

Do dzieła!
        '''

lista5_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista6_zadanie1():
        '''

        '''

lista6_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista6_zadanie2():
        '''

        '''

lista6_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista6_zadanie3():
        '''

        '''

lista6_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista6_zadanie4():
        '''

        '''

lista6_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista6_zadanie5():
        '''

        '''

lista6_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista6_zadanie6():
        '''

        '''

lista6_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista6_zadanie7():
        '''

        '''

lista6_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista6_zadanie8():
        '''

        '''

lista6_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista6_zadanie9():
        '''

        '''

lista6_zadanie9()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista7_zadanie1():
        '''

        '''

lista7_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista7_zadanie2():
        '''

        '''

lista7_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista7_zadanie3():
        '''

        '''

lista7_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista7_zadanie4():
        '''

        '''

lista7_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista7_zadanie5():
        '''

        '''

lista7_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista7_zadanie6():
        '''

        '''

lista7_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista7_zadanie7():
        '''

        '''

lista7_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista7_zadanie8():
        '''

        '''

lista7_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista7_zadanie9():
        '''

        '''

lista7_zadanie9()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista8_zadanie1():
        '''

        '''

lista8_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista8_zadanie2():
        '''

        '''

lista8_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista8_zadanie3():
        '''

        '''

lista8_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista8_zadanie4():
        '''

        '''

lista8_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista8_zadanie5():
        '''

        '''

lista8_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista8_zadanie6():
        '''

        '''

lista8_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista8_zadanie7():
        '''

        '''

lista8_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista8_zadanie8():
        '''

        '''

lista8_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista8_zadanie9():
        '''

        '''

lista8_zadanie9()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista9_zadanie1():
        '''

        '''

lista9_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista9_zadanie2():
        '''

        '''

lista9_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista9_zadanie3():
        '''

        '''

lista9_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista9_zadanie4():
        '''

        '''

lista9_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista9_zadanie5():
        '''

        '''

lista9_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista9_zadanie6():
        '''

        '''

lista9_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista9_zadanie7():
        '''

        '''

lista9_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista9_zadanie8():
        '''

        '''

lista9_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista9_zadanie9():
        '''

        '''

lista9_zadanie9()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista10_zadanie1():
        '''

        '''

lista10_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista10_zadanie2():
        '''

        '''

lista10_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista10_zadanie3():
        '''

        '''

lista10_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista10_zadanie4():
        '''

        '''

lista10_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista10_zadanie5():
        '''

        '''

lista10_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista10_zadanie6():
        '''

        '''

lista10_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista10_zadanie7():
        '''

        '''

lista10_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista10_zadanie8():
        '''

        '''

lista10_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista10_zadanie9():
        '''

        '''

lista10_zadanie9()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista11_zadanie1():
        '''

        '''

lista11_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista11_zadanie2():
        '''

        '''

lista11_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista11_zadanie3():
        '''

        '''

lista11_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista11_zadanie4():
        '''

        '''

lista11_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista11_zadanie5():
        '''

        '''

lista11_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista11_zadanie6():
        '''

        '''

lista11_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista11_zadanie7():
        '''

        '''

lista11_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista11_zadanie8():
        '''

        '''

lista11_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista11_zadanie9():
        '''

        '''

lista11_zadanie9()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista12_zadanie1():
        '''

        '''

lista12_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista12_zadanie2():
        '''

        '''

lista12_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista12_zadanie3():
        '''

        '''

lista12_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista12_zadanie4():
        '''

        '''

lista12_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista12_zadanie5():
        '''

        '''

lista12_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista12_zadanie6():
        '''

        '''

lista12_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista12_zadanie7():
        '''

        '''

lista12_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista12_zadanie8():
        '''

        '''

lista12_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista12_zadanie9():
        '''

        '''

lista12_zadanie9()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0




def performance():
    #liczba wszystkich zadan
    a = sum(slownik_listy_liczba_zadan.values())
    #liczba ukonczonych zadan
    b = ukonczenie_zadania
    #procent ukonczenia wszystkich zadan
    c = round((b/a)*100)


    print('\nukonczona liczba zadan: {}'.format(b))
    print('procent ukonczenia wszystkich zadan : {}%'.format(c))
    wynik = round(szac_poziom_znajomosci_zadania/ukonczenie_zadania)
    print('srednia poziomu znajomosci wykonanych zadan : {}'.format(wynik))
    wynik_2 = round(((szac_poziom_znajomosci_zadania)/(a)))
    print('srednia poziomu znajomosci calego materialu : {}'.format(wynik_2))

performance()





