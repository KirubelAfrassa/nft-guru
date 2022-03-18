import os
import sys
from pathlib import Path

from django.http import FileResponse
from rest_framework import status, views
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

UTIL_PATH = str(Path(__file__).resolve(strict=True).parent.parent.parent / "utils")
sys.path.insert(0, UTIL_PATH)

from ...utils.simple_image_merger import merge

path = Path(__file__).resolve(strict=True).parent.parent.parent / "media"
path.mkdir(parents=True, exist_ok=True)
MEDIA_ROOT = str(path)


class Preview(views.APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        files = request.data.getlist("file")

        merged = merge(files)
        if merged:
            img = open(os.path.join(MEDIA_ROOT, "merged.webp"), "rb")
            return FileResponse(img)

        return Response(status=status.HTTP_400_BAD_REQUEST)
