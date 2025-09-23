from egz2Btesty import runtests

# Jakub Węgrzyniak

#Pomysl:

# Mój algorytm przedstawia bardzo prosty pomysł na rozwiązanie tego problemu, przechodze po kolei
# po elementach tablicy ( dokładam nowy przedzial) i sprawdzam czy prowadzi on do jakiejś kolizji z poprzednimi przedziałami
# jeżeli tak to usuwam te przedziały i zarówno ten który doprowadza do kolizji
# Na koncu zliczam ile przedzialow finalnie zostało.

# Zastapienie liczb z tablicy T liczbami -1 nie prowadzi do błędów , ponieważ w zadaniu mamy tylko przedziały [0,x],
# a jeżeli wartośc T[i] jest równa -1 , to znaczy że ten przedział został już wczesniej usunięty podczas kolizji z innym.

# Zlożoność O(n^2 + n) --> O(n^2)

def bitgame(T):
  n = len(T)

  for i in range(n):
    flag = False   # Zapisuje czy dodany przedział powoduje kolizje

    for j in range(i):

      if T[i] >= T[j] and T[j] != -1: # Jeżeli jest kolizja , a przedział nie został juz wczesniej usunięty,
        T[j] = -1                     # to usuwam przedział oraz zapisuje ze dokładany przedzial powoduje kolizje
        if not flag:
          flag = True
      
    if flag:   # Jeżeli jest kolizja to ten przedział również zostaje usunięty
      T[i] = -1
  
  cnt = 0

  for i in range(n):
    if T[i] != -1:  # Jeżeli nie zostało usunięte podczas jakiejs kolizji, no to wiadomo ze zostało do końca 
      cnt += 1
  
  return cnt
      
runtests( bitgame, all_tests = True )
