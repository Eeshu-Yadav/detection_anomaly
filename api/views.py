# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import DetectionData
from .serializers import DetectionDataSerializer
from .anomaly import AnomalyDetector
from pathlib import Path

@api_view(['POST'])
def create_detection_data(request):
    serializer = DetectionDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data_instance = serializer.instance

        # Load the model and make the prediction
        model_path = Path('model.pkl')  # Adjust the path if necessary
        detector = AnomalyDetector(model_path)

        data = [
            data_instance.protocol,
            data_instance.service,
            data_instance.flag,
            data_instance.src_bytes,
            data_instance.dst_bytes,
            data_instance.count,
            data_instance.same_srv_rate,
            data_instance.diff_srv_rate,
            data_instance.dst_host_serve_count,
            data_instance.dst_host_same_serve_count
        ]

        try:
            result = detector.predict(data)
            result_text = 'Anomaly detected' if result == 1 else 'No anomaly detected'
            data_instance.result = result_text
            data_instance.save()
            return Response({'result': result_text}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
