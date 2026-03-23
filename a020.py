letter_map = {
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 34,
    'J': 18, 'K': 19, 'L': 20, 'M': 21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25,
    'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33
}
while True:
    try:
            s = input().strip()
            total = 0
            first = s[0]
            num = letter_map[first]
            ten = num //10
            en = num  %10
            total += en*9+ten
            we = 8
            for i in range(1,9):
                total +=int(s[i])*we
                we-=1
            total +=int(s[9])
            if total % 10 == 0:
                print('real')
            else:
                print('fake')
    except EOFError:
            break
