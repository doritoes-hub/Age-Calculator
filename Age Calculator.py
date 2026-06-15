import streamlit as st
st.set_page_config(
    page_title="Age Calculator",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide the header and footer completely
st.html("<style>header, footer, .stAppDeployButton {display: none !important;}</style>")

def add_side_doodles(left_file, right_file):
    import base64
    import streamlit as st
    with open(left_file, "rb") as l_img, open(right_file, "rb") as r_img:
        left_b64 = base64.b64encode(l_img.read()).decode()
        right_b64 = base64.b64encode(r_img.read()).decode()
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{left_b64}"), url("data:image/png;base64,{right_b64}");
            background-position: left top, right top;
            background-repeat: no-repeat, no-repeat;
            background-size: contain, contain;
            background-attachment: fixed, fixed;
        }}
       /* Targets ONLY the actual input field box, leaving the row wrapper transparent */
        div[data-baseweb="select"] > div {{
            background-color: #FFFFFF !important;
            border-radius: 8px;
        }}
        </style>
        """,
        unsafe_allow_html=True)
    
add_side_doodles("option 1.png","option 1 - Copy.png")
st.markdown("<style>.stApp {background-color: #C1E1C1;}</style>", unsafe_allow_html=True)
st.title("Calculate Your Age")
user_1 = st.selectbox("Please enter your birth year", [  2026, 2025, 2024, 2023, 2022, 2021, 2020,2019, 2018, 2017, 2016, 2015, 2014,
                                                       2013,2012, 2011, 2010, 2009, 2008, 2007, 2006,2005, 2004, 2003, 2002, 2001, 2000,
                                                       1999,1998, 1997, 1996, 1995, 1994, 1993, 1992,1991, 1990, 1989, 1988, 1987, 1986,
                                                       1985,1984, 1983, 1982, 1981, 1980, 1979, 1978,1977, 1976, 1975, 1974, 1973, 1972, 1971,
                                                       1970, 1969, 1968, 1967, 1966, 1965, 19641963, 1962,
                                                       1961, 1960, 1959, 1958, 1957,1956, 1955, 1954, 1953, 1952, 1951, 1950,
                                                       1949, 1948, 1947, 1946, 1945, 1944, 1943,1942, 1941, 1940, 1939, 1938, 1937, 1936,1935, 1934, 1933, 1932, 1931, 1930])

user_2 = st.selectbox("Please enter your birth month", [1, 2, 3, 4,5,6,7,8,9,10,11,12])
if user_2 in {1,3,5,7,8,10,12}:
    user_3 = st.selectbox("Please enter your birth date", [ 1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11, 12, 13,
                                                           14,15, 16, 17, 18, 19, 20, 21,22, 23, 24,
                                                           25, 26, 27, 28,29, 30, 31])
elif user_2 in {4,6,9,11}:
    user_3 = st.selectbox("Please enter your birth date", [1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11, 12, 13,
                                                           14,15, 16, 17, 18, 19, 20, 21,22, 23, 24,
                                                           25, 26, 27, 28,29, 30])
elif user_2 in {2}:
     user_3 = st.selectbox("Please enter your birth date",[1, 2, 3, 4, 5, 6, 7,8, 9, 10, 11, 12, 13,
                                                           14,15, 16, 17, 18, 19, 20, 21,22, 23, 24,
                                                           25, 26, 27, 28,29,])

age = 2026 - int(user_1)
if int(user_2) >= 6:
    month = 12 - int(user_2) + 6
else:
    month = 6 - int(user_2)
        
    
    
if 6 < int(user_2):
    age -= 1
        
        
         
st.subheader("You are " + str(age) + " years " + str(month) + " months " + "old!")
    
     

     
    


           


