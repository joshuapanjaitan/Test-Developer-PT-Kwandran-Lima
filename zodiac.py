# fungsi untuk menghitung zodiak


def zodiac(date):
    zodiac_sign = ''
    if ((date.month == 12 and date.day >= 22)or(date.month == 1 and date.day <= 19)):
        zodiac_sign = "Capricorn"
    elif ((date.month == 1 and date.day >= 20)or(date.month == 2 and date.day <= 17)):
        zodiac_sign = "aquarium"
    elif ((date.month == 2 and date.day >= 18)or(date.month == 3 and date.day <= 19)):
        zodiac_sign = "Pices"
    elif ((date.month == 3 and date.day >= 20)or(date.month == 4 and date.day <= 19)):
        zodiac_sign = "Aries"
    elif ((date.month == 4 and date.day >= 20)or(date.month == 5 and date.day <= 20)):
        zodiac_sign = "Taurus"
    elif ((date.month == 5 and date.day >= 21)or(date.month == 6 and date.day <= 20)):
        zodiac_sign = "Gemini"
    elif ((date.month == 6 and date.day >= 21)or(date.month == 7 and date.day <= 22)):
        zodiac_sign = "Cancer"
    elif ((date.month == 7 and date.day >= 23)or(date.month == 8 and date.day <= 22)):
        zodiac_sign = "Leo"
    elif ((date.month == 8 and date.day >= 23)or(date.month == 9 and date.day <= 22)):
        zodiac_sign = "Virgo"
    elif ((date.month == 9 and date.day >= 23)or(date.month == 10 and date.day <= 22)):
        zodiac_sign = "Libra"
    elif ((date.month == 10 and date.day >= 23)or(date.month == 11 and date.day <= 21)):
        zodiac_sign = ("Scorpio")
    elif ((date.month == 11 and date.day >= 22)or(date.month == 12 and date.day <= 21)):
        zodiac_sign = "Sagittarius"

    return zodiac_sign
