# Streamlitライブラリをインポート
import streamlit as st
import random



# タイトルを設定
st.title('ラッキーカラーアプリ！')

if st.button("今日のラッキーカラー"):
   results=["グレー","黒","白","茶","紫","ピンク","オレンジ","水色","緑","黄","青","赤"]
   result=random.choice(results)
   st.write(f"結果:{result}")

if st.button("今日のラッキーアイテム"):
   items=["バッグ","靴下","靴","ブレスレット","ネックレス","ピアス","ヘアアクセサリー","リング"]
   item=random.choice(items)
   st.write(f"結果:{item}")
   


