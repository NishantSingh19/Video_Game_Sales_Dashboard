import pandas as pd
import streamlit as st
import plotly.express as px


# Page Title & Page Icon
st.set_page_config("Video Game Sales Dashboard", page_icon="🕹️")

# Read CSV File
st.header("Overview")

data = pd.read_csv("Output.csv")
df = pd.DataFrame(data)

# Creating Tabs 
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["🧠 General", "🎮 Platform", "📈 Genre", "🏢 Publisher", "🌍 Regional & Trend"]
)

# Working with tabs

with tab1:

    st.subheader("🧠 General Insights")

# Q. Top 10 best-selling games based on Global Sales

    st.write("##### Top 10 `best-selling games` based on `Global_Sales`.")

    top10_games = (
        df.groupby("Name")["Global_Sales"].sum().sort_values(ascending=False).head(10)
    )

    # Using Bar graph
    fig1 = px.bar(
        top10_games, x=top10_games.index, y=top10_games.values, color=top10_games.index
    )

    # Customize Graph
    fig1.update_layout(
        xaxis_title="Games",
        yaxis_title="Global Sales",
    )

    fig1.update_traces(hovertemplate="<br>Name : %{x} </br>Sales: %{y}<extra></extra>")
    st.plotly_chart(fig1, use_container_width=True)

# Q. What is the total count of unique Games, Platforms,Genres, and Publishers.

    st.write(
        "##### What is the total count of unique `Games`, `Platforms`, `Genres`, and `Publishers`."
    )

    unique_counts = {
        "Unique Games": df["Name"].nunique(),
        "Platforms": df["Platform"].nunique(),
        "Genres": df["Genre"].nunique(),
        "Publishers": df["Publisher"].nunique(),
    }

    # Creating Cards
    col1, col2, col3, col4 = st.columns(4)
    col1.html(
        f"<div style='background-color: #1E90FF; padding:10px; border-radius:10px; text-align:center; cursor: default; margin: 20px 0;'>"
        f"<h2 style='color:white;'>Total Games</h2>"
        f"<h2 style='color:white;'>{unique_counts['Unique Games']}</h2></div>"
    )

    col2.html(
        f"<div style='background-color:#FF8C00; padding:10px; border-radius:10px; text-align:center; cursor: default;  margin: 20px 0;'>"
        f"<h2 style='color:white;'>Platforms</h2>"
        f"<h2 style='color:white;'>{unique_counts['Platforms']}</h2></div>"
    )

    col3.html(
        f"<div style='background-color:#32CD32; padding:10px; border-radius:10px; text-align:center; cursor: default;  margin: 20px 0;'>"
        f"<h2 style='color:white;'>Genres</h2>"
        f"<h2 style='color:white;'>{unique_counts['Genres']}</h2></div>"
    )

    col4.html(
        f"<div style='background-color:#FF1493; padding:10px; border-radius:10px; text-align:center; cursor: default;  margin: 20px 0;'>"
        f"<h2 style='color:white;'>Publishers</h2>"
        f"<h2 style='color:white;'>{unique_counts['Publishers']}</h2></div>"
    )

# Q. Visualize the trend of game releases per Year.

    st.write("##### Visualize the trend of game releases per `Year`.")

    game_relese_per_year = df.groupby("Year")["Name"].count()

    # Using Area Graph
    fig2 = px.area(
        game_relese_per_year,
        x=game_relese_per_year.index,
        y=game_relese_per_year.values,
        markers=True,
        color_discrete_sequence=["#E410DA"]
    )

    fig2.update_layout(xaxis_title="Release Year", yaxis_title="Game Release per Year")

    fig2.update_traces(hovertemplate="<br>Year : %{x}</br>Total Release : %{y}</br>")

    st.plotly_chart(fig2, use_container_width=True)

# Q. Highlight the year with maximum Global Sales.
    st.write("##### Highlight the year with maximum `Global_Sales`.")

    max_GS = df.groupby('Year')['Global_Sales'].sum().sort_values(ascending=False).reset_index().head(1)

    st.info(f"📆 The year with the highest Global Sales is **{max_GS['Year'][0]}**, with total sales of **{max_GS['Global_Sales'][0]} million** units.")

with tab2:

    st.subheader("🎮 Platform Insights")

# Q. Total Global_Sales by Platform.
    st.write("##### Total `Global_Sales` by `Platform`.")

    sales_by_paltform = df.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(10)

    # Bar Chart
    fig3 = px.bar(sales_by_paltform, x=sales_by_paltform.index, y=sales_by_paltform.values, color=sales_by_paltform.index, color_discrete_sequence=px.colors.qualitative.Vivid)

    fig3.update_layout(
        xaxis_title = "Platforms",
        yaxis_title = "Global Sales",
    )

    fig3.update_traces(hovertemplate="<br>Platform : %{x}</br>GS : %{y}<extra></extra>")
    st.plotly_chart(fig3, use_container_width=True)

