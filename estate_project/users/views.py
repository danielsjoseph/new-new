from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import *

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def houses(request):
    house = Apartments.objects.filter(is_available__icontains='Available')
    
    looking_to = request.query_params.get('looking-to')
    looking_for = request.query_params.get('looking-for')
    if looking_to=="rent":
        house = house.filter(looking_for__icontains='Rent')
    if looking_to=="buy":
        house = house.filter(looking_for__icontains='Sale')
    if looking_for=="duplex":
        house = house.filter(property_type__icontains='duplex')
    if looking_for=="land":
        house = house.filter(property_type__icontains='land')
    if looking_for=="bungalow":
        house = house.filter(property_type__icontains='bungalow')
    if looking_for=="apartments":
        house = house.filter(property_type__icontains='apartments')
    if request.method=="GET":
        serializer = ApartmentsSerializer(house,many=True)
        return Response(serializer.data)
    if request.method=="POST":
        check = request.user
        if check.is_agent==True:
            serializer = ApartmentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        return Response('You are not an agent')    
    


@api_view(['GET'])
@permission_classes([AllowAny])
def house_details(request,slug):
    house = Apartments.objects.get(slug=slug)
    serializer = ApartmentsSerializer(house,many=False)
    if request.method=="GET":
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def agent_details(request,slug):
    agent = AgentProfile.objects.get(slug=slug)
    serializer = AgentSerializer(agent,many=False)
    if request.method=="GET":
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET','POST',])
@permission_classes([IsAuthenticated])
def userProfile(request):
    check = request.user
    user = User.objects.get(slug=check.slug)
    userprofile = UserProfile.objects.get(slug=check.slug)
    serializer = UsersSerializer(user,many=False)
    serializer2= ProfileSerializer(userprofile,many=False)
    if request.method=="GET":
        return Response([serializer.data,serializer2.data])
    elif request.method=="POST":
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response([serializer.data,serializer2.data])
    return Response(serializer.errors)

# @api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated,])
# def userProfile(request):
#     current_user = User

@api_view(["GET","POST",])
@permission_classes([IsAuthenticated])
def agentProfile(request):
    check = request.user
    user = User.objects.get(slug=check.slug)
    userprofile = AgentProfile.objects.get(slug=check.slug)
    serializer = UsersSerializer(user,many=False)
    serializer2= ProfileSerializer(userprofile,many=False) # Prosper changed this from UsersSerializer to ProfileSerializer
    if request.method=="GET":
        return Response([serializer.data,serializer2.data])
    elif request.method=="POST":
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["GET"])
@permission_classes([IsAdminUser])
def allusers(request):
    users = User.objects.all()
    serializer = UsersSerializer(users,many=True)
    if request.method=="GET":
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def allagents(request):
    users = User.objects.filter(is_agent=True)
    serializer = UsersSerializer(users,many=True)
    if request.method=="GET":
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.method=="POST":
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
 
