import requests

def check(crypto):
	reponse = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto+"&tsyms=EUR")
	print(reponse.text)

print("Bonjour\n")
print("Quelle est votre soeur ?\n")
valeur = input("Entre un nom: \n")
check(valeur)