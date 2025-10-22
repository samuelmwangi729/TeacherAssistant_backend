from rest_framework.views import APIView
from rest_framework import status,response
from Word.serializer import WordSerializer
from Word.utils import extract_styles
# Create your views here.
class WordView(APIView):
    serializer_class=WordSerializer


    def post(self,request):

        data = request.data 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            styles = extract_styles(file)
            return response.Response({
                "status":"success",
                "message":"extracted the styles",
                "data":styles
                },status=status.HTTP_200_OK)
        return response.Response({
            "status":"error",
            "message":serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)