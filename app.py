from pathlib import Path

import streamlit as st
from PIL import Image



current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"



PAGE_TITLE = "Python CV | Alashkhan Zhakiya"
PAGE_ICON = ":wave:"
NAME = "Alashkhan Zhakiya"
DESCRIPTION = """
2nd year student from Astana IT University, good guy.
"""
EMAIL = "alashkhanzhakiya@gmail.com"
SOCIAL_MEDIA = {
    "Instagram": "https://www.instagram.com/giorno_jdjd/",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Twitter": "https://twitter.com",
}
ACHIEVEMENTS = {
    "Finished 1st year of AITU(Astana IT University)",
    "Have got 2 retakes from 1st year of AITU",
    "Don't have scholarship due to 2 retakes from 1st year",
    "",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)



st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")



st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 2 Years expereince extracting actionable insights from data
- ✔️ Well knowing Python and Excel
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)



st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL(PgAdmin4)
- 📊 Data Visulization: MS Excel
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MySQL
"""
)



st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**2nd year student | AITU**")
st.write("09/2021 - Present")
st.write(
    """
- ► Used lots of coding platforms
- ► Had Experience on team work of 3 people
- ► Well-knowing some basic coding skills
"""
)
