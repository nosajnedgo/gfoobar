# Challenge: http://pastebin.com/Breq7mRZ

def answer(x):
    trains = len(x)
    rabbits = sum(x)
    if rabbits % trains == 0:
        return trains
    else:
        return trains - 1
