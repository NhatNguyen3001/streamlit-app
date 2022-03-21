import streamlit as st
import pandas as pd

header = st.container()
data_visualize = st.container()
suggestions = st.container()


@st.cache
def get_cafe_data(filename):
    cafe_data = pd.read_csv(filename)
    return cafe_data


@st.cache
def get_restaurant_data(filename):
    restaurant_data = pd.read_csv(filename)
    return restaurant_data


with header:
    st.title("Mafood")
    st.subheader("Web-based data visualization application specialized for restaurants")
    st.image("logo.png")

with data_visualize:
    cafe = get_cafe_data("cafe.csv")
    st.subheader("Top 5 cafe with highest prices")
    if st.checkbox("Show cafe information"):
        st.write(cafe)
    top_cafe_prices = pd.DataFrame(cafe["medium price"].sort_values().head(5))
    st.bar_chart(top_cafe_prices, use_container_width=True)

    restaurant = get_restaurant_data("restaurant.csv")
    st.subheader("Top 5 restaurant with highest prices")
    if st.checkbox("Show restaurant information"):
        st.write(restaurant)
    top_restaurant_prices = pd.DataFrame(restaurant["medium price"].sort_values().head(5))
    st.bar_chart(top_restaurant_prices, use_container_width=True)

with st.sidebar.subheader("Input your favorite"):
    dataset_name = st.sidebar.selectbox("Select", ("Cafe", "Restaurant"))
    price = st.sidebar.slider("Choose a price", min_value=10000, max_value=1500000, value=15)




