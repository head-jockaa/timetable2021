import os
import util

patch_rule = []

def read_patch_file(year, month, day):
	global patch_rule

	patch_file = []
	path = year + "/" + month + "/" + day + "/" + year + "_" + month + "_" + day + "_patch.txt"
	if os.path.exists(path):
		f = open(path, 'r')
		a = f.read()
		patch_file = a.split("\n")
		f.close()
	else:
		patch_file = []

	patch_rule = []
	hit = False
	stations = ""
	for line in patch_file:
		if line.startswith(">"):
			stations = line.split(" ")[1:]
		elif line.startswith("add"):
			time = line.split(" ")[1]
			patch_rule.append({"stations":stations, "action":"add","time":time,"code":"","title":"","desc":"","interval":0})
		elif line.startswith("modify"):
			splited = line.split(" ")
			time = splited[1]
			if len(splited) == 3:
				new_time = splited[2]
			else:
				new_time = None
			patch_rule.append({"stations":stations, "action":"modify","time":time,"new_time":new_time,"code":None,"title":None,"desc":None,"interval":None})
		elif line.startswith("delete"):
			time = line.split(" ")[1]
			patch_rule.append({"stations":stations, "action":"delete","time":time, "interval":None})
		elif line.startswith("code"):
			code = line.split(" ")[1]
			patch_rule[-1]["code"] = code
		elif line.startswith("title"):
			title = util.sanitize(" ".join(line.split(" ")[1:]))
			patch_rule[-1]["title"] = title
		elif line.startswith("desc"):
			desc = util.sanitize(" ".join(line.split(" ")[1:]))
			patch_rule[-1]["desc"] = desc
		elif line.startswith("interval"):
			interval = line.split(" ")[1]
			patch_rule[-1]["interval"] = (int)(interval)

def add(station, pre_start_time, start_time):
	if pre_start_time == None:
		pre_start_time = "0000"
	if start_time == None:
		start_time = "3000"
	if pre_start_time > start_time:
		pre_start_time = "0000"

	result = []
	for rule in patch_rule:
		if station in rule["stations"] and rule["action"] == "add" and rule["time"] > pre_start_time and rule["time"] < start_time:
			result.append({"time":rule["time"], "code":rule["code"], "title":rule["title"], "desc":rule["desc"], "interval":rule["interval"]})

	result_sorted = sorted(result, key=lambda x:x["time"], reverse=False)
	return result_sorted

def pad(station, start_time):
	for rule in patch_rule:
		if station in rule["stations"] and rule["action"] == "add" and rule["time"] == start_time:
			return rule["time"], rule["code"], rule["title"], rule["desc"], rule["interval"]
	return None, None, None, None, None

def modify(station, start_time):
	for rule in patch_rule:
		if station in rule["stations"] and rule["action"] == "modify" and rule["time"] == start_time:
			return rule["new_time"], rule["code"], rule["title"], rule["desc"], rule["interval"]
	return None, None, None, None, None

def delete(station, start_time):
	for rule in patch_rule:
		if station in rule["stations"] and rule["action"] == "delete" and rule["time"] == start_time:
			return True, rule["interval"]
	return False, None
