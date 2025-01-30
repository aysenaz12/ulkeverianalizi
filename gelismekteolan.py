import pandas as pd
import plotly.express as px

# Dosyanın okunması
df = pd.read_csv("Freedom in the World 2013-2022 Dataset (Ver 2.18.23).csv")

# Gelişmekte olan ülkelerin listesi
developing_countries = [
    "China", "India", "Indonesia", "Philippines", "Nigeria", 
    "Kenya", "South Africa", "Egypt", "Brazil", "Argentina", 
    "Colombia", "Peru", "Turkey", "Saudi Arabia", "Iran"
]

# Gelişmekte olan ülkeleri seçme
df_developing = df[df["Country/Territory"].isin(developing_countries)]

# Grafik oluşturma
fig = px.line(
    df_developing,
    x="Edition",
    y="Total",
    color="Country/Territory",
    title="Gelişmekte Olan Ülkelerin Yıllık Özgürlük Puanı",
    labels={"Edition": "Yıl", "Total": "Özgürlük Puanı"}
)

# Grafiği gösterme
fig.show()
