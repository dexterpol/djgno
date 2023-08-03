from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from .models import Nota

@csrf_exempt
def receber_mensagem(request):
    if request.method == 'POST':
        mensagem = request.POST.get('Body')
        remetente = request.POST.get('From')
        media_url = request.POST.get('MediaUrl0')
        response = MessagingResponse()
        
        if mensagem.lower() == 'oi':
            response.message("Olá! Deseja cadastrar uma nota? Responda 'sim' ou 'não'.")
        
        elif mensagem.lower() == 'sim':
            response.message("Ótimo! Por favor, envie o valor da nota .")
        
       
        elif 'valor:' in mensagem.lower():
            valor_material = mensagem.split('valor:')[-1].strip()
            response.message("Obrigado! Agora, digite a descrição da nota.")
            
            # Salvar temporariamente o valor em um campo para a nota em andamento
            request.session['valor_material_temp'] = valor_material
            
        elif 'descricao:' in mensagem.lower():
            
            
            descricao_nota = mensagem.split('descricao:')[-1].strip()
            
            
            valor_material = request.session.get('valor_material_temp', None)
            
            # Salvar a nota completa no banco de dados
            nota = Nota(valor_material=valor_material, descricao=descricao_nota)
            nota.save()
            
           
            request.session.pop('valor_material_temp', None)
            
            response.message("Nota cadastrada com sucesso! Obrigado.")
        
        else:
            response.message("Desculpe, não entendi. Por favor, diga 'oi' para começar o cadastro da nota.")

        # Retornar a resposta para o Twilio
        return HttpResponse(str(response))
    
    return HttpResponse('Método GET não suportado.')
