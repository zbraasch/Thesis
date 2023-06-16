# $ pip install cloudsight==0.9.2

# Import the cloudsight package:
import cloudsight

print("\n")

# Create an API instance using simple key-based authentication:
auth = cloudsight.SimpleAuth('')
api = cloudsight.API(auth)

# Send the image request using a file:
fileName = "Data\\Raw\\Cat\\1-2.jpg"
with open(fileName, 'rb') as f:
    response = api.image_request(f, fileName, {
        'image_request[locale]': 'en-US',
    })
    print("Sent file: " + fileName)

#Or, you can send the image request using a URL:
"""
response = api.remote_image_request('http://www.example.com/image.jpg', {
    'image_request[locale]': 'en-US',
})
"""

# Then, update the job status to see if it's already processed:
# It usually takes 6-12 seconds to receive a completed response. You may use wait() method to wait until the image is processed:
status = api.wait(response['token'], timeout=30)
status = api.image_response(response['token'])
#print(status)
if status['status'] != cloudsight.STATUS_NOT_COMPLETED:
    # Done!
    print("Response: " + status['name'] + "\n")
    print()
    pass
