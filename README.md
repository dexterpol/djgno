

Desenvolvi um sistema usando o framework Django para possibilitar o cadastro de notas atrasadas por meio do WhatsApp. O projeto utiliza a API do Twilio para integração com o WhatsApp e o Ngrok para criar um servidor temporário. Aqui está um resumo dos principais aspectos:

Tecnologias Utilizadas:

Framework Django para desenvolvimento web.
API do Twilio para comunicação com o WhatsApp.
Ngrok para criação de um servidor temporário.
Funcionalidades do Sistema:

Página de cadastro de notas atrasadas no sistema Django.
Integração com o WhatsApp para permitir que os usuários enviem informações.
Respostas automáticas para as mensagens recebidas, fornecendo feedback imediato aos usuários.
Fluxo de Funcionamento:

Os usuários enviam mensagens via WhatsApp para o número configurado.
O Twilio encaminha as mensagens para o servidor Django usando o Ngrok.
O servidor Django processa as mensagens, extrai informações (notas atrasadas) e envia respostas automáticas.
Configurações Necessárias:

Credenciais do Twilio (SID da conta e token de autenticação) para interagir com a API.
Configuração de um número de WhatsApp no painel do Twilio.
Uso do Ngrok para criar um túnel e direcionar as mensagens para o servidor Django.
Testes e Uso:

Execute o servidor Django localmente.
Inicie o Ngrok para permitir o acesso externo.
Envie mensagens para o número de WhatsApp configurado e observe as respostas automáticas.
