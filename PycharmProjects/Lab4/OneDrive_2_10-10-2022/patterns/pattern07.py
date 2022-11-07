import driver

def letter(row, col):
    if col >= 7 and col <= 9 and row >= 4 and row <= 5:
        return 'X'
    elif 2 <= row <= 5 and 4 <= col <= 9:
        return 'Z'
    elif 4 <= row <= 6 and 7 <= col <= 12:
        return 'B'
    else:
        return 'T'


if __name__ == '__main__':
    driver.comparePatterns(letter)