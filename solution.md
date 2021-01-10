# WEB
## HPNY
- Link tham khảo: https://tsublogs.wordpress.com/2018/12/13/wargame-code-breaking-com-solution/
- Source code:
```html
 <!-- Enjoy Tsu's Super Calculator <3, Not Only + - * / but also many other operators <3 <3 <3 -->

<?php

ini_set("display_errors", 0);

if(!isset($_GET["calc"])) 
{
    show_source(__FILE__);
}
else
{
    $wl = preg_match('/^[0-9\+\-\*\/\(\)\'\.\~\^\|\&]+$/i', $_GET["calc"]);
    if($wl === 0 || strlen($_GET["calc"]) > 70) {
        die("Tired of calculating? Lets <a href='https://www.youtube.com/watch?v=wDe_aCyf4aE' target=_blank >relax</a> <3");
    }
    echo 'Result: ';
    eval("echo ".eval("return ".$_GET["calc"].";").";");
} 
```
- Đề bài chỉ cho phép sử dụng các kí tự từ 'a' đến 'z', '(', ')', '_' và '.'
- Do phần nội dung được nhập vào được thực thi bởi `eval()` nên có thể bị dính lỗi dạng code/command execution.
- Thử với `system(ls)`:
[./images/Selection_001.png]
