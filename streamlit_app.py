# Streamlitライブラリをインポート
import streamlit as st
import random

# ページ設定（タブに表示されるタイトル、表示幅）
st.set_page_config(page_title="タイトル", layout="wide")

# タイトルを設定
st.title('おみくじアプリ')

if st.button("おみくじを引く")
   results=["大吉","中吉","小吉","吉","凶","大凶"]
   result=random.choice(results)
   st.write("結果:{result}")
