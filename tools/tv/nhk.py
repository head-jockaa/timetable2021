# coding:utf-8
import util

nhk_areas = ["130","010","011","012","013","014","015","016","020","030","040","050","060","070","080","090","100","110","120","140","150","160","170","180","190","200","210","220","230","240","250","260","270","280","290","300","310","320","330","340","350","360","370","380","390","400","401","410","420","430","440","450","460","470"]

IMG_COMMENT = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAArtJREFUeNrcWctxwjAQFUwaoAUoAUqAEmgBSoAS4MYVLnCGEqAEKAFKgBIcvQxPs14kWUri4MnOaLAlW3r79icZUxSFsbKyrWhYWz2xNRKcA2lkx3a7Ld4twKBANgecD2TLoXzauynSarW+ftupL9xuN7NcLs3lcvlboKkMjkYjczqdzHA4NMfjMaoIWop0Oh3T7/ejDH6kTARgaJBut+uueY9G6fV6WQwB4Pl8/hmDg8EgatrFYmFms9nX9XQ6LTFIZQAEjFEej4ebExaBZXwMuigOiV3cRZSdxDW7YKnfJ3Zh98z1en0Z5xieC41FAVrq3YOWodLY/X4PjmnlrAt4x38EEACsSdwCuA8x62MHgvdCCkjl9dwSoDdI4B+IWvxC4F/SB9GPlAOB78Dn4F/Sx+bzufPFyWTysgbn0+/55IVB6TupDWyDFQgY0+YHS2CdjdYJ+W+liTkRx2EuGRxYgAHDxcbjcQkcnqXs93uvYuv1+nsANZO6T2rOxdFHpQBW+hau0UelcB0CV+mDuSJ9CP7KnAg/RRK3YFzV4H2qfNRVQxEECBQWASRs3ANoLQAZtYxMbh5kny6PjHKdIXIkGSDZkJsC3SflcDiUlJNKUDEK0lAs1SQFCa7RGASIUN3HwEHizklRsUqSzKA2FTTWfZohBAX9DQxuNhu3udA7mqxEnZtmZJ9kTzLjmysmv5pmdBCQ3RDDtQSJ3J8xSnUfzWVZrKyvb8uDMv+F0gs2Itq/mdyzfBClSNfUmK/KUpe70fiWD1LrHHP5tla1RTEKOsbsoskMVj2TG8XtqtMcT27vknasVNHEVemizsN80AfpL2BP+wj8CUdRXfh/K7UkMSjPI74xH7hQgNTy6YMH65B59SeOlKrB/WAs5+nC8H++br09ine7XWNAaSyN/wTc7I/oTf8b4lOAAQCgsVv038qR/wAAAABJRU5ErkJggg=="

IMG_STEREO = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAiRJREFUeNrsmctxwjAQhuVMGqAFWqAFt4BLMCXQAty4wgXOUIIpAUqAEqAEoV9BzCKEtXpMomSyMxoTgvGnf7UPCSGlFMoWasjCxuLOViTcA1LQN9brtfxpA4MFWQ6cC7J6UN79XYpVVaWvH6JwKx7wM/bG3W4nzuez2O/3+m9zhQ0GAzEajcRwONRjPB7ra6zJryXot8vlImezmVQAwSmjrmvZdR07UIKD5Hg8islkoq/UjEoK4Ol9KAqFMaipCYrpdMoOEpaCUE5BPCmiHiJPp5NXCaim3P10L7zAVZAFiC+kD1gul0F5DRO0IX2TCwKk6uFBMQYlKWDbtixAVpqh6wgRGmNYozSS7bWZFMU0avEaLoux7Xar78fwLZMgF8Md1D1wMydAUiwIEDCu3KcSsFYiVtFsgLDD4fASibaqSD1wYw7gYEBjUKwPNBdwNCB1O/Ij3MwpffgcYL8N0LUEDLBddejA/zg1OTtgn8Iu0KxpJgesnap85Y4NaFosDLgxxeyajiBKBqQzRzCkGCZr94jJtZjWz+v1+tIPhlhMHfcConWnNp/PowFXq9VLA5GlWYArQhtOV7sV0nQk12JAcxIvAssVwdw0E7QnaZrG2ceZXs+sV7NWMfDaXocKTu/0su1J7JTTVyneDXgAaYVbl5OPPqAOdm5GJbqDM/tiuj/2KfZOwf+zmT9/NvN7ADebTTFQNkvxR8BlH6KX/jPETYABABrtSu0F1sjRAAAAAElFTkSuQmCC"

