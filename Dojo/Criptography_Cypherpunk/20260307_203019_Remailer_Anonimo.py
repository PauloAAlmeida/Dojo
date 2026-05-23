# Este código simula um remailer anônimo simples que remove metadados do remetente. 
# Ele usa a biblioteca smtplib para enviar e-mails. 
# Para rodar este código, você precisa ter acesso a um servidor SMTP. 
# Instale a biblioteca necessária com: pip install secure-smtplib

import smtplib
from email.mime.text import MIMEText

def enviar_email(destinatario, assunto, corpo):
    remetente = "seu_email@example.com"
    senha = "sua_senha"

    msg = MIMEText(corpo)
    msg['Subject'] = assunto
    msg['From'] = remetente
    msg['To'] = destinatario

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(remetente, senha)
        server.sendmail(remetente, destinatario, msg.as_string())
        print(f'E-mail enviado para {destinatario}')

# Exemplo de uso
enviar_email("destinatario@example.com", "Teste de Remailer", "Este é um e-mail enviado de forma anônima.")