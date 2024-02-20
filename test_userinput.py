from web3 import Web3
from web3.utils.address import to_checksum_address
from web3.middleware import construct_sign_and_send_raw_middleware

#private key
pk="e4f79293e46ec96e49cf7fd1869289e4e380dcc1f72a94d4f6ae3fe5e189b77d"

# Inizializza una lista vuota
dati_utente = []


#configurazione istanza web3 con il provider di ethereum
w3 = Web3(Web3.HTTPProvider('https://sepolia.infura.io/v3/8d9e9b18ae704ff8baef4a9e29458531'))

account= w3.eth.account.from_key(pk)
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
# Indirizzo e ABI del tuo contratto
contract_address_non_checksum = '0x8c45a22d770dfdfb9cf758c4f42c67f251aa13ad'

# Converti l'indirizzo in formato checksum
contract_address_checksum = to_checksum_address(contract_address_non_checksum)

contract_abi = '[{"inputs": [{"internalType": "uint256","name": "_percentuale1","type": "uint256"},{"internalType": "uint256","name": "_percentuale2","type": "uint256"},{"internalType": "uint256","name": "_percentuale3","type": "uint256"},{"internalType": "string","name": "_materiale1","type": "string"},{"internalType": "string","name": "_materiale2","type": "string"},{"internalType": "string","name": "_materiale3","type": "string"},{"internalType": "string","name": "_brand","type": "string"},{"internalType": "uint256","name": "_codiceSeriale","type": "uint256"}],"name": "caricaProdottoIniziale","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "uint256","name": "_idProdottoIniziale1","type": "uint256"},{"internalType": "uint256","name": "_idProdottoIniziale2","type": "uint256"},{"internalType": "uint256","name": "_idProdottoIniziale3","type": "uint256"},{"internalType": "uint256","name": "_percentuale1","type": "uint256"},{"internalType": "uint256","name": "_percentuale2","type": "uint256"},{"internalType": "uint256","name": "_percentuale3","type": "uint256"},{"internalType": "string","name": "_materiale1","type": "string"},{"internalType": "string","name": "_materiale2","type": "string"},{"internalType": "string","name": "_materiale3","type": "string"},{"internalType": "string","name": "_brand","type": "string"},{"internalType": "uint256","name": "_codiceSeriale","type": "uint256"}],"name": "generaProdottoFinale","outputs": [{"internalType": "string","name": "","type": "string"}],"stateMutability": "nonpayable","type": "function"},{"inputs": [{"internalType": "uint256","name": "_id","type": "uint256"}],"name": "trovaProdottoFinale","outputs": [{"internalType": "uint256[3]","name": "","type": "uint256[3]"},{"internalType": "string[3]","name": "","type": "string[3]"},{"internalType": "string","name": "","type": "string"},{"internalType": "uint256","name": "","type": "uint256"},{"internalType": "uint256[3]","name": "","type": "uint256[3]"}],"stateMutability": "view","type": "function"},{"inputs": [{"internalType": "uint256","name": "_id","type": "uint256"}],"name": "trovaProdottoIniziale","outputs": [{"internalType": "uint256[3]","name": "","type": "uint256[3]"},{"internalType": "string[3]","name": "","type": "string[3]"},{"internalType": "string","name": "","type": "string"},{"internalType": "uint256","name": "","type": "uint256"}],"stateMutability": "view","type": "function"}]'

# Carica il contratto utilizzando l'indirizzo checksum
contract = w3.eth.contract(address=contract_address_checksum, abi=contract_abi)

#Richiesta dati utente
percentuale1 = int(input("Inserisci la % del primo materiale").rstrip('%'))
percentuale2 = int(input("Inserisci la % del secondo materiale").rstrip('%'))
percentuale3 = int(input("Inserisci la % del terzo materiale").rstrip('%'))
materiale1 = input("Inserisci la prima tipologia di tessuto")
materiale2 = input("Inserisci la seconda tipologia di tessuto")
materiale3 = input("Inserisci la terza tipologia di tessuto")
brand = input ("Inserisci il brand")
codiceseriale = int(input ("Inserisci il codice seriale del prodotto"))

"""percentuale1 = Web3.toUnsigned(int(percentuale1))
percentuale2 = Web3.toUnsigned(int(percentuale2))
percentuale3 = Web3.toUnsigned(int(percentuale3))
materiale1 = str(materiale1)
materiale2 = str(materiale2)
materiale3 = str(materiale3)
codiceseriale = Web3.toUnsigned(int(codiceseriale))"""

# Ora hai i dati convertiti che possono essere utilizzati nel contratto
# Aggiungi i dati convertiti alla lista dei dati utente
#dati_utente.extend([percentuale1_encoded, percentuale2_encoded, percentuale3_encoded, materiale1, materiale2, materiale3, brand, codiceseriale_encoded])

# Salva i dati in una lista
dati_utente = [percentuale1, percentuale2, percentuale3, materiale1, materiale2, materiale3, brand, codiceseriale]
print("Dati acquisiti:", dati_utente)
#print
#print("Il materiale è composto dai seguenti tessuti: "
   #   + materiale1 + ", " + materiale2 + ", " + materiale3 + ", nelle rispettive %: " 
   #   + percentuale1 + ", " + percentuale2 + ", " + percentuale3)


# Esegui la transazione verso lo smart contract
contract.functions.caricaProdottoIniziale(
    int(percentuale1), int(percentuale2), int(percentuale3),
    str(materiale1), str(materiale2), str(materiale3),
    str(brand), int(codiceseriale)
).transact({"from":account.address})

print("Transazione completata con successo!")

"""# Configure w3, e.g., w3 = Web3(...)
address = '0x1f9840a85d5aF5bf1D1762F925BDADdC4201F988'
abi = '[{"inputs":[{"internalType":"address","name":"account","type":"address"},{"internalType":"address","name":"minter_","type":"address"},...'
contract_instance = w3.eth.contract(address=address, abi=abi)

# read state:
contract_instance.functions.storedValue().call()
# 42

# update state:
tx_hash = contract_instance.functions.updateValue(43).transact() """



