# Streamlit fragments

Streamlit fragments refer to reusable pieces of code that can be modularized and included in different parts of a Streamlit application. This approach helps in maintaining cleaner, more readable, and easily maintainable code. By dividing your app into fragments, you can manage different functionalities or UI components separately, making it easier to debug and update specific parts of your app without affecting others.
<br>

# Key Benefits of Streamlit Fragments

1. **Code Reusability:** You can reuse fragments across different parts of your app, avoiding duplication of code.
2. **Modularity:** Breaking your app into smaller, self-contained pieces makes it easier to understand and manage.
3. **Maintainability:** Changes in one part of the app can be made without affecting other parts, simplifying updates and bug fixes.
4. **Collaboration:** Different team members can work on different fragments simultaneously, enhancing collaboration.
<br>

# Creating Streamlit Fragments

To create Streamlit fragments, you can define functions or classes that encapsulate specific functionalities or UI components. These functions or classes can then be called within the main application script to assemble the complete app.
<br>

## **Example: Customer Feedback App**

Let’s walk through an example of a customer feedback app to illustrate the concept of Streamlit fragments.

**Step 1: Define the Fragments**

We'll define fragments for the header, sidebar, and a feedback form.

```python
import streamlit as st

# Fragment for the header
def header():
    st.title("Customer Feedback App")
    st.subheader("We value your feedback")

# Fragment for the sidebar
def sidebar():
    st.sidebar.header("Navigation")
    st.sidebar.button("Home")
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
```

**Step 2: Assemble the Fragments in the Main App**

Now, we’ll create the main function to assemble these fragments into a complete application.

```python
# Main function to assemble the fragments
def main():
    header()
    sidebar()
    feedback_form()

if __name__ == "__main__":
    main()
```


# Explanation of the form

- **Header Fragment:** This fragment contains the main title and subtitle of the app.
- **Sidebar Fragment:** This fragment includes navigation buttons in the sidebar.
- **Feedback Form Fragment:** This fragment contains input fields for the user’s name, email, rating (using a slider), and comments. There’s a submit button that checks if all fields are filled out and provides feedback accordingly.
- **Main Function:** This function assembles the fragments to build the complete application.

By using this modular approach, you can easily add more fragments for additional features, such as viewing submitted feedback, analyzing it, or integrating with other services. This method keeps your code organized and facilitates easier development and maintenance.
