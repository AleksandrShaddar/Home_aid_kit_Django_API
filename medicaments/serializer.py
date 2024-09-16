from rest_framework import serializers
from medicaments.models import Medicament


class MedicamentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Medicament
        fields = [
            'url', 'id', 'name', 'quantity', 'expiration_date', 'instruction',
            'type_medicament', 'category_medicament', 'owner'
        ]


