def missedLectures(numChapters, b, e):
   
    daysOut = e - b + 1
    fullCycles = daysOut // numChapters
    remainingDays = daysOut % numChapters
    
    if fullCycles > 0:
        return numChapters
    else:
        startChapter = b % numChapters
        e = (b + remainingDays - 1) % numChapters
        if e < b:
            e += numChapters
        return e - b + 1

print(missedLectures(5, 13, 98))