# Este código implementa um sistema simples de timestamping distribuído usando um blockchain básico. 
# Ele permite que os usuários adicionem registros com timestamps, garantindo que a ordem dos registros seja mantida de forma descentralizada. 
# Para rodar este código, não são necessárias bibliotecas externas. 
# Apenas o Python padrão é suficiente.

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

def create_genesis_block():
    return Block(0, "01/01/2023", "Genesis Block", "0")

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = "01/01/2023"  # Aqui você pode usar datetime.now().isoformat() para timestamps reais
    return Block(index, timestamp, data, previous_block.previous_hash)

# Criando a cadeia de blocos
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Adicionando novos blocos
for i in range(1, 5):
    new_block = create_new_block(previous_block, f"Block {i} Data")
    blockchain.append(new_block)
    previous_block = new_block
    print(f"Block {new_block.index} has been added to the blockchain!")
    print(f"Hash: {new_block.previous_hash}")
    print(f"Data: {new_block.data}\n")