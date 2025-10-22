from rest_framework.views import APIView
from .serializers import ExcelSerializer
from rest_framework.response import Response
from rest_framework import status
from Excel.utils import extract_xlsx
# Create your views here.
class ExcelFile(APIView):
    serializer_class = ExcelSerializer


    def post(self,request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            file = serializer.validated_data['file']
            formulas = extract_xlsx(file)
            return Response({
                "status":"success",
                "data":formulas
                },status=status.HTTP_200_OK)
        return Response({
                "status":"error",
                "data":serializer.errors
                },status=status.HTTP_400_BAD_REQUEST)