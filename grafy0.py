from asyncio import sleep
import sys
import time
import timeit
import random
from random import randint, randrange
import math
from queue import Queue

"""
def gentabkrawlos(N, tab):
    t1=[]
    for i in range(N):
        t1.append(randint(0,N))
    for i in range(N):
        tab[i][0]=t1[i]
    for i in range(N):
        while(True):
            tab[i][1]=randint(0,N)
            if (tab[i][1]!=tab[i][0]):
                break
        for j in range (i):
            while(tab[i]==tab[j]):
                tab[i][1]=randint(0,N)

def gentabkraw(N, tab):
    t1=[0,1,2,3,4]
    for i in range(0, N-1):
        tab[i][0]=t1[i]
        tab[i][1]=i+1
"""
    
def pokaz(tab2):
    for i in range(len(tab2)):
        print(tab2[i])
    print("\n")

def generate_random_graph_with_m_edges(N, M):
    # Initialize an adjacency matrix of size NxN with zeros
    graph = [[0 for _ in range(N)] for _ in range(N)]

    # List of all possible edges in a graph with N nodes
    all_edges = [(i, j) for i in range(N) for j in range(i + 1, N)]

    # Shuffle the list of edges to introduce randomness
    random.shuffle(all_edges)
    # Select the first M edges from the shuffled list
    
    # Add the selected edges to the adjacency matrix
    for i in range(int(M)):
        a, b = all_edges[i]
        graph[a][b] = 1
        graph[b][a] = 1

    return graph

def gengraflos_macsas50(N):
    macierz=[[0 for _ in range(N)] for _ in range(N)]
    M = int(N*(N-1)/4)
    i=0
    for j in range(0,N-1):
            i+=1
            if (i>M):
                #print(i)
                break
            k=randrange(j+1,N)
            while(j==k or macierz[j][k] or macierz[k][j]):
                k=randrange(j+1,N)
            if (j<k):
                macierz[j][k]=1
            else:
                macierz[k][j]=-1
    while(i<M):
        i+=1
        if (i>M):
            #print(i)
            break
        j=randrange(0,N-1)
        k=randrange(j,N)
        #print(i)
        #print(j)
        while(j==k or macierz[j][k] or macierz[k][j]):
            j=randrange(0,N-1)
            k=randrange(j,N)
            #print(" ",k)
            
        if (j<k):
            macierz[j][k]=1
        else:
            macierz[k][j]=-1
        #print(macsasnatabkrew(N, macierz))
    #print("\n")        
    return macierz
            
def gengraflos_macsas_tabkraw(N, macierz):
    
    #raczej nie to czego pani oczekuje, to opiera się na tabeli krawędzi bardziej niż macierzy sąsiedztwa
    #brak 100% gwarancji spójności
    
    #for i in range(N):
    #      for j in range(N):
    #           macierz[i][j]=0
    macierz=[[0 for _ in range(N)] for _ in range(N)]
    M = int(N*(N-1)/4)
    wszystkraw = [(i, j) for i in range(N) for j in range(i+1, N)]
    random.shuffle(wszystkraw)
    tabelakraw=[]
    #print(int(M))
    j=0
    for i in range(M):
        a, b = wszystkraw[j]
        j+=1
        while(a==b):
            a, b = wszystkraw[j]
            j+=1
            #print("w2")
            #a = randrange(0,N)
            #b = randrange(0,N)
        #print("a: ", a)
        #print("b: ",b)
        if (a>b):
            #print(macierz[b][a])
            #pokaz(macierz)
            #print("-->>")
            macierz[b][a]=-1
            tabelakraw.append([b,a])
            #pokaz(macierz)
            #print(macierz[b][a])
            #macierz[a][b]=1
        else:
            #print(macierz[a][b])
            #pokaz(macierz)
            #print("-->>")
            macierz[a][b]=1
            tabelakraw.append([a,b])
            #pokaz(macierz)
            #print(macierz[a][b])
            #macierz[b][a]=-1
        #print(macierz[a][b])
        #print(macierz[b][a])
        #pokaz("\n\n")
    return macierz, tabelakraw, M

def macsasnalisnast(N, macierz):
    lisnast=[[] for i in range(N)]
    #print(lisnast)
    for i in range(N):
          for j in range(N):
                if(macierz[i][j]==1):
                   lisnast[i].append(j)
                elif(macierz[i][j]==-1):
                    #dołóż by było minimum j elementów
                    #while (i<j):
                    lisnast[j].append(i)
                #pokaz(lisnast)
    return lisnast


