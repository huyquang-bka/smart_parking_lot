import cv2
import streamlit as st
from tools import detect


st.set_page_config("Smart Parking App", ":car", "wide", "expanded")

list_busy = []

selections = ["Vào", "Ra", "Bản đồ"]
st.sidebar.title("Bãi đỗ xe thông minh")
st_selections = st.sidebar.selectbox("", selections)

if st_selections == "Vào":
    st.markdown("<h1 style='text-align: center; color: white;'>Vào</h1>", unsafe_allow_html=True)
    image_upload = st.sidebar.file_uploader("Tải lên ảnh", type=["png", "jpg", "jpeg"])
    submit = st.sidebar.button("Chấp nhận", key="submit")
    if submit and image_upload is not None:
        with open(f"resources/images/{image_upload.name}", "wb") as f:
            f.write(image_upload.getbuffer())
        st.sidebar.success("Lưu thành công")
        with st.container():
            col1, slot_col_0, slot_col_1, slot_col_2, slot_col_3, slot_col_4 = st.columns([5, 1, 1, 1, 1, 1])
            col1.image(f"resources/images/{image_upload.name}", width=400)
            slot_cols = [slot_col_0, slot_col_1, slot_col_2, slot_col_3, slot_col_4]
            slots = []
            for i in range(5):
                for j in range(5):
                    slot = i * 5 + j + 1
                    if slot in list_busy:
                        slot_cols[i].markdown(f"<h1 style='text-align: center; color: red; font-size: 20px;'>{slot}</h1>", unsafe_allow_html=True)
                    else:
                        slot_cols[i].markdown(f"<h1 style='text-align: center; color: green; font-size: 20px;'>{slot}</h1>", unsafe_allow_html=True)     
        with st.container():
            col_text, col_text_input = st.columns([1, 1])
            col_text.markdown("<h1 style='text-align: center; color: white;'>Loại xe</h1>", unsafe_allow_html=True)
            col_text.markdown("<h1 style='text-align: center; color: white;'>Biển số xe</h1>", unsafe_allow_html=True)
            with st.spinner("Đang xử lý"):
                image = cv2.imread(f"resources/images/{image_upload.name}")
                cls, lp_text = detect(image)
                if cls in [2, 5, 7]:
                    cls = "Ô tô"
                elif cls in [2]:
                    cls = "Xe máy"
                col_text_input.text_input(f"", key="cls", value=cls)
                col_text_input.text_input(f"", key="lp_text", value=lp_text)
            is_set = False
            for i in range(1, 26):
                if slot in list_busy:
                    continue
                for i in range(5):
                    for j in range(5):
                        slot = i * 5 + j + 1
                        if slot == i:
                            print(slot, i)
                            slot_cols[i].markdown(f"<h1 style='text-align: center; color: yellow; font-size: 20px;'>{slot}</h1>", unsafe_allow_html=True)
                            list_busy.append(slot)
                            is_set = True
                            break
                    if is_set:
                        break
                if is_set:
                    is_set = False
                    break
        
        
        