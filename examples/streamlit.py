import streamlit as st
import streambox as sb


def main():
    st.title("Streamlit Session")
    st.subheader("User Info")
    st.write(sb.streamlit.get_user_info())
    st.subheader("Active Session ID")
    st.write(sb.streamlit.get_session_id())
    st.subheader("All Session IDs")
    st.write(sb.streamlit.get_all_sessions())

    chk_footer = st.checkbox("Hide Footer", value=True)
    if chk_footer:
        sb.streamlit.hide_footer()

    chk_hamburger = st.checkbox("Hide hamburger menu", value=True)
    if chk_hamburger:
        sb.streamlit.hide_hamburger_menu()

    chk_radio = st.checkbox("No default radio selection", value=True)
    if chk_radio:
        sb.hide_default_radio_selection()
        list_options = ["-", "Option 1", "Option 2", "Option 3", "Option 4"]
    else:
        list_options = ["Option 1", "Option 2", "Option 3", "Option 4"]

    st.radio("Sample questions", options=list_options)


if __name__ == '__main__':
    main()
