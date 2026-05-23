# Este código demonstra o uso de Tensor Cores da NVIDIA para realizar operações de matriz com precisão mista. 
# Ele utiliza a biblioteca PyTorch, que deve ser instalada com `pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113` 
# para suporte a CUDA. O código cria duas matrizes de precisão mista (float16) e realiza uma multiplicação de matriz, 
# aproveitando a aceleração dos Tensor Cores.

import torch

# Definindo o dispositivo para GPU
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# Criando matrizes de precisão mista
A = torch.rand((1024, 1024), dtype=torch.float16, device=device)
B = torch.rand((1024, 1024), dtype=torch.float16, device=device)

# Multiplicando as matrizes
C = torch.matmul(A, B)

# Convertendo o resultado para float32 para visualização
C_float32 = C.to(torch.float32)

# Imprimindo uma parte do resultado
print(C_float32[0:5, 0:5])