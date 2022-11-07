import driver


def letter(row, col):
    if 3 <= col <= 6 and 2 <= row <= 4:
        return 'M'
    else:
        return 'S'


if __name__ == '__main__':
    driver.comparePatterns(letter)