# WEB
## HPNY
- Link tham khảo: https://tsublogs.wordpress.com/2018/12/13/wargame-code-breaking-com-solution/
- Source code:
```html
<html><body>

<!-- Enjoy Tsu's Super Calculator <3, Not Only + - * / but also many other operators <3 <3 <3 -->

<code><span style="color: #000000">
&lt;!--&nbsp;Enjoy&nbsp;Tsu's&nbsp;Super&nbsp;Calculator&nbsp;&lt;3,&nbsp;Not&nbsp;Only&nbsp;+&nbsp;-&nbsp;*&nbsp;/&nbsp;but&nbsp;also&nbsp;many&nbsp;other&nbsp;operators&nbsp;&lt;3&nbsp;&lt;3&nbsp;&lt;3&nbsp;--&gt;<br /><br /><span style="color: #0000BB">&lt;?php<br /><br />ini_set</span><span style="color: #007700">(</span><span style="color: #DD0000">"display_errors"</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">0</span><span style="color: #007700">);<br /><br />if(!isset(</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">"calc"</span><span style="color: #007700">]))&nbsp;<br />{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">show_source</span><span style="color: #007700">(</span><span style="color: #0000BB">__FILE__</span><span style="color: #007700">);<br />}<br />else<br />{<br />&nbsp;&nbsp;&nbsp;&nbsp;</span><span style="color: #0000BB">$wl&nbsp;</span><span style="color: #007700">=&nbsp;</span><span style="color: #0000BB">preg_match</span><span style="color: #007700">(</span><span style="color: #DD0000">'/^[0-9\+\-\*\/\(\)\'\.\~\^\|\&amp;]+$/i'</span><span style="color: #007700">,&nbsp;</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">"calc"</span><span style="color: #007700">]);<br />&nbsp;&nbsp;&nbsp;&nbsp;if(</span><span style="color: #0000BB">$wl&nbsp;</span><span style="color: #007700">===&nbsp;</span><span style="color: #0000BB">0&nbsp;</span><span style="color: #007700">||&nbsp;</span><span style="color: #0000BB">strlen</span><span style="color: #007700">(</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">"calc"</span><span style="color: #007700">])&nbsp;&gt;&nbsp;</span><span style="color: #0000BB">70</span><span style="color: #007700">)&nbsp;{<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;die(</span><span style="color: #DD0000">"Tired&nbsp;of&nbsp;calculating?&nbsp;Lets&nbsp;&lt;a&nbsp;href='https://www.youtube.com/watch?v=wDe_aCyf4aE'&nbsp;target=_blank&nbsp;&gt;relax&lt;/a&gt;&nbsp;&lt;3"</span><span style="color: #007700">);<br />&nbsp;&nbsp;&nbsp;&nbsp;}<br />&nbsp;&nbsp;&nbsp;&nbsp;echo&nbsp;</span><span style="color: #DD0000">'Result:&nbsp;'</span><span style="color: #007700">;<br />&nbsp;&nbsp;&nbsp;&nbsp;eval(</span><span style="color: #DD0000">"echo&nbsp;"</span><span style="color: #007700">.eval(</span><span style="color: #DD0000">"return&nbsp;"</span><span style="color: #007700">.</span><span style="color: #0000BB">$_GET</span><span style="color: #007700">[</span><span style="color: #DD0000">"calc"</span><span style="color: #007700">].</span><span style="color: #DD0000">";"</span><span style="color: #007700">).</span><span style="color: #DD0000">";"</span><span style="color: #007700">);<br />}</span>
</span>
</code>
	</body>
</html>
```
- Đề bài chỉ cho phép sử dụng các kí tự từ 'a' đến 'z', '(', ')', '_' và '.'
- Do phần nội dung được nhập vào được thực thi bởi `eval()` nên có thể bị dính lỗi dạng code/command execution.
- Thử với `system(ls)`:
[./images/Selection_001.png]
