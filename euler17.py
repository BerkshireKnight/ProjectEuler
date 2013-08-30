
ONE_TO_NINETEEN = ["zero","one","two","three","four","five","six","seven",
                   "eight","nine","ten","eleven","twelve","thirteen",
                   "fourteen","fifteen","sixteen","seventeen","eighteen",
                   "nineteen"
                   ]


TEN_TO_NINETY = ["zero","ten","twenty","thirty","forty","fifty",
                 "sixty","seventy","eighty","ninety"
                 ]


AND = "and"
HUNDRED = "hundred"
THOUSAND = "thousand"


def number_name(n):
    if n <= 0:
        return ""
    elif n < 20:
        return ONE_TO_NINETEEN[n]
    elif n < 100 and n % 10 == 0:
        return TEN_TO_NINETY[n//10]
    elif n < 100:
        return TEN_TO_NINETY[n//10] + ONE_TO_NINETEEN[n%10]
    elif n < 1000 and n % 100 == 0:
        return ONE_TO_NINETEEN[n//100] + HUNDRED
    elif n < 1000:
        return ONE_TO_NINETEEN[n//100] + HUNDRED + AND + number_name(n%100)
    elif n < 10000:
        return ONE_TO_NINETEEN[n//1000] + THOUSAND + number_name(n%1000)


def main():
    counter = 0
    for i in range(1,1001):
        counter += len(number_name(i))

    print(counter)


if __name__ == "__main__":
    main()