IMG_SS = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAflJREFUeNrsmcGxgjAURcMfG4ASoAQsQUqAErAV2LmVDa61BCkBSoASsAR+br5hMgghaPBnwZthGAkJx/dubiKSrusIjRM9OsOO05PNSLgekogX8jzv/jvAMIA0B24M0uopn/U2JSzLYucfYnhsgBtgVVUkiiImWtnhOA4pikL5wbfbjfXDeS66v0k8HmEYKhvr9XpVthLf91mfJElG2198cCp4exzH2nzufr/3484BKmuQZlKLprIsY5JRjZ2s8fF4aIFK05TpE3p+Z8zJEouleDfKspTqdq7Eu7Vtgk4GQiFfMhcEweclbppGG+QqPsi/9eFwYBo6Ho/E87ze+5AF6EuXVhdrEPpAm23bUh25rsu0tiS02AwvMTJEIcj5fCZt27KtWV3XhA7e34ds6pKEcgZhzmiD61OwyVnKM0yloD2DUkBAwWrmgksBB83s90pMM8MmyJJVBmZs3HYL+tRtTUqA2AqtJfyPAeFvWNT3+/3sIGJZIYuvAPIHwWKwA5GFuFFV0awWm8EM5vaB89TsFDcD2NwO26h3jlqUFpsRdzOAxGAcFA8X7WX4JcS+Y/6oBZA/CEuZbKmDkQ+XuiH8aoA8UCqUkMMCCp9xfcrkcQ/gxu5BX7RNLQTbq4/th/sGuBTwcrkYAzVkMf4VsNkv0U3/G+JXgAEAVCNOmMHtm8kAAAAASUVORK5CYII="

IMG_BILINGUAL = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAANdJREFUeNrs2dEJgzAQBuBL6QKukBUyS2aJY/gaX/TZFVzBFZzlGluREizR1jT38P9wCBLIh8J5RGJmCmlCsbBqVptI3Iak9xtd13HpLIYIKQe3h1Sbcn3fUqKUel5vJDwAAlg69yOL6rqmtm0v3VhrTeM4UlVVybX86jKfk+tL4b0/smcaaK29HBeeHM/znASiUaPNAAgggAACCCCA5SbqHJN0nGWiHoaBjDHnJ+p/ncE4576bqHNM0ns1TRMmarQZAH8G9n0vBhVbxB8Byz5El/4b4iHAACMOlM6fJ63HAAAAAElFTkSuQmCC"

IMG_MULTISOUND = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAi1JREFUeNrkmc1xwjAQRu1MGoASoARaoAVaoAVa4JgrXOBMC7QAJdAClKD4EaTZLJYtOVJQJprRmB8jP+/37UoWlTGmatpH001h/ePBViScg6zkB7vdzry6waAgy4Frg6wd5UPvUlpd1/fjW4rBbrdbNtAfA26322o6nVbj8bg6n89ZIM2XwvFts9k4r0wmE3O9XpP58ClJYtt6vY4uG4vFIj/g5XIx8/l8cG07Ho95AAFbLpffLkYUQ35nzx+NRsE2CAY8nU5PYKFyATObzdxv8GxSibWUJMJqtXLvubgvIkRuKFw0IEd5AXyEXD7Iw+HgvucYC5cki5FeQ+oE4nPOe0mZsZGU8usEAg5gbPESQO0zawfAZIQ5/hogUESnDczWODwn4YbIHATIwBgeIMqKltGWGwuGD2WW93XG8yVQL2DXVEb0+J5oSj+23UBIHwQoEwD5KNbcrS4pOnNDygpjyChmSRJuAHm1D2VUQxYavulyECCeZECflF0zS1v97FqiRQESlTYoa3K5LgQyBI7eld1RgAykM5fs9smGX3WT01/I3BwtMZ7jIl0SylWP9ZYuPaFzc5KZpC07pRW0X2OKdhZAXZ60LWKeWZIDIj8SS5/ZRNJ+zQ5IVhMpJPQ9n3RNY0kBkYXIAKIXCD4ph0RsMGDf4yWR8k2DKQDf+57qm4jcdwzs9kYDdO9NNN3rrHs0/2LzKGf7O4D7/b4YKM1S/BZw2Zvopf8N8SnAAEt34YLOt+bLAAAAAElFTkSuQmCC"

