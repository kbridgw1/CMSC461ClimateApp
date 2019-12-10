import psycopg2
import plotly.graph_objects as go
def Co2globalem():

    conn = psycopg2.connect("dbname=climate user=kristinabridgwater")

    cur = conn.cursor()

    cur.execute("SELECT year FROM co2globalem")
    years = cur.fetchall()
    years_list = []
    for x in years:
        years_list.append(x[0])

    cur.execute("SELECT total FROM co2globalem")
    totals = cur.fetchall()
    totals_list = []
    for x in totals:
        totals_list.append(x[0])

    cur.execute("SELECT gasfuel FROM co2globalem")
    gfs = cur.fetchall()
    gfs_list = []
    for x in gfs:
        gfs_list.append(x[0])

    cur.execute("SELECT liquidfuel FROM co2globalem")
    lfs = cur.fetchall()
    lfs_list = []
    for x in lfs:
        lfs_list.append(x[0])

    cur.execute("SELECT solidfuel FROM co2globalem")
    sfs = cur.fetchall()
    sfs_list = []
    for x in sfs:
        sfs_list.append(x[0])

    cur.execute("SELECT cement FROM co2globalem")
    cements = cur.fetchall()
    cements_list = []
    for x in cements:
        cements_list.append(x[0])

    cur.execute("SELECT gasflaring FROM co2globalem")
    gasfs = cur.fetchall()
    gasfs_list = []
    for x in gasfs:
        gasfs_list.append(x[0])


    fig = go.Figure([
        go.Bar(name='Total', x=years_list, y=totals_list),
        go.Bar(name='Gas Fuel', x=years_list, y=gfs_list),
        go.Bar(name='Liquid Fuel', x=years_list, y=lfs_list),
        go.Bar(name='Solid Fuel', x=years_list, y=sfs_list),
        go.Bar(name='Cement', x=years_list, y=cements_list),
        go.Bar(name='Gas Flaring', x=years_list, y=gasfs_list)
    ])
    fig.update_layout(
        title='Global CO2 Emissions from Fossil Fuels',
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