def macsasnatabkrew(N, macierz):
    tabelakraw = []
    M=0
    for i in range(N):
          for j in range(N):
               if(macierz[i][j]==1):
                   tabelakraw.append([i, j])
                   M+=1
               elif(macierz[i][j]==-1):
                    tabelakraw.append([j, i])
                    M+=1
    return tabelakraw, M


#macierz sąsiedztwa (nasycenie lukami w grafie): 50% z n*(n-1)/2 + możliwość wczytania
#przetwarzanie z macierzy sąsiedztwa na listę następników i tabelę krawędzi, algorytmy w wersji dla każdego z nich
    #procedury przeglądania i sortowania grafu
#DFS            DFS             Tarjana
#BFS            BFS             Kahna


""""def dfsGomacsas(start, graf, odwiedzone, N):
    for i in range(N):
        if (graf[start][i]):
            graf[start][i] = false
            graf[i][start] = false;
            EdfsGo(i, graf, cEuler);
        }
    }
    cEuler.push(start);
}"""

def dfsGo_macsas(start, graf, odwiedzone, N):
    print(start)
    for i in range(N):
        if (graf[start][i]==1):
            if (odwiedzone[i]==False):
                odwiedzone[i] = True
                dfsGo_macsas(i, graf, odwiedzone, N)

def DFSmacsas(graf, N):
    #kolejka=Queue() 
    odwiedzone=[]
    for i in range(N):
        odwiedzone.append(False)
    for i in range(N):
        if (odwiedzone[i]==False):
            odwiedzone[i]=True
            dfsGo_macsas(i, graf,odwiedzone,N)
#lisnas
def dfsGo_lisnas(start, graf, odwiedzone, N):
    print(start)
    for i in graf[start]:
        if (odwiedzone[i]==False):
                odwiedzone[i] = True
                dfsGo_lisnas(i, graf, odwiedzone, N)
                
def DFSlisnas(graf, N):
    #kolejka=Queue() 
    odwiedzone=[]
    for i in range(N):
        odwiedzone.append(False)
    for i in range(N):
        if (odwiedzone[i]==False):
            odwiedzone[i]=True
            dfsGo_lisnas(i, graf,odwiedzone,N)
#tabkraw
def dfsGo_tabkraw(start, graf, M, odwiedzone):
    odwiedzone[start] = True
    print(start)
    for i in range(M):
         #print(i)
        if (graf[i][0]==start):
            if (odwiedzone[graf[i][1]]==False):
                odwiedzone[graf[i][1]] = True
                dfsGo_tabkraw(graf[i][1], graf, M, odwiedzone)
                
def DFStabkraw(graf, N, M):
    #kolejka=Queue() 
    odwiedzone=[]
    for i in range(N):
        odwiedzone.append(False)
    for i in range(N):
        if (odwiedzone[i]==False):
            dfsGo_tabkraw(i, graf, M, odwiedzone)



def bfsGomacsas(start, graf, N, odwiedzone):
    #for i in range (N):
    #    odwiedzone[i] = False
    kolejka = Queue()
    odwiedzone[start]=True
    kolejka.put(start)
    while (kolejka.empty()==False):
        u = kolejka.get()
        print(u)
        for i in range(N):
            if(graf[u][i]==1):
                if (odwiedzone[i]==False):
                    odwiedzone[i] = True
                    kolejka.put(i)

def BFSmacsas(graf, N):
    odwiedzone=[]
    for i in range(N):
        odwiedzone.append(False)
    for i in range(N):
        if (odwiedzone[i]==False):
            bfsGomacsas(i, graf, N, odwiedzone)

def bfsGolisnas(start, graf, N, odwiedzone):
    kolejka = Queue()
    odwiedzone[start]=True
    kolejka.put(start)
    while (kolejka.empty()==False):
        u = kolejka.get()
        print(u)
        for i in range(len(graf[u])):
            if (odwiedzone[graf[u][i]]==False):
                odwiedzone[graf[u][i]] = True
                kolejka.put(graf[u][i])

def BFSlisnas(graf, N):
    odwiedzone=[]
    for i in range(N):
        odwiedzone.append(False)
    for i in range(N):
        if (odwiedzone[i]==False):
            bfsGolisnas(i, graf, N, odwiedzone)
