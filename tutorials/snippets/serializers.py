from .models import Snippet,languages_choice,styles_choices
from rest_framework import serializers

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id','title','code','linenos','language','style']