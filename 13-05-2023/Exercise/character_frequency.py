with open("/home/ananta/Desktop/Python-for-Geographers-v0.1/13-05-2023/Exercise/speech.txt", "r") as file:
    line = file.readlines()
# file = open('/home/ananta/Desktop/Python-for-Geographers-v0.1/13-05-2023/Exercise/speech.txt', 'r')
# line = open("speech.txt", "r").read()

for word in file:
    words = word.split()