IMG_SUB = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAaNJREFUeNrsmd2NgzAMx8OJBViBFViBFZiBEViBx77CCzzDCDACjAAjwAg5O9cgroKUkKQNEpYiUD+sXx3nb+MSSikBe8Cilq3Hk81KuAWSrF8oioJ+25DhBdIeuC1IZ6F87rct5jgOu7q6HM7zTPI8Z/dJkmiFpX8BVLOmaZZtwXtV475+yAVsN4Jd19EgCIzJCPquqkoYQSGgSTi+PM87D8jfg6TXLiXoU5SzUjkYhqH2vDrq0/pDIqWDqHOod2cMco1EUcSuRgDHcSRxHCtFo+97kmWZPkCQAAbG8yVNU2motm3Z4tVmnYPc37t81FJJtgyixWSEywnqqmwl0Qo4TRO7ovj6vv9PkGXgjAAOw7BEay3CGEWVWmykWUAwyK8loiqArgntwsOlS9xdkSTw03dUhrjVdc2+f9QgX5lGSp1iiMBHH5Ckt1j0i/Y6ah41OLVSFQM/f3fUpuwGvAEv1bBuScq6mf34Y+eegUYKRVelBhuXGWxCZdt64Yzm7PBoq07LVpAjwyPrp1vXkZmyLK2BemWxfgRs9xDd9r8hfgUYAA08qySnAKtYAAAAAElFTkSuQmCC"

IMG_SIGN = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAWNJREFUeNrsWcENgzAMNFUXYAVWYAUYgRVgBFbg2TcfeLMCrMAKjAAjpHHaVG1EoIRArSonWZEiiE92cjgGGGPAcePGiNntyY0kuRdJeJ+oqor9GshBIUmH3BxJ78XymW8q8DxPjBcgjusZTvq+h2maxDgMgxjRoiiCtm2XI7mW4q7rZufRETpV59DW3pXwfR/GcVxM8WIEsyyDsiytRTIIgg9LkmRfinERHTA9umjje2maQhiGH8RMwR4Z3g+5FidvbS3yp9gRtAHtHmya5vCCgB8k8z34rmlHYc2HsVDPIY5jMaK8FEWxSRt1Qu1kxskMWZnB43/W3YNXNULSNu3BMyRGAss2nT+tzKi13VEyI+tCWfk4mXEy4wj+G8GriWapNz2UiS1Vz6GXpjzPV78M+MzPZAajtQS8jnKC9no0Js0j2cr45q68t3nkulvWZKauazKkVC7kW8C0m+jUf0PcBRgAAxRlO2wJrDYAAAAASUVORK5CYII="

IMG_DATA = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAb5JREFUeNrsWdGRgjAUDDfXAJRAC7YgJUgJUIIt4J+/fOk3lCAlQAlYApSQy+YMExEEjwDvZtiZDAko7LyXbPYB45wzgbNonFg7P7iRJNeQZPqJy+XC1wY4tEjSIddF0mpYPvJNBZZlyeMXI45FCd7vd+Z5HsuyTI5932eO48jz78B/Mzw/kiSRz7JtW473+70cB0Hw8tvV5iAiVtc1E2SbKAJVVTFB/GUODkZQ/JG7rmtE16IoktFCH9EDEE2M4zjujOAgwTzPjQnvbrfjZVk2fZV29PGcP6c4DENWFMXk9B6PR3Y4HOSiQDr1lPbJzKaD/0oHN4Jr4LvvAsQUIorjnFAr++OtDsK5hCnFJtAFdb03xULp3+qUKQxFz6gOPu2fE+9nXAd1y2Qy8rMQFPOKHkF9ryZJULlkQLgTowtpsqOGZ9SlA5ZqKkb7wTFQJlT3eWQI3m63p+hhTIagKoJUE6JrrMCaRBD2XFVkemoxF1cjiNSh6AGRrlrDJLmPCarKq6sJNzJLDT2aYFtCVMPKNSEnQwRHmYXT6cTSNJUCDJezhNPZqjrje/H1eiVDqs2F/Ctg2i/RqX+G+BFgAB1oOJ1sLZI+AAAAAElFTkSuQmCC"

