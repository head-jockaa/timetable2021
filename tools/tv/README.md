jsファイルの作り方
==

次の２つを実行してJSファイルを作成します。  
pythonコマンドはバージョン3系です。  

```
python 01_title.py
python 02_table.py
python 03_encode.py
```

`01_title.py` では先に `titles_raw.js` および `descriptions_raw.js` を作成します。この時、出現頻度の高い物に対しては、できるだけ桁数の小さいIDを与えます。  
`02_table.py` で `timetables.js` を作成します。  
最後に `03_encode.py` で容量をさらに縮めた `titles.js` および `descriptions.js` を作成します。

JSファイルに取り込み済みのデータについては、次を実行して最低限のHTMLを復元する事もできます。

```
python 00_restore.py
```

サンプル
==

`2021.7z` を展開してフォルダ `2021` を配置します。  
五輪や大雨でNHK番組表がぐっちゃぐちゃになった2021年8月8日の物です。  
パッチファイル `2021/08/08/2021_08_08_patch.txt` による番組表の修正もあります。

HTMLファイルの配置方法
==

HTMLの取得方法は各自に任せます。  
以下に示すURLおよび保存先は2021年1月1日の例なので、目的の日付へと適宜読み替えてください。

* 各地域の主なチャンネルの番組表

※ 早朝5時で日付を区切ります。時間が早すぎると放送予定の変更やニュース番組の概要などを正しく得られないので、当日深夜のデータ取得が望ましいです。  
※ 生中継番組の欠落がよく発生しています(特にNHKとWOWOW)。予定より早く終了して穴埋め番組を入れる際に起こりやすいようです。早めに公式サイトなどから情報を得て補いましょう。  
※ NHKは地域ごとにローカル枠が存在するので、全ての地域をチェックしましょう。北海道のNHKも稀に室蘭限定とか道北限定とかの番組があったりします。

