from rest_framework import serializers

from ..models import Image, Layer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        exclude = ["creator"]

    def create(self, validated_data):
        return Image.objects.create(**validated_data)


# class LayerListSerializer(serializers.ListSerializer):
#     images = serializers.PrimaryKeyRelatedField(many=True, queryset=Image.objects.all(), write_only=True)
#     image_set = ImageSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Layer
#         fields = ['layerName', 'image_set', 'images']
#
#     def create(self, validated_data):
#         # reqImages = validated_data.pop('images')
#
#         # imageReqData = {'images': requestData['images'][0]}
#
#         # imageSerializer = ImageSerializer(data=validated_data['images'])
#         # if imageSerializer.is_valid():
#         #     imageSerializer.save()
#
#         global layers
#         for item in validated_data.pop('data'):
#             image = item.pop('images')
#             layers = [Layer.objects.create(**item)]
#             Image.objects.create(**image)
#             # self.images.add(image)
#             # self.images.
#             # layers = [Layer(**item)]
#         # imageList = [Image(**image) for image in reqImages]
#
#         # layers = [Layer(**item) for item in validated_data.pop('data')]
#
#
#         return Layer.objects.bulk_create(layers)


class LayerSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Layer
        fields = ["layerName", "images"]

    def create(self, validated_data):
        reqImages = validated_data.pop("images")
        imageList = [Image(**image) for image in reqImages]

        layer = Layer.objects.create(**validated_data)

        images = [
            Image(layer_id=layer.pk, imageName=image.imageName)
            # for layer in layers
            for image in imageList
        ]
        Image.objects.bulk_create(images)
        return layer
