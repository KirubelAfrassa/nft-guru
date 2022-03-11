from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response

from .api.serializers import ImageSerializer, LayerSerializer
from .models import Image, Layer


class LayerImageList(generics.ListCreateAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer
    parser_classes = (MultiPartParser, JSONParser)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if isinstance(request.data.get("data"), list):
            serializer = self.get_serializer(data=request.data.get("data"), many=True)
        else:
            serializer = self.get_serializer(data=request.data.get("data"))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


@csrf_exempt
def image_list(request):
    """
    List all code images, or create a new image.
    """
    if request.method == "GET":
        layers = Layer.objects.all()
        serializer = LayerSerializer(layers, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = LayerSerializer(data=data.get("data"), many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def image_detail(request, pk):
    """
    Retrieve, update or delete a code image.
    """
    try:
        image = Image.objects.get(pk=pk)
    except Image.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = ImageSerializer(image, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
