### HackaVision

Hackavision is a python based visually impaired helper. It uses computer vision to help identify people and objects for those who are visually impaired.

#### Installation
* `git clone`
* `virtualenv <your-env-name>`
* `source <your-env-name>/bin/activate`
* `pip3 install -r requirements.txt`

#### Running
* Add aws credentials. To learn [see here](https://boto3.readthedocs.io/en/latest/guide/configuration.html#guide-configuration)
* `python3 hackavision.py`
* The program will open a window where you can see a preview of the image before taking it
* press spacebar to snap an image
* press ESC to quit
* Upon pressing spacebar, the program will take a photo of you and, ideally, respond with what age range it thinks you are in! More to come soon.