"""
calc_frequency
"""


def calc_frequency():

    result = 0
    with open('day01a_input.txt') as fh:
        for freq in fh:
            if freq[0] == '+':
                result += int(freq[1:])
            else:
                result -= int(freq[1:])
    print(result)

if __name__ == '__main__':
    calc_frequency()
