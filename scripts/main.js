var selected_tv = "";
var selected_year = 2021;
var selected_month = 4;
var selected_day = 1;
var selected_station = "";
var station_select_mode = "";
var adding_way_mode = 0;
var table_index = 0;
var hour_height = 3;
var hour_width = 200;
var font_size = 16;
var fix_hour_height = true;
var now_showing = Array();

var search_title = "";
var search_description = "";
var search_category = Array();
var search_month = Array();
var search_station = Array();
var mutable_station_form = Array();
var searching_month = 1;
var searching_day = 1;
var search_hits = 0;
var search_progress = 0;
var search_progress_max = 0;
var searching_process;

decoder1_range = decoder1.length;
decoder2_range = decoder2.length / 2;
decoder3_range = decoder3.length / 3;

// 時刻のdecodeに用いる60進数
var base60 = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"];
// チャプター番号のdecodeに用いる50進数
var base50 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x"];
// タイトル・番組概要のdecodeに用いる50進数
var base64_special = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","@","$","{","|","}",";","*","_","~","^","`","'"];

var date_list;

function create_calendar() {
	date_list = {};
	var column = 0;
	var row, days;
	for (var m = 1 ; m <= 12 ; m++) {
		column = 0;
		days = Array();
		row = Array();
		var startWeek = new Date(selected_year,m-1,1).getDay();
		for (var d = 0 ; d < startWeek ; d++) {
			row.push(0);
			column++;
		}
		var daysOfMonth = new Date(selected_year, m, 0).getDate();
		for (var d = 1 ; d <= daysOfMonth ; d++) {
			row.push(d);
			column++;
			if (column == 7) {
				days.push(row);
				row = Array();
				column = 0;
			}
		}
		if (row.length != 0) {
			days.push(row);
		}
		date_list[m] = days;
	}
}

var area_list = {
	10: "札幌",
	11: "函館",
	12: "旭川",
	13: "帯広",
	14: "釧路",
	15: "北見",
	16: "室蘭",
	22: "青森",
	20: "岩手",
	17: "宮城",
	18: "秋田",
	19: "山形",
	21: "福島",
	26: "茨城",
	28: "栃木",
	25: "群馬",
	29: "埼玉",
	27: "千葉",
	23: "東京",
	24: "神奈川",
	31: "新潟",
	37: "富山",
	34: "石川",
	36: "福井",
	32: "山梨",
	30: "長野",
	39: "岐阜",
	35: "静岡",
	33: "愛知",
	38: "三重",
	45: "滋賀",
	41: "京都",
	40: "大阪",
	42: "兵庫",
	44: "奈良",
	43: "和歌山",
	49: "鳥取",
	48: "島根",
	47: "岡山",
	46: "広島",
	50: "山口",
	53: "徳島",
	52: "香川",
	51: "愛媛",
	54: "高知",
	55: "福岡",
	61: "佐賀",
	57: "長崎",
	56: "熊本",
	60: "大分",
	59: "宮崎",
	58: "鹿児島",
	62: "沖縄"
}

var nhk_list = {
	G23: "NHK総合・東京",
	G10: "NHK総合・札幌",
	G11: "NHK総合・函館",
	G12: "NHK総合・旭川",
	G13: "NHK総合・帯広",
	G14: "NHK総合・釧路",
	G15: "NHK総合・北見",
	G16: "NHK総合・室蘭",
	G22: "NHK総合・青森",
	G20: "NHK総合・盛岡",
	G17: "NHK総合・仙台",
	G18: "NHK総合・秋田",
	G19: "NHK総合・山形",
	G21: "NHK総合・福島",
	G26: "NHK総合・水戸",
	G28: "NHK総合・宇都宮",
	G25: "NHK総合・前橋",
	G31: "NHK総合・新潟",
	G37: "NHK総合・富山",
	G34: "NHK総合・金沢",
	G36: "NHK総合・福井",
	G32: "NHK総合・甲府",
	G30: "NHK総合・長野",
	G39: "NHK総合・岐阜",
	G35: "NHK総合・静岡",
	G33: "NHK総合・名古屋",
	G38: "NHK総合・津",
	G45: "NHK総合・大津",
	G41: "NHK総合・京都",
	G40: "NHK総合・大阪",
	G42: "NHK総合・神戸",
	G44: "NHK総合・奈良",
	G43: "NHK総合・和歌山",
	G49: "NHK総合・鳥取",
	G48: "NHK総合・松江",
	G47: "NHK総合・岡山",
	G46: "NHK総合・広島",
	G50: "NHK総合・山口",
	G53: "NHK総合・徳島",
	G52: "NHK総合・高松",
	G51: "NHK総合・松山",
	G54: "NHK総合・高知",
	G55: "NHK総合・福岡",
	Gkk: "NHK総合・北九州",
	G61: "NHK総合・佐賀",
	G57: "NHK総合・長崎",
	G56: "NHK総合・熊本",
	G60: "NHK総合・大分",
	G59: "NHK総合・宮崎",
	G58: "NHK総合・鹿児島",
	G62: "NHK総合・沖縄"
};

var nhk_sub_list = {
	sG23: "NHK総合2・東京",
	sG10: "NHK総合2・札幌",
	sG11: "NHK総合2・函館",
	sG12: "NHK総合2・旭川",
	sG13: "NHK総合2・帯広",
	sG14: "NHK総合2・釧路",
	sG15: "NHK総合2・北見",
	sG16: "NHK総合2・室蘭",
	sG22: "NHK総合2・青森",
	sG20: "NHK総合2・盛岡",
	sG17: "NHK総合2・仙台",
	sG18: "NHK総合2・秋田",
	sG19: "NHK総合2・山形",
	sG21: "NHK総合2・福島",
	sG26: "NHK総合2・水戸",
	sG28: "NHK総合2・宇都宮",
	sG25: "NHK総合2・前橋",
	sG31: "NHK総合2・新潟",
	sG37: "NHK総合2・富山",
	sG34: "NHK総合2・金沢",
	sG36: "NHK総合2・福井",
	sG32: "NHK総合2・甲府",
	sG30: "NHK総合2・長野",
	sG39: "NHK総合2・岐阜",
	sG35: "NHK総合2・静岡",
	sG33: "NHK総合2・名古屋",
	sG38: "NHK総合2・津",
	sG45: "NHK総合2・大津",
	sG41: "NHK総合2・京都",
	sG40: "NHK総合2・大阪",
	sG42: "NHK総合2・神戸",
	sG44: "NHK総合2・奈良",
	sG43: "NHK総合2・和歌山",
	sG49: "NHK総合2・鳥取",
	sG48: "NHK総合2・松江",
	sG47: "NHK総合2・岡山",
	sG46: "NHK総合2・広島",
	sG50: "NHK総合2・山口",
	sG53: "NHK総合2・徳島",
	sG52: "NHK総合2・高松",
	sG51: "NHK総合2・松山",
	sG54: "NHK総合2・高知",
	sG55: "NHK総合2・福岡",
	sGkk: "NHK総合2・北九州",
	sG61: "NHK総合2・佐賀",
	sG57: "NHK総合2・長崎",
	sG56: "NHK総合2・熊本",
	sG60: "NHK総合2・大分",
	sG59: "NHK総合2・宮崎",
	sG58: "NHK総合2・鹿児島",
	sG62: "NHK総合2・沖縄"
};

var etv_list = {
	E23: "NHK教育・東京",
	E10: "NHK教育・札幌",
	E11: "NHK教育・函館",
	E12: "NHK教育・旭川",
	E13: "NHK教育・帯広",
	E14: "NHK教育・釧路",
	E15: "NHK教育・北見",
	E16: "NHK教育・室蘭",
	E22: "NHK教育・青森",
	E20: "NHK教育・盛岡",
	E17: "NHK教育・仙台",
	E18: "NHK教育・秋田",
	E19: "NHK教育・山形",
	E21: "NHK教育・福島",
	E31: "NHK教育・新潟",
	E37: "NHK教育・富山",
	E34: "NHK教育・金沢",
	E36: "NHK教育・福井",
	E32: "NHK教育・甲府",
	E30: "NHK教育・長野",
	E35: "NHK教育・静岡",
	E33: "NHK教育・名古屋",
	E40: "NHK教育・大阪",
	E49: "NHK教育・鳥取",
	E48: "NHK教育・松江",
	E47: "NHK教育・岡山",
	E46: "NHK教育・広島",
	E50: "NHK教育・山口",
	E53: "NHK教育・徳島",
	E52: "NHK教育・高松",
	E51: "NHK教育・松山",
	E54: "NHK教育・高知",
	E55: "NHK教育・福岡",
	Ekk: "NHK教育・北九州",
	E61: "NHK教育・佐賀",
	E57: "NHK教育・長崎",
	E56: "NHK教育・熊本",
	E60: "NHK教育・大分",
	E59: "NHK教育・宮崎",
	E58: "NHK教育・鹿児島",
	E62: "NHK教育・沖縄"
};

var etv_sub_list = {
	sE23: "NHK教育3・東京",
	sE10: "NHK教育3・札幌",
	sE11: "NHK教育3・函館",
	sE12: "NHK教育3・旭川",
	sE13: "NHK教育3・帯広",
	sE14: "NHK教育3・釧路",
	sE15: "NHK教育3・北見",
	sE16: "NHK教育3・室蘭",
	sE22: "NHK教育3・青森",
	sE20: "NHK教育3・盛岡",
	sE17: "NHK教育3・仙台",
	sE18: "NHK教育3・秋田",
	sE19: "NHK教育3・山形",
	sE21: "NHK教育3・福島",
	sE31: "NHK教育3・新潟",
	sE37: "NHK教育3・富山",
	sE34: "NHK教育3・金沢",
	sE36: "NHK教育3・福井",
	sE32: "NHK教育3・甲府",
	sE30: "NHK教育3・長野",
	sE35: "NHK教育3・静岡",
	sE33: "NHK教育3・名古屋",
	sE40: "NHK教育3・大阪",
	sE49: "NHK教育3・鳥取",
	sE48: "NHK教育3・松江",
	sE47: "NHK教育3・岡山",
	sE46: "NHK教育3・広島",
	sE50: "NHK教育3・山口",
	sE53: "NHK教育3・徳島",
	sE52: "NHK教育3・高松",
	sE51: "NHK教育3・松山",
	sE54: "NHK教育3・高知",
	sE55: "NHK教育3・福岡",
	sEkk: "NHK教育3・北九州",
	sE61: "NHK教育3・佐賀",
	sE57: "NHK教育3・長崎",
	sE56: "NHK教育3・熊本",
	sE60: "NHK教育3・大分",
	sE59: "NHK教育3・宮崎",
	sE58: "NHK教育3・鹿児島",
	sE62: "NHK教育3・沖縄"
};

var ntv_list = {
	NTV:"日本テレビ",
	YTV: "読売テレビ",
	CTV: "中京テレビ",
	STV: "札幌テレビ",
	RAB: "青森放送",
	ABS: "秋田放送",
	TVI: "テレビ岩手",
	YBC: "山形放送",
	MMT: "ミヤギテレビ",
	FCT: "福島中央テレビ",
	YBS: "山梨放送",
	TENY: "テレビ新潟",
	TSB: "テレビ信州",
	SDT: "静岡第一テレビ",
	KNB: "北日本放送",
	KTK: "テレビ金沢",
	FBC: "福井放送",
	RNC: "西日本放送",
	HTV: "広島テレビ",
	NKT: "日本海テレビ",
	KRY: "山口放送",
	JRT: "四国放送",
	RNB: "南海放送",
	RKC: "高知放送",
	FBS: "福岡放送",
	NIB: "長崎国際テレビ",
	KKT: "熊本県民テレビ",
	TOS: "テレビ大分",
	UMK: "テレビ宮崎",
	KYT: "鹿児島読売テレビ",
	ABS2: "秋田放送2",
	KYT3: "鹿児島読売テレビ3"
};

var tbs_list = {
	TBS: "TBSテレビ",
	MBS: "毎日放送",
	CBC: "中部日本放送",
	HBC: "北海道放送",
	ATV: "青森テレビ",
	IBC: "岩手放送",
	TUY: "テレビユー山形",
	TBC: "東北放送",
	TUF: "テレビユー福島",
	UTY: "テレビ山梨",
	BSN: "新潟放送",
	SBC: "信越放送",
	SBS: "静岡放送",
	TUT: "チューリップテレビ",
	MRO: "北陸放送",
	RSK: "山陽放送",
	RCC: "中国放送",
	BSS: "山陰放送",
	TYS: "テレビ山口",
	ITV: "あいテレビ",
	KUTV: "テレビ高知",
	RKB: "RKB毎日放送",
	NBC: "長崎放送",
	RKK: "熊本放送",
	OBS: "大分放送",
	MRT: "宮崎放送",
	MBC: "南日本放送",
	RBC: "琉球放送"
};

var cx_list = {
	CX: "フジテレビ",
	KTV: "関西テレビ",
	THK: "東海テレビ",
	UHB: "北海道文化放送",
	AKT: "秋田テレビ",
	MIT: "岩手めんこいテレビ",
	SAY: "さくらんぼテレビ",
	OX: "仙台放送",
	FTV: "福島テレビ",
	NST: "新潟総合テレビ",
	NBS: "長野放送",
	SUT: "テレビ静岡",
	BBT: "富山テレビ",
	ITC: "石川テレビ",
	FTB: "福井テレビ",
	OHK: "岡山放送",
	TSS: "テレビ新広島",
	TSK: "山陰中央テレビ",
	EBC: "テレビ愛媛",
	KSS: "高知さんさんテレビ",
	TNC: "テレビ西日本",
	STS: "サガテレビ",
	KTN: "テレビ長崎",
	TKU: "テレビ熊本",
	TOS: "テレビ大分",
	UMK: "テレビ宮崎",
	KTS: "鹿児島テレビ",
	OTV: "沖縄テレビ",
	TSK2: "山陰中央テレビ2",
};

var ex_list = {
	EX: "テレビ朝日",
	ABC: "朝日放送",
	NBN: "名古屋テレビ",
	HTB: "北海道テレビ",
	ABA: "青森朝日放送",
	AAB: "秋田朝日放送",
	IAT: "岩手朝日テレビ",
	YTS: "山形テレビ",
	KHB: "東日本放送",
	KFB: "福島放送",
	UX: "新潟テレビ21",
	ABN: "長野朝日放送",
	SATV: "静岡朝日テレビ",
	HAB: "北陸朝日放送",
	FBC: "福井放送",
	KSB: "瀬戸内海放送",
	HOME: "広島ホームテレビ",
	YAB: "山口朝日放送",
	EAT: "愛媛朝日テレビ",
	KBC: "九州朝日放送",
	NCC: "長崎文化放送",
	KAB: "熊本朝日放送",
	OAB: "大分朝日放送",
	UMK: "テレビ宮崎",
	KKB: "鹿児島放送",
	QAB: "琉球朝日放送",
	EX2: "テレビ朝日2",
};

var tx_list = {
	TX: "テレビ東京",
	TVO: "テレビ大阪",
	TVA: "テレビ愛知",
	TVH: "テレビ北海道",
	TSC: "テレビせとうち",
	TVQ: "TVQ九州放送",
};

var other_list = {
	MX: "TOKYO MX",
	MX2: "TOKYO MX2",
	TVK: "テレビ神奈川",
	TVS: "テレビ埼玉",
	CTC: "チバテレビ",
	CTC2: "チバテレビ2",
	GTV: "群馬テレビ",
	TTV: "とちぎテレビ",
	MTV: "三重テレビ",
	MTV2: "三重テレビ2",
	GBS: "岐阜放送",
	SUN: "サンテレビ",
	SUN2: "サンテレビ2",
	KBS: "KBS京都",
	BBC: "びわ湖放送",
	TVN: "奈良テレビ",
	WTV: "テレビ和歌山",
	CTC3: "チバテレビ3",
};

var bs_list = {
	BS1: "NHK BS1 (101)",
	NB2: "NHK BS1 (102)",
	BSp: "NHK BSプレミアム",
	BS4: "BS日テレ (141)",
	BN2: "BS日テレ (142)",
	BS6: "BS-TBS",
	BS8: "BSフジ",
	BS5: "BS朝日",
	BS7: "BSテレ東",
	WW1: "WOWOWプライム",
	WW2: "WOWOWライブ",
	WW3: "WOWOWシネマ",
	WW4: "WOWOWプラス",
	SC1: "スターチャンネル1",
	SC2: "スターチャンネル2",
	SC3: "スターチャンネル3",
	BS11: "BS11",
	BS12: "TwellV",
	OU1: "放送大学ex",
	OU2: "放送大学on",
	GCH: "グリーンチャンネル",
	BSA: "BSアニマックス",
	SKY: "BSスカパー!",
	JS1: "J SPORTS 1",
	JS2: "J SPORTS 2",
	JS3: "J SPORTS 3",
	JS4: "J SPORTS 4",
	BSF: "BS釣りビジョン",
	JMV: "BS日本映画専門チャンネル",
	DCH: "ディズニー・チャンネル",
	FK1: "NHK BS4K",
	FK4: "BS日テレ 4K",
	FK6: "BS-TBS 4K",
	FK8: "BSフジ 4K",
	FK5: "BS朝日 4K",
	FK7: "BSテレ東 4K",
	EK1: "NHK BS8K",
	FKW: "WOWOW 4K",
	FKS: "ショップチャンネル 4K",
	QVC: "4K QVC",
	FKC: "ザ・シネマ 4K"
};

/* 次の番組の開始時刻から、放映時間を求める(ただし同じ日付に限る) */
function get_interval(start_time_string, next_time_string) {
	var start_hour = parseInt(start_time_string.split(":")[0]);
	var start_minute = parseInt(start_time_string.split(":")[1]);
	var next_hour = parseInt(next_time_string.split(":")[0]);
	var next_minute = parseInt(next_time_string.split(":")[1]);
	var interval = 0;
	if (start_hour > next_hour) {
		interval = next_minute-60;
		next_minute = 0;
		start_hour--;
		interval += 60 * (next_hour - start_hour);
	}
	else if (start_hour < next_hour) {
		interval = 60-start_minute;
		start_minute = 0;
		start_hour++;
		interval += 60 * (next_hour - start_hour);
	}
	return interval + next_minute - start_minute;
}

function split_chunk(s) {
	var splited = Array();
	var index = 0;
	splited[0] = "";
	for (var i = 0 ; i < s.length ; i++) {
		if (s[i] == ":") {
			index--;
			splited.pop();
		}
		splited[index] += s[i];
		if (s[i] == "." || s[i] == ",") {
			index++;
			splited[index] = "";
		}
	}
	return splited;
}

/* キー局あるいはメインチャンネル番組表から同じ時刻の番組データを拾ってくる事により、省略されたchunkを復元する */
function fetch_from_key_station(month, day, s, chunk_string) {
	var keysta = "";
	if (s == "G10" || s == "G11" || s == "G12" || s == "G13" || s == "G14" || s == "G15" || s == "G16" || s == "G17" || s == "G18" || s == "G19" || s == "G20" || s == "G21" || s == "G22" || s == "G23" || s == "G25" || s == "G26" || s == "G28" || s == "G30" || s == "G31" || s == "G32" || s == "G33" || s == "G34" || s == "G35" || s == "G36" || s == "G37" || s == "G38" || s == "G39" || s == "G40" || s == "G41" || s == "G42" || s == "G43" || s == "G44" || s == "G45" || s == "G46" || s == "G47" || s == "G48" || s == "G49" || s == "G50" || s == "G51" || s == "G52" || s == "G53" || s == "G54" || s == "G55" || s == "G56" || s == "G57" || s == "G58" || s == "G59" || s == "G60" || s == "G61" || s == "G62" || s == "Gkk") {
		keysta = "G23";
	}
	else if (s == "E10" || s == "E11" || s == "E12" || s == "E13" || s == "E14" || s == "E15" || s == "E16" || s == "E17" || s == "E18" || s == "E19" || s == "E20" || s == "E21" || s == "E22" || s == "E23" || s == "E30" || s == "E31" || s == "E32" || s == "E33" || s == "E34" || s == "E35" || s == "E36" || s == "E37" || s == "E40" || s == "E46" || s == "E47" || s == "E48" || s == "E49" || s == "E50" || s == "E51" || s == "E52" || s == "E53" || s == "E54" || s == "E55" || s == "E56" || s == "E57" || s == "E58" || s == "E59" || s == "E60" || s == "E61" || s == "E62" || s == "Ekk") {
		keysta = "E23";
	}
	else if (s == "YTV" || s == "CTV" || s == "STV" || s == "RAB" || s == "ABS" || s == "TVI" || s == "YBC" || s == "MMT" || s == "FCT" || s == "YBS" || s == "TENY" || s == "TSB" || s == "SDT" || s == "KNB" || s == "KTK" || s == "FBC" || s == "RNC" || s == "HTV" || s == "NKT" || s == "KRY" || s == "JRT" || s == "RNB" || s == "RKC" || s == "FBS" || s == "NIB" || s == "KKT" || s == "KYT") {
		keysta = "NTV";
	}
	else if (s == "MBS" || s == "CBC" || s == "HBC" || s == "ATV" || s == "IBC" || s == "TUY" || s == "TBC" || s == "TUF" || s == "UTY" || s == "BSN" || s == "SBC" || s == "SBS" || s == "TUT" || s == "MRO" || s == "RSK" || s == "RCC" || s == "BSS" || s == "TYS" || s == "ITV" || s == "KUTV" || s == "RKB" || s == "NBC" || s == "RKK" || s == "OBS" || s == "MRT" || s == "MBC" || s == "RBC") {
		keysta = "TBS";
	}
	else if (s == "KTV" || s == "THK" || s == "UHB" || s == "AKT" || s == "MIT" || s == "SAY" || s == "OX" || s == "FTV" || s == "NST" || s == "NBS" || s == "SUT" || s == "BBT" || s == "ITC" || s == "FTB" || s == "OHK" || s == "TSS" || s == "TSK" || s == "EBC" || s == "KSS" || s == "TNC" || s == "STS" || s == "KTN" || s == "TKU" || s == "KTS" || s == "OTV") {
		keysta = "CX";
	}
	else if (s == "ABC" || s == "NBN" || s == "HTB" || s == "ABA" || s == "AAB" || s == "IAT" || s == "YTS" || s == "KHB" || s == "KFB" || s == "UX" || s == "ABN" || s == "SATV" || s == "HAB" || s == "KSB" || s == "HOME" || s == "YAB" || s == "EAT" || s == "KBC" || s == "NCC" || s == "KAB" || s == "OAB" || s == "KKB" || s == "QAB" || s == "EX2") {
		keysta = "EX";
	}
	else if (s == "TVO" || s == "TVA" || s == "TVH" || s == "TSC" || s == "TVQ") {
		keysta = "TX";
	}
	else if (s == "CTC2" || s == "CTC3") {
		keysta = "CTC";
	}
	else if (s == "MTV2") {
		keysta = "MTV";
	}
	else if (s == "SUN2") {
		keysta = "SUN";
	}
	else if (s == "NB2") {
		keysta = "BS1";
	}
	else if (s == "BN2" || s == "FK4") {
		keysta = "BS4";
	}
	else if (s == "FK5") {
		keysta = "BS5";
	}
	else if (s == "FK6") {
		keysta = "BS6";
	}
	else if (s == "FK7") {
		keysta = "BS7";
	}
	else if (s == "FK8") {
		keysta = "BS8";
	}

	var keystas_table = Array();
	var keysta_string = "";
	if (timetables[month] && timetables[month][day]) {
		if (s.indexOf("sG") == 0 && timetables[month][day][s.substring(1)]) {
			if (s == "sG23") {
				keysta_string = timetables[month][day]["G23"];
			} else {
				keysta_string = fetch_from_key_station(month, day, s.substring(1), timetables[month][day][s.substring(1)]);
			}
		}
		else if (s.indexOf("sE") == 0 && timetables[month][day][s.substring(1)]) {
			if (s == "sE23") {
				keysta_string = timetables[month][day]["E23"];
			} else {
				keysta_string = fetch_from_key_station(month, day, s.substring(1), timetables[month][day][s.substring(1)]);
			}
		}
		else if (s == "ABS2") {
			keysta_string = fetch_from_key_station(month, day, "ABS", timetables[month][day]["ABS"]);
		}
		else if (s == "TSK2") {
			keysta_string = fetch_from_key_station(month, day, "TSK", timetables[month][day]["TSK"]);
		}
		else if (s == "KYT3") {
			keysta_string = fetch_from_key_station(month, day, "KYT", timetables[month][day]["KYT"]);
		}
		else if (timetables[month][day][keysta]) {
			keysta_string = timetables[month][day][keysta];
		}
	}
	var splitedColon = keysta_string.split(":");
	keystas_table = split_chunk(splitedColon[0]);

	var result = Array();
	var chunks = split_chunk(chunk_string);
	for (var c = 0 ; c < chunks.length ; c++) {
		var splitedColon = chunks[c].split(":");
		var chunk = splitedColon[0];

		var splited_by_space = (chunk[chunk.length-1] == ",");
		chunk = chunk.substring(0, chunk.length-1);

		// フォーマット2
		if (chunk.length <= 2) {
			// キー局からフォーマット1のデータを得る
			for (var k = 0 ; k < keystas_table.length ; k++) {
				if (chunk == keystas_table[k].substring(0,2)) {
					result.push(keystas_table[k]);
					break;
				}
			}
		}
		// フォーマット3
		else if (chunk.indexOf('*') != -1) {
			var splited = chunk.split("*");
			// キー局からフォーマット1のデータを得る
			for (var i = 0 ; i < keystas_table.length ; i++) {
				var hit = false;
				if (splited[0] == keystas_table[i].substring(0,2)) {
					hit = true;
					// desc_id を付け替える
					for (var k = keystas_table[i].length - 2 ; k >= 0 ; k--) {
						if (!(keystas_table[i].charAt(k) >= '0' && keystas_table[i].charAt(k) <= '9')) {
							result.push(keystas_table[i].substring(0, k + 1) + splited[1] + keystas_table[i].substring(keystas_table[i].length-1));
							break;
						}
					}
				}
				if (hit) break;
			}
		}
		// フォーマット4
		else if (chunk.indexOf('-') != -1) {
			var splited = chunk.split("-");
			// キー局からフォーマット1のデータを得る
			var start = false;
			for (var k = 0 ; k < keystas_table.length ; k++) {
				if (splited[0] == keystas_table[k].substring(0,2)) {
					start = true;
				}
				if (start) {
					result.push(keystas_table[k]);
				}
				if (splited[1] == keystas_table[k].substring(0,2)) {
					break;
				}
			}
		}
		// フォーマット5
		else if (chunk.indexOf('^') != -1) {
			// キー局のサブチャンネルからフォーマット1のデータを得る
			var keysta_sub_string = "";
			if (s.indexOf("sG") == 0 && timetables[month][day]["sG23"]) {
				keysta_sub_string = timetables[month][day]["sG23"];
				keysta_sub_string = fetch_from_key_station(month, day, "G23", keysta_sub_string);
			}
			else if (s.indexOf("sE") == 0 && timetables[month][day]["sE23"]) {
				keysta_sub_string = timetables[month][day]["sE23"];
				keysta_sub_string = fetch_from_key_station(month, day, "E23", keysta_sub_string);
			}
			var splitedColon_sub = keysta_sub_string.split(":");
			var keystas_sub_table = split_chunk(splitedColon_sub[0]);
			for (var k = 0 ; k < keystas_sub_table.length ; k++) {
				if (chunk.substring(0,2) == keystas_sub_table[k].substring(0,2)) {
					result.push(keystas_sub_table[k]);
					break;
				}
			}
		}
		// フォーマット1
		else {
			result.push(chunk + (splited_by_space ? "," : "."));
		}
	}

	return result.join("") + ":" + chunk_string.split(":")[1];
}

function get_tv_by_area(area) {
	var keys;
	switch (area) {
		case "10": keys = ["G10","E10","STV","HBC","UHB","HTB","TVH"]; break;
		case "11": keys = ["G11","E11","STV","HBC","UHB","HTB","TVH"]; break;
		case "12": keys = ["G12","E12","STV","HBC","UHB","HTB","TVH"]; break;
		case "13": keys = ["G13","E13","STV","HBC","UHB","HTB","TVH"]; break;
		case "14": keys = ["G14","E14","STV","HBC","UHB","HTB","TVH"]; break;
		case "15": keys = ["G15","E15","STV","HBC","UHB","HTB","TVH"]; break;
		case "16": keys = ["G16","E16","STV","HBC","UHB","HTB","TVH"]; break;
		case "22": keys = ["G22","E22","RAB","ATV","ABA"]; break;
		case "20": keys = ["G20","E20","TVI","IBC","MIT","IAT"]; break;
		case "17": keys = ["G17","E17","MMT","TBC","OX","KHB"]; break;
		case "18": keys = ["G18","E18","ABS","AKT","AAB"]; break;
		case "19": keys = ["G19","E19","YBC","TUY","SAY","YTS"]; break;
		case "21": keys = ["G21","E21","FCT","TUF","FTV","KFB"]; break;
		case "26": keys = ["G26","E23","NTV","TBS","CX","EX","TX"]; break;
		case "28": keys = ["G28","E23","NTV","TBS","CX","EX","TX","TTV"]; break;
		case "25": keys = ["G25","E23","NTV","TBS","CX","EX","TX","GTV"]; break;
		case "29": keys = ["G23","E23","NTV","TBS","CX","EX","TX","TVS"]; break;
		case "27": keys = ["G23","E23","NTV","TBS","CX","EX","TX","CTC","CTC2"]; break;
		case "23": keys = ["G23","E23","NTV","TBS","CX","EX","TX","MX","MX2"]; break;
		case "24": keys = ["G23","E23","NTV","TBS","CX","EX","TX","TVK"]; break;
		case "31": keys = ["G31","E31","TENY","BSN","NST","UX"]; break;
		case "37": keys = ["G37","E37","KNB","TUT","BBT"]; break;
		case "34": keys = ["G34","E34","KTK","MRO","ITC","HAB"]; break;
		case "36": keys = ["G36","E36","FBC","FTB"]; break;
		case "32": keys = ["G32","E32","YBS","UTY"]; break;
		case "30": keys = ["G30","E30","TSB","SBC","NBS","ABN"]; break;
		case "39": keys = ["G39","E33","CTV","CBC","THK","NBN","GBS"]; break;
		case "35": keys = ["G35","E35","SDT","SBS","SUT","SATV"]; break;
		case "33": keys = ["G33","E33","CTV","CBC","THK","NBN","TVA"]; break;
		case "38": keys = ["G38","E33","CTV","CBC","THK","NBN","MTV","MTV2"]; break;
		case "45": keys = ["G45","E40","YTV","MBS","KTV","ABC","BBC"]; break;
		case "41": keys = ["G41","E40","YTV","MBS","KTV","ABC","KBS"]; break;
		case "40": keys = ["G40","E40","YTV","MBS","KTV","ABC","TVO"]; break;
		case "42": keys = ["G42","E40","YTV","MBS","KTV","ABC","SUN","SUN2"]; break;
		case "44": keys = ["G44","E40","YTV","MBS","KTV","ABC","TVN"]; break;
		case "43": keys = ["G43","E40","YTV","MBS","KTV","ABC","WTV"]; break;
		case "49": keys = ["G49","E49","NKT","BSS","TSK"]; break;
		case "48": keys = ["G48","E48","NKT","BSS","TSK"]; break;
		case "47": keys = ["G47","E47","RNC","RSK","OHK","KSB","TSC"]; break;
		case "46": keys = ["G46","E46","HTV","RCC","TSS","HOME"]; break;
		case "50": keys = ["G50","E50","KRY","TYS","YAB"]; break;
		case "53": keys = ["G53","E53","JRT"]; break;
		case "52": keys = ["G52","E52","RNC","RSK","OHK","KSB","TSC"]; break;
		case "51": keys = ["G51","E51","RNB","ITV","EBC","EAT"]; break;
		case "54": keys = ["G54","E54","RKC","KUTV","KSS"]; break;
		case "55": keys = ["G55","E55","FBS","RKB","TNC","KBC","TVQ","Gkk","Ekk"]; break;
		case "61": keys = ["G61","E61","STS"]; break;
		case "57": keys = ["G57","E57","NIB","NBC","KTN","NCC"]; break;
		case "56": keys = ["G56","E56","KKT","RKK","TKU","KAB"]; break;
		case "60": keys = ["G60","E60","OBS","TOS","OAB"]; break;
		case "59": keys = ["G59","E59","MRT","UMK"]; break;
		case "58": keys = ["G58","E58","KYT","MBC","KTS","KKB"]; break;
		case "62": keys = ["G62","E62","RBC","OTV","QAB"]; break;
		default: break;
	}
	return keys;
}

/* この地域のテレビ番組表をまとめて表示 */
function add_tv_area(area) {
	remove_modal();
	var keys = get_tv_by_area(area);
	for (var i = 0 ; i < keys.length ; i++) {
		add_tv(keys[i]);
	}
	remove_modal();
}

function get_tv_by_net(net) {
	var keys;
	switch (net) {
		case "NHK": keys = Object.keys(nhk_list); break;
		case "NHK2": keys = Object.keys(nhk_sub_list); break;
		case "ETV": keys = Object.keys(etv_list); break;
		case "ETV3": keys = Object.keys(etv_sub_list); break;
		case "NTV": keys = Object.keys(ntv_list); break;
		case "TBS": keys = Object.keys(tbs_list); break;
		case "CX": keys = Object.keys(cx_list); break;
		case "EX": keys = Object.keys(ex_list); break;
		case "TX": keys = Object.keys(tx_list); break;
		case "OTHER": keys = Object.keys(other_list); break;
		case "BS": keys = Object.keys(bs_list); break;
		default: break;
	}
	return keys;
}

/* 同じ系列のテレビ番組表をまとめて表示 */
function add_tv_net(tv) {
	remove_modal();
	var keys = get_tv_by_net(tv);
	for (var i = 0 ; i < keys.length ; i++) {
		add_tv(keys[i]);
	}
	remove_modal();
}

/* timetable.jsのデータ読み込み */
function decompressProgramChunk(month, day, tv, chunk_string) {
	// フォーマット1 (例: 8FAB37CFB126.)
	// 最初の2文字は固定。3文字目以降は英字、数字、英字、数字という順に並べてあり、文字種の違いが区切りを表す。
	// チャンク1 (例では8F) は開始時刻を表す2文字で、1文字目が「時」2文字目が「分」を示す。字数を減らすための60進数表記にしてある。
	// チャンク2 (例ではAB) は再放送や字幕放送などのアイコンを表す文字で、複数並べられる。どの文字が何を表すかは type_names.js による。何も無い場合は省略でき、3文字目が数字ならアイコン無しと解釈する。
	// チャンク3 (例では37) は番組名を表す数値で、titles.js の行数と一致する。
	// チャンク4 (例ではCFB) はジャンルとチャプターを表す文字列。1文字目と2文字目は省略不可でジャンルを表す。どの文字が何のジャンルを表すかは categories.js による。3文字目以降は省略可能でチャプター番号を表す50進数。
	// チャンク5 (例では126) は番組概要を表す数値で、descriptions.js の行数と一致する。デフォルトは0。

	// フォーマット2 (例: BP.)
	// 開始時刻を表す2文字のみ。キー局の同じ時刻の番組と全く同じ情報であることを意味する。
	// サブチャンネルの場合は、同じ局のメインチャンネルの同じ時刻の番組を参照する。

	// フォーマット3 (例: OP*8113.)
	// アスタリスクで区切り、左側は開始時刻を表す2文字で、右側は番組概要を表す数値になる。キー局(またはサブチャンネル)との同時放映ではあるが、番組表の概要の文章に違いがある場合。

	// フォーマット4 (例: 70-DP.)
	// 「フォーマット2」が3つ以上連続する場合、間を全てハイフンひとつで省略できる。

	// フォーマット5 (例: EK^.)
	// NHK地上波サブチャンネルのみで使用。NHK高校講座ばかりで文字数が増えてしまうのを避けるためだけに用意した。
	// メインチャンネルではなく東京キー局サブチャンネルから、同じ時刻の番組情報を参照することを表す。

	// フォーマット6 (例: QU?.)
	// この時間には番組情報がない事を表す。

	// また、1日の最後の番組データには RvA41B0.:23 などのように、コロン記号の後に放映時間を添えてある。

	// ピリオド(.)またはコンマ(,)は末尾を表す区切り文字。ただしフォーマット1でコンマの場合は、番組名とチャプターを半角スペースで区切るという意味も表す。

	var result = Array();
	var full_chunk_string = fetch_from_key_station(month, day, tv, chunk_string);
	var chunks = split_chunk(full_chunk_string);
	for (var i = 0 ; i < chunks.length ; i++) {
		var splitedColon = chunks[i].split(":");
		var chunk = splitedColon[0];
		result.push(decompress(chunk));
		// デバッグ用
		result[result.length-1].original_chunk = chunks[i];
	}

	// 放映時間を計算する
	for (var i = 0 ; i < result.length - 1 ; i++) {
		if (i == 0 && result[i].start_time > result[i+1].start_time) {
			result[i].interval = get_interval(result[i].start_time, "24:00") + get_interval("00:00", result[i+1].start_time);
		} else {
			result[i].interval = get_interval(result[i].start_time, result[i+1].start_time);
		}
	}
	result[result.length-1].interval = chunk_string.split(":")[1];

	return result;
}

function decompress(chunk) {
	if (!chunk) {
		return {};
	}

	var pointer = 0;
	var start_time = "";
	var title_id = "";
	var chapter_id = 0;
	var category_id = "";
	var sub_category_id = "";
	var desc_id = "";
	var types = Array();

	var splited_by_space = (chunk[chunk.length-1] == ",");
	chunk = chunk.substring(0,chunk.length-1);

	// 開始時刻
	var hour = base60.indexOf(chunk.charAt(0));
	pointer++;
	var minute = base60.indexOf(chunk.charAt(1));
	pointer++;
	start_time = (hour < 10 ? "0" : "") + hour + ":" + (minute < 10 ? "0" : "") + minute;

	if (chunk.charAt(pointer) == "?") {
		// 番組情報なし
		return {
			start_time: start_time,
			nodata: true
		}
	} else {

		// アイコン
		for (var c = pointer ; c < chunk.length ; c++) {
			if (chunk.charAt(c) >= '0' && chunk.charAt(c) <= '9') {
				break;
			}
			types.push(chunk.charAt(c));
			pointer++;
		}

		// 題名
		for (var c = pointer ; c < chunk.length ; c++) {
			if (!(chunk.charAt(c) >= '0' && chunk.charAt(c) <= '9')) {
				break;
			}
			title_id += chunk.charAt(c);
			pointer++;
		}

		// ジャンル
		category_id = chunk.charAt(pointer);
		pointer++;
		sub_category_id = chunk.charAt(pointer);
		pointer++;

		// チャプター
		if (chunk.charAt(pointer) >= '0' && chunk.charAt(pointer) <= '9') {
			chapter_id = -1;
		} else {
			for (var c = pointer ; c < chunk.length ; c++) {
				if (chunk.charAt(c) >= '0' && chunk.charAt(c) <= '9') {
					break;
				}
				chapter_id = chapter_id * 50 + base50.indexOf(chunk.charAt(c));
				pointer++;
			}
		}

		// 概要
		desc_id = chunk.substring(pointer);

		return {
			start_time: start_time,
			types: types,
			title_id: parseInt(title_id),
			chapter_id: chapter_id,
			category_id: category_id,
			sub_category_id: sub_category_id,
			desc_id: parseInt(desc_id),
			title: typeof titles != "undefined" ? decode_string(titles[title_id][0]) : "",
			chapter: typeof titles != "undefined" && titles[title_id].length == 2 && chapter_id != -1 ? decode_string(titles[title_id][1][chapter_id]) : "",
			description: typeof descriptions != "undefined" ? decode_string(descriptions[desc_id]) : "",
			splited_by_space: splited_by_space,
			nodata: false
		};
	}
}

/* タイトルや番組概要の復元 */
function decode_string(s) {
	// titles.js および descriptions.js は独自の2バイト文字コードに圧縮されている。
	// 「半角英字および使用頻度の低い記号による2文字」は独自の64進数で、decoder.jsに書いてある単語のいくつ目と置き換えるかを表す。
	// decoder.js に収容できる単語は4096個までで、そこに入り切らなかった文字はそのままになっている。
	// 他の半角記号・半角数字は何の変換もせず、そのままになっている。
	// < > で囲まれた半角英字は、変換せずにそのまま出力する。（半角記号 < > は文章に使わない前提として、全角記号の＜＞に置き換えてある）

	var result = "";
	var in_abc_mode = false;
	for (var i = 0 ; i < s.length ; i++) {
		if(s.charAt(i) == '\n') {
			result += '<br />';
		}
		else if (in_abc_mode) {
			if (s.charAt(i) == '>') {
				in_abc_mode = false;
			} else {
				result += s.charAt(i);
			}
		} else {
			if (s.charAt(i) == '<') {
				in_abc_mode = true;
			}
			else if (base64_special.indexOf(s.charAt(i)) != -1) {
				var code = base64_special.indexOf(s.charAt(i)) * 64 + base64_special.indexOf(s.charAt(i+1));
				if (code < decoder1_range) {
					result += decoder1.charAt(code);
				}
				else if (code < decoder1_range + decoder2_range) {
					result += decoder2.charAt((code - decoder1_range)*2) + decoder2.charAt((code - decoder1_range)*2+1);
				} else {
					result += decoder3.charAt((code - decoder1_range - decoder2_range)*3) + decoder3.charAt((code - decoder1_range - decoder2_range)*3+1) + decoder3.charAt((code - decoder1_range - decoder2_range)*3+2);
				}
				i++;
			} else {
				result += s.charAt(i);
			}
		}
	}
	return result;
}

/* 番組表右上のxボタンを押した時 */
function remove_tv(n) {
	var a = document.getElementById("tv" + n);
	a.remove();
	a = document.getElementById("head" + n);
	a.remove();
	delete now_showing[n];
}

function slide_yesterday(tv, month, day, insert) {
	day--;
	if (day == 0) {
		day = new Date(selected_year, month-1, 0).getDate();
		month--;
	}
	if (month == 0) {
		return;
	}
	add_tv(tv, month, day, insert);
}

function slide_tomorrow(tv, month, day, insert) {
	day++;
	if (day > new Date(selected_year, month, 0).getDate()) {
		day = 1;
		month++;
	}
	if (month == 13) {
		return;
	}
	add_tv(tv, month, day, insert);
}

function wide_cell(e) {
	if (!fix_hour_height) return;
	var test1 = e.cloneNode(true);
	test1.style.width=hour_width + "px";
	test1.style.height = "auto";
	test1.children[0].style.height = "auto";
	document.getElementById("sizetest").appendChild(test1);
	var autoSize = document.getElementById("sizetest").children[0].getBoundingClientRect();
	document.getElementById("sizetest").children[0].remove();
	if (autoSize.height > e.clientHeight) {
		e.style.height = autoSize.height + "px";
		e.children[0].style.height = autoSize.height + "px";
	}
}

function narrow_cell(e) {
	if (!fix_hour_height) return;
	e.style.height = (parseInt(e.attributes["value"].nodeValue) * hour_height * 60 / 60) + "px";
	e.children[0].style.height = "100%";
}

/* テレビ局名の取得 */
function get_station_name(tv) {
	var station_name = nhk_list[tv];
	if(!station_name)station_name = nhk_sub_list[tv];
	if(!station_name)station_name = etv_list[tv];
	if(!station_name)station_name = etv_sub_list[tv];
	if(!station_name)station_name = ntv_list[tv];
	if(!station_name)station_name = tbs_list[tv];
	if(!station_name)station_name = cx_list[tv];
	if(!station_name)station_name = ex_list[tv];
	if(!station_name)station_name = tx_list[tv];
	if(!station_name)station_name = other_list[tv];
	if(!station_name)station_name = bs_list[tv];
	if(!station_name)return "";
	return station_name;
}

function render_program_cell(program, fs) {
	var html = '';

	// debug
	//html += '<div style="color:black;font-size:0.7em;font-family:sans-serif;">' + program.original_chunk + '</div>';

	// 開始時刻
	html += '<span class="program_time" style="font-size:' + fs + 'px;">' + program.start_time + '</span>';

	// アイコン
	for (var j = 0 ; j < program.types.length ; j++) {
		var class_name = "";
		switch (type_names[program.types[j]].icon) {
			case "新": class_name = "icon_new"; break;
			case "再": class_name = "icon_re"; break;
			case "終": class_name = "icon_end"; break;
			default: break;
		}
		html += '<div class="program_icon ' + class_name + '" style="font-size:' + fs + 'px;min-width:' + fs + 'px;height:' + fs + 'px;line-height:' + (fs*1.2) + 'px;">' + type_names[program.types[j]].icon + '</div>';
	}

	// 番組名
	html += '<span class="program_title" style="font-size:' + fs + 'px;">' +  program.title + '</span>';
	if (program.chapter != "") {
		if (program.splited_by_space) {
			html += ' ';
		}
		html += '<span class="program_chapter" style="font-size:' + fs + 'px;">' + program.chapter + '</span>';
	}
	html += '<br />';

	// 番組概要
	html += '<span class="program_desc" style="font-size:' + (fs*0.9) + 'px;">' + program.description + '</span>';

	// ジャンル
	if (!(program.category_id == "H" && program.sub_category_id == "C")) {
		html += '<br /><span class="program_category" style="font-size:' + (fs*0.9) + 'px;">' + categories[program.category_id] + '</span>';
	}
	html += '<br /><span class="program_sub_category" style="font-size:' + (fs*0.9) + 'px;">' + sub_categories[program.category_id][program.sub_category_id] + '</span>';

	return html;
}

/* 番組表の作成 */
function add_tv(tv, month, day, insert) {
	var programs = [];

	if (typeof month == "undefined") {
		month = selected_month;
	}
	if (typeof day == "undefined") {
		day = selected_day;
	}

	if (typeof timetables != "undefined") {
		var monthTables = timetables[month];
		if (monthTables) {
			var dayTables = monthTables[day];
			if (dayTables) {
				var StationTables = dayTables[tv];
				if (StationTables) {
					programs = decompressProgramChunk(month, day, tv, timetables[month][day][tv]);
				}
			}
		}
	}

	var top_space = 0;
	table_index++;

	// テレビ局名のヘッダ
	var station_name = get_station_name(tv);
	var fontclass = station_name.length > 8 ? "station_font_small" : "station_font";
	var result = '<div id="head' + table_index + '" class="tv_table_header">';
	result += '<div class="tv_table_header_date">';
	result += '<button class="tv_table_header_date_button" onClick="slide_yesterday(\'' + tv + '\',' + month + ',' + day + ',' + table_index + ')">▲</button>';
	result += month + '月' + day + '日';
	result += '<button class="tv_table_header_date_button" onClick="slide_tomorrow(\'' + tv + '\',' + month + ',' + day + ',' + table_index + ')">▼</button>';
	result += '</div>';
	result += '<div class="tv_table_header_station_name ' + fontclass + '">' + station_name + '</div>';
	result += '<button class="tv_table_header_close_button" onclick="remove_tv(' + table_index + ')" style="position:absolute;top:0px;right:0px;">x</button>';
	result += '</div>';

	if (typeof insert == "undefined") {
		document.getElementById("headers").insertAdjacentHTML("beforeend", result);
	} else {
		document.getElementById("head" + insert).insertAdjacentHTML("afterend", result);
	}

	// 最初の番組が4:00ちょうどから始まらない場合、頭の空白の縦幅を求める
	if (programs.length > 1 && programs[0].start_time > programs[1].start_time) {
		top_space = -240 - get_interval(programs[0].start_time, "24:00");
	}
	else if (programs.length > 0) {
		top_space = get_interval("4:00", programs[0].start_time);
	}

	// ここから番組表
	result = '<div id="tv' + table_index + '" value="' + (top_space >= 0 ? top_space : 0) + '" class="tv_table" style="padding-bottom:15em;display:inline-block;white-space:normal;vertical-align:top;">';

	if (programs.length > 0) {
		for (var i = 0 ; i < programs.length ; i++) {
			var cell_height = programs[i].interval;

			// 開始時刻が午前4時より前の場合、表示調整
			if (i == 0 && top_space < 0) {
				cell_height += top_space;
			}
			if (cell_height <= 0) {
				cell_height = 1;
			}

			if (programs[i].nodata) {
				result += '<div class="table_cell" value="' + cell_height + '" onmouseover="wide_cell(this)" onmouseout="narrow_cell(this)" style="transition: all 0.1s linear;">';
				result += '<div class="table_cell_inner table_cell_nodata" style="overflow:hidden;transition: all 0.1s linear;">';
				result += '<span class="program_time" style="font-size:' + font_size + 'px;">' + programs[i].start_time + '</span>';
				result += '<br /><span class="program_category" style="font-size:' + (font_size*0.9) + 'px;">データなし</span>';
				result += '</div></div>';
			} else {
				// ジャンルによる背景色
				var class_name = "";
				switch (programs[i].category_id) {
					case "A": class_name = "table_cell_news"; break;
					case "B": class_name = "table_cell_sports"; break;
					case "C": class_name = "table_cell_information"; break;
					case "D": class_name = "table_cell_drama"; break;
					case "E": class_name = "table_cell_music"; break;
					case "F": class_name = "table_cell_variety"; break;
					case "G":
						if (programs[i].sub_category_id == "C") {
							class_name = "table_cell_anime";
						} else {
							class_name = "table_cell_movie";
						}
						break;
					case "H":
						if (programs[i].sub_category_id == "C") {
							class_name = "table_cell_drama";
						} else {
							class_name = "table_cell_anime";
						}
						break;
					case "I": class_name = "table_cell_documentary"; break;
					case "J": class_name = "table_cell_theater"; break;
					case "K": class_name = "table_cell_education"; break;
					case "L": class_name = "table_cell_welfare"; break;
					default: break;
				}

				// show_program_modal() に与える引数
				var types_string = "";
				for (var j = 0 ; j < programs[i].types.length ; j++) {
					types_string += "【" + type_names[programs[i].types[j]].name + "】";
				}
				var args = "'" + station_name + "','" + programs[i].title.replace("'", "\\'") + "','" + programs[i].chapter.replace("'", "\\'") + "','" + month + "','" + day + "','" + programs[i].start_time + "','" + programs[i].interval + "','" + types_string + "','" + programs[i].category_id + "','" + programs[i].sub_category_id + "','" + programs[i].description.replace("'", "\\'") + "'";

				result += '<div class="table_cell" value="' + cell_height + '" onclick="show_program_modal(' + args + ')" onmouseover="wide_cell(this)" onmouseout="narrow_cell(this)" style="transition: all 0.1s linear;">';
				result += '<div class="table_cell_inner ' + class_name + '" style="overflow:hidden;transition: all 0.1s linear;">';

				result += render_program_cell(programs[i], font_size);

				result += '</div></div>';
			}

		}

	}
	result += "</div>";

	if (typeof insert == "undefined") {
		document.getElementById("new_table").insertAdjacentHTML("beforebegin", result);
	} else {
		document.getElementById("tv" + insert).insertAdjacentHTML("afterend", result);
		remove_tv(insert);
	}

	adjust_height(fix_hour_height);
	adjust_width();
	now_showing[table_index] = {tv:tv, month:month, day:day};
}

/* fix=trueの場合は時間ごとの縦幅を統一する、fix=falseの場合は縦幅の指定を無くす */
function adjust_height(fix) {
	var headers = document.getElementsByClassName("tv_table_header");
	var tables = document.getElementsByClassName("tv_table");
	var cells = document.getElementsByClassName("table_cell");
	var cell_inners = document.getElementsByClassName("table_cell_inner");
	var hour_bar_cells = document.getElementsByClassName("hour_bar_cell");

	if (fix) {
		for(var i = 0 ; i < headers.length ; i++) {
			var value = parseInt(tables[i].getAttribute("value"));
			tables[i].style.paddingTop = (value * hour_height * 60 / 60) + "px";
		}
		for(var i = 0 ; i < cells.length ; i++) {
			var value = parseInt(cells[i].getAttribute("value"));
			cells[i].style.height = (value * hour_height * 60 / 60) + "px";
			cell_inners[i].style.height = "100%";
		}
		for(var i = 0 ; i < hour_bar_cells.length ; i++) {
			hour_bar_cells[i].style.height = (hour_height * 60 - 2) + "px";
			hour_bar_cells[i].style.display = "block";
		}
	} else {
		for(var i = 0 ; i < tables.length ; i++) {
			tables[i].style.paddingTop = "0px";
		}
		for(var i = 0 ; i < cells.length ; i++) {
			cells[i].style.height = "auto";
			cell_inners[i].style.height = "auto";
		}
		for(var i = 0 ; i < hour_bar_cells.length ; i++) {
			hour_bar_cells[i].style.display = "none";
		}
	}
}

function adjust_width() {
	var headers = document.getElementsByClassName("tv_table_header");
	var tables = document.getElementsByClassName("tv_table");
	var station_font = document.getElementsByClassName("station_font");
	var station_font_small = document.getElementsByClassName("station_font_small");
	var fontsize = 1.5 * hour_width / 200;
	for(var i = 0 ; i < headers.length ; i++) {
		headers[i].style.width = hour_width + "px";
	}
	for(var i = 0 ; i < tables.length ; i++) {
		tables[i].style.width = hour_width + "px";
	}
	for(var i = 0 ; i < station_font.length ; i++) {
		station_font[i].style.fontSize = fontsize + "em";
	}
	for(var i = 0 ; i < station_font_small.length ; i++) {
		station_font_small[i].style.fontSize = (fontsize * 0.8) + "em";
	}
	document.getElementById("tables").style.width = ((tables.length + 1) * hour_width + 32) + "px";
}

function change_fix_hour_height(checked) {
	fix_hour_height = checked;
	adjust_height(fix_hour_height);
}

function change_hour_height(value) {
	hour_height = value;
	adjust_height(fix_hour_height);
}

function change_hour_width(value) {
	hour_width = value;
	adjust_width(fix_hour_height);
}

function change_font_size(value) {
	font_size = value;
	var times = document.getElementsByClassName("program_time");
	var icons = document.getElementsByClassName("program_icon");
	var title_names = document.getElementsByClassName("program_title");
	var chapters = document.getElementsByClassName("program_chapter");
	var descs = document.getElementsByClassName("program_desc");
	var tags = document.getElementsByClassName("program_category");
	var sub_tags = document.getElementsByClassName("program_sub_category");
	for(var i = 0 ; i < times.length ; i++) {
		times[i].style.fontSize = font_size + "px";
	}
	for(var i = 0 ; i < icons.length ; i++) {
		icons[i].style.fontSize = font_size + "px";
		icons[i].style.width = font_size + "px";
		icons[i].style.height = font_size + "px";
		icons[i].style.lineHeight = (font_size*1.2) + "px";
	}
	for(var i = 0 ; i < title_names.length ; i++) {
		title_names[i].style.fontSize = font_size + "px";
	}
	for(var i = 0 ; i < chapters.length ; i++) {
		chapters[i].style.fontSize = font_size + "px";
	}
	for(var i = 0 ; i < descs.length ; i++) {
		descs[i].style.fontSize = (font_size*0.9) + "px";
	}
	for(var i = 0 ; i < tags.length ; i++) {
		tags[i].style.fontSize = (font_size*0.9) + "px";
	}
	for(var i = 0 ; i < sub_tags.length ; i++) {
		sub_tags[i].style.fontSize = (font_size*0.9) + "px";
	}
}

function remove_modal() {
	clearInterval(searching_process);
	var modal = document.getElementById("modal");
	if (modal) {
		modal.remove();
	}
}

/* 番組をクリックした時に見せる */
function show_program_modal(station_name, title, chapter, month, day, start_time, interval, types, category_id, sub_category_id, description) {
	remove_modal();
	var html = '';

	var category_name = "";
	if (category_id == "H" && sub_category_id == "C") {
		category_name = sub_categories[category_id][sub_category_id];
	} else {
		category_name = categories[category_id] + ' - ' + sub_categories[category_id][sub_category_id];
	}

	html += '<div id="modal" style="text-align:center;background-color:white;color:black;width:30%;height:80%;white-space:normal;position:fixed;left:35%;top:10%;">';
	html += '<div style="height:2.8em;"><button class="btn btn--green btn--emboss btn--cubic" onclick="remove_modal()">閉じる</button><hr /></div><div style="overflow-y:scroll;width:100%;height:calc(100% - 2.8em);">';
	html += '<table border="1" style="color:black;margin:auto;">';
	html += '<tr><th>放送局</th><td>' + station_name + '</td></tr>';
	html += '<tr><th>番組名</th><td>' + title + '</td></tr>';
	html += '<tr><th>副題</th><td>' + chapter + '</td></tr>';
	html += '<tr><th>開始時刻</th><td>' + month + '月' + day + '日' + ' ' + start_time + '</td></tr>';
	//html += '<tr><th>放映時間</th><td>' + interval + '分</td></tr>';
	html += '<tr><th>放映形態</th><td>' + types + '</td></tr>';
	html += '<tr><th>ジャンル</th><td>' + category_name + '</td></tr>';
	html += '<tr><th>番組概要</th><td>' + description + '</td></tr>';
	html += '</table>';
	html += '</div></div>';

	document.getElementById("tables").insertAdjacentHTML("beforeend", html);
}



/*
 * モーダル
 */

function on_click_station(station_key) {
	selected_station = station_key;
	if (adding_way_mode == 0) {
		add_tv(station_key);
	}
	document.getElementById("click_calendar_label").innerHTML = "日付ボタンを押して" + get_station_name(selected_station) + "番組表を追加";
	show_tv_menu(station_select_mode);
	show_calendar();
}

function on_click_calendar(month, day) {
	selected_month = month;
	selected_day = day;
	if (adding_way_mode == 1 && selected_station != "") {
		add_tv(selected_station);
	}
	document.getElementById("click_station_label").innerHTML = "放送局ボタンを押して" + selected_month + "月" + selected_day + "日の番組表を追加";
	show_calendar();
}

function show_tv_menu(group_name) {
	station_select_mode = group_name;
	var html = '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_area_menu()">戻る</button>';
	if (group_name == "NHK") {
		keys = Object.keys(nhk_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + nhk_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'NHK\')">全部並べる</button>';
	}
	else if (group_name == "NHK2") {
		keys = Object.keys(nhk_sub_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + nhk_sub_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'NHK2\')">全部並べる</button>';
	}
	else if (group_name == "ETV") {
		keys = Object.keys(etv_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + etv_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'ETV\')">全部並べる</button>';
	}
	else if (group_name == "ETV3") {
		keys = Object.keys(etv_sub_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + etv_sub_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'ETV3\')">全部並べる</button>';
	}
	else if (group_name == "NTV") {
		keys = Object.keys(ntv_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + ntv_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'NTV\')">全部並べる</button>';
	}
	else if (group_name == "TBS") {
		keys = Object.keys(tbs_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + tbs_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'TBS\')">全部並べる</button>';
	}
	else if (group_name == "CX") {
		keys = Object.keys(cx_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + cx_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'CX\')">全部並べる</button>';
	}
	else if (group_name == "EX") {
		keys = Object.keys(ex_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + ex_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'EX\')">全部並べる</button>';
	}
	else if (group_name == "TX") {
		keys = Object.keys(tx_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + tx_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'TX\')">全部並べる</button>';
	}
	else if (group_name == "OTHER") {
		keys = Object.keys(other_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + other_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'OTHER\')">全部並べる</button>';
	}
	else if (group_name == "BS") {
		keys = Object.keys(bs_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn ';
			if (keys[i] == selected_station) {
				html += 'btn--blue btn--emboss btn--cubic';
			} else {
				html += 'btn--green btn--emboss btn--cubic';
			}
			html += '" onclick="on_click_station(\'' + keys[i] + '\')">' + bs_list[keys[i]] + '</button>';
		}
		html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_net(\'BS\')">全部並べる</button>';
	}
	else if (group_name == "AREA") {
		keys = Object.keys(area_list);
		for (var i = 0 ; i < keys.length ; i++) {
			html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="add_tv_area(\'' + keys[i] + '\')">' + area_list[keys[i]] + '</button>';
		}
	}
	document.getElementById("area_menu").innerHTML = html;
}

/* 放送局メニューのHTMLを出力 */
function show_area_menu() {
	station_select_mode = "";
	var html = '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'NHK\')">NHK総合から選ぶ</i></button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'NHK2\')">NHK総合2から選ぶ</i></button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'ETV\')">NHK教育から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'ETV3\')">NHK教育3から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'NTV\')">日テレ系から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'TBS\')">TBS系から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'CX\')">フジ系から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'EX\')">テレ朝系から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'TX\')">テレ東系から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'OTHER\')">独立局から選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'BS\')">BSデジタルから選ぶ</button>';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="show_tv_menu(\'AREA\')">地域から選ぶ</button>';
	document.getElementById("area_menu").innerHTML = html;
}

/* 日付選択のHTMLを出力 */
function show_calendar() {
	var html = "";
	for (var month = 1 ; month <= 12 ; month++) {
		html += '<h2>' + month + '月</h2>';
		html += '<table border="1" style="margin:auto;text-align:center;">';
		for (var i = 0 ; i < date_list[month].length ; i++) {
			html += '<tr>';
			for (var j = 0 ; j < date_list[month][i].length ; j++) {
				html += '<td style="width:3em;">';
				if (date_list[month][i][j] != 0) {
					var day = date_list[month][i][j];
					if (
						typeof timetables[month] != "undefined" &&
						typeof timetables[month][day] != "undefined" &&
						(selected_station == "" || (typeof timetables[month][day][selected_station] != "undefined" && timetables[month][day][selected_station] != ""))
					) {
						html += '<button class="btn ';
						if (month == selected_month && day == selected_day) {
							html += 'btn--blue btn--emboss btn--cubic';
						} else {
							html += 'btn--green btn--emboss btn--cubic';
						}
						html += '" onclick="on_click_calendar(' + month + ',' + day + ');">' + day + '</button>';
					} else {
						html += '<span style="font-size:1.5em;color:black;">' + day + '</span>';
					}
				}
				html += '</td>';
			}
			html += '</tr>';
		}
		html += '</table>';
	}
	document.getElementById("calendar_menu").innerHTML = html;
}

function on_click_adding_way() {
	var mode0 = document.adding_way_form.adding_way[0].checked;
	var mode1 = document.adding_way_form.adding_way[1].checked;
	if (mode0) {
		adding_way_mode = 0;
	}
	else if (mode1) {
		adding_way_mode = 1;
	}
}

/* 「クリックして番組表を追加」をクリックした時に見せる */
function show_menu_modal() {
	remove_modal();
	var html = '<div id="modal" class="menu_modal" style="white-space:normal;position:fixed;">';

	html += '<div style="height:3.2em;">';
	html += '<button class="btn btn--green btn--emboss btn--cubic" style="float:right;" onclick="remove_modal()">閉じる</button>';
	html += '<form name="adding_way_form">';
	html += '<input id="click_station" name="adding_way" type="radio" onclick="on_click_adding_way()" /><label id="click_station_label" for="click_station" />放送局ボタンを押して' + selected_month + '月' + selected_day + '日の番組表を追加</label><br />';
	html += '<input id="click_calendar" name="adding_way" type="radio" onclick="on_click_adding_way()" /><label id="click_calendar_label" for="click_calendar">日付ボタンを押して' + get_station_name(selected_station) + '番組表を追加</label>';
	html += '</form>';
	html += '<div style="clear:both;"></div></div>';
	html += '<div style="width:100%;height:calc(100% - 3.2em);">';

	html += '<table style="height:100%;"><tbody style="height:100%;"><tr><td style="width:70%;height:100%;"><div id="area_menu" style="overflow-y:scroll;width:100%;height:100%;">';

	html += '</div></td><td style="height:100%;"><div id="calendar_menu" class="calendar_menu" style="overflow-y:scroll;width:100%;height:100%;color:black;text-align:center;">';

	html += '</div></td></tr></tbody></table>';

	html += '</div></div>';

	document.getElementById("tables").insertAdjacentHTML("beforeend", html);
	show_area_menu();
	show_calendar();

	document.adding_way_form.adding_way[0].checked = adding_way_mode == 0;
	document.adding_way_form.adding_way[1].checked = adding_way_mode == 1;
}



/*
 * 検索機能
 */

function save_search_form() {
	search_title = document.getElementById("search_title").value;
	search_description = document.getElementById("search_description").value;
	var menu = document.category_form.search_category;
	search_category = Array();
	for(var i=0 ; i<menu.length ; i++) {
		if(menu[i].checked) {
			search_category.push(menu[i].value);
		}
	}
	menu = document.month_form.search_month;
	search_month = Array();
	for(var i=0 ; i<menu.length ; i++) {
		if(menu[i].checked) {
			search_month.push(menu[i].value);
		}
	}
	menu = document.station_form.search_station;
	search_station = Array();
	if (menu) {
		for(var i=0 ; i<menu.length ; i++) {
			if(menu[i].checked) {
				search_station.push(menu[i].value);
			}
		}
	}
}

function restore_search_form() {
	document.getElementById("search_title").value = search_title;
	document.getElementById("search_description").value = search_description;
	var menu = document.category_form.search_category;
	for(var i=0 ; i<menu.length ; i++) {
		if(search_category.indexOf(menu[i].value) != -1) {
			menu[i].checked = true;
		}
	}
	menu = document.month_form.search_month;
	for(var i=0 ; i<menu.length ; i++) {
		if(search_month.indexOf(menu[i].value) != -1) {
			menu[i].checked = true;
		}
	}
	var html = '';
	for(var i=0 ; i<mutable_station_form.length ; i++) {
		var checked = search_station.indexOf(mutable_station_form[i]) != -1 ? "checked" : "";
		html += '<input id="station_' + mutable_station_form[i] + '" type="checkbox" name="search_station" value="' + mutable_station_form[i] + '" ' + checked + ' /><label for="station_' + mutable_station_form[i] + '">' + get_station_name(mutable_station_form[i]) + '</label>';
	}
	document.getElementById("mutable_station_form").insertAdjacentHTML("beforeend", html);
}

function searching() {
	if (search_month.indexOf(searching_month+"") == -1){
		if(searching_month==12){
			clearInterval(searching_process);
			return;
		}
		searching_month++;
		searching_day=1;
		return;
	}

	var result = search(searching_month, searching_day);
	searching_day++;
	search_progress++;

	document.getElementById("search_result").insertAdjacentHTML("beforeend", result);
	document.getElementById("search_hits").innerHTML = document.getElementById("search_result").children.length + "件";
	document.getElementById("search_progress").style.width = Math.round(100*search_progress/search_progress_max) + "%";

	if(searching_day==32) {
		if(searching_month==12){
			clearInterval(searching_process);
			return;
		}
		searching_month++;
		searching_day=1;
	}
}

function sanitize_search_string(str) {
	return str.trim()
		.replace(/[Ａ-Ｚａ-ｚ０-９]/g, function(s) {
			return String.fromCharCode(s.charCodeAt(0) - 0xFEE0);
		})
		.replace(/\s+/g," ")
		.replace("～","〜");
}

function search(month,day) {
	var html = "";
	if (timetables[month] && timetables[month][day]) {
		var keys = Object.keys(timetables[month][day]);
		for (var tv=0 ; tv<=keys.length ; tv++) {
			if (search_station.indexOf(keys[tv]) == -1) continue;
			var station_name = get_station_name(keys[tv]);
			if (timetables[month][day][keys[tv]]) {
				var result = decompressProgramChunk(month, day, keys[tv], timetables[month][day][keys[tv]]);
				for (var r=0 ; r<result.length ; r++) {
					if (search_category.indexOf("H") != -1 && result[r].category_id == "G" && result[r].sub_category_id == "C"); // 「映画/アニメ」はアニメ扱いする
					else if (search_category.indexOf("D") != -1 && result[r].category_id == "H" && result[r].sub_category_id == "C"); // 「特撮」はドラマ扱いする
					else if (search_category.indexOf("H") != -1 && result[r].category_id == "H" && result[r].sub_category_id == "C")continue; // 「特撮」はドラマ扱いする
					else if (search_category.indexOf(result[r].category_id) == -1) continue;
					var splited = sanitize_search_string(search_title).split(" ");
					var notfound = false;
					if (splited[0] != "") {
						var full_title = result[r].title + result[r].chapter;
						for (var s=0 ; s<splited.length ; s++) {
							if (full_title.toLowerCase().indexOf(splited[s].toLowerCase()) == -1) notfound = true;
						}
					}
					if (notfound) continue;
					splited = sanitize_search_string(search_description).split(" ");
					if (splited[0] != "") {
						for (var s=0 ; s<splited.length ; s++) {
							if (result[r].description.toLowerCase().indexOf(splited[s].toLowerCase()) == -1) notfound = true;
						}
					}
					if (notfound) continue;
					html += '<table border="1" style="width:100%;"><tr><td style="width:30%;">';
					html += '<div style="color:green;font-weight:bold;">' + month + '月' + day + '日' + '</div><div style="color:black;">' + station_name + '</div>';
					html += '</td><td style="width:70%;">';
					html += render_program_cell(result[r], 16);
					html += '</td></tr></table>';
				}
			}
		}
	}
	return html;
}

function search_result_modal() {
	save_search_form();
	remove_modal();

	var html = '<div id="modal" style="text-align:center;background-color:white;color:black;width:50%;height:80%;white-space:normal;position:fixed;left:20%;top:10%;">';

	html += '<div style="height:3.7em;">';
	html += '<table style="width:100%;"><tr><td style="width:5em;">';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="open_search_modal()">戻る</button>';
	html += '</td><td style="text-align:center;color:black;">';
	html += '<span id="search_hits"></span>';
	html += '<div style="background-color:#80ff80; width:90%;height:0.3em;"><div id="search_progress" style="background-color:#008000;width:0%;height:0.3em;"></div></div>';
	html += '</td><td style="width:5em;">';
	html += '<button class="btn btn--green btn--emboss btn--cubic" onclick="remove_modal()">閉じる</button>';
	html += '</td></tr></table><hr />';
	html += '</div>';
	html += '<div id="search_result" style="overflow-y:scroll;width:100%;height:calc(100% - 3.7em);">';

	html += '</div></div>';
	document.getElementById("tables").insertAdjacentHTML("beforeend", html);

	search_progress = 0;
	search_progress_max = 0;
	for (var m = 1 ; m <= 12 ; m++) {
		if (search_month.indexOf(m+"") != -1) {
			var daysOfMonth = new Date(selected_year, m, 0).getDate();
			search_progress_max += daysOfMonth;
		}
	}

	searching_month=1;
	searching_day=1;
	search_hits = 0;
	searching_process = setInterval("searching()",10);
}

function mutate_station_form1() {
	var index = document.net_form.search_net.selectedIndex;
	if(index == 0)return;
	var selected = document.net_form.search_net.options[index].value;
	var tv = get_tv_by_net(selected);
	var html = '';
	for (var i=0 ; i<tv.length ; i++) {
		if (mutable_station_form.indexOf(tv[i]) == -1) {
			html += '<input id="station_' + tv[i] + '" type="checkbox" name="search_station" value="' + tv[i] + '" checked /><label for="station_' + tv[i] + '">' + get_station_name(tv[i]) + '</label>';
			mutable_station_form.push(tv[i]);
		}
	}
	document.getElementById("mutable_station_form").insertAdjacentHTML("beforeend", html);
}

function mutate_station_form2() {
	var index = document.area_form.search_area.selectedIndex;
	if(index == 0)return;
	var selected = document.area_form.search_area.options[index].value;
	var tv = get_tv_by_area(selected);
	var html = '';
	for (var i=0 ; i<tv.length ; i++) {
		if (mutable_station_form.indexOf(tv[i]) == -1) {
			html += '<input id="station_' + tv[i] + '" type="checkbox" name="search_station" value="' + tv[i] + '" checked /><label for="station_' + tv[i] + '">' + get_station_name(tv[i]) + '</label>';
			mutable_station_form.push(tv[i]);
		}
	}
	document.getElementById("mutable_station_form").insertAdjacentHTML("beforeend", html);
}

function check_category_form() {
	var menu = document.category_form.search_category;
	for(var i=0 ; i<menu.length ; i++) {
		menu[i].checked = true;
	}
}

function uncheck_category_form() {
	var menu = document.category_form.search_category;
	for(var i=0 ; i<menu.length ; i++) {
		menu[i].checked = false;
	}
}

function check_month_form() {
	var menu = document.month_form.search_month;
	for(var i=0 ; i<menu.length ; i++) {
		menu[i].checked = true;
	}
}

function uncheck_month_form() {
	var menu = document.month_form.search_month;
	for(var i=0 ; i<menu.length ; i++) {
		menu[i].checked = false;
	}
}

function check_mutate_station_form() {
	var menu = document.station_form.search_station;
	if (menu) {
		for(var i=0 ; i<menu.length ; i++) {
			menu[i].checked = true;
		}
	}
}

function uncheck_mutate_station_form() {
	var menu = document.station_form.search_station;
	if (menu) {
		for(var i=0 ; i<menu.length ; i++) {
			menu[i].checked = false;
		}
	}
}

function clear_mutate_station_form() {
	document.getElementById("mutable_station_form").innerHTML = "";
	mutable_station_form = Array();
	document.net_form.search_net.selectedIndex = 0;
	document.area_form.search_area.selectedIndex = 0;
}

function open_search_modal() {
	remove_modal();

	var html = '<div id="modal" style="text-align:center;white-space:normal;position:fixed;" class="search_modal">';
	html += '<div style="height:2.3em;"><button class="btn btn--green btn--emboss btn--cubic" style="float:right;" onclick="save_search_form();remove_modal();">閉じる</button><hr style="clear:both;" /></div>';
	html += '<div style="overflow-y:scroll;width:100%;height:calc(100% - 2.3em);">';

	html += '<table border="1" style="color:black;">';

	html += '<tr><td width="20%">ジャンル<br />';
	html += '<button onClick="check_category_form()">全て選択</button><br />';
	html += '<button onClick="uncheck_category_form()">全て解除</button></td>';
	html += '<td><form name="category_form">';
	var keys = Object.keys(categories);
	for (var c=0 ; c<keys.length ; c++) {
		html += '<input id="category_' + keys[c] + '" type="checkbox" name="search_category" value="' + keys[c] + '" /><label for="category_' + keys[c] + '">' + categories[keys[c]] + '</label>';
	}
	html += '</form></td></tr>';

	html += '<tr><td>シーズン<br />';
	html += '<button onClick="check_month_form()">全て選択</button><br />';
	html += '<button onClick="uncheck_month_form()">全て解除</button></td>';
	html += '<td><form name="month_form">';
	for (var m=1 ; m<=12 ; m++) {
		html += '<input id="month_' + m + '" type="checkbox" name="search_month" value="' + m + '" /><label for="month_' + m + '">' + m + '月</label>';
	}
	html += '</form></td></tr>';

	html += '<tr><td>テレビ局<br />';
	html += '<button onClick="check_mutate_station_form()">全て選択</button><br />';
	html += '<button onClick="uncheck_mutate_station_form()">全て解除</button><br />';
	html += '<button onClick="clear_mutate_station_form()">クリア</button></td>';
	html += '<td><table border="1" style="color:black;"><tr><td>系列から選ぶ<form name="net_form"><select name="search_net" onChange="mutate_station_form1()">';
	html += '<option value=""></option>';
	html += '<option value="NHK">NHK総合</option>';
	html += '<option value="NHK2">NHK総合2</option>';
	html += '<option value="ETV">NHK教育</option>';
	html += '<option value="ETV3">NHK教育3</option>';
	html += '<option value="NTV">日本テレビ系</option>';
	html += '<option value="TBS">TBSテレビ系</option>';
	html += '<option value="CX">フジテレビ系</option>';
	html += '<option value="EX">テレビ朝日系</option>';
	html += '<option value="TX">テレビ東京系</option>';
	html += '<option value="OTHER">独立局</option>';
	html += '<option value="BS">BSデジタル</option>';
	html += '</select></form></td>';
	html += '<td>地域から選ぶ<form name="area_form"><select name="search_area" onChange="mutate_station_form2()">';
	html += '<option value=""></option>';
	keys = Object.keys(area_list);
	for (var a=0 ; a<keys.length ; a++) {
		html += '<option value="' + keys[a] + '">' + area_list[keys[a]] + '</option>';
	}
	html += '</select></form></td></tr></table>';
	html += '<form name="station_form" id="mutable_station_form"></form>';
	html += '</td></tr>';

	var expl = '<br />半角スペースで複数キーワード検索可能。<br />空欄の場合は絞り込まない。';
	html += '<tr><td>番組名</td><td><input id="search_title" type="text" />' + expl + '</td></tr>';
	html += '<tr><td>番組概要</td><td><input id="search_description" type="text" />' + expl + '</td></tr>';

	html += '</table>';

	html += '<button class="btn btn--green btn--emboss btn--cubic" onClick="search_result_modal()">検索</button>';

	html += '</div></div>';
	document.getElementById("tables").insertAdjacentHTML("beforeend", html);
	restore_search_form();
}

function slide_yesterday_all() {
	now_showing_clone = now_showing.concat();
	var keys = Object.keys(now_showing_clone);
	for (var i = 0 ; i < keys.length ; i++) {
		slide_yesterday(now_showing_clone[keys[i]].tv, now_showing_clone[keys[i]].month, now_showing_clone[keys[i]].day, keys[i]);
	}
}

function slide_tomorrow_all() {
	now_showing_clone = now_showing.concat();
	var keys = Object.keys(now_showing_clone);
	for (var i = 0 ; i < keys.length ; i++) {
		slide_tomorrow(now_showing_clone[keys[i]].tv, now_showing_clone[keys[i]].month, now_showing_clone[keys[i]].day, keys[i]);
	}
}

function clear_all_tables() {
	var html = '<div id="new_table" style="width:200px;height:400px;border:1px dotted;display: inline-block;vertical-align:top;" onclick="show_menu_modal()">';
	html += '<div style="font-size:5em;text-align:center;">+</div>クリックして番組表を追加';
	html += '</div>';

	document.getElementById("headers").innerHTML = "";
	document.getElementById("tables").innerHTML = html;
	now_showing.length=0;
}

function setup_first_table() {
	var html = '';

	html += '<button onClick="open_search_modal()">検索</button>';
	html += '<button onClick="clear_all_tables()">クリア</button><br />';

	// 「縦幅の調整」チェックボックス
	html += '<input type="checkbox" id="fix_hour_height" onchange="change_fix_hour_height(checked)" checked></input><label for="fix_hour_height">縦幅の調整</label> / ';
	// 縦幅
	html += '<input type="number" id="hour_height" onchange="change_hour_height(value)" value="' + hour_height + '"></input>倍の縦幅';
	// 横幅
	html += ' : 横幅<input type="number" id="hour_width" onchange="change_hour_width(value)" value="' + hour_width + '"></input>px';
	// 文字サイズ
	html += ' : 文字サイズ<input type="number" step="1" id="font_size" onchange="change_font_size(value)" value="' + font_size + '"></input>px';

	html += '<div style="white-space: nowrap;">';

	// 左端の時刻バー
	html += '<div id="hour_bar" style="vertical-align:top;float:left;">';

	html += '<div id="hour_bar_header" style="vertical-align:top;">';
	html += '<button class="tv_table_header_date_button" onClick="slide_yesterday_all()">▲</button><br />';
	html += '<button class="tv_table_header_date_button" onClick="slide_tomorrow_all()">▼</button>';
	html += '</div>';

	html += '<div id="hour_bar_wrapper" style="width:auto;height:75%;overflow-y:scroll;overflow-x:hidden;">';
	for (var i = 4 ; i <= 29 ; i++) {
		html += '<div class="hour_bar_cell" style="display: none;height:' + (hour_height * 60) + 'px;"><div style="height:100%;">' + i + '</div></div>';
	}
	html += '</div>';
	html += '</div>';
	html += '<div id="headers_wrapper" style="width:calc(100% - 30px);overflow-x:scroll;float:left;">';

	// 番組表ヘッダを表示する場所
	html += '<div id="headers"></div><div style="clear:both;"></div>';

	// 番組表を表示する場所
	html += '<div id="tables" style="width:auto;height:75%;overflow-y:scroll;overflow-x:hidden;">';
	html += '</div><div style="clear:both;"></div>';

	html += '</div><div style="clear:both;"></div>';

	html += '</div>';

	html += '<div id="sizetest" style="position:absolute;top:0;left:0;"></div>';
	document.getElementById("app").innerHTML = html;

	// 番組表追加ボタンの表示
	clear_all_tables();

	// スクロール同期
	var func = function() {
		document.getElementById("hour_bar_wrapper").scrollTop = document.getElementById("tables").scrollTop;
	};
	setInterval(func, 100);
}

function init() {
	create_calendar();
	setup_first_table();
	//test();
}

function test() {
	var test_string = "", test_target = "MBS";
	var test_result = {};
	for(var m=1 ; m<=12 ; m++) {
		if (!timetables[m])continue;
		for(var d=1 ; d<=31 ; d++) {
			if (!timetables[m][d])continue;
			if (timetables[m][d][test_target]) {
				var splited = split_chunk(timetables[m][d][test_target].split(":")[0]);
				for (var s = 0 ; s<splited.length ; s++) {
					if (splited[s] == "" || splited[s].length == 3 || splited[s][2] == "-" || splited[s][2] == "*")continue;
					var dc = decompress(splited[s]);
					if (!test_result[dc.title]) {
						test_result[dc.title] = [];
					}
					test_result[dc.title].push(dc.chapter);
				}
			}
		}
	}

	var result_keys = Object.keys(test_result).sort();
	for (var k = 0 ; k<result_keys.length ; k++) {
		test_string += '<div style="background-color:#8080ff;font-size:1.0em;color:white;">' + result_keys[k] + '</div>';
		test_string += '<div style="background-color:#c0c0ff;font-size:0.7em;color:black;">';
		var result_sets = Array.from(new Set(test_result[result_keys[k]]));
		for (var k2 = 0 ; k2<result_sets.length ; k2++) {
			if (result_sets[k2] == "")continue;
			test_string += result_sets[k2] + "<br>";
		}
		test_string += '</div>';
	}

	document.getElementById("test").innerHTML = test_string;
}

init();
