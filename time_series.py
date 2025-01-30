import pandas as pd
import plotly.express as px
import time

# Dosyanın okunması
df = pd.read_csv("Freedom in the World 2013-2022 Dataset (Ver 2.18.23).csv")

# Yıllara göre en düşük 20 ülkeyi seçme
df_sorted = df.sort_values(by=["Edition", "Total"]).groupby("Edition").head(20)

# Renk skalasını belirleme (Koyu kırmızıdan açık yeşile)
custom_scale = ["darkred", "red", "orange", "yellow"]

# Animasyonlu çubuk grafik oluşturma
fig = px.bar(
    df_sorted,
    x="Total",
    y="Country/Territory",
    color="Total",
    color_continuous_scale=custom_scale,
    animation_frame="Edition",
    title="Yıllara Göre En Kötü 20 Ülke (Özgürlük Puanına Göre)",
    orientation="h"
)

# Her yıl geçişi arasında 2 saniye bekleme süresi ayarlama
fig.layout.updatemenus[0].buttons[0].args[1]["frame"] = {"duration": 4000, "redraw": True}

# Haritayı HTML olarak kaydetme
fig.write_html("freedom_worst_20_animation.html")

# Haritayı gösterme
fig.show()
