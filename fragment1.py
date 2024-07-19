import streamlit as st

# Main app logic
st.title("Streamlit HTML Fragment Example")

st.write("This example demonstrates the use of HTML, CSS, and JavaScript fragments in Streamlit.")

# HTML, CSS, and JavaScript fragment
html_fragment = """
<style>
.custom-box {
    border: 2px solid #4CAF50;
    padding: 20px;
    margin-top: 20px;
    background-color: #f9f9f9;
    border-radius: 10px;
}
.custom-box h2 {
    color: #4CAF50;
}
.custom-box p {
    font-size: 16px;
}
.custom-box button {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}
.custom-box button:hover {
    background-color: #45a049;
}
</style>
<div class="custom-box">
    <h2>Interactive HTML Fragment</h2>
    <p id="text">This text will change when you click the button.</p>
    <button onclick="document.getElementById('text').innerText = 'The text has been changed!';">Click me</button>
</div>
"""

# Inject the HTML fragment into the Streamlit app
st.markdown(html_fragment, unsafe_allow_html=True)
