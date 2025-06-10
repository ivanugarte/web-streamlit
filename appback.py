import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Page configuration
st.set_page_config(page_title="My Website", layout="wide")

# Custom CSS for red buttons
st.markdown("""
<style>
    .stButton>button {
        border: 2px solid #d10000;
        color: white;
        background-color: #ff3333;
        transition: all 0.3s;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #d10000;
        border-color: #a80000;
        color: white;
    }
    .stButton>button:focus:not(:active) {
        background-color: #a80000;
        border-color: #800000;
        color: white;
        box-shadow: 0 0 0 0.2rem rgba(255, 0, 0, 0.5);
    }
    .portfolio-image {
        border-radius: 10px;
        transition: transform 0.3s;
        margin-bottom: 15px;
    }
    .portfolio-image:hover {
        transform: scale(1.03);
    }
</style>
""", unsafe_allow_html=True)

# State management with query_params
if 'page' in st.query_params:
    st.session_state.current_page = st.query_params['page']
else:
    st.session_state.current_page = "About"

# Portfolio image data (using Unsplash)
portfolio_images = [
    {
        "url": "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?w=600",
        "title": "Project Management",
        "desc": "Interactive project management dashboard system"
    },
    {
        "url": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600",
        "title": "Data Analysis",
        "desc": "Real-time data visualization platform"
    },
    {
        "url": "https://images.unsplash.com/photo-1467232004584-a241de8bcf5d?w=600",
        "title": "Mobile App",
        "desc": "iOS/Android client application development"
    }
]

def load_image(url):
    """Load image from URL"""
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def change_page(page_name):
    """Change page and update URL parameters"""
    st.session_state.current_page = page_name
    st.query_params.page = page_name

# Navigation bar
cols = st.columns(3)
with cols[0]:
    if st.button("About", key="btn_about"):
        change_page("About")
with cols[1]:
    if st.button("Contact", key="btn_contact"):
        change_page("Contact")
with cols[2]:
    if st.button("Portfolio", key="btn_portfolio"):
        change_page("Portfolio")

# Page content
if st.session_state.current_page == "About":
    st.title("About Us")
    st.write("Welcome to our company profile.")
    st.write("We specialize in web development and digital solutions.")

elif st.session_state.current_page == "Contact":
    st.title("Contact Us")
    st.write("Get in touch with our team.")
    with st.form("contact_form"):
        name = st.text_input("Full name")
        email = st.text_input("Email")
        subject = st.selectbox("Subject", ["Inquiry", "Quote", "Support", "Other"])
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you for your message! We'll contact you within 24 hours.")

elif st.session_state.current_page == "Portfolio":
    st.title("Our Portfolio")
    st.write("Some of our recent projects:")
    
    # Display images in responsive grid
    columns = st.columns(3)
    for idx, project in enumerate(portfolio_images):
        with columns[idx % 3]:
            try:
                img = load_image(project["url"])
                st.image(
                    img, 
                    use_container_width=True,  # Updated parameter here
                    caption=project["title"]
                )
                st.markdown(f"**{project['title']}**")
                st.markdown(f"<small>{project['desc']}</small>", unsafe_allow_html=True)
                st.markdown("---")
            except Exception as e:
                st.error(f"Error loading image {idx+1}: {str(e)}")