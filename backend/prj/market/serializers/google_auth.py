from rest_framework import serializers

class GoogleAuthRequestSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    email = serializers.CharField()
    photoUrl = serializers.CharField()
    firstName = serializers.CharField()
    authToken = serializers.CharField()
    provider = serializers.CharField()
    socket_id = serializers.CharField()

    