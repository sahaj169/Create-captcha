from captcha.image import ImageCaptcha
import random

image = ImageCaptcha()

# This will give a random 7 letter word with 3 capital letters 2 small letters and 2 numerical values
capitalletterList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
smallletterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k','l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
randomthreeBigLetter = random.choices(capitalletterList, k=3)
randomtwosmallLetter = random.choices(smallletterList, k=2)
randomtwonumber = random.choices(numberList, k=2)
listrandom = randomthreeBigLetter + randomtwosmallLetter + randomtwonumber
random.shuffle(listrandom)
captcha = ("".join(listrandom))
print(f"The Captcha is: {captcha}")

image_data = image.generate(captcha)
image.write(captcha,'captcha.png')


#generate audio captcha
from captcha.audio import AudioCaptcha

audio = AudioCaptcha()

#this will give 2 random integers
randomtwoint = random.choices(numberList, k=2)
twoint = ("").join(randomtwoint)
print(f"The Audio Captcha is: {twoint}")

audio_data = audio.generate(str(twoint))
audio.write(str(twoint),'audioCaptcha.wav')




