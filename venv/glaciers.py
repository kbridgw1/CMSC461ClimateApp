import psycopg2, plotly.graph_objects as go
def Glaciers():

    conn = psycopg2.connect("dbname=climate user=kristinabridgwater")

    cur = conn.cursor()

    cur.execute("SELECT year FROM glaciers")
    years = cur.fetchall()
    years_list = []
    for x in years:
        years_list.append(x[0])

    cur.execute("SELECT cmb FROM glaciers")
    cmbs = cur.fetchall()
    cmbs_list = []
    for x in cmbs:
        cmbs_list.append(x[0])

    fig = go.Figure([go.Bar(x=years_list, y=cmbs_list)])
    fig.update_layout(
        title='Glacier Size',
        yaxis=dict(
            title='Average Cumulative Mass Balance',
            titlefont_size=16,
            tickfont_size=14,
        ),
        xaxis=dict(
            title='Year',
            titlefont_size=16,
            tickfont_size=14,
        )
    )

    conn.commit()

    cur.close()
    conn.close()

    return fig
