# creazione posti a sedere
platea={
    'posto':[' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9','10'],
    '-----':['-----------------------------------------------'],  
    'fila9':[10,10,10,10,10,10,10,10,10,10],
    'fila8':[10,10,10,10,10,10,10,10,10,10],
    'fila7':[10,10,10,10,10,10,10,10,10,10],
    'fila6':[10,10,20,20,20,20,20,20,10,10],
    'fila5':[10,10,20,20,20,20,20,20,10,10],
    'fila4':[10,10,20,20,20,20,20,20,10,10],
    'fila3':[20,20,30,30,30,30,30,30,20,20],
    'fila2':[20,30,30,40,50,50,40,30,30,20],
    'fila1':[30,40,50,50,50,50,50,50,40,30],
}

#  stampa posti a sedere
def sta_posti(platea):
    print(f"""
_____________________POSTI A SEDERE_____________________""")
    for fila in platea:
        print(f"\n{fila}: ",end='')
        for posto in platea[fila]:
            print(f" {posto} ",end=" ")
        

# scegli un posto
def scelta_posto(platea):
    
    while True:
        
        r=input('Fila? ')
        c=input('Poltrona? ')
        if r.isdecimal() and c.isdecimal():
            rn=int(r)
            cn=int(c)
            if rn>0 and rn<=9 and cn>0 and cn<=10:
                return rn,cn-1
        sta_posti(platea)
        print('\nRiprova! ')
        

# controllo posto libero
def crl_poltrona(r,c,tab):
    if tab[f"fila{str(r)}"][c]!=' 0':
        return True
    else:
        print("\npoltrona occupata!")
        return False


# menu di scelta
def menu():
    while True:
        print('\nScegli una opzione')
        mah=input("(1)=posto (2)=prezzo (3)=stoKazzo!")
        if mah=='1' or  mah=='2' or mah=='3':
            return int(mah)


# prendi posto!
def pre_poltrona(f,p):
    platea[f'fila{str(f)}'][p]=' 0'



# scelta del prezzo
def quantiEuro():
    while True:        
        euro=input('Posto da 10 20 30 40 50 Euro?')
        if euro in ['10','20','30','40','50']:
            return int(euro)
        else:
            print('riprova!')


# prendi x prezzo
def cercaXprezzo(euro):
    for fi in platea.__reversed__():
        for posto in range(len(platea[fi])):
            if platea[fi][posto]==euro:
                platea[fi][posto]=' 0'
                print(f"\nbiglietto N {posto+1}, {fi} venduto!")
                return True
    return False


# main
lavoro=True
while lavoro:
    sta_posti(platea)
    s_m=menu()
    if s_m==1:
        n_f,n_p=scelta_posto(platea)
        p_VF=crl_poltrona(n_f,n_p,platea)
        if p_VF:
            pre_poltrona(n_f,n_p)
            print(f'\nPoltrona N {n_p+1},Fila {n_f} Venduto!')
    elif s_m==2:
        eu=quantiEuro()
        if not cercaXprezzo(eu):
            print(f'\nbiglietti da {eu} Euro sono ESAURITI!')
        
    elif s_m==3:
        print('\nAssorrrate!!!')
        lavoro=False
