import base64

message = "3d3d516343746d4d6d6c315669563362"

message = bytes.fromhex(message)
decodedbase = base64.b64decode(message[::-1])
final = decodedbase.decode('ascii')
print(final)