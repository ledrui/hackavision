import boto3
import cv2
import json
from pygame import mixer
from contextlib import closing

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

def addFace(img_name, img_counter):
    with open(img_name, 'rb') as image:
        client = boto3.client('rekognition','us-west-2')
        #response = client.detect_labels(Image={'Bytes': image.read()})
        response = client.detect_faces(Image={'Bytes': image.read()}, Attributes=['ALL'])
        # for label in response['Labels']:
        #     print(label)
        #     print (label['Name'] + ' : ' + str(label['Confidence']))
        results = []
        for face_detail in response['FaceDetails']:
            results.append('The detected face is between ' + str(face_detail['AgeRange']['Low']) + ' and ' + str(face_detail['AgeRange']['High']) + ' years old')
            print(results)
            print('Here are the other attributes:')
            print(json.dumps(face_detail, indent=4, sort_keys=True))
        polly = boto3.client('polly', 'us-west-2')
        voice = polly.synthesize_speech(Text=results[0], OutputFormat="mp3", VoiceId="Joanna", TextType="text")
        with closing(voice['AudioStream']) as stream:
            output = "speech_{}.mp3".format(img_counter)
            try:
                with open(output, "wb") as file:
                    file.write(stream.read())
                    mixer.init()
                    mixer.music.load(output)
                    mixer.music.play()
            except IOError as error:
                print(error)
                sys.exit(-1)



img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        addFace(img_name, img_counter)

cam.release()

cv2.destroyAllWindows()