#tabkr
def bfsGotabkraw(start, graf, M, odwiedzone):
    kolejka = Queue()
    odwiedzone[start]=True
    kolejka.put(start)
    while (kolejka.empty()==False):
        u = kolejka.get()
        print(u)
        for i in range(M):
            if(graf[i][0]==u):
                if (odwiedzone[graf[i][1]]==False):
                    odwiedzone[graf[i][1]] = True
                    kolejka.put(graf[i][1])

def BFStabkraw(graf, N, M):
    odwiedzone=[]
    for i in range(N):
        odwiedzone.append(False)
    for i in range(N):
        if (odwiedzone[i]==False):
            bfsGotabkraw(i, graf, M, odwiedzone)

#def DFSmacsas_sort_top(macierzsas, N)','DFSlisnas_sort_top(lisnast, N)','DFStabkraw_sort_top(tabelakraw, N, M)'
def dfsGo_macsas_sort_top(start, graf, odwiedzone, N, rozw):
    odwiedzone[start]=1
    #print(start)
    for i in range(N):
        if (graf[start][i]==1):
            if (odwiedzone[i]==1):
                print("graf cykliczny")
                return 0
            if (odwiedzone[i]==0):
                odwiedzone[i] = 1
                dfsGo_macsas_sort_top(i, graf, odwiedzone, N,rozw)
    odwiedzone[start]=2
    rozw.append(start)
def dfsGo_lisnas_sort_top(start, graf, odwiedzone, N, rozw):
    odwiedzone[start]=1
    for i in graf[start]:
        if (odwiedzone[i]==1):
                print("graf cykliczny")
                return 0
        if (odwiedzone[i]==0):
                odwiedzone[i] = 1
                dfsGo_lisnas_sort_top(i, graf, odwiedzone, N, rozw)
    odwiedzone[start]=2
    rozw.append(start)
def dfsGo_tabkraw_sort_top(start, graf, odwiedzone,M, rozw):
    odwiedzone[start] = 1
    for i in range(M):
         #print(i)
        if (graf[i][0]==start):
            if (odwiedzone[graf[i][1]]==1):
                print("graf cykliczny")
                return 0
            if (odwiedzone[graf[i][1]]==0):
                odwiedzone[graf[i][1]] = 1
                dfsGo_tabkraw_sort_top(graf[i][1], graf, odwiedzone, M, rozw)
    odwiedzone[start]=2
    rozw.append(start)

def DFS_sort_top(graf, N, M, O):
    #kolejka=Queue() 
    odwiedzone=[]
    rozw=[]
    for i in range(N):
        odwiedzone.append(0)
    for i in range(N):
        if (odwiedzone[i]==0):
            if(O==1):
                dfsGo_macsas_sort_top(i, graf,odwiedzone,N, rozw)
            elif(O==2):
                dfsGo_lisnas_sort_top(i, graf,odwiedzone, N, rozw)
            elif(O==3):
                #print(i)
                dfsGo_tabkraw_sort_top(i, graf,odwiedzone, M, rozw)
    rozw.reverse()        
    print(rozw)

#def BFSmacsas_sort_top(macierzsas, N)','BFSlisnas_sort_top(lisnast, N)','BFStabkraw_sort_top(tabelakraw, N, M)

def bfsGo_macsas_sort_top(start, graf,odwiedzone,N, wej):
    #print("bfsGo_macsas_sort")
    kolejka = Queue()
    odwiedzone[start]=True
    kolejka.put(start)
    while (kolejka.empty()==False):
        u = kolejka.get()
        for i in range(N):
            #print("ui:",u," ",i)
            if(graf[u][i]==1):
                wej[i]+=1
                if (odwiedzone[i]==False):
                    odwiedzone[i] = True
                    kolejka.put(i)
def bfsGo_lisnas_sort_top(start, graf,odwiedzone, N, wej):
    kolejka = Queue()
    odwiedzone[start]=True
    kolejka.put(start)
    while (kolejka.empty()==False):
        u = kolejka.get()
        for i in range(len(graf[u])):
            wej[graf[u][i]]+=1
            if (odwiedzone[graf[u][i]]==False):
                odwiedzone[graf[u][i]] = True
                kolejka.put(graf[u][i])
