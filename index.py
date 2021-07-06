#! C:\Users\s4223\AppData\Local\Programs\Python\Python39\python.exe
# -*- coding: utf-8 -*-
print('Content-Type: text/html')
print()
print('hello')
print('''<!doctype html>
<html>
<head>
    <title>WEB-1 welcome</title> <!--title태그는 웹페이지에 표시되는 이름을 변경-->
    <meta charset="utf-8"> <!--utf-8로 문서를 읽기-->
</head>
<body>
    <h1><a href = "index.html" target = "-blank">WEB</a></h1>
    <ol><!--orderedlist-->
        <li><a href ="1.html" target = "-blank">HTML</a></li>
        <li><a href ="2.html" target = "-blank">CSS</a></li>
        <li><a href ="3.html" target = "-blank">JavaScript</a></li>
        <li><a href ="checkbox.html" target = "-blank">checkbox</a></li>
    </ol>
    <H2>WEB</H2> <!-- a: anchor 링크를 연결, target: 새로운 페이지로 열기, title: 마우스를 갖다대면 어떤 페이지인지 설명-->
    <p>월드 와이드 웹(World Wide Web, WWW, W3)은 인터넷에 연결된 컴퓨터를 통해 사람들이 정보를 공유할 수 있는 전 세계적인 정보 공간을 말한다. 간단히 웹(the Web)이라 부르는 경우가 많다. 이 용어는 인터넷과 동의어로 쓰이는 경우가 많으나 엄격히 말해 서로 다른 개념이다. 웹은 전자 메일과 같이 인터넷 상에서 동작하는 하나의 서비스일 뿐이다. 그러나 1993년 이래로 웹은 인터넷 구조의 절대적 위치를 차지하고 있다. 인터넷에서 HTTP 프로토콜, 하이퍼텍스트, HTML형식 등을 사용하여 그림과 문자를 교환하는 전송방식을 말하기도 한다.
    </p>
    <p><div id="disqus_thread"></div>
        <script>
            /**
            *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
            *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables    */
            /*
            var disqus_config = function () {
            this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
            this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
            };
            */
            (function() { // DON'T EDIT BELOW THIS LINE
            var d = document, s = d.createElement('script');
            s.src = 'https://web2-inbspaedsy.disqus.com/embed.js';
            s.setAttribute('data-timestamp', +new Date());
            (d.head || d.body).appendChild(s);
            })();
        </script>
        <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript></p>
</body>
</html>''')
