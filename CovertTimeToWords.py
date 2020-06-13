def timeInWords(hr, min):
    past = ["quarter","half"]
    numbers = ["zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
        "twenty",
        "twenty one",
        "twenty two",
        "twenty three",
        "twenty four",
        "twenty five",
        "twenty six",
        "twenty seven",
        "twenty eight",
        "twenty nine"]
    middle = " minutes "
    if min == 30 or min == 15:
        return past[min/15-1]+" past "+numbers[hr]
    if min  == 45:
        return past[0]+" to " + numbers[hr+1]
    if min <10:
        middle = " minute "
    if min == 0:
        return numbers[hr]+" o' clock"
    if min < 30:
        return numbers[min]+middle+"past "+numbers[hr]
    if min > 30:
        return numbers[60-min]+middle+"to "+numbers[hr+1]

print(timeInWords(1,1))

