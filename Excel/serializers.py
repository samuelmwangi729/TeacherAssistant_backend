from rest_framework import serializers



class ExcelSerializer(serializers.Serializer):
    class Meta:
        fields =['file']
    file = serializers.FileField(required=True)