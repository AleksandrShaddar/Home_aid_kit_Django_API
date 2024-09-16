from django.shortcuts import render
from rest_framework import viewsets, permissions
from medicaments.models import Medicament
from medicaments.serializer import MedicamentSerializer


# Create your views here.

class MedicamentViewSet(viewsets.ModelViewSet):
    serializer_class = MedicamentSerializer
    queryset = Medicament.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Medicament.objects.filter(owner=self.request.user.id)
