import streamlit as st


def hide_footer():
    hide_footer_style = """
                <style>
                /* This is to hide hamburger menu completely */
                footer {visibility: hidden;}
                </style>
            """
    st.markdown(hide_footer_style, unsafe_allow_html=True)


def hide_hamburger_menu():
    hide_hamburger_menu_style = """
                <style>
                /* This is to hide hamburger menu completely */
                #MainMenu {visibility: hidden;}
                </style>
            """
    st.markdown(hide_hamburger_menu_style, unsafe_allow_html=True)


def hide_default_radio_selection():
    # hide the selection of the default value for the radio button
    # https://discuss.streamlit.io/t/radio-button-group-with-no-selection/3229/6
    st.markdown(
        """ <style>
                div[role="radiogroup"] >  :first-child{
                    display: none !important;
                }
            </style>
            """,
        unsafe_allow_html=True
    )