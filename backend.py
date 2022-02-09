from tkinter.tix import Form
import boto3
from decouple import config
def searchNdownolad(realfilename):
    session = boto3.Session(
        aws_access_key_id=config("ACCESS_KEY_ID"),
        aws_secret_access_key=config("SECRET_ACCSESS_KEY")
    )

    #session.resource('s3').Bucket('maor-bucket-1').download_file('Lionel_Messi.jpeg','Lionel_Messi.jpeg')
    maorb = session.resource('s3').Bucket('maor-bucket-1')

    for my_bucket_object in maorb.objects.all():
        filename = my_bucket_object.key 
        if realfilename in filename :
            x=filename
    if 'x' in locals():        
        maorb.download_file(x,realfilename)
    else:
        print('didnt exist')   