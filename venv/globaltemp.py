import psycopg2, plotly.graph_objects as go
def Globaltemp():

    conn = psycopg2.connect("dbname=climate user=kristinabridgwater")

    cur = conn.cursor()

    cur.execute("SELECT year FROM globaltemp")
    years = cur.fetchall()
    years_list = []
    for x in years:
        years_list.append(x[0])

    cur.execute("SELECT avgtemp FROM globaltemp")
    temps = cur.fetchall()
    temps_list = []
    for x in temps:
        temps_list.append(x[0])

    fig = go.Figure(data=go.Scatter(x=years_list, y=temps_list))
    fig.update_layout(title='Average Global Temperature', xaxis_title='Year', yaxis_title='Degrees in Fahrenheit')

    conn.commit()

    cur.close()
    conn.close()

    return fig
