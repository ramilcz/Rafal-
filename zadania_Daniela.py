
import math
import sys

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






slownik_listy_liczba_zadan = {'lista1': 5, 'lista2': 8, 'lista3': 5, 'lista4': 10, 'lista5': 10, 'lista6': 10, 'lista7': 10, 'lista8': 10, 'lista9': 10, 'lista10': 10, 'lista11': 10, 'lista12': 10}
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
    print(slubowanie)
    print(slubowanie[0])
    print(slubowanie.upper()) # zaczyna sie wielka litera :) co tam ze wszystkie inne tez sa wielkie
    i = slubowanie.count(' i ')
    print(i)
    i = slubowanie.count('i')
    print(i)
    if "Uniwersytet" in slubowanie:
        print('tak, wystepuje')

    lista = slubowanie.split()
    print(lista)
    print(*lista, sep = ', ') # drukuje tylko elementy listy i zadany separator
    print(len(lista))
    print(*lista, sep ='\n')




#lista2_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 4

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

        '''

lista3_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista3_zadanie3():
        '''

        '''

lista3_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista3_zadanie4():
        '''

        '''

lista3_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista3_zadanie5():
        '''

        '''

lista3_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista4_zadanie1():
        '''

        '''

lista4_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista4_zadanie2():
        '''

        '''

lista4_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista4_zadanie3():
        '''

        '''

lista4_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista4_zadanie4():
        '''

        '''

lista4_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista4_zadanie5():
        '''

        '''

lista4_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista4_zadanie6():
        '''

        '''

lista4_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista4_zadanie7():
        '''

        '''

lista4_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista4_zadanie8():
        '''

        '''

lista4_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista4_zadanie9():
        '''

        '''

lista4_zadanie9()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie1():
        '''

        '''

lista5_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie2():
        '''

        '''

lista5_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie3():
        '''

        '''

lista5_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie4():
        '''

        '''

lista5_zadanie4()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie5():
        '''

        '''

lista5_zadanie5()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie6():
        '''

        '''

lista5_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie7():
        '''

        '''

lista5_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie8():
        '''

        '''

lista5_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista5_zadanie9():
        '''

        '''

lista5_zadanie9()
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
    wynik = szac_poziom_znajomosci_zadania/ukonczenie_zadania
    print('srednia poziomu znajomosci wykonanych zadan : {}'.format(wynik))
    wynik_2 = round(((szac_poziom_znajomosci_zadania)/(a)))
    print('srednia poziomu znajomosci calego materialu : {}%'.format(wynik_2))

performance()





