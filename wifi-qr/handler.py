import sys
import json
import wifi_qrcode_generator.generator
import base64
from io import BytesIO

def handle(event, context):
    # clientdata_dict = json.loads(event.body)
    clientdata_dict = event.query 
    try:
        ssid = clientdata_dict['ssid']
        password = clientdata_dict['password']
    except Exception as e:
        sys.stderr.write(str(e))
        return {
            "statusCode": 400,
            "body": str(e)
        }

    auth = clientdata_dict.get('auth', 'WPA')
    hidden = clientdata_dict.get('hidden', 'false')

    qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
        ssid=ssid, hidden=hidden, authentication_type=auth, password=password
    )

    img = qr_code.make_image()

    buffered = BytesIO()
    img.save(buffered)
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    return {
        "statusCode": 200,
        "body": f'<img src=data:image/png;base64,{img_str}>',
    }
