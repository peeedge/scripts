import sys
import base64

# print(base64.b64encode(.encode))
string = sys.argv[1]
data = base64.b64encode(string.encode())
print(data)