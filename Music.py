import streamlit as st

st.set_page_config(
    page_title="Music Player",
    page_icon="🎵",
    layout="centered"
)

st.title("🎵 TuneX")
st.write("Upload one or more MP3 files and enjoy your music!")

uploaded_files = st.file_uploader(
    "Choose MP3 Files",
    type=["mp3"],
    accept_multiple_files=True
)

if uploaded_files:

    song_names = [song.name for song in uploaded_files]

    selected_song = st.selectbox(
        "🎶 Playlist",
        song_names
    )

    for song in uploaded_files:
        if song.name == selected_song:

            st.subheader(f"Now Playing 🎧")
            st.success(song.name)

            st.audio(song)

            st.info(f"File Size : {round(song.size/1024,2)} KB")

            break

else:
    st.warning("Upload at least one MP3 file.")