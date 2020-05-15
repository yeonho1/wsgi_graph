try:
    from urllib.parse import parse_qs
except ImportError:
    from cgi import parse_qs
from html import escape
import matplotlib.pyplot as plt

plt.grid(True)

html = b"""
<html>
<body>
    <form action="">
        y = <input type="number" name="a"> * x^2 + <input type="number" name="b"> * x + <input type="number" name="c"><br><br>
        <input type="submit">
    </form>
    <img src="result.png" alt="Result here">
</body>
</html>
"""

def application(environ, start_response):
    if 'result.png' in environ['PATH_INFO']:
        try:
            with open('result.png', 'rb') as f:
                response_body = f.read()
                start_response('200 OK', [
                    ('Content-Type', 'image/png'),
                    ('Content-Length', str(len(response_body)))
                ])
                return [response_body]
        except:
            pass
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    c = d.get('c', [''])[0]
    if '' not in [a, b, c]:
        a, b, c = int(a), int(b), int(c)
        x_values = list(range(-4, 5))
        y_values = [a * x ** 2 + b * x + c for x in x_values]
        xAxis_x = x_values
        xAxis_y = [0] * len(x_values)
        yAxis_x = [0] * len(y_values)
        yAxis_y = y_values
        fig = plt.figure()
        graph = plt.plot(x_values, y_values)
        print(yAxis_x)
        print(yAxis_y)
        xAxis = plt.plot(xAxis_x, xAxis_y, color='k')
        yAxis = plt.plot(yAxis_x, yAxis_y, color='k')
        fig.savefig('result.png')
    response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
