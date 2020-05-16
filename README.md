# wsgi_graph
![GitHub](https://img.shields.io/github/license/yeonho1/wsgi_graph)
> matplotlib을 이용해서 그래프를 이용한 뒤에 wsgi로 웹페이지에 표시하는 프로그램

> ## Requirement
> ```
> Python 2/3
> Matplotlib
> ```

> ## Usage
> ### Install `matplotlib`
> ```
> $ pip install matplotlib
> ```
> **Note**: superuser privilege is required. If you don't have superuser privilege, you can use `--user` option.
> ### Standalone run
> (in root directory of repository)
> ```
> $ cd standalone && python serve.py
> ```
> ### Associate with `mod_wsgi` on Apache (On development)
> Install `mod_wsgi` (with `apt`, `yum`, or by compiling source) and:
> #### On Red Hat Linux
> Create a file on directory `/etc/httpd/conf.d/` (Recommend a filename ends with `.conf`)
> and write as below:
> ```
> WSGIScriptAlias /graph /your_directory_to_this_repo/apache/wsgi.py
> ```
> Restart apache.
> ```
> $ service httpd restart
> ```
> **Note**: superuser privilege is required.
> #### On Debian Linux
> Create a file on directory `/etc/apache2/conf-enabled/` (Recommend a filename ends with `.conf`)
> and write as below:
> ```
> WSGIScriptAlias /graph /your_directory_to_this_repo/apache/wsgi.py
> ```
> Restart apache.
> ```
> $ service apache2 restart
> ```
> **Note**: superuser privilege is required.