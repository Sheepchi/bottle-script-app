import streamlit as st

st.set_page_config(page_title="弗雷尔卓德瓶盖 · 互动剧本", page_icon="🍻")

# 初始化状态
if "step" not in st.session_state:
    st.session_state.step = 0
if "fail" not in st.session_state:
    st.session_state.fail = False

# 红温结局处理
def red_alert():
    st.session_state.fail = True
    st.error("👿 对方红温，饭局提前结束！")
    st.button("🔁 重新开始", on_click=reset_app)

# 重置状态
def reset_app():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# 主流程
def main():
    st.title("🍻 瓶盖飞进菜里 · 互动剧本")

    if st.session_state.fail:
        st.error("【结局】对方红温，饭局提前结束，烟也没了，饭也没吃。")
        if st.button("🔁 重新开始"):
            reset_app()
        return

    # step 0
    if st.session_state.step == 0:
        st.write("你开瓶盖，“啪”一声，瓶盖飞到对方的菜里。")
        st.write('对方：“**ber哥们咋开的瓶盖啊？都开我菜里啦！**”')
        st.write("你要怎么回应？")
        choice = st.radio("选择回应：", [
            "对不起哥们，我给你换一盘吧，实在对不住。",
            "怪我咯？你自己坐太近了吧。",
            "开个瓶盖都不行？我还不能吃饭了？"
        ])
        if st.button("提交"):
            if choice.startswith("对不起"):
                st.session_state.step += 1
            else:
                red_alert()

    # step 1
    elif st.session_state.step == 1:
        st.write('对方：“你都这么说了那还说啥了？拿出来扔了就完事了呗”')
        choice = st.radio("你要怎么回应？", [
            "实在是不好意思",
            "你计较太多了吧",
            "菜又没坏，不至于吧"
        ])
        if st.button("提交"):
            if choice.startswith("实在"):
                st.session_state.step += 1
            else:
                red_alert()

    # step 2
    elif st.session_state.step == 2:
        st.write("🎭 大家各自回桌继续吃饭……")
        st.write("对方：哎哥们你还有烟吗？\n\n朋友：没有\n\n对方：哎，服务员……")
        choice = st.radio("你听到了，打算起身帮忙吗？", [
            "是，让老婆去拿烟",
            "否，继续吃饭当没听见"
        ])
        if st.button("提交"):
            if choice.startswith("是"):
                st.session_state.step += 1
            else:
                red_alert()

    # step 3
    elif st.session_state.step == 3:
        st.write("你走过去：")
        choice = st.radio("你会怎么做？", [
            "哥们，我这儿正好有烟！你先抽着",
            "这点事也值得叫服务员？自己去买呗。",
            "你抽不抽关我啥事？"
        ])
        if st.button("提交"):
            if choice.startswith("哥们"):
                st.session_state.step += 1
            else:
                red_alert()

    # step 4
    elif st.session_state.step == 4:
        st.write('对方：“这多不好意思”')
        choice = st.radio("你会怎么回应？", [
            "大家都是弗雷尔卓德人，没有那些个",
            "给你就拿着，别逼逼",
            "那你还我"
        ])
        if st.button("提交"):
            if choice.startswith("大家"):
                st.session_state.step += 1
            else:
                red_alert()

    # step 5
    elif st.session_state.step == 5:
        st.write("对方：“你说这扯不扯？”\n\n对方：行哥们，你先吃我们走了昂")
        st.write("你：服务员，买单\n\n服务员：买过单了哥\n\n你：谁买的？\n\n服务员：刚才后面那桌一起结的。")
        choice = st.radio("你最后要说什么？", [
            "哎，兄弟！🙏",
            "看不出来你还有点人情味儿",
            "你是不是图什么啊？结账干嘛？"
        ])
        if st.button("提交"):
            if choice.startswith("哎"):
                st.session_state.step += 1
            else:
                red_alert()

    # step 6 结局
    elif st.session_state.step == 6:
        st.success("🎉 剧本完美落幕！")
        st.write("你双手合十表示感谢，对方也挥手回应。\n\n【BGM】“提着昨日种种千辛万苦，向明天换一些美满和幸福……”")
        st.balloons()
        if st.button("🔁 再来一遍"):
            reset_app()


# 运行主函数
main()