IMG_INTER = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAn9JREFUeNrsmcmRwjAQReUpEoAQSIEUIARSgBAgBLhxhQucSQFCgBAgBAjB4++hXR9Na/FCjQ7TVS7AlqWnXr5kY/I8N4VtiiNP7Ni82JKEqyANn9jv9/lfGxgsyHTgNMisonzFOxXLsqz8/DKJW8938Xq9mufzGexkPB6//T6fz8F7+v2+GY1GUZD5T4Tf7XK5RFdbMVjZHrZaraLvKwDzx+Oh5uGvIrHtdruVA9cZDHY8HmtJyWw2awYYY5j9dDrN6/ZxOp2qe4r08AK2KpI6eeTLWZ91VsWAFdvtdma9XjvbcuGFJthrCyYVywPN5/PqnOYtqIM2sUYeXC6XZjAYlF6pawzCdr/foz34FTMIQgKvANblQfbUcDj09smAobbBKkalQkI0WYAUyfntdludR2X6KlSuF3DOcWvJjAuSNQ/SISZiDR3V+gppIAP2Yiu0ADCTyaQMueQjJ7gWYqQGwslh5GWw1VIX40mX2LKXOPQweE2uuZa5ViuJBomQ2iZtsNLwvbJ8+sLbeqnDQEhwl5fsTYN4Cu20nP3IWsyAvJvxVbjc46veTgDZE76tk4QZQOxRzeOdArL3FouFUzZcE4mxxoDsCQHiorFDzZPRrncKiM6lCvEpIeXNrQ3A+8VY7zUCtOXFlhZA4uD2rHl18q8RIA8W8oQ9GXznx4fOi4ThMBB7SqtwhpHqtgsmBBkFqIXJleQQXtmluKTHfuJD342f6rQlTZu1BuZa/jTpQZVrkw4C8mwRMmyttEdTbeMQkhINsjagSIprhrbOwduh9dXuXyIEsf/Ic7GkQqz4ukB9Ofj/dqutVYCHwyEZKJsl+VfAab9ET/1viG8BBgCSNPvEZxdw6AAAAABJRU5ErkJggg=="

IMG_RE = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAoCAYAAACM/rhtAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAZpJREFUeNrsWdGRgyAQxZs0YAu2YAtagi3Ygpagf/n2R7+1BC1BW7AELYFjc8G544TABXHnxp1hwgSEl919y5MQSilhdmeNImv3JzaU4DaQ5PsXdV3Tsw0wCCDxgNsD6W0on/HGYp7nPT4/CHK7qQaHYXACIgxD4vu+dJx+RfinpWnqjK1BEPzan49JQ8wechZG8KDKdj1oan3fU1traXkQi6EHqBXicRxpkiTWSMFyjrZtqxViLYA2wfHGyoo9gHxOlmVvkwQ8x+fBM1ZJEkXR2/nEovG/SHIzmdx1HZmmaXdsnuetX5alWxYfdcTp5KCRB9n5LD0CwYNVVT36RVEo18nz/BgPqn6xyVF3GIuvo86ExcBEUbBC7siE5bquWz+OY63N+Xogt2R5K30n4e8EzgSBZH+pB1kCbzWPs07FYhMT13u1phUW/0WMXiy+AJqKBVOD0iOKC5nYOIUkTD8qxcKyLOeSRHVbAIVZNf6yUIs6ENQKk/zGIPeuT3SUOS/U1+2WtTLTNA0aUCIW9FfAuC/Rsf8N8SnAANZNZZfq9eAgAAAAAElFTkSuQmCC"

