import re


def credit_card_validator(card_number):
    pattern = r"\S"

    # list
    card_digits = re.findall(pattern, card_number)
    sum_odd = 0
    sum_even_digits = 0

    for (index, card_letter) in enumerate(card_digits):
        card_digit = int(card_letter)
        # if is a even
        if index % 2 == 0:
            double = card_digit * 2
            if (double < 10):
                sum_even_digits += double
            else:
                sum_even_digits += sum(int(digit) for digit in str(double))
        # if is odd
        else:
            sum_odd += card_digit
    return (sum_odd + sum_even_digits) % 10 == 0


card_number = "5610 5910 8101 8250"
if (credit_card_validator(card_number)):
    print("VALID")
else:
    print("INVALID")
