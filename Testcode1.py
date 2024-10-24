def getTime(s):
    total_time = 0
    current_position = 0
    for char in s:
        target_position = ord(char) - ord('A')
        distance = min(abs(target_position - current_position), 26 - abs(target_position - current_position))
        total_time += distance
        current_position = target_position
    return total_time

print(getTime("AZGB"))  # Output: 13
print(getTime("ZNMD"))  # Output: 23