# Q. Show top 5 Platforms by number of games released.

    st.write("##### `Top 5 Platforms` by number of games released.")

    top5_platforms = df.groupby('Platform')['Name'].count().sort_values(ascending=False).head(5)

    # Pie Chart
    fig4 = px.pie(top5_platforms, names=top5_platforms.index, values=top5_platforms.values, hole=0.45, color=top5_platforms.index, color_discrete_sequence=px.colors.diverging.Portland)

    # Customization
    fig4.update_traces(textinfo="label+percent" ,hovertemplate="<br>Platform : %{label}</br>Total Game Release : %{value}<extra></extra>", marker=dict(line=dict(color='#0e1117', width=5)))
    st.plotly_chart(fig4, use_container_width=True)

# Q. Regional Sales Comparison by Platform.

    st.write("##### `Regional Sales` Comparison by `Platform`")
    region = ['NA_Sales', 'EU_Sales', 'JP_Sales']
    total_sales = df.groupby('Platform')[region].sum().reset_index()

    # Group Bar Graph
    fig5 = px.bar(total_sales, x='Platform', y=region)

    # Customization
    fig5.update_layout(
        xaxis_title = "Platforms",
        yaxis_title = "Regional Sales",
    )

    fig5.update_traces(hovertemplate="<br>Platform : %{x}</br>Regional Sales : %{y}<extra></extra>")

    st.plotly_chart(fig5, use_container_width=True)

# Q. Platform Popularity Over Time

    st.write("##### `Platform` Popularity Over Time.")

    choice = df['Platform'].unique()
    platform = st.selectbox(label="Select Platform", options=choice)

    platform_trend = (df[df['Platform'] == platform].groupby('Year')['Global_Sales'].sum().reset_index())

    platform_trend['Platform'] = platform

    fig6 = px.area(platform_trend, x='Year', y='Global_Sales', color_discrete_sequence=["#0088FF"], markers=True)
    
    fig6.update_layout(xaxis_title="Year", yaxis_title="Global Sales")

    fig6.update_traces(text=platform_trend['Platform'],hovertemplate="<b>Platform:</b> %{text}<br>"
                  "<b>Year:</b> %{x}<br>"
                  "<b>Global Sales:</b> %{y} million")

    st.plotly_chart(fig6, use_container_width=True)

with tab3:

    st.subheader("📈 Genre Insights")
# Q. Visualize total Global_Sales by Genre

    st.write("##### Total `Global_Sales` by `Genre`.")

    sales_by_genres = df.groupby("Genre")['Global_Sales'].sum()

    # Horizontal Bar Chart

    fig7 = px.bar(sales_by_genres, y=sales_by_genres.index, x=sales_by_genres.values, color=sales_by_genres.index, color_discrete_sequence=px.colors.qualitative.D3, text_auto=True)

    # Customization
    fig7.update_layout(
        xaxis_title = "Global Sales",
        yaxis_title = "Genre",
    )

    fig7.update_traces(hovertemplate="<br>Genre : %{y}</br>Global Sales : %{x}<extra></extra>")

    st.plotly_chart(fig7, use_container_width=True)

# Q. Average Global Sales per Genre

    st.write("##### Average `Global Sales` per `Genre`.")

    avg_sales_by_genres = df.groupby("Genre")['Global_Sales'].mean().round(2).sort_values(ascending=False)

    # Pie Chart
    fig8 = px.pie(avg_sales_by_genres, names=avg_sales_by_genres.index, values=avg_sales_by_genres.values, color=avg_sales_by_genres.index, hole=0.4)

    # Customization
    fig8.update_traces(hovertemplate="<br>Genre : %{label}</br>Avg Sales : %{value}<extra></extra>")

    st.plotly_chart(fig8, use_container_width=True)

# Q. Most popular Genre in NA, EU, JP.

    st.write("##### Most Popular `Genre` in `Region`.")

    region = ['NA_Sales', 'EU_Sales', 'JP_Sales']
    popular_genre = df.groupby("Genre")[region].sum().reset_index()
    
    # Group Bar Graph
    fig9 = px.bar(popular_genre, x='Genre', y=region,
    barmode='group')

    # Customization
    fig9.update_layout(
        xaxis_title="Genre",
        yaxis_title="Region"
    )

    st.plotly_chart(fig9, use_container_width=True)

