from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import NotYourProfile, ProfileNotFound
from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer, UpdateProfileSerializer


class AgentListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(is_agent=True)
    serializer_class = ProfileSerializer


"""
# Function Based View of Above Class
from rest_framework import api_view, permissions

@api_view(["GET"])
@permission_classes((permissions.IsAuthenticated))
def get_all_agents(request):
    agents = Profile.objects.filter(is_agent=True)
    serializer=ProfileSerializer(agents, many=True)
    name_spaced_response={"agents": serializer.data}
    return Response(name_spaced_response,status=status.HTTP_200_OK)
"""


class TopAgentListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(top_agent=True)
    serializer_class = ProfileSerializer


class GetProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = request.user
        user_profile = get_object_or_404(Profile, user=user)  # Profile.objects.get(user=user)
        serializer = ProfileSerializer(user_profile, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UpdateProfileAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]
    serializer = UpdateProfileSerializer

    def patch(self, request, username):
        user = request.user
        try:
            Profile.objects.get(user__username=username)

        except Profile.DoseNotExist:
            raise ProfileNotFound

        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile

        data = request.data
        serializer = UpdateProfileSerializer(instance=request.user.profile, data=data, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
