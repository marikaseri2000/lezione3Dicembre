
#Creare una lista server contenente: ["web01", "db01", "cache01"]
#Aggiungere "backup01" alla fine
#Inserire "proxy01" all'inizio (indice 0)
#Rimuovere "cache01"
#Stampare la lista finale e la sua lunghezza

server :list[str]=["web01","db01","cache01"]
server.append("backup01")
server.insert(0, "proxy01")
#server.remove("cache01") rimuove il dato 
server.pop(3)
print(server)
print(len(server))