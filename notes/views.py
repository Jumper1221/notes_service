from functools import partial
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer


class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class NoteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    lookup_field = "id"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        if not any([field in data for field in ["title", "content"]]):
            return Response(
                {"detail": "One field or mo must be providet"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        partial = kwargs.pop("partial", False)
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
