
from random import *
inimesed=['A','B','C','D','E','F']
palgad=[2000,2000,122,122,2000,50]
nimi=''
count=0

def sisesta_andmed(i,p):
    #N=randint(4,8)
    N=3
    for n in range(N):
        inimene=input('Nimi: ')
        i.append(inimene)
        palk=randint(100,10000)
        p.append(palk)
    return i,p


def andmed_ekranile(i,p):
    N=len(i)
    for n in range(N):
        print(i[n],'-',p[n])


def kustutamine(i,p):
    nimi=input('Sisesta nimi, keda vaja kustutada: ')
    n=i.count(nimi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==nimi:
                t+=1
                abi_list.append(int(e)) #список индексов
                print(t,'. ',i[e], '-', p[e])
        jaak=int(input('Järjekordne number: '))
        i.pop(abi_list[jaak-1])
        p.pop(abi_list[jaak-1])
        andmed_ekranile(i,p)
    return i,p


#def max_palk(i,p):
#    max_list_palk=[]
#    max_list_nimi=[]
#    suurim=max(p)
#    count_max=0
#    for m in range(len(p)):
#        count_max+=1
#        max_list_palk.append(max(p[m])) # неработающая дичь
#        max_list_nimi.append(i[m])
#        print(count_max, '. ', max_list_nimi, '- ', max_list_palk)


def sorteerimine_max_to_min(i,p,v):
    N=len(p)
    if v==1:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
       for n in range(0,N):
            for m in range(n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    andmed_ekranile(i,p)


def vordsed_palgad(i,p):
    N=len(p)
    dublikaadid=[x for x in palgad if palgad.count(x)>1]
    dublikaadid=list(set(dublikaadid))
    print(dublikaadid) 
    for palk in dublikaadid:
        n=p.count(palk)
        k=-1
        for j in range(n):
            k=p.index(palk,k+1)
            nimi=i[k]
            print(palk,'saab kätte',nimi)


#def sarnased_palgad(i,p):
#    N=len(p)
#    for n in range(0,N):
#        for m in range(n,N):
#            if p[n]==p[m]:
#                n=p.count(p[n])

#    print(p[n], i[n])
#    print()


def otsi_nimi(i,p):
    otsi=input('Sisesta nimi, keda otsime: ')
    n=i.count(otsi)
    abi_list=[]
    if n>0:
        t=0
        for e in range(len(i)):
            if i[e]==otsi:
                t+=1
                abi_list.append(int(e)) #список индексов
                print(i[e], '-', p[e])


def rikad_inimesed(i,p):
    otsi=int(input('Sisesta palk, leiame rohkem kui: '))
    abi_list=[]
    t=0
    for e in range(len(p)):
        if p[e]>otsi:
            t+=1
            abi_list.append(int(e)) #список индексов
            print(i[e], '-', p[e])
        else:
            print('Kedagi ei ole')


def vaened_inimesed(i,p):
    otsi=int(input('Sisesta palk, leiame vähem kui: '))
    abi_list=[]
    t=0
    for e in range(len(p)):
        if p[e]<otsi:
            t+=1
            abi_list.append(int(e)) #список индексов
            print(i[e], '-', p[e])
        else:
            print('Kedagi ei ole')


def top_inimesed(i,p):
    top=input ('Kas esimene max või min maksimum palgaga? ')
    N=len(p)
    if top=='max':
        for y in range (0, N-1):
            for x in range (0, N-1):
                if p[y]>p[x]:
                    abi=p[y]
                    p[y]=p[x]
                    p[x]=abi

                    abi=i[y]
                    i[y]=i[x]
                    i[x]=abi
        print(f'Esimene on',i[1], 'palgaga ', p[1],'. ', '\nTeine on',i[2], 'palgaga ', p[2],'. ', '\nKolmas on',i[3], 'palgaga ', p[3],'. ')
    elif top=='min':
        for y in range (0, N):
            for x in range (0, N):
                if p[y]<p[x]:
                    abi=p[y]
                    p[y]=p[x]
                    p[x]=abi

                    abi=i[y]
                    i[y]=i[x]
                    i[x]=abi
        print(f'Esimene on',i[1], 'palgaga ', p[1],'. ', '\nTeine on',i[2], 'palgaga ', p[2],'. ', '\nKolmas on',i[3], 'palgaga ', p[3],'. ')#
    

def kesk_palk(i,p):
    summa=0
    for palk in p:
        summa+=palk
    summa/=len(p)
    print('Keskmine palk on: ', summa)
    for palk in p:
        if palk==summa:
            n=p.index(palk)
            print('Keskpalga saaja on: ',i[n])
        else:
            print('Kedagi selle palgaga ei ole')


def sort_nimi_jargi(p,i,v):
    N=len(p)
    if v==1:
        for n in range(0,N):
            for m in range(n,N):
                if p[n]<p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    else:
       for n in range(0,N):
            for m in range(n,N):
                if p[n]>p[m]:
                    abi=p[n]
                    p[n]=p[m]
                    p[m]=abi
                    abi=i[n]
                    i[n]=i[m]
                    i[m]=abi
    andmed_ekranile(i,p)


def tulumaks(i,p):
    summ=0
    for p1 in p:
        ind=p.index(p1)
        if p1<=1200:
            m=p1-500
            n=m*0.2
            summ=(m-n)+500
            print(i[ind],f'Maksab tulumakse {n} EUR ja saab palga {summ}EUR')
        elif p1>2100:
            pass


while 1:
#    valik=input('a-andmete sisestamine \ne-andmed ekranile ')
    print('a-andmete sisestamine \ne-andmed ekranile \nk-kustutamine \ns-max-sorteerimise \nv-vordsed palgad \no-otsi nimi \nr-palk suurem kui \np-palk vähem kui \nm-keskpalk \nn-sort nimi \nt-rikkam inimesed \nx-arvestame tulumakse')
    valik=input()
    if valik.lower()=='a':
        inimesed,palgad=sisesta_andmed(inimesed,palgad)
    elif valik.lower()=='e':
        andmed_ekranile(inimesed,palgad)
    elif valik=='k':
        inimesed,palgad=kustutamine(inimesed,palgad)
    elif valik=='s':
        sorteerimine_max_to_min(inimesed,palgad,int(input('1 - kahaneb, 2 - kasvab ')))
    #elif valik=='d':
    #    sarnased_palgad(inimesed,palgad)
    elif valik=='v':
        vordsed_palgad(inimesed,palgad)
    elif valik=='o':
        otsi_nimi(inimesed,palgad)
    elif valik=='r':
        rikad_inimesed(inimesed,palgad)
    elif valik=='p':
        vaened_inimesed(inimesed,palgad)
    elif valik=='m':
        kesk_palk(inimesed,palgad)
    elif valik=='n':
        sort_nimi_jargi(inimesed,palgad,int(input('1 - kahaneb, 2 - kasvab ')))
    elif valik=='t':
        top_inimesed(inimesed,palgad)
    elif valik=='j':
        kerjus_inimesed(inimesed,palgad)
    elif valik=='x':
        tulumaks(inimesed,palgad)
    else:
        break