
import argparse

slownik_listy_liczba_zadan = {'lista1': 3, 'lista2': 3, 'lista3': 5, 'lista4': 6, 'lista5': 6, 'lista6': 3, 'lista7': 5, 'lista8': 5, 'lista9': 2, 'lista10': 5, 'lista11': 4, 'lista12': 10}
# wyjsciowy poziom znajomosci zagadnien i ilosci wykonanych zadan
szac_poziom_znajomosci_zadania = 0
ukonczenie_zadania = 0


def lista1_zadanie1():
    '''

	'''
    kraj = "Polska"
    print("Hello {}".format(kraj))

#lista1_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 9

def lista1_zadanie2():
    '''

    '''
    x = 1   # [zmienna] [operator przypisania] [wartość]
    y = 1.0
    z = True

    # drukuj typy zmiennych x, y i z (oddzielone przecinkiem)
    print(type(x), type(y), type(z))

#lista1_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 9

def lista1_zadanie3(a,b):

    print('dodaje dwie liczby: {} oraz {}'.format(a,b))
    print('wynik: {}'.format(a+b))


#lista1_zadanie3(5,4)
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 8


def lista2_zadanie1():
	s = 'Python'
	print(s)
	print(s[0], s[1])
	new_s = s.replace(s[0], 'p')
	print(new_s)

#lista2_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 9

def lista2_zadanie2():
	#lista
	lista = [1, 2, 'c', 'smok']
	print(lista)
	len(lista)
	print('trzeci element listy : {}'.format(lista[3]))

#lista2_zadanie2()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 9

def lista2_zadanie3():
	# basics krotka tuple
	lista = [1, 2, 'trzy']
	print('zadana lista : {}'.format(lista))
	krotka = tuple(lista)
	print('krotka z listy : {}'.format(krotka))
	string = "amadeusz"
	print('zadany string :{}'.format(string))
	x = tuple(string)
	print('krotka ze stringa : {}'.format(x))

#lista2_zadanie3()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 9

def lista3_zadanie1():
	#petla for
	lista = ['a', 'b', 'c']
	print('zadana lista: {}'.format(lista))
	print('petla for po liscie')
	for litera in lista:
		print(litera)

	print('petla for po enumerate lista')
	for pozycja, litera in enumerate(lista):
		print(pozycja,'.',litera)

#lista3_zadanie1()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 1
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 7

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

def lista3_zadanie6():
	'''

	'''

lista3_zadanie6()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista3_zadanie7():
	'''

	'''

lista3_zadanie7()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista3_zadanie8():
	'''

	'''

lista3_zadanie8()
#zadanie ukonczone? wpisz 1 jesli tak
ukonczenie_zadania += 0
#szacunkowy poziom znajomosci zagadnienia od 1 do 10
szac_poziom_znajomosci_zadania += 0

def lista3_zadanie9():
	'''

	'''

lista3_zadanie9()
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
    wynik = round(szac_poziom_znajomosci_zadania/ukonczenie_zadania)
    print('srednia poziomu znajomosci wykonanych zadan : {}'.format(wynik))
    wynik_2 = round(((szac_poziom_znajomosci_zadania)/(a)))
    print('srednia poziomu znajomosci calego materialu : {}'.format(wynik_2))

performance()


