# Challenge: http://pastebin.com/JUKqQTeG

def answer(digest):
    output = [0] * 16
    for i in range(len(digest)):
        if i == 0:
            output[i] = lookup(digest[i], 0)
        else:
            output[i] = lookup(digest[i], output[i-1])
    return output
    
def lookup(curr, prev):
    for i in range(256):
        if (129*i ^ prev) % 256 == curr:
            return i;
    raise Exception("Solution not found.")
