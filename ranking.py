import pickle

def updateRanking(nombre,score):
#Ademas devuelve True si se rompio un record
    try:
        a = open("scores.txt")
        rank = pickle.load(a)
        a.close()
    except:
        nuevoRanking()
        a = open("scores.txt")
        rank = pickle.load(a)
        a.close()
    x = 0
    while rank[x][1]>score and x<9:
        x += 1
    if x<10:
        modificado = True
        rank.pop(x)
        rank.append((nombre,score))
        rank = sorted(rank, key=lambda jugador: jugador[1])
        a = open("scores.txt","w")
        pickle.dump(rank,a)
        a.close()
    else:
        modificado = False
    return modificado

def nuevoRanking():
    lista = []
    for x in range(0,10):
        lista.append(("Libre",0))
    a = open("scores.txt","w")
    pickle.dump(lista,a)
    a.close()

def get_Ranking():
    try:
        a = open("scores.txt")
        lista = pickle.load(a)
        a.close()
    except:
        nuevoRanking()
        lista = get_Ranking()
    finally:
        return lista
