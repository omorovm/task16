from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Triangle
from .serializers import TriangleSerializer

@api_view(['GET'])
def get_triangles(request):
    queryset = Triangle.objects.all()
    serializer = TriangleSerializer(queryset, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_triangle(request):
    serializer = TriangleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_perimeter(request, pk):
    try:
        product = Triangle.objects.get(pk=pk)
    except Triangle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TriangleSerializer(product)
    return Response(sum(serializer.data.values())- serializer.data['id'])

@api_view(['PUT', 'PUTCH'])
def update_triangle(request, pk):
    try:
        product = Triangle.objects.get(pk=pk)
    except Triangle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = TriangleSerializer(product, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_triangle(request, pk):
    try:
        product = Triangle.objects.get(pk=pk)
    except Triangle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)