def bfsGo_tabkraw_sort_top(start, graf,odwiedzone, M, wej):
    kolejka = Queue()
    odwiedzone[start]=True
    kolejka.put(start)
    while (kolejka.empty()==False):
        u = kolejka.get()
        for i in range(M):
            if(graf[i][0]==u):
                wej[graf[i][1]]+=1
                if (odwiedzone[graf[i][1]]==False):
                    odwiedzone[graf[i][1]] = True
                    kolejka.put(graf[i][1])
##pseudobfs-y odejmujące - by je stworzyć trzeba najpierw użyć dawnej części funkcji sterującej zmodyfikować o mechanizm kolejki, 
#a potem odjąć jak w pierwotnych funkcjach odej
def bfsGo_macsas_sort_topodej(graf,wej,N, rozw):
    #print("bfsGo_macsas_sort_topodej")
    kolejka = Queue()
    cykl=True
    for i in range(N):
        if (wej[i]==0):
            kolejka.put(i)
            cykl=False
    if(cykl):
        print("graf cykliczny")
        return 0
    while (kolejka.empty()==False):
        u = kolejka.get()
        rozw.append(u)
        wej[u]=-1
        for i in range(N):
            if(graf[u][i]==1):
                wej[i]-=1

def bfsGo_lisnas_sort_topodej(graf,wej,N, rozw):
    print("bfsGo_lisnas_sort_topodej")
    kolejka = Queue()
    cykl=True
    for i in range(N):
        if (wej[i]==0):
            kolejka.put(i)
            cykl=False
    if(cykl):
        print("graf cykliczny")
        return 0
    while (kolejka.empty()==False):
        u = kolejka.get()
        rozw.append(u)
        for i in range(N):
            if(graf[u][i]==1):
                wej[i]-=1

def bfsGo_tabkraw_sort_topodej(graf,wej,N, rozw):
    kolejka = Queue()
    cykl=True
    for i in range(N):
        if (wej[i]==0):
            kolejka.put(i)
            cykl=False
    if(cykl):
        #print("graf cykliczny")
        return 0
    while (kolejka.empty()==False):
        u = kolejka.get()
        rozw.append(u)
        for i in range(N):
            if(graf[u][i]==1):
                wej[i]-=1

def sasodej_macsas_sort_top(start, graf, N, wej):
    for i in range(N):
            if(graf[start][i]==1):
                wej[i]-=1
def sasodej_lisnas_sort_top(start, graf, wej):
    for i in graf[start]:
        wej[i]-=1
def sasodej_tabkraw_sort_top(start, graf, M, wej):
    for i in range(M):
        if (graf[i][0]==start):
            wej[graf[i][1]]-=1
                        
def BFS_sort_top(graf, N, M, O):
    odwiedzone=[]
    wej=[]
    rozw=[]
    for i in range(N):
        odwiedzone.append(False)
        wej.append(0)
    for i in range(N):
        if (odwiedzone[i]==False):
            print(i)
            if(O==1):
                bfsGo_macsas_sort_top(i, graf,odwiedzone,N, wej)
            elif(O==2):
                bfsGo_lisnas_sort_top(i, graf,odwiedzone, N, wej)
            elif(O==3):
                #print(i)
                bfsGo_tabkraw_sort_top(i, graf,odwiedzone, M, wej)
    print(wej)
    while(len(rozw)<N):
        if(O==1):
            if(bfsGo_macsas_sort_topodej(graf,wej,N, rozw)==0):
                break            
        elif(O==2):
            if(bfsGo_lisnas_sort_topodej(graf,wej,N, rozw)==0):
                break
        elif(O==3):
            #print(i)
            if(bfsGo_tabkraw_sort_topodej(graf,wej,N, rozw)==0):
                break
        """for i in range(N):
            if (wej[i]==0):
                rozw.append(i)
                cykl=False
                if(O==1):
                    sasodej_macsas_sort_top(i, graf, N, wej)
                elif(O==2):
                    sasodej_lisnas_sort_top(i, graf, wej)
                elif(O==3):
                    #print(i)
                    sasodej_tabkraw_sort_top(i, graf, M, wej)"""
       

    print(rozw)
#
#def
#def

