# anomaly_detector.py
import pickle
from pathlib import Path
from sklearn.preprocessing import LabelEncoder

class AnomalyDetector:
    def __init__(self, model_path):
        with open(model_path, 'rb') as model_file:
            self.model = pickle.load(model_file)
        # Initialize label encoders for categorical features
        self.protocol_encoder = LabelEncoder()
        self.service_encoder = LabelEncoder()
        self.flag_encoder = LabelEncoder()
        # Fit the encoders with the original training data categories
        # These categories should match those used during training
        self.protocol_encoder.fit(['tcp', 'udp', 'icmp'])
        self.service_encoder.fit(['http', 'ftp', 'smtp'])
        self.flag_encoder.fit(['SF', 'S0', 'REJ'])

    def preprocess(self, data):
        # Assume data format: [protocol, service, flag, feature1, feature2, ..., featureN]
        protocol, service, flag, *features = data
        protocol = self.protocol_encoder.transform([protocol])[0]
        service = self.service_encoder.transform([service])[0]
        flag = self.flag_encoder.transform([flag])[0]
        return [protocol, service, flag] + features

    def predict(self, data):
        processed_data = self.preprocess(data)
        return self.model.predict([processed_data])[0]
