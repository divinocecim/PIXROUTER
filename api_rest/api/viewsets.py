from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api_rest.models import Chavespix, Enviapix
from .serializers import EnviapixSerializer, ChavepixSerializer

import json

def get_vinculo_pix_key(pix_key):
    global resposta

    print(pix_key)
    try:
        titular = Chavespix.objects.get(pk=pix_key)
        resposta = True
    except:
        titular = ''
        resposta = False
        
    print(f'Titular retornado: {titular}')
    print(f'Segunda resposta: {resposta}')
    return Response(resposta)
   
@api_view(['GET'])
def get_all_pix(request):

    if request.method == 'GET':

        registros = Enviapix.objects.all()                      # Get all objects in Enviapix's database (It returns a queryset)

        serializer = EnviapixSerializer(registros, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)                    # Return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_textid(request, textid):

    try:
        trans_pix = Enviapix.objects.get(pk=textid)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = EnviapixSerializer(trans_pix)
        return Response(serializer.data)


@api_view(['POST','PUT'])
def pix_manager(request):
# CRIANDO DADOS
    if request.method == 'POST':
       
        chave_pix = request.data['chavepix']
        dados = request.data 
        
        print(f'Antes da chamada: {chave_pix}')
        vinculo = get_vinculo_pix_key(chave_pix) 
        print(f'Status_code: {vinculo.status_code}')
        print(f'Terceira resposta: {resposta}')
        
        if resposta:
            print('Vou serializar os dados')
            serializer = EnviapixSerializer(data=dados)
            
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response('Chave PIX ',status=status.HTTP_404_NOT_FOUND)
#    else:
#        return Response(status=status.HTTP_400_BAD_REQUEST)
    
# BUSCANDO HISTORICO PIX
    if request.method == 'PUT':
        pix_trans = request.data['idtrans']
        try:
            updated_trans = Enviapix.objects.get(pk=pix_trans)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EnviapixSerializer(updated_trans, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def pix_delete(request):
    if request.method == 'DELETE':
        try:
            user_to_delete = Enviapix.objects.get(pk=request.data['idtrans'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)   
            
@api_view(['GET']) 
def get_all_keys(request):
    if request.method == 'GET':
        chaves_pix = Chavespix.objects.all()
        serializer = ChavepixSerializer(chaves_pix, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)   
    
    return Response(status=status.HTTP_400_BAD_REQUEST)          