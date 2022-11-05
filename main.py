import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
import time


st.title('Streamlit 超入門')


# """
# #   章
# ##  節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """





# st.write('DataFrame')

# df = pd.DataFrame({
#     '1列目': [1,2,3,4],
#     '2列目': [10,20,30,40]
# })

# df = pd.DataFrame(
#     np.random.rand(20,3),   #20行3列の行列にランダムに数字が入る
#     columns=['a','b','c']   #列名にabcの名前を付ける
# )

# st.line_chart(df)   #動的な折れ線グラフを描けるのでズームやグラフの保存が可能
# st.area_chart(df)   #動的な折れ線グラフ（積分部分の塗り潰しあり）を描けるのでズームやグラフの保存が可能
# st.bar_chart(df)   #動的な積み上げ棒グラフを描けるのでズームやグラフの保存が可能

# st.write(df)  #writeでは引数の指定が不可で表の大きさの指定などはできない、大きい順に並び替えなど表示後に操作可能（動的）
# st.dataframe(df.style.highlight_max(axis=0),width=300,height=300)   #axis=0で列・=1で行を意味する
# st.table(df.style.highlight_max(axis=0))   #編集不可の表を表示することができる（静的）

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50]+[35.69,139.70],  #100行2列の行列にランダムに数字が入る・行列それぞれの値を50で割る・東京の緯度経度に近づける
#     columns=['lat','lon']   #列名にlat緯度・lon経度の名前を付ける
# )
# st.map(df)  #東京付近の地図に該当する緯度経度をマッピングできる（動的）





# st.write('Display Image')

# if st.checkbox('Show Image'):
#     img = Image.open('sample.jpg')
#     st.image(img,caption='Ayuni・D',use_column_width=True)  #captionは画像名称・use_colunmn_widthはWebアプリに合わせたサイズでの表示を意味





# st.write('Interactive Widgets') #ウィジェットはグラフィカルユーザインタフェースのインタフェース部品の総称を意味
# option = st.selectbox(
#     'あなたが好きな数字を教えてください、',
#     list(range(1,11))
# )
# 'あなたの好きな数字は、', option, 'です。'

# text = st.text_input('あなたの趣味を教えてください、')  #st.sidebar.text_inputで左端に別途表示が可能・回答表示はsidebarに入れないので中央表示
# 'あなたの趣味：', text
# condition = st.slider('あなたの今の調子は？',0,100,50)  #最小～最大のバーの値とデフォルト値を指定
# 'コンディション：',condition

# left_column,right_column = st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# expander1 = st.expander('お問合せ①')
# expander1.write('お問合せ①の回答')
# expander2 = st.expander('お問合せ②')
# expander2.write('お問合せ②の回答')





st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)    #プログレスバーの表示（ゲージが溜まっていく）

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.05)

'Done!!'
