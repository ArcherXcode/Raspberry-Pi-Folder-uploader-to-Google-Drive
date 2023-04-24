from googleapiclient.http import MediaFileUpload
from Google import Create_Service

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# Upload a file
file_metadata = {
    'name': '%d.jpg',
    'parents': ['1TB3f9-BFmtoPGguvXWd_gBBKZHKO9mQi']
}

media_content = MediaFileUpload('/home/pi/Desktop/Drive/Images/Apple_%d.jpg', mimetype='image/jpg')

file = service.files().create(
    body=file_metadata,

    media_body=media_content
).execute()

print(file)


# Replace Existing File on Google Drive
#file_id = '<file id>'

#media_content = MediaFileUpload('mp4.png', mimetype='image/png')

#service.files().update(
    #fileId=file_id,
    #media_body=media_content
#).execute()
