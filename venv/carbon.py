import psycopg2
import plotly.graph_objects as go
def Carbon():

    conn = psycopg2.connect("dbname=climate user=kristinabridgwater")

    cur = conn.cursor()

    cur.execute("SELECT year FROM carbon")
    years = cur.fetchall()
    years_list = []
    for x in years:
        years_list.append(x[0])

    cur.execute("SELECT fossil FROM carbon")
    fossils = cur.fetchall()
    fossils_list = []
    for x in fossils:
        fossils_list.append(x[0])

    cur.execute("SELECT landuse FROM carbon")
    lus = cur.fetchall()
    lus_list = []
    for x in lus:
        lus_list.append(x[0])

    cur.execute("SELECT atmos FROM carbon")
    atmos = cur.fetchall()
    atmos_list = []
    for x in atmos:
        atmos_list.append(x[0])

    cur.execute("SELECT ocean FROM carbon")
    ocean = cur.fetchall()
    ocean_list = []
    for x in ocean:
        ocean_list.append(x[0])

    cur.execute("SELECT land FROM carbon")
    land = cur.fetchall()
    land_list = []
    for x in land:
        land_list.append(x[0])



    fig = go.Figure([
        go.Bar(name='Fossil Fuel and Industry', x=years_list, y=fossils_list),
        go.Bar(name='Land-Use Change Emissions', x=years_list, y=lus_list),
        go.Bar(name='Atmospheric Growth', x=years_list, y=atmos_list),
        go.Bar(name='Ocean Sink', x=years_list, y=ocean_list),
        go.Bar(name='Land Sink', x=years_list, y=land_list),
    ])
    fig.update_layout(
        title='Global Carbon Budget',
        yaxis=dict(
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Year',
            titlefont_size=16,
            tickfont_size=14,
        ),
        barmode='stack'
    )

    conn.commit()

    cur.close()
    conn.close()

    return fig
