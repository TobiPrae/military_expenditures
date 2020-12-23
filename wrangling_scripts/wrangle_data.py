import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """
    
    # graph 1
    
    military_president_usa = pd.read_csv("data/military_president_usa.csv")

    colors = {'Barack Obama': '#0058e6',
              'Bill Clinton': '#7aadff',
              'Donald Trump': '#9c0000',
              'George H. W. Bush': '#ffa600',
              'George W. Bush': '#81ff4f',
              'Gerald Ford': '#299100',
              'Jimmy Carter': '#00ffee',
              'John F. Kennedy': '#80ff00',
              'Lyndon B. Johnson': '#ff7e29',
              'Richard Nixon': '#fffb00',
              'Ronald Reagan': '#ff0000'}
    
    graph_one = go.Figure()   
    
    for t in military_president_usa['President'].unique():

        dfp = military_president_usa[military_president_usa['President']==t]
        graph_one.add_traces(go.Bar(x=dfp['Year'], y = dfp['Expense'], name=t))
    
    graph_one.update_layout(
    yaxis_title='Expenditure (USD)',
    title='US Military Spendings per President and Year',
    hovermode="x",
    template="plotly_white"
    )
    
  
    # graph 2

    country_max = max(military_president_usa['Expense'])

    graph_two=go.Figure()

    for key in colors:

        graph_two.add_traces(go.Scatter(
            name=key,
            x=military_president_usa.loc[military_president_usa["President"] == key]['Year'],
            y=military_president_usa.loc[military_president_usa["President"] == key]['Expense'],
            mode='lines',
            marker=dict(color=colors[key], size=1),
            showlegend=True,
            fill='tozeroy'
        ))

    graph_two.update_layout(
        yaxis_title='Expenditure (USD)',
        title='US Military Spendings per President and Year in the Context of Global Armed Conflicts',
        hovermode="x",
        template="plotly_white",
    )
    ####### VERTICAL LINES
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1961,
                y0=0,
                x1=1961,
                y1=country_max*1,
                line=dict(color='rgba(255, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=1961,
                y=1.01,
                yref='paper',
                showarrow=False,
                text="Vietnam War and Cuba Crisis",
                font_color="rgba(255, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1965,
                y0=0,
                x1=1965,
                y1=country_max*0.9,
                line=dict(color='rgba(0, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=1965,
                y=0.91,
                yref='paper',
                showarrow=False,
                text="Dominican Republic",
                font_color="rgba(0, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1982,
                y0=0,
                x1=1982,
                y1=country_max*1,
                line=dict(color='rgba(255, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=1982,
                y=1.01,
                yref='paper',
                showarrow=False,
                text="Lebanon",
                font_color="rgba(255, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1983,
                y0=0,
                x1=1983,
                y1=country_max*0.9,
                line=dict(color='rgba(0, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=1983,
                y=0.91,
                yref='paper',
                showarrow=False,
                text="Grenada",
                font_color="rgba(0, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1989,
                y0=0,
                x1=1989,
                y1=country_max*0.95,
                line=dict(color='rgba(255, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=1989,
                y=0.96,
                yref='paper',
                showarrow=False,
                text="Panama",
                font_color="rgba(255, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1991,
                y0=0,
                x1=1991,
                y1=country_max*1,
                line=dict(color='rgba(0, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=1991,
                y=1.01,
                yref='paper',
                showarrow=False,
                text="Gulf War",
                font_color="rgba(0, 0, 0, 1)")                
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1993,
                y0=0,
                x1=1993,
                y1=country_max*0.9,
                line=dict(color='rgba(255, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=1994,
                y=0.91,
                yref='paper',
                showarrow=False,
                text="Somalia",
                font_color="rgba(255, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1994,
                y0=0,
                x1=1994,
                y1=country_max*1.04,
                line=dict(color='rgba(0, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=1994,
                y=1.05,
                yref='paper',
                showarrow=False,
                text="Bosnia and Haiti",
                font_color="rgba(0, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1999,
                y0=0,
                x1=1999,
                y1=country_max*1,
                line=dict(color='rgba(255, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=1999,
                y=1.01,
                yref='paper',
                showarrow=False,
                text="Kosovo",
                font_color="rgba(255, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=2001,
                y0=0,
                x1=2001,
                y1=country_max*0.93,
                line=dict(color='rgba(0, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=2001,
                y=0.94,
                yref='paper',
                showarrow=False,
                text="Afghanistan",
                font_color="rgba(0, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=2003,
                y0=0,
                x1=2003,
                y1=country_max*1.04,
                line=dict(color='rgba(255, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=2003,
                y=1.05,
                yref='paper',
                showarrow=False,
                text="Iraq",
                font_color="rgba(255, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=2011,
                y0=0,
                x1=2011,
                y1=country_max*1.04,
                line=dict(color='rgba(0, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=2009,
                y=1.02,
                yref='paper',
                showarrow=False,
                text="Libya",
                font_color="rgba(0, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=2012,
                y0=0,
                x1=2012,
                y1=country_max*1.09,
                line=dict(color='rgba(255, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=2012,
                y=1.08,
                yref='paper',
                showarrow=False,
                text="War with ISIL",
                font_color="rgba(255, 0, 0, 1)")
    graph_two.add_shape(type='line',
                yref="y",
                xref="x",
                x0=2017,
                y0=0,
                x1=2017,
                y1=country_max*1.04,
                line=dict(color='rgba(0, 0, 0, 0.5)', width=2, dash='dot'))
    graph_two.add_annotation(
                x=2017,
                y=1.02,
                yref='paper',
                showarrow=False,
                text="Syria",
                font_color="rgba(0, 0, 0, 1)")
    
    
    # graph 3
    
    df_military = pd.read_csv("data/Military Expenditure.csv")
    countries_of_interest = ["United States", "Germany", "China", "Russian Federation", "United Kingdom"]
    df_military = df_military.loc[df_military["Name"].isin(countries_of_interest)]
    spending_chi = df_military.iloc[:, 34:].loc[38, ].tolist()
    spending_ger = df_military.iloc[:, 34:].loc[53, ].tolist()
    spending_rus = df_military.iloc[:, 34:].loc[200, ].tolist()
    spending_usa = df_military.iloc[:, 34:].loc[249, ].tolist()
    spending_uk = df_military.iloc[:, 34:].loc[79, ].tolist()
    military_df = pd.DataFrame(
        {'Year': list(range(1990, 2019)),
         'China': spending_chi,
         'Germany': spending_ger,
         'Russia': spending_rus,
         'USA': spending_usa,
         #"United Kingdom": spending_uk
        })

    colors = {'USA': '#0058e6',
              'Russia': '#7aadff',
              'China': '#9c0000',
              'Germany': '#ffa600',
              #'United Kingdom': 'red'
             }

    graph_three=go.Figure()

    for key in colors:

        graph_three.add_traces(go.Scatter(
            name=key,
            x=military_df["Year"],
            y=military_df[key],
            mode='lines',
            marker=dict(color=colors[key], size=1),
            showlegend=True,
        ))

    graph_three.update_layout(
        yaxis_title='Expenditure (USD)',
        title='Military Spendings per Country and Year',
        hovermode="x",
        template="plotly_white",
    )
    
    # graph 4
    for col in military_df.iloc[: , 1:].columns:
        military_df[F"{col}_p"] = None
    
        for i in range(1, military_df.shape[0]):
            if((pd.isna(military_df[col][i]) == False) & (pd.isna(military_df[col][i-1]) == False)):
                military_df[F"{col}_p"][i] = (military_df[col][i] / military_df[col][i-1] * 100) - 100
            else:
                continue
    
    graph_four=go.Figure()

    colors = {'USA': '#0058e6',
              'China': '#9c0000',
             }

    for key in colors:

        graph_four.add_traces(go.Scatter(
            name=key,
            x=military_df["Year"],
            y=military_df[F"{key}_p"],
            mode='lines',
            marker=dict(color=colors[key], size=1),
            showlegend=True,
        ))

    graph_four.update_layout(
        yaxis_title='Expense Growth (%)',
        title='Yearly Growth of Military Spending – USA vs. China',
        hovermode="x",
        template="plotly_white",
    )

    graph_four.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1990,
                y0=0,
                x1=2018,
                y1=0,
                line=dict(color='rgba(255, 0, 0, 0.5)', width=1))
    
    # graph 5 & 6
    df_military_2 = pd.read_csv("data/Military Expenditure.csv")

    df_military_1990 = df_military_2[["Name", "1990"]]
    df_military_2000 = df_military_2[["Name", "2000"]]
    df_military_2010 = df_military_2[["Name", "2010"]]
    df_military_2018 = df_military_2[["Name", "2018"]]

    countries_of_interest = ["United States", "Germany", "China", "Russian Federation"]

    df_military_1990_coi = df_military_1990.loc[df_military_1990["Name"].isin(countries_of_interest)]
    df_military_1990_rest = df_military_1990.loc[~df_military_1990["Name"].isin(countries_of_interest)]
    new_row = ["Rest", sum(df_military_1990_rest["1990"].fillna(0).tolist())]
    s = pd. Series(new_row, index = df_military_1990_coi.columns)
    df_military_1990_new = df_military_1990_coi.append(s, ignore_index=True)

    df_military_2000_coi = df_military_2000.loc[df_military_2000["Name"].isin(countries_of_interest)]
    df_military_2000_rest = df_military_2000.loc[~df_military_2000["Name"].isin(countries_of_interest)]
    new_row = ["Rest", sum(df_military_2000_rest["2000"].fillna(0).tolist())]
    s = pd. Series(new_row, index = df_military_2000_coi.columns)
    df_military_2000_new = df_military_2000_coi.append(s, ignore_index=True)

    df_military_2010_coi = df_military_2010.loc[df_military_2010["Name"].isin(countries_of_interest)]
    df_military_2010_rest = df_military_2010.loc[~df_military_2010["Name"].isin(countries_of_interest)]
    new_row = ["Rest", sum(df_military_2010_rest["2010"].fillna(0).tolist())]
    s = pd. Series(new_row, index = df_military_2010_coi.columns)
    df_military_2010_new = df_military_2010_coi.append(s, ignore_index=True)

    df_military_2018_coi = df_military_2018.loc[df_military_2018["Name"].isin(countries_of_interest)]
    df_military_2018_rest = df_military_2018.loc[~df_military_2018["Name"].isin(countries_of_interest)]
    new_row = ["Rest", sum(df_military_2018_rest["2018"].fillna(0).tolist())]
    s = pd. Series(new_row, index = df_military_2018_coi.columns)
    df_military_2018_new = df_military_2018_coi.append(s, ignore_index=True)
    
    graph_five = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

    graph_five.add_trace(go.Pie(labels=df_military_1990_new["Name"], values=df_military_1990_new["1990"], name="1990"),
                  1, 1)
    graph_five.add_trace(go.Pie(labels=df_military_2000_new["Name"], values=df_military_2000_new["2000"], name="2000"),
                  1, 2)

    graph_five.update_traces(hole=.3, hoverinfo="label+percent+name", marker=dict(colors=['#9c0000', '#ffa600',  '#7aadff', '#0058e6', 'lightgrey' ]))


    graph_five.update_layout(
        title_text="Global Expenditure (USD)",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='1990', x=0.19, y=0.5, font_size=20, showarrow=False),
                     dict(text='2000', x=0.81, y=0.5, font_size=20, showarrow=False)])
    
    graph_six = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])

    graph_six.add_trace(go.Pie(labels=df_military_2010_new["Name"], values=df_military_2010_new["2010"], name="2010"), 1, 1)
    graph_six.add_trace(go.Pie(labels=df_military_2018_new["Name"], values=df_military_2018_new["2018"], name="2018"), 1, 2)

    graph_six.update_traces(hole=.3, hoverinfo="label+percent+name", marker=dict(colors=['#9c0000', '#ffa600',  '#7aadff', '#0058e6', 'lightgrey' ]))

    graph_six.update_layout(
        title_text="Global Expenditure (USD)",
        # Add annotations in the center of the donut pies.
        annotations=[dict(text='2010', x=0.19, y=0.5, font_size=20, showarrow=False),
                     dict(text='2018', x=0.81, y=0.5, font_size=20, showarrow=False)])
    
    
    
    # graph 7
    df_gdp_percentage = pd.read_csv("data/API_MS.MIL.XPND.GD.ZS_DS2_en_csv_v2_1740297.csv")
    countries_of_interest = ["United States", "Germany", "China", "Russian Federation", "United Kingdom"]
    df_gdp_percentage = df_gdp_percentage.loc[df_gdp_percentage["Country Name"].isin(countries_of_interest)]
    spending_chi = df_gdp_percentage.iloc[:, 4:63].loc[38, ].tolist()
    spending_ger = df_gdp_percentage.iloc[:, 4:63].loc[53, ].tolist()
    spending_rus = df_gdp_percentage.iloc[:, 4:63].loc[200, ].tolist()
    spending_usa = df_gdp_percentage.iloc[:, 4:63].loc[249, ].tolist()
    spending_uk = df_gdp_percentage.iloc[:, 4:63].loc[79, ].tolist()
    df_gdp_percentage = pd.DataFrame(
        {'Year': list(range(1960, 2019)),
         'China': spending_chi,
         'Germany': spending_ger,
         'Russia': spending_rus,
         'USA': spending_usa,
         #"United Kingdom": spending_uk
        })

    colors = {'USA': '#0058e6',
              'Russia': '#7aadff',
              'China': '#9c0000',
              'Germany': '#ffa600',
              #'United Kingdom': 'red'
             }

    graph_seven=go.Figure()

    for key in colors:

        graph_seven.add_traces(go.Scatter(
            name=key,
            x=df_gdp_percentage["Year"],
            y=df_gdp_percentage[key],
            mode='lines',
            marker=dict(color=colors[key], size=1),
            showlegend=True,
        ))

    graph_seven.update_layout(
        yaxis_title='Military Expenditure vs. GDP (%)',
        title="Military Expenditure as a Share of GDP",
        hovermode="x",
        template="plotly_white",
    )

    # graph 8
 

    df_gdp_growth = pd.read_csv("data/gdp-growth.csv", sep=";")
    countries_of_interest = ["United States", "Germany", "China", "Russian Federation", "United Kingdom"]
    df_gdp_growth = df_gdp_growth.loc[df_gdp_growth["Country Name"].isin(countries_of_interest)]
    gdp_growth_china = df_gdp_growth.iloc[:, 2:].loc[42, ].tolist()
    gdp_growth_china.reverse()
    gdp_growth_ger = df_gdp_growth.iloc[:, 2:].loc[59, ].tolist()
    gdp_growth_ger.reverse()
    gdp_growth_rus = df_gdp_growth.iloc[:, 2:].loc[199, ].tolist()
    gdp_growth_rus.reverse()
    gdp_growth_usa = df_gdp_growth.iloc[:, 2:].loc[243, ].tolist()
    gdp_growth_usa.reverse()
    gdp_growth_uk = df_gdp_growth.iloc[:, 2:].loc[84, ].tolist()
    gdp_growth_uk.reverse()

    gdp_growth_df = pd.DataFrame(
        {'Year': range(1961, 2014),
         'China': gdp_growth_china,
         'Germany': gdp_growth_ger,
         'Russia': gdp_growth_rus,
         'USA': gdp_growth_usa,
         #'United Kingdom': gdp_growth_uk,

        })

    for col in gdp_growth_df.iloc[:, 1:].columns:
        gdp_growth_df[col] = gdp_growth_df[col].astype(str)
        gdp_growth_df[col] = gdp_growth_df[col].apply(lambda x: x.replace(',', '.')).astype(float)

    colors = {'USA': '#0058e6',
              'Russia': '#7aadff',
              'China': '#9c0000',
              'Germany': '#ffa600',
              #'United Kingdom': 'red'
             }

    graph_eight=go.Figure()

    for key in colors:

        graph_eight.add_traces(go.Scatter(
            name=key,
            x=gdp_growth_df["Year"],
            y=gdp_growth_df[key],
            mode='lines',
            marker=dict(color=colors[key], size=1),
            showlegend=True,
        ))

    graph_eight.update_layout(
        yaxis_title='GDP Growth (%)',
        title="Yearly GDP Growth in Percent",
        hovermode="x",
        template="plotly_white",
    )

    graph_eight.add_shape(type='line',
                yref="y",
                xref="x",
                x0=1960,
                y0=0,
                x1=2018,
                y1=0,
                line=dict(color='rgba(255, 0, 0, 0.5)', width=1))
    
    # graph 9
    df_export = pd.read_csv("data/API_MS.MIL.XPRT.KD_DS2_en_csv_v2_1740278.csv")
    countries_of_interest = ["United States", "Germany", "China", "Russian Federation", "United Kingdom"]
    df_export = df_export.loc[df_export["Country Name"].isin(countries_of_interest)]
    exports_chi = df_export.iloc[:, 4:63].loc[38, ].tolist()
    exports_ger = df_export.iloc[:, 4:63].loc[53, ].tolist()
    exports_rus = df_export.iloc[:, 4:63].loc[200, ].tolist()
    exports_usa = df_export.iloc[:, 4:63].loc[249, ].tolist()
    exports_uk = df_export.iloc[:, 4:63].loc[79, ].tolist()
    df_export = pd.DataFrame(
        {'Year': list(range(1960, 2019)),
         'China': exports_chi,
         'Germany': exports_ger,
         'Russia': exports_rus,
         'USA': exports_usa,
         #"United Kingdom": exports_uk
        })
    colors = {'USA': '#0058e6',
              'Russia': '#7aadff',
              'China': '#9c0000',
              'Germany': '#ffa600',
              #'United Kingdom': 'red'
             }

    graph_nine=go.Figure()

    for key in colors:

        graph_nine.add_traces(go.Scatter(
            name=key,
            x=df_export["Year"],
            y=df_export[key],
            mode='lines',
            marker=dict(color=colors[key], size=1),
            showlegend=True,
        ))

    graph_nine.update_layout(
        yaxis_title='Exports (USD)',
        title="Weapon Exports by Country and Year",
        hovermode="x",
        template="plotly_white",
    )

    # graph 10
    df_import = pd.read_csv("data/API_MS.MIL.MPRT.KD_DS2_en_csv_v2_1745336.csv")
    countries_of_interest = ["United States", "Germany", "China", "Russian Federation", "United Kingdom"]
    df_import = df_import.loc[df_import["Country Name"].isin(countries_of_interest)]
    imports_chi = df_import.iloc[:, 4:63].loc[38, ].tolist()
    imports_ger = df_import.iloc[:, 4:63].loc[53, ].tolist()
    imports_rus = df_import.iloc[:, 4:63].loc[200, ].tolist()
    imports_usa = df_import.iloc[:, 4:63].loc[249, ].tolist()
    imports_uk = df_import.iloc[:, 4:63].loc[79, ].tolist()
    df_import = pd.DataFrame(
        {'Year': list(range(1960, 2019)),
         'China': imports_chi,
         'Germany': imports_ger,
         'Russia': imports_rus,
         'USA': imports_usa,
         #"United Kingdom": imports_uk,
        })

    graph_ten=go.Figure()

    for key in colors:

        graph_ten.add_traces(go.Scatter(
            name=key,
            x=df_import["Year"],
            y=df_import[key],
            mode='lines',
            marker=dict(color=colors[key], size=1),
            showlegend=True,
        ))

    graph_ten.update_layout(
        yaxis_title='Imports (USD)',
        title="Weapon Imports by Country and Year",
        hovermode="x",
        template="plotly_white",
    )

    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one))
    figures.append(dict(data=graph_two))
    figures.append(dict(data=graph_three))
    figures.append(dict(data=graph_four))
    figures.append(dict(data=graph_five))
    figures.append(dict(data=graph_six))
    figures.append(dict(data=graph_seven))
    figures.append(dict(data=graph_eight))
    figures.append(dict(data=graph_nine))
    figures.append(dict(data=graph_ten))

    return figures