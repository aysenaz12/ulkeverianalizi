import pandas as pd
import plotly.express as px

# Dosyanın okunması
df = pd.read_csv("Freedom in the World 2013-2022 Dataset (Ver 2.18.23).csv")

# Türkiye'yi seçme
df_turkey = df[df["Country/Territory"] == "Turkey"]

# Türkiye'nin yıllar içindeki özgürlük puanlarını görselleştirme
fig = px.line(
    df_turkey,
    x="Edition",
    y="Total",
    title="Türkiye'nin Yıllar İçindeki Özgürlük Puanı",
    labels={"Edition": "Yıl", "Total": "Özgürlük Puanı"},
    line_shape="linear"
)

# Grafiği gösterme
fig.show()
