# Challenge: http://pastebin.com/h8q48xqA

def answer(chunk, word):
    length = len(word)
    overlaps = findOverlaps(chunk, word, length)
    best = chunk
    for start in overlaps:
        test = answer(removeString(chunk, start, length), word)
        if len(test) < len(best) or test < best:
            best = test
    return best

def findOverlaps(string, word, length):
    output = []
    for i in range(len(string)-length+1):
        if string[i:i+length] == word:
            if not output:
                output.append(i)
            elif output[-1]+length > i:
                output.append(i)
    return output

def removeString(string, index, length):
    if index == 0:
        return string[length:]
    else:
        return string[0:index] + string[index+length:]