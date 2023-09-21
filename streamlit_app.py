# Streamlitライブラリをインポート
import streamlit as st
import random



# タイトルを設定
st.title('おみくじアプリ')

if st.button("おみくじを引く"):
   results=["メガビッグ","ロト7","ハロウィンジャンボ","大吉","中吉","小吉","吉","凶","大凶"]
   result=random.choice(results)
   st.write(f"結果:{result}")
