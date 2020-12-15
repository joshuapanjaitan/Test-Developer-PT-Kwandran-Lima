import re
import math
import zodiac as zd
from datetime import datetime
now_date = '20/12/15'

# fungsi untuk menghitung usia


def findAge(dob):
    umur = []
    tahun = 0
    bulan = 0
    today = datetime.today()
    dob = dob.date()
    tahun = today.year-dob.year
    if today.month >= dob.month:
        bulan = today.month - dob.month
    else:
        tmp = dob.month - today.month
        bulan = 12-tmp
        tahun -= 1
    umur.append(tahun)
    umur.append(bulan)
    return(umur)


name = input("Nama : ")
text = input('Masukkan Tanggal Lahir (YY-MM-DD): ')
# validasi input
pattern = r'([0-99])\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])'
match = re.search(pattern, text)
if match:
    dob = match.group()
    dob = dob.replace("-", "/")
else:
    print('Format tanggal salah')

date_nowdate = datetime.strptime(now_date, '%y/%m/%d')
date_dob = datetime.strptime(dob, '%y/%m/%d')
zodiac = zd.zodiac(date_dob)
age = findAge(date_dob)
print("Halo ", name)
print("Umur kamu adalah: ")
print(age[0], "Tahun")
print(age[1], "Bulan")
print(date_nowdate.day, "Hari")
print("Bintang Anda Adalah : ")
print(zodiac)
