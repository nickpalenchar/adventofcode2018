"""
calc_frequency
"""


def calc_frequency():

    result = 0
    seen = set()

    while True:
        with open('input.txt') as fh:
            for freq in fh:
                if freq[0] == '+':
                    result += int(freq[1:])
                else:
                    result -= int(freq[1:])
                print(result)
                if result in seen:
                    print(result)
                    return result
                else:
                    seen.add(result)


if __name__ == '__main__':
    calc_frequency()
