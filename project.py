import streamlit as st
import requests

#ฟังก์ชันสำหรับค้นหา Anime
def search_anime(query):
    url = (f'https://api.jikan.moe/v4/anime?q={query}&sfw')
    response = requests.get(url)
    data = response.json()
    return data['data']

#หน้าเว็บ
def main():
    st.title('Anime Search')
    
    # ช่องใส่ข้อความสำหรับค้นหา Anime
    query = st.text_input('ค้าหา')
    
    # เมื่อกดปุ่มค้นหา
    if st.button('ค้นหา'):
        results = search_anime(query)
        
        # แสดงผลลัพธ์
        for result in results:
            st.title(f"ชื่อ: {result['title']}")
            st.subheader(f"ประเภท: {result['type']}")
            st.subheader(f"จำนวนตอน: {result['episodes']}")
            st.subheader(f"คะแนน: {result['score']}")
            st.image(result['images']['jpg']['image_url'], width=200)

if __name__ == '__main__':
    main()
bg = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://wallpaper-mania.com/wp-content/uploads/2018/09/High_resolution_wallpaper_background_ID_77700124558.jpg");
background-size: cover;
}

}
</style>
"""
st.markdown(bg, unsafe_allow_html=True) 