# Q. Genre performance across regions.

    st.write("##### `Genre` performance across `Regions`.")
    genre_performance = df.groupby("Genre")[region].sum().reset_index()

    fig10 = px.imshow(genre_performance.set_index('Genre').T,
    color_continuous_scale='Reds',
    text_auto=True,
    labels=dict(x="Genre", y="Region", color="Sales"))

    st.plotly_chart(fig10, use_container_width=True)

with tab4:

    st.subheader("🏢 Publisher Insights")
# Q. Top 5 Publishers by total Global_Sales.
    st.write("##### Top 5 `Publishers` by total `Global_Sales`.")

    top_pub = df.groupby("Publisher")['Global_Sales'].sum().sort_values(ascending=False).reset_index().head()
    
    # Pie Chart
    fig11 = px.pie(top_pub, names='Publisher', values='Global_Sales', hole=0.4, color_discrete_sequence=px.colors.qualitative.Bold)

    # Customization
    fig11.update_traces(hovertemplate="<br>Publisher : %{label}</br>Global Sales : %{value}<extra></extra>", marker=dict(line=dict(color='#0e1117', width=7)))

    st.plotly_chart(fig11, use_container_width=True)

# Q. Average Global_Sales per game by Publisher.
    st.write("##### Average `Global_Sales` per game by `Publisher`.")

    pub_avg = df.groupby("Publisher")['Global_Sales'].mean().nlargest(10).round(2)
    
    # Pie Chart
    fig12 = px.bar(pub_avg, x=pub_avg.index, y=pub_avg.values, color=pub_avg.index)

    # Customization
    fig12.update_layout(xaxis_title="Publisher",yaxis_title="Avg Global Sales")

    fig12.update_traces(hovertemplate="<br>Publisher : %{label}</br>Avg Global Sales : %{value}<extra></extra>", marker=dict(pattern=dict(shape=".",size=8, solidity=0.5,)))

    st.plotly_chart(fig12, use_container_width=True)

# Q. Publisher Performance by Genre

    st.write("##### `Publisher` Performance by `Genre`")

    selected_publisher = st.selectbox("Select a Publisher:", sorted(df['Publisher'].unique()))

    pub_genre_sales = df[df['Publisher'] == selected_publisher].groupby('Genre')['Global_Sales'].sum().sort_values(ascending=True).reset_index()

    fig13 = px.bar(pub_genre_sales, y='Genre', x='Global_Sales', title=f"{selected_publisher} – Sales by Genre", color='Genre', color_discrete_sequence=px.colors.qualitative.D3)

    st.plotly_chart(fig13, use_container_width=True)

with tab5:

    st.subheader("🌍 Regional & Trend Insights")

# Q. Region-wise contribution (NA_Sales, EU_Sales, JP_Sales, Other_Sales) to total Global_Sales.

    st.write("##### `Region-wise` contribution to total `Global_Sales`.")

    all_region = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
    region_totals = df[all_region].sum()

    fig14 = px.pie(region_totals, values=region_totals.values, names=region_totals.index, color=region_totals.index, color_discrete_sequence=px.colors.qualitative.Plotly, hole=0.4)

    fig14.update_traces(textinfo="label+percent",marker=dict(line=dict(color="#0e1117", width=8)))

    st.plotly_chart(fig14, use_container_width=True)

# Q. Top 5 games in Japan vs North America.

    st.write("##### Top 5 Games in `Japan` vs `North America`.")

    jp_top = df.groupby("Name")['JP_Sales'].sum().nlargest(5).reset_index()
    na_top = df.groupby("Name")['NA_Sales'].sum().nlargest(5).reset_index()

    fig_jp = px.funnel(
        jp_top,
        y='Name',
        x='JP_Sales',
        title=f"Japan: Top 5 Games by Sales",
    )
    st.plotly_chart(fig_jp, use_container_width=True)

    fig_na = px.funnel(
        na_top,
        y='Name',
        x='NA_Sales',
        title="North America: Top 5 Games by Sales",
        color_discrete_sequence=px.colors.sequential.Sunset
    )
    st.plotly_chart(fig_na, use_container_width=True)

# Q. Global_Sales trend by Year.

    st.write("##### `Global_Sales` trend by `Year`.")

    trend = df.groupby('Year')['Global_Sales'].sum()

    fig15 = px.line(trend, x=trend.index, y=trend.values, markers=True)

    # Customization
    fig15.update_layout(xaxis_title="Year", yaxis_title="Global Sales")
    fig15.update_traces(hovertemplate="<br>Year : %{x}</br> Sales: %{y}")

    st.plotly_chart(fig15, use_container_width=True)

# Q. Heatmap between regional sales and global sales

    st.write("##### Heatmap between `Regional Sales` and `Global Sales.`")

    corr = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].corr().round(2)

    fig16 = px.imshow(corr, text_auto=True, color_continuous_scale="ice")
    st.plotly_chart(fig16, use_container_width=True)

