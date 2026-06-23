import streamlit as st

st.set_page_config(
    page_title="For Divya 🌸",
    page_icon="✨",
    layout="centered"
)

# Session State
if "page" not in st.session_state:
    st.session_state.page = 1

# Custom CSS
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:50px;
    color:#ff4b6e;
    font-weight:bold;
}
.message{
    text-align:center;
    font-size:24px;
    padding:15px;
}
</style>
""", unsafe_allow_html=True)

# PAGE 1
if st.session_state.page == 1:

    st.markdown(
        '<p class="main-title">🌸 Hello Divya 🌸</p>',
        unsafe_allow_html=True
    )

    

    st.markdown("""
    <div class="message">
    
    ✨ Welcome to this little surprise.
    
    🌷 Some special words are waiting for you.
    
    💫 Click Next and continue the journey.
    
    </div>
    """, unsafe_allow_html=True)

    if st.button("Next ➡️"):
        st.session_state.page = 2
        st.rerun()

# PAGE 2
elif st.session_state.page == 2:

    st.title("✨ A Special Message")

    st.write("""
    🌟 Your positivity makes every day brighter.

    🌸 Keep smiling because your smile spreads happiness.

    🌈 Keep believing in yourself.

    ✨ You are capable of amazing things.
    """)

    if st.button("Next ➡️"):
        st.session_state.page = 3
        st.rerun()

# PAGE 3
elif st.session_state.page == 3:

    st.title("🎮 Fun Question")

    choice = st.radio(
        "What do you like most?",
        [
            "🌍 Traveling",
            "🎵 Music",
            "📚 Books",
            "🌄 Nature"
        ]
    )

    if st.button("Submit & Continue"):
        st.session_state.choice = choice
        st.session_state.page = 4
        st.rerun()

# PAGE 4
elif st.session_state.page == 4:

    st.title("🌟 Your Choice")

    st.success(
        f"You selected: {st.session_state.choice}"
    )

    st.write("""
    🌷 Great choice!

    ✨ Life becomes beautiful when we enjoy what we love.

    🌈 Keep exploring new experiences.

    💫 Keep shining and growing every day.
    """)

    if st.button("Final Surprise ❤️"):
        st.session_state.page = 5
        st.rerun()

# PAGE 5
elif st.session_state.page == 5:

    st.balloons()

    st.markdown(
        '<p class="main-title">💌 Best Wishes Divya 💌</p>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="message">

    🌸 May every day bring happiness to your life.

    🌟 May your dreams become reality.

    🌈 May success follow you wherever you go.

    ✨ Keep being the wonderful person you are.

    💫 Never stop believing in yourself.

    🌷 Thank you for visiting this little website.

    😊 Have a fantastic day!

    </div>
    """, unsafe_allow_html=True)

    st.snow()

    if st.button("Start Again 🔄"):
        st.session_state.page = 1
        st.rerun()