from rest_framework import serializers

from boutique.models import Boutique


class BoutiqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boutique
        fields = "__all__"

    # def validate(self, data):
    #     if data['name']:
    #         if Boutique.objects.filter(name=data['name']).exists():
    #             raise serializers.ValidationError('name exists')
    #     return data

    # def create(self, validated_data):
    #     boutique = Boutique.objects.create(**validated_data)
    #     boutique.save()
    #     return validated_data


