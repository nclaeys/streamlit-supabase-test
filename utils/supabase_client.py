import os
import streamlit as st
from supabase import create_client, Client

@st.cache_resource
def init_supabase():
    url = os.environ.get("SUPABASE_URL") or st.secrets.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY") or st.secrets.get("SUPABASE_KEY")
    
    if not url or not key:
        st.error("Supabase URL and API key must be set in environment variables or Streamlit secrets.")
        st.stop()
    
    return create_client(url, key)

supabase: Client = init_supabase()