| 地域 | URL | 保存先 |
| --- | --- | --- |
| 札幌 | `https://www.tvkingdom.jp/chart/10.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_10.html` |
| 函館 | `https://www.tvkingdom.jp/chart/11.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_11.html` |
| 旭川 | `https://www.tvkingdom.jp/chart/12.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_12.html` |
| 帯広 | `https://www.tvkingdom.jp/chart/13.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_13.html` |
| 釧路 | `https://www.tvkingdom.jp/chart/14.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_14.html` |
| 北見 | `https://www.tvkingdom.jp/chart/15.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_15.html` |
| 室蘭 | `https://www.tvkingdom.jp/chart/16.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_16.html` |
| 宮城 | `https://www.tvkingdom.jp/chart/17.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_17.html` |
| 秋田 | `https://www.tvkingdom.jp/chart/18.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_18.html` |
| 山形 | `https://www.tvkingdom.jp/chart/19.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_19.html` |
| 岩手 | `https://www.tvkingdom.jp/chart/20.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_20.html` |
| 福島 | `https://www.tvkingdom.jp/chart/21.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_21.html` |
| 青森 | `https://www.tvkingdom.jp/chart/22.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_22.html` |
| 東京 | `https://www.tvkingdom.jp/chart/23.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_23.html` |
| 神奈川 | `https://www.tvkingdom.jp/chart/24.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_24.html` |
| 群馬 | `https://www.tvkingdom.jp/chart/25.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_25.html` |
| 茨城 | `https://www.tvkingdom.jp/chart/26.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_26.html` |
| 千葉 | `https://www.tvkingdom.jp/chart/27.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_27.html` |
| 栃木 | `https://www.tvkingdom.jp/chart/28.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_28.html` |
| 埼玉 | `https://www.tvkingdom.jp/chart/29.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_29.html` |
| 長野 | `https://www.tvkingdom.jp/chart/30.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_30.html` |
| 新潟 | `https://www.tvkingdom.jp/chart/31.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_31.html` |
| 山梨 | `https://www.tvkingdom.jp/chart/32.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_32.html` |
| 愛知 | `https://www.tvkingdom.jp/chart/33.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_33.html` |
| 石川 | `https://www.tvkingdom.jp/chart/34.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_34.html` |
| 静岡 | `https://www.tvkingdom.jp/chart/35.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_35.html` |
| 福井 | `https://www.tvkingdom.jp/chart/36.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_36.html` |
| 富山 | `https://www.tvkingdom.jp/chart/37.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_37.html` |
| 三重 | `https://www.tvkingdom.jp/chart/38.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_38.html` |
| 岐阜 | `https://www.tvkingdom.jp/chart/39.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_39.html` |
| 大阪 | `https://www.tvkingdom.jp/chart/40.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_40.html` |
| 京都 | `https://www.tvkingdom.jp/chart/41.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_41.html` |
| 兵庫 | `https://www.tvkingdom.jp/chart/42.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_42.html` |
| 和歌山 | `https://www.tvkingdom.jp/chart/43.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_43.html` |
| 奈良 | `https://www.tvkingdom.jp/chart/44.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_44.html` |
| 滋賀 | `https://www.tvkingdom.jp/chart/45.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_45.html` |
| 広島 | `https://www.tvkingdom.jp/chart/46.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_46.html` |
| 岡山 | `https://www.tvkingdom.jp/chart/47.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_47.html` |
| 島根 | `https://www.tvkingdom.jp/chart/48.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_48.html` |
| 鳥取 | `https://www.tvkingdom.jp/chart/49.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_49.html` |
| 山口 | `https://www.tvkingdom.jp/chart/50.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_50.html` |
| 愛媛 | `https://www.tvkingdom.jp/chart/51.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_51.html` |
| 香川 | `https://www.tvkingdom.jp/chart/52.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_52.html` |
| 徳島 | `https://www.tvkingdom.jp/chart/53.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_53.html` |
| 高知 | `https://www.tvkingdom.jp/chart/54.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_54.html` |
| 福岡 | `https://www.tvkingdom.jp/chart/55.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_55.html` |
| 熊本 | `https://www.tvkingdom.jp/chart/56.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_56.html` |
| 長崎 | `https://www.tvkingdom.jp/chart/57.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_57.html` |
| 鹿児島 | `https://www.tvkingdom.jp/chart/58.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_58.html` |
| 宮崎 | `https://www.tvkingdom.jp/chart/59.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_59.html` |
| 大分 | `https://www.tvkingdom.jp/chart/60.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_60.html` |
| 佐賀 | `https://www.tvkingdom.jp/chart/61.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_61.html` |
| 沖縄 | `https://www.tvkingdom.jp/chart/62.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_62.html` |

* マルチチャンネル

| テレビ | URL | 保存先 |
| --- | --- | --- |
| TOKYOMX2 | `https://www.tvkingdom.jp/chart/23.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0&selectedStationId=123610` | `./2021/01/01/2021_01_01_23_MX2.html` |
| チバテレ2 | `https://www.tvkingdom.jp/chart/27.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0&selectedStationId=127705` | `./2021/01/01/2021_01_01_27_CTC2.html` |
| 放送大学on | `https://www.tvkingdom.jp/chart/bs2.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0&selectedStationId=200232` | `./2021/01/01/2021_01_01_bs2_ON.html` |

* 主なBSチャンネルの番組表

| URL | 保存先 |
| --- | --- |
| `https://www.tvkingdom.jp/chart/bs1.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_bs1.html` |
| `https://www.tvkingdom.jp/chart/bs2.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_bs2.html` |
| `https://www.tvkingdom.jp/chart/bs3.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_bs3.html` |
| `https://www.tvkingdom.jp/chart/bs4.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_bs4.html` |
| `https://www.tvkingdom.jp/chart/bs4k8k_1.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_bs4k8k_1.html` |
| `https://www.tvkingdom.jp/chart/bs4k8k_2.action?head=202101010500&span=24&chartWidth=950&cellHeight=3&sticky=true&descriptive=true&buttonType=0` | `./2021/01/01/2021_01_01_bs4k8k_2.html` |