def convertToTvkingdomArea(nhk_area):
	if nhk_area == "010":
		return "10"
	elif nhk_area == "011":
		return "11"
	elif nhk_area == "012":
		return "12"
	elif nhk_area == "013":
		return "13"
	elif nhk_area == "014":
		return "14"
	elif nhk_area == "015":
		return "15"
	elif nhk_area == "016":
		return "16"
	elif nhk_area == "040":
		return "17"
	elif nhk_area == "050":
		return "18"
	elif nhk_area == "060":
		return "19"
	elif nhk_area == "030":
		return "20"
	elif nhk_area == "070":
		return "21"
	elif nhk_area == "020":
		return "22"
	elif nhk_area == "130":
		return "23"
	elif nhk_area == "140":
		return "24"
	elif nhk_area == "100":
		return "25"
	elif nhk_area == "080":
		return "26"
	elif nhk_area == "120":
		return "27"
	elif nhk_area == "090":
		return "28"
	elif nhk_area == "110":
		return "29"
	elif nhk_area == "200":
		return "30"
	elif nhk_area == "150":
		return "31"
	elif nhk_area == "190":
		return "32"
	elif nhk_area == "230":
		return "33"
	elif nhk_area == "170":
		return "34"
	elif nhk_area == "220":
		return "35"
	elif nhk_area == "180":
		return "36"
	elif nhk_area == "160":
		return "37"
	elif nhk_area == "240":
		return "38"
	elif nhk_area == "210":
		return "39"
	elif nhk_area == "270":
		return "40"
	elif nhk_area == "260":
		return "41"
	elif nhk_area == "280":
		return "42"
	elif nhk_area == "300":
		return "43"
	elif nhk_area == "290":
		return "44"
	elif nhk_area == "250":
		return "45"
	elif nhk_area == "340":
		return "46"
	elif nhk_area == "330":
		return "47"
	elif nhk_area == "320":
		return "48"
	elif nhk_area == "310":
		return "49"
	elif nhk_area == "350":
		return "50"
	elif nhk_area == "380":
		return "51"
	elif nhk_area == "370":
		return "52"
	elif nhk_area == "360":
		return "53"
	elif nhk_area == "390":
		return "54"
	elif nhk_area == "400":
		return "55"
	elif nhk_area == "401":
		return "kk"
	elif nhk_area == "430":
		return "56"
	elif nhk_area == "420":
		return "57"
	elif nhk_area == "460":
		return "58"
	elif nhk_area == "450":
		return "59"
	elif nhk_area == "440":
		return "60"
	elif nhk_area == "410":
		return "61"
	elif nhk_area == "470":
		return "62"

def checkContent(html, year, month, day, area):
	if not "area=\"" + area + "\"" in html or not "date=\"" + year + month + day + "\"" in html:
		print(year + "_" + month + "_" + day + "_NHK" + area + ".htmlの内容が間違っています")

def getTargetPrograms(nhk_area):
	area = convertToTvkingdomArea(nhk_area)
	result = ["", "", "", "", "", "", "", "" ,"" ,"" ,"" ,""]
	if not "sG"+area in util.already and not area in ["24","27","29"]:
		result[1] = "sG"+area
		util.already.add("sG"+area)
	if not "sE"+area in util.already and not area in ["24","25","26","27","28","29","38","39","41","42","43","44","45"]:
		result[3] = "sE"+area
		util.already.add("sE"+area)
	if not "NB2" in util.already:
		result[5] = "NB2"
		util.already.add("NB2")
	return result

def extractTodays(html):
	splited = html.split("現在の時刻")
	if len(splited) == 1:
		return ""
	return splited[1]

# extractTodaysで切り分けたhtmlを与える
def splitByItem(html):
	splited = html.split("<td data-")
	splited.pop(0)
	return splited

# splitByItemで切り分けたhtmlを与える
def getInterval(html):
	splited = html.split("rowspan=\"")
	splited2 = splited[1].split("\"")
	return (int)(splited2[0])

# splitByItemで切り分けたhtmlを与える
def getColspan(html):
	splited = html.split("colspan=\"")
	splited2 = splited[1].split("\"")
	return (int)(splited2[0])

# splitByItemで切り分けたhtmlを与える
def extractStartTime(html, rowspan):
	splited = html.split("class=\"time\">")
	if len(splited) == 1:
		return ""
	splited2 = splited[1].split("<")
	splited3 = splited2[0].replace("午前","").replace("午後","").strip()
	start_hour = splited3.split(":")[0]
	start_minute = splited3.split(":")[1]
	if "午後" in splited2[0]:
		start_hour = str((int)(start_hour) + 12)
	elif rowspan > 720 and "午前" in splited2[0]:
		start_hour = str((int)(start_hour) + 24)
	elif len(start_hour) == 1:
		start_hour = "0" + start_hour
	return start_hour + start_minute

