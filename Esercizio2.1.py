#Creare un dizionario config con le seguenti coppie:
#"host": "192.168.1.1"
#"port": 8080
#"ssl": True
#"timeout": 30

#Stampare il valore di "host"
#Modificare "port" in 443
#Aggiungere una nuova chiave "protocol" con valore "https"
#Stampare il dizionario completo


config : dict [str, str | bool | int]= {
    "host" : "192.168.1.1",
    "port" : 8080,
    "ssl" : True,
    "timeout" : 30
}

print(f"Host ha come valore: {config["host"]}")
config["port"]=443
config["protocol"]= "https"

print(config)