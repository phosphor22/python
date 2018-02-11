2018.02.10 作業開始

──────────────────────────────────────────────────────────────────────
開発環境
──────────────────────────────────────────────────────────────────────
・python 3.6.4

  Pythonをインストールする (for Windows) - Qiita
  https://qiita.com/taiponrock/items/f574dd2cddf8851fb02c


  ・Binance SDK(非公式)
    バイナンスのAPIを操作するためのPython用非公式開発キット

    PythonでBinanceAPIを動かしてみた。 - 仮想通貨に全ツッパ
    http://www.crypto-attack.work/entry/20180108/1515402000
──────────────────────────────────────────────────────────────────────
・sublime text 3
  フリーで使えるプログラムエディタ。カスタマイズ性が高く人気がある

  Sublime Text - A sophisticated text editor for code, markup and prose
  https://www.sublimetext.com/


    「Package Control」のインストール
      「Package Control」はSublime Textにパッケージを入れるためのパッケージ管理ツールです。

      (1)ショートカット「Ctrl + `」でコマンドライン表示。
      (2)コマンドラインに以下を入力して実行する。

      import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)


    sublime text 3に日本語インライン対応させる
      (1)Package Controlをひらく(Windows: Controll + Shist + P)
      (2)Package Control: Install Packageを選択しIMESupportをインストール


    視認性を上げるためのテーマをインストールする
      (1)ショートカットキー「Command + Shift + P」を押します。
      (2)「Package Congrol: Install Package」を選択します。
      (3)「soda」と入力し、「Theme - Soda」を選択します。

        その他好みのを探したければ以下を参考に

          Sublime Text - テーマの検索とインストール - 開発メモ - Webkaru
          https://webkaru.net/dev/sublime-text-theme/



    カラースキームをインストールする
        (1)ページ下方の color-schemes.zipをDLする

            buymeasoda/soda-theme: Dark and light custom UI themes for Sublime Text
            https://github.com/buymeasoda/soda-theme/

        (2)Preference -> Browse Pacakagesでフォルダが開くので，UserフォルダにDLしたファイルの中身を配置する
            Espresso Soda.tmTheme
            Monokai Soda.tmTheme


    設定を書き換える
        (1)Preferences -> Settings で設定ファイルが開くので，user側に以下をコピペする
           (コメントは保存後削除されてしまうので説明は参考までに。)

──────────────────────────────────────────────────────────────────────
{
    //テキスト■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    // フォント。人気なのは”Ricty”、”Consolas”、”Panic Sans”
    "font_face": "Ricty",

    //フォントサイズ
    "font_size": 12,

    //行間
    "line_padding_bottom": 1,
    "line_padding_top": 1,

    //入力補助■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    //タブサイズ(デザイナやPythonユーザは4、Rubyユーザは2)
    "tab_size": 4,

    // タブをスペースに変換
    "translate_tabs_to_spaces": true,

    // Backスペースでインデントとしてのスペースをtab_size分削除する
    "use_tab_stops": true,

    // C言語でif ()の後に改行を行なうと次の行がインデントされるなど、オートインデントが少し便利になります。
    "smart_indent": true,

    // 改行で次の行に移動する時、空行だった場合は、オートインデントによって追加されていた空白を削除します。
    "trim_automatic_white_space": true,


    //デザイン■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    //ボタン、タブ、スクロールバー等、Sublime TextのUIの外観を制御します。
    //カラースキーマと違いメニューからは変更できないので、ユーザー設定ファイルを直接変更する必要があります。
//    "theme": "Adaptive.sublime-theme",
    "theme": "Soda Dark 3.sublime-theme",

    // カラースキームに「Espresso Soda.tmTheme」を選択
    "color_scheme": "Packages/User/Monokai Soda.tmTheme",

    //表示設定■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    //タブやスペースなどの不過視文字を表示
    "draw_white_space": "all",

    //指定文字数で改行を行う
    "word_wrap": true,
    "wrap_width": 100,//折り返し文字数

    //現在の選択行をハイライト表示
    "highlight_line": true,

    //折りたたみアイコンの非表示
    "fade_fold_buttons": false,

    // エンコーディングの文字コードを右下のステータスバーに表示
    "show_encoding": true,

    // 改行コードをステータスバーに表示
    "show_line_endings": true,

    // 通常のスクロールバーを使用する
    "overlay_scroll_bars": "disabled",

    // 半角スペースの可視化
    "draw_white_space": "all",

    // タブインデント時にインデント位置にガイドを表示する
    "draw_indent_guides": true,

    //インデントガイドの描画方法を制御します。
    //draw_noraml : インデントガイドが必要な箇所を全て描画
    //draw_active : カーソル位置のインデントとその親要素を別の色で区別して描画
    "indent_guide_options":
    [
        "draw_normal",
        "draw_active"
    ],

    //trueにすると、インデントを行なう時に(の位置まで空白を追加します。
    "indent_to_bracket": true,

    //ミニマップの可視領域をマウスカーソルをあわせた時のみ表示するか、常時表示するかを設定します。
    "always_show_minimap_viewport": true,

    //サイドバーに表示するフォルダ名を太字に
    "bold_folder_labels": true,

    // <> の括弧を強調する
    "match_brackets_angle": true,


    //動作設定■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

    //文字コード
    "default_encoding": "UTF-8", // デフォルト
    "fallback_encoding": "UTF-8", // 文字コードが不明なファイル

    //セーブ時に末尾の不要な空白を削除
    "trim_trailing_white_space_on_save": true,

    // Sublimeを終了する直前に開いていたファイルを記憶するかどうか
    "remember_open_files": true,

    // 開いているファイルがなくなったらSublimeを終了するかどうか
    "close_windows_when_empty": true,

    //カーソルの表示方法を設定する。
        //smooth : phaseとblinkをあわせたような感じで表示する
        //phase : カーソルをフェードイン・アウトさせながら表示する
        //blink : カーソルを点滅させる
        //solid : カーソルの点滅を止める
    "caret_style": "smooth",

    //ファイルの読み込み時にインデントにタブとスペースのどちらが使われてるかを判定し、
    //そのファイルにあわせた適切な設定に変更します。
    "detect_indentation": false,

    //無効化するパッケージをリストします。
    //このリストからエントリーを削除した時、パッケージにプラグインが含まれている場合は、
    //再起動が必要にある事があります。
    "ignored_packages":
    ["Vintage"],
}


──────────────────────────────────────────────────────────────────────


    あとは，好みのプラグインを入れて完了。

    SublimeText3を2年以上使って、生き残ったPluginを紹介します。 - Qiita
    https://qiita.com/MakoTano/items/8853caa206283df5e1f9