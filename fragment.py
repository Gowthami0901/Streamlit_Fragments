import streamlit as st

# Fragment for the header
def header():
    st.title("Customer Feedback App")
    st.subheader("We value your feedback")

# Fragment for the sidebar
def sidebar():
    st.sidebar.header("Navigation")
    st.sidebar.button("Submit Feedback")

# Fragment for the feedback form
def feedback_form():
    st.write("## Submit Your Feedback")
    
    name = st.text_input("Name", "")
    email = st.text_input("Email", "")
    rating = st.slider("Rating (1-5)", 1, 5, 3)
    comments = st.text_area("Comments", "")
    
    if st.button("Submit"):
        if name and email and comments:
            st.success("Thank you for your feedback!")
        else:
            st.error("Please fill out all the fields.")
            
def main():
    header()
    sidebar()
    feedback_form()

if __name__ == "__main__":
    main()