* NHKサブチャンネル

マルチチャンネルの番組表は「テレビ王国」でも見れるのですが、NHK公式の方が信頼性が高いのと、負荷分散を考えて以下のURLから取得します。  

※ 動的生成された結果のHTMLを得る必要があります。地域や日付を切り替える場合はプルダウンメニューを操作せず、URLから直接アクセスします。それによってHTML内に `area="010" date="20210101"` などの文字列が含まれ、あとで誤り確認に利用できます。  
※ 放送予定の変更が反映されるまでに何日もかかる事が多いので、１週間ぐらい前の番組表を得た方が安全です。  
※ 地方大会や災害があると地域ごとに異なってくるので、全てチェックしておきましょう。  
※ スマホ版のHTML(ウィンドウの横幅が狭い場合のデザイン)には対応していません。  
※ 本ツールではサブチャンネルの部分しか読み取りません。  
※ 万が一、テレビ王国の番組データとの食い違いがある場合は手直しになります。それを自動的に修正するような仕組みは本ツールにはありません。

| 地域 | URL | 保存先 |
| --- | --- | --- |
| 札幌 | `https://www.nhk.jp/timetable/010/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK010.html` |
| 函館 | `https://www.nhk.jp/timetable/011/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK011.html` |
| 旭川 | `https://www.nhk.jp/timetable/012/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK012.html` |
| 帯広 | `https://www.nhk.jp/timetable/013/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK013.html` |
| 釧路 | `https://www.nhk.jp/timetable/014/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK014.html` |
| 北見 | `https://www.nhk.jp/timetable/015/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK015.html` |
| 室蘭 | `https://www.nhk.jp/timetable/016/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK016.html` |
| 青森 | `https://www.nhk.jp/timetable/020/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK020.html` |
| 盛岡 | `https://www.nhk.jp/timetable/030/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK030.html` |
| 仙台 | `https://www.nhk.jp/timetable/040/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK040.html` |
| 秋田 | `https://www.nhk.jp/timetable/050/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK050.html` |
| 山形 | `https://www.nhk.jp/timetable/060/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK060.html` |
| 福島 | `https://www.nhk.jp/timetable/070/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK070.html` |
| 水戸 | `https://www.nhk.jp/timetable/080/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK080.html` |
| 宇都宮 | `https://www.nhk.jp/timetable/090/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK090.html` |
| 前橋 | `https://www.nhk.jp/timetable/100/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK100.html` |
| さいたま | `https://www.nhk.jp/timetable/110/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK110.html` |
| 千葉 | `https://www.nhk.jp/timetable/120/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK120.html` |
| 東京 | `https://www.nhk.jp/timetable/130/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK130.html` |
| 横浜 | `https://www.nhk.jp/timetable/140/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK140.html` |
| 新潟 | `https://www.nhk.jp/timetable/150/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK150.html` |
| 富山 | `https://www.nhk.jp/timetable/160/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK160.html` |
| 金沢 | `https://www.nhk.jp/timetable/170/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK170.html` |
| 福井 | `https://www.nhk.jp/timetable/180/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK180.html` |
| 甲府 | `https://www.nhk.jp/timetable/190/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK190.html` |
| 長野 | `https://www.nhk.jp/timetable/200/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK200.html` |
| 岐阜 | `https://www.nhk.jp/timetable/210/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK210.html` |
| 静岡 | `https://www.nhk.jp/timetable/220/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK220.html` |
| 名古屋 | `https://www.nhk.jp/timetable/230/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK230.html` |
| 津 | `https://www.nhk.jp/timetable/240/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK240.html` |
| 大津 | `https://www.nhk.jp/timetable/250/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK250.html` |
| 京都 | `https://www.nhk.jp/timetable/260/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK260.html` |
| 大阪 | `https://www.nhk.jp/timetable/270/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK270.html` |
| 神戸 | `https://www.nhk.jp/timetable/280/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK280.html` |
| 奈良 | `https://www.nhk.jp/timetable/290/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK290.html` |
| 和歌山 | `https://www.nhk.jp/timetable/300/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK300.html` |
| 鳥取 | `https://www.nhk.jp/timetable/310/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK310.html` |
| 松江 | `https://www.nhk.jp/timetable/320/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK320.html` |
| 岡山 | `https://www.nhk.jp/timetable/330/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK330.html` |
| 広島 | `https://www.nhk.jp/timetable/340/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK340.html` |
| 山口 | `https://www.nhk.jp/timetable/350/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK350.html` |
| 徳島 | `https://www.nhk.jp/timetable/360/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK360.html` |
| 高松 | `https://www.nhk.jp/timetable/370/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK370.html` |
| 松山 | `https://www.nhk.jp/timetable/380/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK380.html` |
| 高知 | `https://www.nhk.jp/timetable/390/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK390.html` |
| 福岡 | `https://www.nhk.jp/timetable/400/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK400.html` |
| 北九州 | `https://www.nhk.jp/timetable/401/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK401.html` |
| 佐賀 | `https://www.nhk.jp/timetable/410/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK410.html` |
| 長崎 | `https://www.nhk.jp/timetable/420/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK420.html` |
| 熊本 | `https://www.nhk.jp/timetable/430/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK430.html` |
| 大分 | `https://www.nhk.jp/timetable/440/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK440.html` |
| 宮崎 | `https://www.nhk.jp/timetable/450/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK450.html` |
| 鹿児島 | `https://www.nhk.jp/timetable/460/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK460.html` |
| 沖縄 | `https://www.nhk.jp/timetable/470/tv/20210101/daily/all/` | `./2021/01/01/2021_01_01_NHK470.html` |

