from rest_framework.decorators import api_view

from .models import Todo
from .serializers import TodoSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TodoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        todo = Todo.objects.all()
        serializers = TodoSerializer(todo, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def todoList(request):
    todo = Todo.objects.all()
    serializers = TodoSerializer(todo, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def todoDetail(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def todoUpdate(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def todoDelete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response('Deleted')
