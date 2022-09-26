from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def resume_list(request):
    if request.method == 'GET':
        profiles = Profile.objects.all()
        profiles_serializer = ProfileSerializer(profiles, many=True)
        return JsonResponse(profiles_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        # profile_data = JSONParser().parse(request)
        profile_serializer = ProfileSerializer(data=request.data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return JsonResponse(profile_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Profile.objects.all().delete()
        return JsonResponse({'message': '{} Profiles were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def resume_detail(request, pk):
    try: 
        profile = Profile.objects.get(pk=pk) 
    except Profile.DoesNotExist: 
        return JsonResponse({'message': 'The Profile does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        profile_serializer = ProfileSerializer(profile) 
        return JsonResponse(profile_serializer.data) 
 
    elif request.method == 'PUT': 
        profile_serializer = ProfileSerializer(profile, data=request.data) 
        if profile_serializer.is_valid(): 
            profile_serializer.save() 
            return JsonResponse(profile_serializer.data) 
        return JsonResponse(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        profile.delete() 
        return JsonResponse({'message': 'Profile was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
