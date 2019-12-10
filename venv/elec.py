import psycopg2, plotly.graph_objects as go
def Elec():

    conn = psycopg2.connect("dbname=climate user=kristinabridgwater")

    cur = conn.cursor()

    cur.execute("SELECT year FROM elec")
    years = cur.fetchall()
    years_list = []
    for x in years:
        years_list.append(x[0])

    cur.execute("SELECT fossil FROM elec")
    fossil = cur.fetchall()
    f_list = []
    for x in fossil:
        f_list.append(x[0])

    cur.execute("SELECT nuclear FROM elec")
    nuclear = cur.fetchall()
    n_list = []
    for x in nuclear:
        n_list.append(x[0])

    fig = go.Figure([
        go.Bar(name='Fossil Fuels', x=years_list, y=f_list),
        go.Bar(name='Nuclear + Renewables', x=years_list, y=n_list),
    ])
    fig.update_layout(
        title='Global Electricity Production by Source',
        yaxis=dict(
            title='Percent',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Year',
            titlefont_size=16,
            tickfont_size=14,
        ),
        barmode='group'
    )

    conn.commit()

    cur.close()
    conn.close()

    return fig
