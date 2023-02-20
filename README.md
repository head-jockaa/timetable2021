テレビ番組表の記録(2021年分)
==

概要
--

日本全国のテレビ番組表１年分をどれだけ小さな容量でアーカイブできるか実験をおこなうプロジェクトです。  
なおかつ、まとまったデータを欲しい人が大量にHTTPリクエストを投げなくても済むようなアーカイブ作成も目的としています。  
`timetable.yanbe.net` が使いづらいサイトになってしまったため、2021年1月18日分から独自に記録をつける事にしました。    
うp主によっぽどの惨事が降りかからない限りは継続予定です。  
2021年分の集計は終わりましたが、データの修正をおこなう場合もあります。

* [2022年分はこちら](https://github.com/head-jockaa/timetable2022)

使い方
--

`https://github.com/head-jockaa/timetable2021` のページにある緑色の `Code` ボタンを押して `Download ZIP` を選んでください。  
ダウンロードされたZIPファイルを展開して `2021.html` をブラウザで開けばOKです。  
`scripts` フォルダの中にある圧縮ファイル `archive.7z` を展開すると、たぶん `archive` というフォルダができるので、その中にjsファイルを配置するようにします。  
7-Zip形式に対応した解凍ソフトを使ってください。

* `scripts/archive/encoder.js`
* `scripts/archive/timetables.js`
* `scripts/archive/titles.js`
* `scripts/archive/descriptions.js`
* `scripts/archive/radio_encoder.js`
* `scripts/archive/radio_timetables.js`
* `scripts/archive/radio_titles.js`
* `scripts/archive/radio_descriptions.js`

データ収集対象
--

* 全都道府県の地上波テレビ、BSデジタルテレビ
  * 普段から独自編成しているマルチチャンネルはできるだけ対象とする（NHK総合2、NHKEテレ3、TOKYOMX2、チバテレ2、三重テレビ2、サンテレビ2、NHK-BS1、BS日テレ、放送大学on）
  * CS放送の番組表については検討中だが、どちらかというと、あんまりやりたくない
  * インターネット放送は対象外
* タイムテーブルを形作る上で最低限必要な要素
  * 開始時刻、放映時間、ジャンル、各種アイコン、番組名、番組概要を記録する
  * 🙇‍♀️出演者等の詳細な記事情報については、負担が大きい事と目的にそぐわない事から対象外とさせて下さい🙇‍♂️
 
※ ニュース番組概要など番組表の変更を考慮して、当日深夜に取得（3月20日分から）  
※ 3月25日分からラジオ放送の記録も試験的に始める

2020年以前
--

`timetable.yanbe.net` から吸い出したデータをこちらで公開します。  
恐る恐るアクセスしなくてはならず、全てのデータが揃うには3年掛かるかもしれません。

* [2007年分](https://github.com/head-jockaa/timetable2007)
* [2008年分](https://github.com/head-jockaa/timetable2008)
* [2009年分](https://github.com/head-jockaa/timetable2009)
* [2010年分](https://github.com/head-jockaa/timetable2010)
* [2011年分](https://github.com/head-jockaa/timetable2011)
* [2012年分](https://github.com/head-jockaa/timetable2012)
* [2013年分](https://github.com/head-jockaa/timetable2013)
* [2014年分](https://github.com/head-jockaa/timetable2014)
* [2015年分](https://github.com/head-jockaa/timetable2015)
* [2016年分](https://github.com/head-jockaa/timetable2016)
* [2017年分](https://github.com/head-jockaa/timetable2017)
* [2018年分](https://github.com/head-jockaa/timetable2018)
* [2019年分](https://github.com/head-jockaa/timetable2019)
* [2020年分](https://github.com/head-jockaa/timetable2020)

設計
--

* javascriptを利用し、番組表のデザインに自由度を与える。
* 辞書ファイルの用意、2バイト文字への変換、関東キー局との差分を求めることにより、データサイズをなるべく小さく抑える。 
  * 7zipの力も借りて、今の所20MB以下に抑えられる見込み。

作り方は2022年版をご覧ください。

著作権
--

* 動作確認のため `tools/tv/2021.7z` および `tools/radio/radio2021.7z` には、データ取得元WebサイトのHTMLをサンプルとして入れてあります。
* `descriptions.js` は編集者の努力の産物だと言われれば編集著作物にあたる可能性もありますが、 `titles.js` や `timetables.js` は単なる事実やデータです。
* それ以外はオープンソースとします。

完全に私のオリジナル作品というわけではないので、営利・非営利を問わず大掛かりなサービス展開には利用しない方がきっと平和です。  
アニメ番組一覧サイトを作るとかその程度は構わないですしArugoworksぐらいの趣味活動はあって然るべきですが、地味めな利用形態(これは調査研究目的だと言い張るなりしてw)に留めておく事を推奨します。
