import os
from turtle import onclick
import requests
import streamlit as st
from dotenv import load_dotenv
from data.model_options import model_options

# Load environment variables once at startup
load_dotenv()
FAST_API_BASE_URL = os.getenv("FAST_API_BASE_URL", "").rstrip("/")

# 1. Page Configuration
st.set_page_config(page_title="Synthetix", layout="wide")

st.balloons()

st.title("Synthetix", text_alignment="center", anchor=False)
st.caption("Powered by multiple models", text_alignment="center")


st.session_state.setdefault("generating", False)

# 2. Layout Setup
left_pad, center_col, right_pad = st.columns([1, 2, 1])

with center_col:
    # 3. Input Fields
    user_input = st.text_area(
        label="Your Input",
        placeholder="Type in your topic and I'll generate a summary for you.",
        label_visibility="collapsed",
        disabled=st.session_state.generating,
    )

    selected_model = st.selectbox(
        label="Select Model",
        options=model_options,
        index=0,
        disabled=st.session_state.generating,
    )

    # 4. Centered Button
    _, b_center, _ = st.columns([1, 1, 1])
    with b_center:
        submit_button = st.button(
            "Generate ➡️",
            use_container_width=True,
            disabled=st.session_state.generating,
            on_click=lambda: st.session_state.update(generating=True),
        )

    # 5. Form Submission & API Interaction
    if submit_button:

        cleaned_input = user_input.strip()

        if not cleaned_input:
            st.toast("Please provide some input text.", icon="⚠️")
        else:
            payload = {"input": cleaned_input, "model": f"{selected_model}:free"}

            with st.spinner("Generating..."):
                try:
                    # Using requests.Session() handles connections more efficiently
                    with requests.Session() as session:
                        response = session.post(
                            f"{FAST_API_BASE_URL}/generate", json=payload, timeout=10
                        )
                        data = response.json()

                    if response.status_code == 200:
                        st.divider()
                        st.subheader(
                            f"🎇{data.get('title', 'No Title Returned')}", anchor=False
                        )
                        st.write(data.get("summary", "No summary returned."))
                    else:
                        st.error(
                            f"Something went wrong: {data.get('error', 'Unknown Error')}"
                        )

                except requests.exceptions.ConnectionError:
                    st.error(f"Cannot connect to backend at {API_BASE_URL}")
                except requests.exceptions.Timeout:
                    st.error(
                        "The request timed out. Please try again later or choose a different model."
                    )
                except Exception as e:
                    st.error(f"An unexpected error occurred: {str(e)}")
                finally:
                    st.session_state.update(generating=False)
