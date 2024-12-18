from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import serializers
from apps.blog.models import Preference, Slideshow, Navbar


class SlideshowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slideshow
        fields = ['id', 'title', 'image', 'link', 'order', 'preference']
                

class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = ['id', 'title', 'link', 'icon', 'order', 'preference']


class PreferenceSerializer(serializers.ModelSerializer):
    slideshows = SlideshowSerializer(many=True, read_only=True)
    navbars = NavbarSerializer(many=True, read_only=True)    
    class Meta:
        model = Preference
        fields = [
            'id', 
            'site_title', 
            'site_subtitle', 
            'site_description', 
            'site_logo', 
            'site_favicon', 
            'contact_email', 
            'contact_phone', 
            'slideshows', 
            'navbars'
        ]
        read_only_fields = ['id']


        
class PreferenceViewSet(ModelViewSet):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]