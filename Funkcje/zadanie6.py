import plotly




import math
def delta(a, b, c):
    try:
        d = b**2 - 4*a*c
        p = math.sqrt(d)
        x1 = (-b + p) / (2*a)
        x1 = int(x1)
        x2 = (-b - p) / (2*a)
        x2 = int(x2)
        return x1, x2
    except ValueError:
        print("Nie można obliczyć pierwiastka z liczby ujemnej")

import plotly.graph_objects as go

x = list(range(-10, 10))
y = [i**2 for i in x]

fig = go.Figure(data=go.Scatter(x=x, y=y))
fig.show()

def test_delta():
    assert delta(5, 15, 4) == (0, -2)