#####
l=1
def testuj_dla(algorytm_macierzsas, algorytm_lisnas, algorytm_tabkraw):
    results = [timeit.timeit(algorytm_macierzsas, globals=globals(), number=l)]
    print("\n")
    results.append(timeit.timeit(algorytm_lisnas, globals=globals(), number=l))
    print("\n")
    results.append(timeit.timeit(algorytm_tabkraw, globals=globals(), number=l))
    
    print(results)



while(True):
    print("Testowanie algorytmów na grafach czy chcesz graf:"
    "\n A. Wprowadzony z klawiatury(macierz sąsiedztwa). \n B. Wygenerowany losowy.")
    odp=str(input())
    print("Ile chcesz liczb:")
    N=int(input())
    #macierzsas = N*[0]
    #pokaz(macierzsas)
    macierzsas = N*[N*[0]]
    #pokaz(macierzsas)
    if(odp=="A") | (odp=="a") | (odp=="A.") | (odp=="a."):
        if(N<=10):
            for i in range(N):
                for j in range(N):
                    macierzsas[i][j]=(int(input()))
        else:
            for i in range(10):
                for j in range(10):
                    macierzsas[i][j]=(int(input()))
    else:
        #macierzsas, tabelakraw, M=gengraflos_macsas_tabkraw(N, macierzsas)
        macierzsas=gengraflos_macsas50(N)
    #macierzsas=generate_random_graph_with_m_edges(N, N*(N-1)/4)
    print(macierzsas)
    #generowanie innych reprezentacji
    lisnast = macsasnalisnast(N, macierzsas)
    print(lisnast)
    tabelakraw, M = macsasnatabkrew(N, macierzsas)
    print(tabelakraw)
    #funkcja do wyświetlania tych które są czytelne?
    sys.setrecursionlimit(100000000)
    while(True):
        print("Który algorytm chcesz przetestować?")
        print("\n1. DFS z wypisywaniem. \n2. BFS z wypisywaniem")
        print("\n3. DFS sortowanie topologiczne(Algorytm Tarjana?).\n4. BFS sortowanie topologiczne(Algorytm Kahna?).")
        print("5. Wyświetl.\n 6. Wyświetl macierz sąsiedztwa.\n 7. Wyświetl listę następników\n 8. Wyświetl listę krawędzi\n")
        algorytm=int(input())
        print("\n")
        #if algorytm<=0:#
            #del_post_order(BST)
            #del_post_order(AVL)
            #testuj_dla('creatBST(N, ciagros)', 'creatAVL(N, ciagros)')#___próbne utworzenie nowych drzew z danych___
        #el
        if algorytm==1:
            testuj_dla('DFSmacsas(macierzsas, N)','DFSlisnas(lisnast, N)','DFStabkraw(tabelakraw, N, M)')#1-macsas,2-lisnas,3-tabkraw
        elif algorytm==2:
            testuj_dla('BFSmacsas(macierzsas, N)','BFSlisnas(lisnast, N)','BFStabkraw(tabelakraw, N, M)')
        elif algorytm==3:
            testuj_dla('DFS_sort_top(macierzsas, N, M, 1)','DFS_sort_top(lisnast, N, M, 2)','DFS_sort_top(tabelakraw, N, M, 3)')
        elif algorytm==4:
            testuj_dla('BFS_sort_top(macierzsas, N, M, 1)','BFS_sort_top(lisnast, N, M, 2)','BFS_sort_top(tabelakraw, N, M, 3)')
        elif algorytm==5:
            testuj_dla('pokaz(macierzsas)','pokaz(lisnast)','pokaz(tabelakraw)')
        elif algorytm==6:
            pokaz(macierzsas)
        elif algorytm==7:
            pokaz(lisnast)
        elif algorytm==8:
            pokaz(tabelakraw)
        #else:
        #    testuj_dla("del_post_order(BST),del_post_order(AVL)")
        #print("Zresetować drzewa?")
        #odp=str(input())
        #if(odp=="Tak") | (odp=="TAK") | (odp=="tak") | (odp=="T") | (odp=="t"):
            #____usuniecie i dodanie w miejsce zmiennej BST i AVL
        print("Kontynuować, dla tych samych danych?")
        odp=str(input())
        if(odp=="Nie") | (odp=="NIE") | (odp=="nie") | (odp=="N") | (odp=="n"):
            break
    
    print("kontynuować, dla innych danych?")
    odp=str(input())
    if(odp=="Nie") | (odp=="NIE") | (odp=="nie") | (odp=="N") | (odp=="n"):
        break
    #""""""