* 放送大学on (revoked)

※ こちらは番組表のデザイン変更に伴い、廃止しました。サブタイトルを取得できないため。  
※ （テレビ王国には無いもんだと思い込んでいて、予備として公式サイトからも取得できる仕組みも用意してありました）

| URL | 保存先 |
| --- | --- |
| `https://www.ouj.ac.jp/hp/bangumi2/bangumi.php?month=1&date=1` | `2021/01/01/2021_01_01_OUJ.html` |

* TOKYOMX2 (deprecated)

※ 以下のURLから取得する仕組みは作ってあるのですが、番組概要を得やすいテレビ王国の方が望ましいです。  
※ メインチャンネルとは全く内容が異なるので、チェックしておきましょう。

| URL | 保存先 |
| --- | --- |
| `https://s.mxtv.jp/bangumi/?date=20210101` | `2021/01/01/2021_01_01_MX.html` |

* 三重テレビ2

※ あまり面白い番組はありませんが、一応チェックしておきましょう。

| URL | 保存先 |
| --- | --- |
| `https://www.mietv.com/timetable/time_table_day.html` | `2021/01/01/2021_01_01_MTV.html` |

* サンテレビ2

※ 毎週同じパターンのように見えますが、何かあるといけないので、まめにチェックしておきましょう。

| URL | 保存先 |
| --- | --- |
| `https://sun-tv.co.jp/weekly` | `2021/01/01/2021_01_01_SUN.html` |

* BS日テレ(142ch)

公式サイトの「先週の番組表」から取得することができます。  
※ ラジオボタンをクリックして動的生成された結果のHTMLを得る必要があります。差分を求めるために141と142の両方を取得します。  
※ 週間番組表なので1週間あたり1ファイルとします。ラジオボタンは「週間」と「先週」を選びましょう。  
※ 53という数字は第何週目かを表しますが、これはpython関数 `datetime.date(2021,1,1).isocalendar()[1]` の値に従います。

| チャンネル | URL | 保存先 |
| --- | --- | --- |
| 141ch | `https://www.bs4.jp/programschedule/` | `2021/01/2021_53week_bs141.html` |
| 142ch | `https://www.bs4.jp/programschedule/` | `2021/01/2021_53week_bs142.html` |