# splitByItemで切り分けたhtmlを与える
def extractTitle(html):
	splited1 = html.split("class=\"to-dtl\">")
	if len(splited1) == 1:
		return ""
	else:
		splited2 = splited1[1].split("</a>")
		result = util.sanitize(splited2[0])
		return result.replace(" ［終］","")

# splitByItemで切り分けたhtmlを与える
def extractDescription(html):
	splited1 = html.split("class=\"arrow\">")
	if len(splited1) == 1:
		return ""
	else:
		splited2 = splited1[1].split("</div>")
		return util.sanitize(splited2[0])

# splitByItemで切り分けたhtmlを与える
def extractIcons(html):
	types = []
	if IMG_COMMENT in html:
		types.append(util.append_type_name("解"))
	if IMG_STEREO in html:
		types.append(util.append_type_name("S"))
	if IMG_SS in html:
		types.append(util.append_type_name("SS"))
	if IMG_BILINGUAL in html:
		types.append(util.append_type_name("二"))
	if IMG_MULTISOUND in html:
		types.append(util.append_type_name("多"))
	if IMG_SUB in html:
		types.append(util.append_type_name("字"))
	if IMG_SIGN in html:
		types.append(util.append_type_name("手"))
	if IMG_DATA in html:
		types.append(util.append_type_name("デ"))
	if IMG_INTER in html:
		types.append(util.append_type_name("双"))
	if IMG_RE in html:
		types.append(util.append_type_name("再"))
	if "［終］" in html:
		types.append(util.append_type_name("終"))
	return types

def get_first_time(station_tag):
	if station_tag.startswith("sG"):
		return util.time_decode_base60(util.standard_programs_timeline[station_tag[1:]][0])
	elif station_tag.startswith("sE"):
		return util.time_decode_base60(util.standard_programs_timeline[station_tag[1:]][0])
	elif station_tag == "NB2":
		return util.time_decode_base60(util.standard_programs_timeline["BS1"][0])

def getCategoryCode(title_name):
	if "ニュース" in title_name:
		if "ワールド" in title_name or "CNN" in title_name or "世界" in title_name:
			return "100105"
		else:
			return "100100"
	elif "マーケット" in title_name:
		return "100104"
	elif "オリンピック" in title_name or "パラリンピック" in title_name:
		return "101106"
	elif "MLB" in title_name or "野球" in title_name:
		return "101101"
	elif "Jリーグ" in title_name or "サッカー" in title_name or "JFA" in title_name:
		return "101102"
	elif "ゴルフ" in title_name:
		return "101103"
	elif "Bリーグ" in title_name or "Vリーグ" in title_name or "Wリーグ" in title_name or "熱血バスケ" in title_name or "バスケットボール" in title_name or "ラグビー" in title_name or "テニス" in title_name or "ウィンブルドン" in title_name or "ハンドボール" in title_name  or "バレーボール" in title_name  or "甲子園ボウル" in title_name or "Nitto" in title_name:
		return "101104"
	elif  "相撲" in title_name or "剣道" in title_name or "柔道" in title_name or "空手道" in title_name:
		return "101105"
	elif "競泳" in title_name:
		return "101107"
	elif "ノルディック" in title_name or "アルペン" in title_name or "カーリング" in title_name or "アイスホッケー" in title_name or "NHK杯フィギュア" in title_name:
		return "101109"
	elif "ジャンプ" in title_name and "ワールドカップ" in title_name:
		return "101109"
	elif "体操" in title_name or "クライミング" in title_name:
		return "101115"
	elif "スタジオパーク" in title_name:
		return "102107"
	elif "連続テレビ小説" in title_name:
		return "103100"
	elif "せかほし" in title_name:
		return "105105"
	elif "アニ×パラ" in title_name:
		return "107100"
	elif "美景" in title_name or "トラムの旅" in title_name or "大空撮" in title_name or "大縦走" in title_name or "天空の塩田" in title_name or "古代中国" in title_name or "空旅中国" in title_name or title_name == "京都 音めぐり":
		return "108101"
	elif "動物" in title_name or "生きもの" in title_name or "小笠原" in title_name or "北アルプス" in title_name or "空中散歩" in title_name or "名峰" in title_name or "にっぽん百名山" in title_name:
		return "108102"
	elif "クルージング" in title_name:
		return "110100"
	elif "高校講座" in title_name or title_name == "ロンリのちから":
		return "110109"
	else:
		return "115115"
