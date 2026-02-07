# Este código gera um Identificador Descentralizado (DID) e seu documento associado. 
# O DID é uma nova forma de identidade digital que permite que indivíduos possuam e controlem suas próprias identidades sem depender de uma autoridade central. 
# Para executar este código, você precisará instalar a biblioteca `didkit`. 
# Instale-a usando: pip install didkit

import didkit

# Gerar um novo DID
did_document = didkit.key_create("Ed25519")
did = did_document["id"]

# Exibir o DID e seu documento
print("DID:", did)
print("DID Document:", did_document)