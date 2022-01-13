# %%
# funzione stampa tabella
def sta_tab(tab):
    print(f"""
    ___________
 1<[ {tab[0][0]} | {tab[0][1]} | {tab[0][2]} ]
   [-----------]
 2<[ {tab[1][0]} | {tab[1][1]} | {tab[1][2]} ]
   [-----------] 
 3<[ {tab[2][0]} | {tab[2][1]} | {tab[2][2]} ]
    TTTTTTTTTTT
     1   2   3
    """)


# %%
# funzione input giocata
def giocata(ab):
    
    while True:
        print(f"gioca: {ab}")
        r=input('Riga? ')
        c=input('Col? ')
        if r.isdecimal() and c.isdecimal():
            rn=int(r)
            cn=int(c)
            if rn>0 and rn<4 and cn>0 and cn<4:
                return rn-1,cn-1
        print('Riprova! ')    

# %%
#funzione controllo giocata
def crl_gio(r,c,tab):
    if tab[r][c]==" ":
        return True
    else:
        print("casella occupata!")
        return False
        

# %%
# funzione se vincitore
def vincitore(ab,t):
    g=[ab]*3
    if g==t[0] or g==t[1] or g==t[2]:
        return True
    elif g==[t[0][0],t[1][0],t[2][0]]:
        return True
    elif g==[t[0][1],t[1][1],t[2][1]]:
        return True   
    elif g==[t[0][2],t[1][2],t[2][2]]:
        return True  
    elif g==[t[0][0],t[1][1],t[2][2]]:
        return True   
    elif g==[t[2][0],t[1][1],t[0][2]]:
        return True                    

# %%
tab=[[' ']*3,[' ']*3,[' ']*3]
play=True
pieno=0
a='X'
b='O'
print('GIOCO DEL TRIS')
sta_tab(tab)

while play:
    r,c=giocata(a)
    if crl_gio(r,c,tab):
        tab[r][c]=a
        a,b=b,a
        pieno+=1
    if pieno==9:
        play=False
        print('Finita pari!')
    if vincitore(b,tab):
        print(f"{b} HA VINTO!!!")
        play=False
    sta_tab(tab)



