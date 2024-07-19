import streamlit as st

# Main app logic
st.title("Streamlit HTML Fragment Example")

st.write("Below is a custom HTML fragment:")

# HTML fragment
html_fragment = """
<div style="border: 2px solid #4CAF50; padding: 20px; margin-top: 20px;">
    <h2 style="color: #4CAF50;">Custom HTML Fragment</h2>
    <p>This content is rendered using an HTML fragment in Streamlit.</p>
    <button onclick="alert('Button clicked!')">Click me</button>
</div>
"""

# Inject the HTML fragment into the Streamlit app
st.markdown(html_fragment, unsafe_allow_html=True)
