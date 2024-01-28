#!/usr/bin/env python3
import  sys, os, getpass

try:
    import sqlite3 
except ImportError:
    print("")
    print("")
    print("*** Attenzione !!!")
    print("\tPer poter utilizzare questo script devi avere installato il modulo:")
    print("\tPySqlite. Da un analisi del tuo sistema non riuslta installato.")
    print("\tPer installaro da gentoo esegui da root il seguente comando:")
    print("\tpip install pysqlite. Dopo l'eesecuzione rilancia CapQuery\n\n")
    print("\tPer la versione windows scaricate il modulo da qui:")
    print("\thttp://prdownloads.sourceforge.net/pysqlite/pysqlite-0.5.0.win32-py2.3.exe?download")
    print("")
    sys.exit(-1)


def cls():
    if os.name=='posix':
        os.system('clear')
    else:
        os.system('cls')

def intesta():
    cls()
    print("\nC.A.P							Ver 1.0")
    print("\nInterrogazione remota  database Codici Avviamento\n\n")


def menu():
    risp=0
    while ((risp < 1) or (risp > 4)):
        intesta()
        print("\n\n\n\n\n")
        print("\t\t\t(1) Cerca Per Cap\n\n")
        print("\t\t\t(2) Cerca Per Comune\n\n")
        print("\t\t\t(3) Cerca Per Provincia e/o Comune\n\n")	
        print("\t\t\t(4) Esci\n\n")
        risp=input('\n\n Seleziona voce menu [ 1 - 4 ] ')
        if (risp=="1") or (risp=="2") or (risp=="3") or (risp=="4"):
            risp=int(risp)
        else:
            risp=0
		
        return(risp)

def displ_rec(d):
    intesta()
    if (len(d) == 1):
        Stringa=""
        Stringa='CAP : ' +d[0][1]+ ' - Prov: ' +d[0][3] +' - Comune: ' +d[0][5]
        print(Stringa)
    else:
        for i in range(0,len(d)):
            Stringa=""
            Stringa='CAP : ' +d[i][1]+ ' - Prov: ' +d[i][3] +' - Comune: ' +d[i][5]
            print(Stringa)



def Search_Cap(db):
    risp=0
    try:
        risp=int(input("\nCodice Avviamento postale ? [0 per uscire] "))
    except:
        print(f"Risp = {risp}")
        input("Premi un tasto per continuare...")
        input("\nDevi dare un valore numerico !!\nPremi INVIO per continuare...")
    if (risp==0):
       return()


    c=db.cursor()
    req="SELECT * from CAP where Codice='" + str(risp) + "';"
    c.execute(req)
    d=c.fetchall()
    if (len(d)==0):
        input("\nRecord inesistente !!!\nPremi INVIO per continuare...")
        sel=99
    else:
        sel=100
        while (sel != 99):
            displ_rec(d)
            try:
                sel=int(input('\n\nDigita 99 per uscire '))
            except:
                print("\nDevi dare un valore numerico !!")
                sel=100
                if (sel==99):
                    break

            selval=""
            upd=1


def Search_Comune(db):
    risp=""
    risp=input("\nNome (o parte) del comune ? [0 per uscire] ")
    if (len(risp) == 0):
        input("\nDigta 0 per uscre !!\nPremi INVIO per continuare...")
        Search_Comune(db)
    if (risp=="0"):
        return()
        
    req="SELECT * from CAP where Comune Like '%" + risp + "%' Order by Comune;"
    c=db.cursor()
    c.execute(req)
    d=c.fetchall()
    if (len(d)==0):
        input("\nRecord inesistente !!!\nPremi INVIO per continuare...")
        sel=99
    else:
        sel=100
		
    while (sel != 99):
        displ_rec(d)
        try:
            sel=int(input('\n\nDigita 99 per uscire '))
        except:
            print("\nDevi dare un valore numerico !!")
            sel=100
            if (sel==99):
                break

            selval=""
            upd=1


def Search_Prov_Comune(db):
    rispP=""
    rispC=""
    print("\nPossono essere selezionati la PRVOINCIA e/o il Comune (o parte di esso)\nNON sono ammessi entrambi campi vuoti.\n\n")
    rispP=input("\n Digta la sigla della provincia [0 per uscire] ")
    if (rispP=="0"):
        return()
    rispC=input("\n Digta il comune, o parte di esso [0 per uscire] ")
    if (rispC=="0"):
        return()
    if (len(rispP) == 0 and len(rispC) == 0):
        input("\nDigta 0 per uscre !!\nPremi INVIO per continuare...")
        Search_Prov_Comune(db)
    if (len(rispP) == 0):
        req="SELECT * from CAP where Comune Like '%"+rispC.upper()+"%';"
    else:
        req="SELECT * from CAP where Prov='" + rispP.upper() +"' and Comune Like '%"+rispC.upper()+"%' Order By Prov;"
    c=db.cursor()
    c.execute(req)

    d=c.fetchall()
    if (len(d)==0):
        input("\nRecord inesistente !!!\nPremi INVIO per continuare...")
        sel=99
    else:
        sel=100

    while (sel != 99):
        displ_rec(d)
        try:
            sel=int(input('\n\nDigita 99 per uscire '))
        except:
            print("\nDevi dare un valore numerico !!")
            sel=100
        if (sel==99):
            break

        selval=""
        upd=1




#***************************************************
intesta()


try:
	db = sqlite3.connect(database="cap.db")
except:
    print("")
    print("")
    print("*** Attenzione !!!")
    print("")
    print("Connessione al database CAP fallito !!")
    print("Verifica la presenza del databasee si riprova. ")
    print("")
    print("")
    sys.exit(-2)

c=db.cursor()
risp=0

while(risp != 4):
    risp=menu()
    if (risp==1):
       Search_Cap(db)
    if (risp==2):
       Search_Comune(db)
    if (risp==3):
        Search_Prov_Comune(db)
    if (risp==4):
        print("\n\nFine sessione.")
        sys.exit(0)

