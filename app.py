
#pip install streamlit
import streamlit as st
st.title("Summer Olympics 1896 to 2024")
st.write("Data Analysis")
st.video("https://www.youtube.com/watch?v=YtyXgRFa5Qo&t=51s")
import pandas as pd
df = pd.read_csv("data.csv")
st.dataframe(df)
st.sidebar.title("Navigation Window")
st.sidebar.write("Explore different Sections")
page = st.sidebar.radio("Choose the visual you want:", ["Medal Count by Country", "Performance by Gender", "Medal Trend Over Time", "Top Medalist","Most Popular Sports","Funfacts"])
#filters
st.sidebar.title("Filters")
selected_year = st.sidebar.slider(
    "Select Year Range",
    min_value=int(df["Year"].min()),
    max_value=int(df["Year"].max()),
    value=(int(df["Year"].min()), int(df["Year"].max()))
)#df = df[(df["Year"]>=selected_year[0])&(df["Year"] <= selected_year[1])]
selected_gender = st.sidebar.multiselect("Select Gender",options=df['Sex'].unique(),default=df['Sex'].unique())
selected_medal = st.sidebar.multiselect("Select Medal",options=df['Medal'].unique(),default=df['Medal'].unique())
selected_country = st.sidebar.multiselect("Select Country", options=df['Country'].unique(),default=df['Country'].unique())
selected_sport = st.sidebar.multiselect("Select Sport",options=df['Sport'].unique(),default=df['Sport'].unique())
df =df[(df["Sex"].isin(selected_gender))&(df["Medal"].isin(selected_medal))&(df["Country"].isin(selected_country))&(df['Sport'].isin(selected_sport))&(df["Year"] >=selected_year[0]) & (df["Year"] <= selected_year[1])]

# Page Content

import plotly.express as px
import plotly.graph_objects as go


if page == "Medal Count by Country":
    st.subheader("Medal Count by Country")

    medal_count = (
        df[df["Medal"] != "No medal"]
        .groupby("Country")["Medal"]
        .count()
        .sort_values(ascending=False)
    )

    fig1 = px.bar(
        x=medal_count.index,
        y=medal_count.values,
        labels={
            "x": "Country",
            "y": "Medal Count"
        }
    )

    st.plotly_chart(fig1, use_container_width=True)


elif page == "Performance by Gender":
    st.subheader("Performance by Gender")

    gender_medal_count = (
        df[df["Medal"] != "No medal"]
        .groupby("Sex")["Medal"]
        .count()
    )

    fig2 = px.pie(
        names=gender_medal_count.index,
        values=gender_medal_count.values,
        labels={
            "Sex": "Gender",
            "Medal": "Medal Count"
        }
    )

    st.plotly_chart(fig2, use_container_width=True)


elif page == "Medal Trend Over Time":
    st.subheader("Medal Trend Over Time")

    trend = (
        df[df["Medal"] != "No medal"]
        .groupby("Year")["Medal"]
        .count()
    )

    fig3 = px.line(
        x=trend.index,
        y=trend.values,
        labels={
            "x": "Year",
            "y": "Medal Count"
        },
        markers=True
    )

    st.plotly_chart(fig3, use_container_width=True)


elif page == "Top Medalist":
    st.subheader("Top Medalist")

    top_medalist = (
        df[df["Medal"] != "No medal"]
        .groupby("Name")["Medal"]
        .count()
        .sort_values(ascending=False)
        .head(10)
    )

    fig4 = px.bar(
        x=top_medalist.index,
        y=top_medalist.values,
        labels={
            "x": "Athlete",
            "y": "Medal Count"
        }
    )

    st.plotly_chart(fig4, use_container_width=True)


elif page == "Most Popular Sports":
    st.subheader("Most Popular Sports")

    sport_count = (
        df.groupby("Sport")["Event"]
        .count()
        .sort_values(ascending=False)
    )

    fig5 = px.bar(
        x=sport_count.values,
        y=sport_count.index,
        orientation="h",
        labels={
            "x": "Event Count",
            "y": "Sport"
        }
    )

    st.plotly_chart(fig5, use_container_width=True)


elif page == "Funfacts":
    st.subheader("Funfacts")

    st.write("Tug of War was one of the Olympic events.")
    st.write("Tug of War first appeared in the Olympics in 1900.")