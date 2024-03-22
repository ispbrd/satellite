import streamlit as st


st.set_page_config(page_title="Satellite Capture", layout="wide")
css = """
        <style>
            [data-testid="stSidebar"]{
                min-width: 400px;
                max-width: 800px;
            }
        </style>
    """
st.markdown(css, unsafe_allow_html=True)

if "lat" not in st.session_state:
    st.session_state["lat"] = 34.752731
    st.session_state["long"] = -86.74384
    st.session_state["zoom"] = 15
    st.session_state["width"] = 640
    st.session_state["height"] = 640
    st.session_state["size"] = "640x640"

with st.sidebar:
    lat = st.number_input('Latitude:', placeholder="Insert Latitude, i.e., 34.752731", format="%.6f", step=None,
                          value=None, key="1")
    long = st.number_input('Longitude:', placeholder="Insert Longitude, i.e., -86.74384", format="%.6f", step=None,
                           value=None, key="2")
    zm = st.number_input('Zoom:', placeholder="Insert Zoom, i.e., 15, increment of 5", format="%.0f", step=None, value=None, key="3")

    ht = st.number_input('Height:', placeholder="Insert Height, i.e., 640", format="%.0f", step=None, value=None,
                         key="4")
    wd = st.number_input('Width:', placeholder="Insert Width, i.e., 640", format="%.0f", step=None, value=None, key="5")

    if st.button('Submit'):
        st.session_state["lat"] = lat
        st.session_state["long"] = long
        st.session_state["zoom"] = zm
        st.session_state["height"] = ht
        st.session_state["width"] = wd
        st.write('Geo info updated!')


def get_google_satellite_image_url(latitude, longitude, zoom=20, size="640x640", api_key="YOUR_API_KEY"):
    base_url = "https://maps.googleapis.com/maps/api/staticmap?"
    params = {
        "center": f"{latitude},{longitude}",
        "zoom": zoom,
        "size": size,
        "maptype": "satellite",
        "key": api_key
    }
    url = base_url + "&".join([f"{key}={value}" for key, value in params.items()])
    return url


# Example usage

latitude = st.session_state["lat"]
longitude = st.session_state["long"]
zoom = st.session_state["zoom"]
width = st.session_state["width"]
height = st.session_state["height"]

if (width is not None)&(height is not None):
    size = str(int(width)) + 'x' + str(int(height))
else:
    size = None

# size = str(st.session_state["size"])
api_key = "AIzaSyA9_uQNWHYSYcYhni16yiGK6uCPtegFiBM"

# st.write(latitude)
# st.write(longitude)
# st.write(zoom)
# st.write(size)

# st.text_area(str(zoom), key="3")
# st.text_area(size, key="4")

# 34.752731
# -86.74384
# 15
# 640

if (latitude is not None)&(longitude is not None)&(zoom is not None)&(width is not None)&(height is not None):

    image_url = get_google_satellite_image_url(latitude=float(latitude),
                                               longitude=float(longitude),
                                               zoom=int(zoom),
                                               size=size,
                                               api_key=api_key)
    st.write(image_url)
    st.image(image_url)
else:
    st.write("Put all the parameters")
