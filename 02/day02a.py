

def compute_checksum():

    doubles = 0
    tripples = 0

    with open('input.txt') as fh:
        for line in fh:
            count = {}
            
            for char in line:
                if char not in count:
                    count[char] = 0
                count[char] += 1
            
            double, tripple = [0, 0]
            for k in count:
                v = count[k]
                if v == 2:
                    double = 1
                if v == 3:
                    tripple = 1

            doubles += double
            tripples += tripple

    print(doubles * tripples)


if __name__ == '__main__':
    compute_checksum()
