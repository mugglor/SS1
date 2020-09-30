digit = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

hangDonVi = ['mốt', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu'
    , 'bảy', 'tám', 'chín', 'lăm']

hangChuc = ['mười', 'hai', 'ba', 'bốn', 'năm', 'sáu'
    , 'bảy', 'tám', 'chín', 'lẻ']

hangTram = [0, 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu'
    , 'bảy', 'tám', 'chín']


def main():
    money = input("nhap so tien: ")
    number_2_text(money)


def number_2_text(money):
    number = money.split(',')
    print(number)

    for i in range(1, len(number) + 1):
        if i == 1:
            hang_don_vi(number[-1])
        elif i == 2:
            hang_chuc(number[-2])
        elif i == 3:
            hang_tram(number[-3])


def hang_tram(number):
    number = str(number)

    for i in range(-1, 10):
        if number[0] != 0:
            if number[0] == str(digit[i]):
                print(hangTram[digit[i]], end=' ')
                print("trăm", end=' ')


            if number[1] == 0:
                if number[2] != 0:
                    print("le", end=' ')

def hang_chuc(number):
    print('hehe2')


def hang_don_vi(number):
    number = str(number)

    print('hehe3')


main()
