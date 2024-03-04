import streamlit as st

# streamlit configuration
page_title = 'Hello'
layout = 'wide'
sidebar_state = 'expanded'


def main():
    st.set_page_config(page_title=page_title, layout=layout, initial_sidebar_state=sidebar_state)
    st.text('Hello world')


if __name__ == '__main__':
    main()
