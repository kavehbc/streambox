from streambox.lib.streamlit_import import (
    VER_GTE_1_12_1,
    VER_GTE_1_14_0,
    VER_GTE_1_18_0,
    AppSession,
    SessionInfo,
    get_script_run_ctx,
)
from streamlit.runtime.runtime import Runtime


def get_session_id() -> str:
    ctx = get_script_run_ctx()
    if ctx is None:
        raise Exception("Failed to get the thread context")
    return ctx.session_id


def get_user_info():
    ctx = get_script_run_ctx()
    if ctx is None:
        raise Exception("Failed to get the thread context")
    return ctx.user_info


def get_all_sessions():
    all_session_ids = []
    for session in Runtime.instance()._session_mgr.list_active_sessions():
        all_session_ids.append(session.session.id)
    return all_session_ids
