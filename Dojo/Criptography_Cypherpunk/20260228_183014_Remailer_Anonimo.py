# Este código simula o funcionamento de um remailer anônimo, removendo metadados do remetente antes de reenviar uma mensagem. 
# Para fins educacionais, o código utiliza uma função simples que oculta o remetente e simula o envio de uma mensagem anônima. 
# É importante notar que este é um exemplo didático e não deve ser usado para atividades ilegais. 
# Para executar, basta ter Python instalado.

def anonymize_sender(original_sender, message):
    # Simula a remoção de metadados do remetente
    anonymized_sender = "anon@example.com"
    return f"Mensagem de: {anonymized_sender}\nConteúdo: {message}"

# Exemplo de uso
original_sender = "user@example.com"
message = "Esta é uma mensagem confidencial."
anonymized_message = anonymize_sender(original_sender, message)

print(anonymized_message)