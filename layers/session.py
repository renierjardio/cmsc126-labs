import json
import base64

class SessionLayer:
    def send(self, data):
        if isinstance(data, bytes):
            data = base64.b64encode(data).decode('utf-8')
        session = {'Session_ID': 12345, 'Data': data}
        print(f"[SESSION] Managing session: {session}")
        return json.dumps(session)
        
    def receive(self, session):
        session_data = json.loads(session)
        print(f"[SESSION] Handling session: {session_data}")
        data = session_data['Data']
        try:
            data = base64.b64decode(data.encode('utf-8'))
        except (base64.binascii.Error, UnicodeDecodeError):
            pass
        return data