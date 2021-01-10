# WEB
## HPNY
- Link tham khảo: https://tsublogs.wordpress.com/2018/12/13/wargame-code-breaking-com-solution/
- Source code:
```php
 <!-- Let's pray for new year lucky things <3 -->

<?php

function get_lucky_word() {
    $words = array("Chuc mung nam moi", "gongxifacai", "happy new year!", "bonne année", "Akemashite omedeto gozaimasu", "Seh heh bok mahn ee bahd euh sae yo", "kimochi", "Feliz Año Nuevo", "S novim godom", "Gelukkig Nieuwjaar", "selamat tahun baru", "iniya puthandu nal Vazhthukkal");
    return $words[array_rand($words)];
}

function get_lucky_number() {
    $numb = rand(0,100);
    return strval($numb);
}


if(!isset($_GET["roll"])) {
    show_source(__FILE__);
}
else
{
    $wl = preg_match('/^[a-z\(\)\_\.]+$/i', $_GET["roll"]);

    if($wl === 0 || strlen($_GET["roll"]) > 50) {
        die("bumbadum badum");
    }
    eval("echo ".$_GET["roll"]."();");
}

?>
```
- Đề bài chỉ cho phép sử dụng các kí tự từ 'a' đến 'z', '(', ')', '_' và '.'
- Do phần nội dung được nhập vào được thực thi bởi `eval()` nên có thể bị dính lỗi dạng code/command execution.
- Thử với `system(ls)`:
[./images/Selection_001.png]
