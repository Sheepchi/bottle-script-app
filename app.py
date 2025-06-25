# app.py
import streamlit as st

st.set_page_config(page_title="弗雷尔卓德瓶盖", layout="centered")

# ------------------------
# 初始化状态
# ------------------------
if "step" not in st.session_state:
    st.session_state.step = 0
if "red_alert" not in st.session_state:
    st.session_state.red_alert = False

# ------------------------
# 工具函数
# ------------------------

def reset_story():
    st.session_state.step = 0
    st.session_state.red_alert = False
    st.rerun()

def trigger_red_alert():
    st.session_state.red_alert = True
    st.session_state.step = -1
    st.rerun()

def form_choice(prompt, options: dict, correct_key: str, key_prefix: str):
    with st.form(key=f"{key_prefix}_form"):
        st.markdown(f"**{prompt}**")
        choice = st.radio("请选择：", options, format_func=lambda x: options[x], key=f"{key_prefix}_choice")
        submitted = st.form_submit_button("提交")
        if submitted:
            if choice != correct_key:
                trigger_red_alert()
            else:
                st.session_state.step += 1
                st.rerun()

# ------------------------
# 页面内容
# ------------------------

st.title("🍺 弗雷尔卓德瓶盖 · 互动剧本")

if st.session_state.red_alert:
    st.error("👿 对方红温，饭局提前结束！")
    if st.button("🔁 重新开始"):
        reset_story()

elif st.session_state.step == 0:
    st.write("你开瓶盖，“啪”一声，瓶盖飞到对方的菜里。")
    st.write('对方：“**ber哥们咋开的瓶盖啊？都开我菜里啦！**”')
    form_choice(
        prompt="你要怎么回应？",
        options={
            "1": "开个瓶盖都不行？我还不能吃饭了？",
            "2": "怪我咯？你自己坐太近了吧。",
            "3": "对不起哥们，我给你换一盘吧，实在对不住。"
        },
        correct_key="3",
        key_prefix="step0"
    )

elif st.session_state.step == 1:
    st.write("对方：你都这么说了那还说啥了？拿出来扔了就完事了呗")
    form_choice(
        prompt="你要怎么回应？",
        options={
            "1": "实在是不好意思",
            "2": "你计较太多了吧",
            "3": "菜又没坏，不至于吧"
        },
        correct_key="1",
        key_prefix="step1"
    )

elif st.session_state.step == 2:
    st.info("大家各自回桌继续吃饭。")
    st.write("对方：哎哥们你还有烟吗？")
    st.write("朋友：没有")
    st.write("对方：哎，服务员……")
    form_choice(
        prompt="你听到了这一幕，打算起身帮忙吗？",
        options={
            "1": "是，让老婆去拿烟",
            "2": "否，继续吃饭当没听见"
        },
        correct_key="1",
        key_prefix="step2"
    )

elif st.session_state.step == 3:
    form_choice(
        prompt="你会怎么做？",
        options={
            "1": "这点事也值得叫服务员？自己去买呗。",
            "2": "哥们，我这儿正好有烟！你先抽着",
            "3": "你抽不抽关我啥事？"
        },
        correct_key="2",
        key_prefix="step3"
    )

elif st.session_state.step == 4:
    st.write("对方：这多不好意思")
    form_choice(
        prompt="你会怎么回应？",
        options={
            "1": "给你就拿着，别逼逼",
            "2": "大家都是弗弗雷尔卓德人，没有那些个",
            "3": "那你还我"
        },
        correct_key="2",
        key_prefix="step4"
    )

elif st.session_state.step == 5:
    st.info("对方：你说这扯不扯？")
    if st.button("继续"):
        st.session_state.step += 1
        st.rerun()

elif st.session_state.step == 6:
    st.write("对方：行哥们，你先吃我们走了昂")
    st.write("我：服务员，买单")
    st.write("服务员：买过单了哥")
    st.write("我：媳妇，你买单了吗？")
    st.write("老婆：我没买啊")
    st.write("我：谁买的？")
    st.write("服务员：刚才后面那桌一起结的。")
    if st.button("站起身，看着他们走到门口"):
        st.session_state.step += 1
        st.rerun()

elif st.session_state.step == 7:
    form_choice(
        prompt="你最后要说什么？",
        options={
            "1": "哎，兄弟！🙏",
            "2": "看不出来你还有点人情味儿",
            "3": "你是不是图什么啊？结账干嘛？"
        },
        correct_key="1",
        key_prefix="step7"
    )

elif st.session_state.step == 8:
    st.success("你双手合十表示感谢 🙏")
    st.write("【BGM】“提着昨日种种千辛万苦，向明天换一些美满和幸福……”")
    st.write("对方：🙏（合十并挥手）")
    st.balloons()
    if st.button("🎬 完成剧本，重新开始"):
        reset_story()
