# Este código gera um Identificador Descentralizado (DID) e seu documento associado. 
# O DID é uma nova forma de identidade digital que não depende de uma autoridade central. 
# Para executar este código, instale a biblioteca `didkit` usando: 
# pip install didkit
# O código utiliza a biblioteca para criar um DID e um documento simples.

import didkit

# Gerar um novo DID
did = didkit.create_did("key")  # Usando o método de chave para criar um DID

# Criar um documento DID
document = {
    "@context": "https://www.w3.org/ns/did/v1",
    "id": did,
    "publicKey": [{
        "id": f"{did}#keys-1",
        "type": "Ed25519VerificationKey2018",
        "controller": did,
        "publicKeyBase58": "3n7Xy9H3gF4h1Wg1J1j8W1X3d1D1z1B1a1Q1z1A1b1E1F1g1H1j1K1L1M1N1O1"
    }],
    "authentication": [f"{did}#keys-1"]
}

# Imprimir o DID e seu documento
print("DID:", did)
print("Documento DID:", document)