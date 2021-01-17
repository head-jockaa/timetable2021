# coding:utf-8
import sys
import os
import math
import unicodedata
import util

range1=546
range2=1600
range3=1950

base64_special = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","@","$","{","|","}",";","*","_","~","^","`","'"]

def to_base64_special(n):
	c1 = base64_special[math.floor(n/64)]
	c2 = base64_special[n%64]
	return c1 + c2

if __name__ == "__main__":
	special = 0
	if len(sys.argv) > 1:
		special = (int)(sys.argv[1])

	f = open("scripts/titles_raw.js", 'r')
	titles_js = f.read()
	f.close()
	f = open("scripts/descriptions_raw.js", 'r')
	descriptions_js = f.read()
	f.close()


	# ABCを括弧でくくる


	outfile = open("scripts/titles.js", 'w')
	idx = 0
	in_text_area = False
	in_abc_area = False
	is_backslash = False
	for c in titles_js:
		if is_backslash and c == 'n':
			outfile.write("n")
			continue
		is_backslash = (c == '\\')
		if in_abc_area:
			if c == '"':
				in_abc_area = False
			elif c in base64_special or unicodedata.east_asian_width(c) == "Na" or c == '\n':
				outfile.write(c)
				idx += 1
				continue
			else:
				in_abc_area = False
				outfile.write(">")

		if not in_text_area:
			outfile.write(c)
			if c == "\"":
				in_text_area = True
		else:
			if c == "\"":
				in_text_area = False
				outfile.write(c)
			elif c in base64_special:
				in_abc_area = True
				outfile.write("<" + c)
			else:
				outfile.write(c)

		idx += 1
	outfile.close()

	outfile = open("scripts/descriptions.js", 'w')
	idx = 0
	in_text_area = False
	in_abc_area = False
	is_backslash = False
	for c in descriptions_js:
		if is_backslash and c == 'n':
			outfile.write("n")
			continue
		is_backslash = (c == '\\')
		if in_abc_area:
			if c == '"':
				in_abc_area = False
			elif c in base64_special or unicodedata.east_asian_width(c) == "Na" or c == '\n':
				outfile.write(c)
				idx += 1
				continue
			else:
				in_abc_area = False
				outfile.write(">")

		if not in_text_area:
			outfile.write(c)
			if c == "\"":
				in_text_area = True
		else:
			if c == "\"":
				in_text_area = False
				outfile.write(c)
			elif c in base64_special:
				in_abc_area = True
				outfile.write("<" + c)
			else:
				outfile.write(c)

		idx += 1
	outfile.close()

	print("STEP1 completed")


	# よく出る３文字を変換（east_asianを対象とする）


	f = open("scripts/titles.js", 'r')
	titles_js = f.read()
	f.close()
	f = open("scripts/descriptions.js", 'r')
	descriptions_js = f.read()
	f.close()

	result3 = {}

	idx = 0
	titles_js_len = len(titles_js)
	for c in titles_js:
		if idx < titles_js_len-2 and unicodedata.east_asian_width(titles_js[idx]) != "Na" and titles_js[idx] != '\n' and unicodedata.east_asian_width(titles_js[idx+1]) != "Na" and titles_js[idx+1] != '\n' and unicodedata.east_asian_width(titles_js[idx+2]) != "Na" and titles_js[idx+2] != '\n':
			a = titles_js[idx] + titles_js[idx+1] + titles_js[idx+2]
			if a in result3:
				result3[a] += 1
			else:
				result3[a] = 1
		idx += 1
	print("STEP2-1 completed")

	idx = 0
	descriptions_js_len = len(descriptions_js)
	for c in descriptions_js:
		if idx < descriptions_js_len-2 and unicodedata.east_asian_width(descriptions_js[idx]) != "Na" and descriptions_js[idx] != '\n' and unicodedata.east_asian_width(descriptions_js[idx+1]) != "Na" and descriptions_js[idx+1] != '\n' and unicodedata.east_asian_width(descriptions_js[idx+2]) != "Na" and descriptions_js[idx+2] != '\n':
			a = descriptions_js[idx] + descriptions_js[idx+1] + descriptions_js[idx+2]
			if a in result3:
				result3[a] += 1
			else:
				result3[a] = 1
		idx += 1
	print("STEP2-2 completed")


	score_sorted3 = sorted(result3.items(), key=lambda x:x[1], reverse=True)

	if special > 0:
		if special > range3:
			limit = range3
		else:
			limit = special
		#print(score_sorted3[:limit])
		top_index = 0
		top_word = score_sorted3[top_index][0]
		checking_titles_js = titles_js.replace(top_word, " ")
		checking_descriptions_js = descriptions_js.replace(top_word, " ")
		top_index += 1
		top_word = score_sorted3[top_index][0]

		while top_index < limit:
			new_count = 0
			new_count += checking_titles_js.count(top_word)
			new_count += checking_descriptions_js.count(top_word)

			old_count = result3[top_word]
			result3[top_word] = new_count
			score_sorted3 = sorted(result3.items(), key=lambda x:x[1], reverse=True)
			#print(score_sorted3[:limit])
			print(str(top_index) + " " + top_word + " " + str(old_count) +  " -> " + str(new_count))
			if score_sorted3[top_index][0] == top_word:
				checking_titles_js = checking_titles_js.replace(top_word, " ")
				checking_descriptions_js = checking_descriptions_js.replace(top_word, " ")
				top_index += 1
				top_word = score_sorted3[top_index][0]
			else:
				top_word = score_sorted3[top_index][0]


	score_sorted3 = score_sorted3[:range3]
	encoder_string3 = ""
	for s in score_sorted3:
		encoder_string3 += s[0] + " "

	outfile = open("scripts/titles.js", 'w')
	idx = 0
	for aaa in titles_js:
		if idx >= titles_js_len:
			break
		c = titles_js[idx]
		if idx < titles_js_len-2:
			c3 = titles_js[idx] + titles_js[idx+1] + titles_js[idx+2]

		if unicodedata.east_asian_width(c) == "Na" or c == '\n':
			outfile.write(c)
		elif idx < titles_js_len-2 and c3 in encoder_string3 and titles_js[idx+1] != " " and titles_js[idx+2] != " ":
			outfile.write(to_base64_special((int)(encoder_string3.index(c3)/4)+range1+range2))
			idx += 2
		else:
			outfile.write(c)
		idx += 1
	outfile.close()
	print("STEP2-3 completed")

	outfile = open("scripts/descriptions.js", 'w')
	idx = 0
	for aaa in descriptions_js:
		if idx >= descriptions_js_len:
			break
		c = descriptions_js[idx]
		if idx < descriptions_js_len-2:
			c3 = descriptions_js[idx] + descriptions_js[idx+1] + descriptions_js[idx+2]

		if unicodedata.east_asian_width(c) == "Na" or c == '\n':
			outfile.write(c)
		elif idx < descriptions_js_len-2 and c3 in encoder_string3 and descriptions_js[idx+1] != " " and descriptions_js[idx+2] != " ":
			outfile.write(to_base64_special((int)(encoder_string3.index(c3)/4)+range1+range2))
			idx += 2
		else:
			outfile.write(c)
		idx += 1
	outfile.close()

	print("STEP2-4 completed")


	# よく出る２文字を変換（east_asianを対象とする）


	f = open("scripts/titles.js", 'r')
	titles_js = f.read()
	f.close()
	f = open("scripts/descriptions.js", 'r')
	descriptions_js = f.read()
	f.close()

	result2 = {}

	idx = 0
	titles_js_len = len(titles_js)
	for c in titles_js:
		if idx < titles_js_len-1 and unicodedata.east_asian_width(titles_js[idx]) != "Na" and titles_js[idx] != '\n' and unicodedata.east_asian_width(titles_js[idx+1]) != "Na" and titles_js[idx+1] != '\n':
			a = titles_js[idx] + titles_js[idx+1]
			if a in result2:
				result2[a] += 1
			else:
				result2[a] = 1
		idx += 1
	print("STEP3-1 completed")

	idx = 0
	descriptions_js_len = len(descriptions_js)
	for c in descriptions_js:
		if idx < descriptions_js_len-1 and unicodedata.east_asian_width(descriptions_js[idx]) != "Na" and descriptions_js[idx] != '\n' and unicodedata.east_asian_width(descriptions_js[idx+1]) != "Na" and descriptions_js[idx+1] != '\n':
			a = descriptions_js[idx] + descriptions_js[idx+1]
			if a in result2:
				result2[a] += 1
			else:
				result2[a] = 1
		idx += 1
	print("STEP3-2 completed")


	score_sorted2 = sorted(result2.items(), key=lambda x:x[1], reverse=True)

	if special > 0:
		if special > range2:
			limit = range2
		else:
			limit = special
		#print(score_sorted2[:limit])
		top_index = 0
		top_word = score_sorted2[top_index][0]
		checking_titles_js = titles_js.replace(top_word, " ")
		checking_descriptions_js = descriptions_js.replace(top_word, " ")
		top_index += 1
		top_word = score_sorted2[top_index][0]

		while top_index < limit:
			new_count = 0
			new_count += checking_titles_js.count(top_word)
			new_count += checking_descriptions_js.count(top_word)

			old_count = result2[top_word]
			result2[top_word] = new_count
			score_sorted2 = sorted(result2.items(), key=lambda x:x[1], reverse=True)
			#print(score_sorted2[:limit])
			print(str(top_index) + " " + top_word + " " + str(old_count) +  " -> " + str(new_count))
			if score_sorted2[top_index][0] == top_word:
				checking_titles_js = checking_titles_js.replace(top_word, " ")
				checking_descriptions_js = checking_descriptions_js.replace(top_word, " ")
				top_index += 1
				top_word = score_sorted2[top_index][0]
			else:
				top_word = score_sorted2[top_index][0]


	score_sorted2 = score_sorted2[:range2]
	encoder_string2 = ""
	for s in score_sorted2:
		encoder_string2 += s[0] + " "

	outfile = open("scripts/titles.js", 'w')
	idx = 0
	for aaa in titles_js:
		if idx >= titles_js_len:
			break
		c = titles_js[idx]
		if idx < titles_js_len-1:
			c2 = titles_js[idx] + titles_js[idx+1]

		if unicodedata.east_asian_width(c) == "Na" or c == '\n':
			outfile.write(c)
		elif idx < titles_js_len-1 and c2 in encoder_string2 and titles_js[idx+1] != " ":
			outfile.write(to_base64_special((int)(encoder_string2.index(c2)/3)+range1))
			idx += 1
		else:
			outfile.write(c)
		idx += 1
	outfile.close()
	print("STEP3-3 completed")

	outfile = open("scripts/descriptions.js", 'w')
	idx = 0
	for aaa in descriptions_js:
		if idx >= descriptions_js_len:
			break
		c = descriptions_js[idx]
		if idx < descriptions_js_len-1:
			c2 = descriptions_js[idx] + descriptions_js[idx+1]

		if unicodedata.east_asian_width(c) == "Na" or c == '\n':
			outfile.write(c)
		elif idx < descriptions_js_len-1 and c2 in encoder_string2 and descriptions_js[idx+1] != " ":
			outfile.write(to_base64_special((int)(encoder_string2.index(c2)/3)+range1))
			idx += 1
		else:
			outfile.write(c)
		idx += 1
	outfile.close()

	print("STEP3-4 completed")


	# よく出る一文字を変換（east_asianを対象とする）


	f = open("scripts/titles.js", 'r')
	titles_js = f.read()
	f.close()
	f = open("scripts/descriptions.js", 'r')
	descriptions_js = f.read()
	f.close()

	result = {}

	for c in titles_js:
		if unicodedata.east_asian_width(c) != "Na" and c != '\n':
			if c in result:
				result[c] += 1
			else:
				result[c] = 1
	print("STEP4-1 completed")

	for c in descriptions_js:
		if unicodedata.east_asian_width(c) != "Na" and c != '\n':
			if c in result:
				result[c] += 1
			else:
				result[c] = 1
	print("STEP4-2 completed")

	score_sorted = sorted(result.items(), key=lambda x:x[1], reverse=True)
	if len(score_sorted) > range1:
		score_sorted = score_sorted[:range1]

	encoder_string = ""
	for s in score_sorted:
		#print(s[0] + " " + str(s[1]))
		encoder_string += s[0]

	outfile = open("scripts/titles.js", 'w')
	for c in titles_js:
		if unicodedata.east_asian_width(c) == "Na" or c == '\n':
			outfile.write(c)
		elif c in encoder_string:
			outfile.write(to_base64_special(encoder_string.index(c)))
		else:
			outfile.write(c)
	outfile.close()
	print("STEP4-3 completed")

	outfile = open("scripts/descriptions.js", 'w')
	for c in descriptions_js:
		if unicodedata.east_asian_width(c) == "Na" or c == '\n':
			outfile.write(c)
		elif c in encoder_string:
			outfile.write(to_base64_special(encoder_string.index(c)))
		else:
			outfile.write(c)
	outfile.close()
	print("STEP4-4 completed")


	# encoder.js作成

	while len(encoder_string) < range1:
		encoder_string += "あ"
	encoder_string2 = encoder_string2.replace(" ","")
	while len(encoder_string2) < range2:
		encoder_string2 += "ああ"
	encoder_string3 = encoder_string3.replace(" ","")
	while len(encoder_string3) < range3:
		encoder_string3 += "あああ"

	outfile = open("scripts/decoder.js", 'w')
	outfile.write("var decoder1=\"" + encoder_string + "\";\nvar decoder2=\"" + encoder_string2 + "\";\nvar decoder3=\"" + encoder_string3 + "\";\n")
	outfile.close()

	#print(score_sorted3)
	#print(score_sorted2)
	#print(score_sorted)
