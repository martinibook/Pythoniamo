# richiesta di nuova parola
def ric_parola():
    while True:
        npa=input('Parola: ')
        if npa.isalpha():    
            return npa.lower()
        else:
            print('Solo lettere!')
                

#  controlla se in archivio
def se_nuova(npa,arkivio):
    if not npa in arkivio:
        return True
    

# controllo sillabe
def ctl_sillabe(npa,arkivio):
    if len(arkivio)>0:
        if arkivio[-1][-2:]==npa[0:2]:
            return True
    elif len(arkivio)==0:
        return True
    else:
        return False


# main
arkivio=[]
gioco=True

print('Gioco delle parole concatenate')
print('Scrivi la prima libera.')
while gioco:
    npa=ric_parola()
    if ctl_sillabe(npa,arkivio):
        print(f'"{npa}" parola valida!',end=' ')
        if se_nuova(npa,arkivio):
            print('e mai usata!')
            arkivio.append(npa)
        else:
            print('ma già uscita!')
            print('FINE.')
            gioco=False
    else:
        print(f'Mi dispiace ma "{arkivio[-1]}" e "{npa}" non si concatenano!')
        print('FINE.')
        gioco=False
print(arkivio)
print(f'{len(arkivio)}: parole trovate.')     


