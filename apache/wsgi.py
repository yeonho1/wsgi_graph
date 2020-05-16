try:
    from urllib.parse import parse_qs
except ImportError:
    from cgi import parse_qs
from html import escape
import matplotlib.pyplot as plt

html = b"""
<html>
<body>
    <form action="">
        y = <input type="number" name="a"> * x^2 + <input type="number" name="b"> * x + <input type="number" name="c"><br><br>
        <input type="submit">
    </form>
    <img src="/result.png" alt="Result here">
</body>
</html>
"""

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    c = d.get('c', [''])[0]
    if '' not in [a, b, c]:
        a, b, c = int(a), int(b), int(c)
        x_values = list(range(-4, 5))
        y_values = [a * x ** 2 + b * x + c for x in x_values]
        fig = plt.figure()
        graph = plt.plot(x_values, y_values)
        plt.grid()
        fig.savefig('/var/www/html/result.png')
    response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
