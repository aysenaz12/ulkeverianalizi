import pandas as pd
import plotly.express as px


df = pd.read_csv("Freedom in the World 2013-2022 Dataset (Ver 2.18.23).csv")


df_latest = df[df["Edition"] == 2022]

# sütun icin olan kisim
df_map = df_latest[["Country/Territory", "Total"]].copy()
df_map.columns = ["Country", "Freedom Score"]

custom_scale = ["darkred", "red", "orange", "yellow", "lightgreen", "green"]


fig = px.choropleth(
    df_map,
    locations="Country",
    locationmode="country names",
    color="Freedom Score",
    color_continuous_scale=custom_scale,
    title="Global Freedom Index (Total Score) - 2022",
)


fig.write_html("freedom_total_map.html")


fig.show()
