import pickle

class PresentationLayer:
    def send(self, data):
        encoded_data = pickle.dumps(data)
        print(f"[PRESENTATION] Encoding data: {encoded_data}")
        return encoded_data
    
    def receive(self, encoded_data):
        decoded_data = pickle.loads(encoded_data)
        print(f"[PRESENTATION] Decoding data: {decoded_data}")
        return decoded_data