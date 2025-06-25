import streamlit as st

# 用于存储用户选择状态
if "step" not in st.session_state:
    st.session_state.step = 0
if "fail" not in st.session_state:
    st.session_state.fail = False

# 多步选择题函数
def choose(question, opts, correct, step_key):
    st.write(question)
    choice = st.radio("请选择：", list(opts.keys()), format_func=lambda x: f"{x}. {opts[x]}", key=f"radio_{step_key}")
    if st.button("确认", key=f"btn_{step_key}"):
        if choice != correct:
            st.session_state.fail = True
        else:
            st.session_state.step += 1

def main():
    st.title("🍺 瓶盖飞进菜里 · 互动剧本")

    if st.session_state.fail:
        st.error("👿 对方红温，饭局提前结束！")
        if st.button("🔁 重新开始"):
            st.session_state.step = 0
            st.session_state.fail = False
            st.experimental_rerun()
        st.stop()

    step = st.session_state.step

    if step == 0:
        st.write("你开瓶盖，“啪”一声，瓶盖飞到对方的菜里。")
        st.write("对方：**“ber哥们咋开的瓶盖啊？都开我菜里啦！”**")
        choose(
            "你要怎么回应？",
            {
                "1": "对不起哥们，我给你换一盘吧，实在对不住。",
                "2": "怪我咯？你自己坐太近了吧。",
                "3": "开个瓶盖都不行？我还不能吃饭了？"
            },
            "1",
            step_key=0
        )

    elif step == 1:
        st.write("对方：你都这么说了那还说啥了？拿出来扔了就完事了呗")
        choose(
            "你接着怎么说？",
            {
                "1": "实在是不好意思",
                "2": "你计较太多了吧",
                "3": "菜又没坏，不至于吧"
            },
            "1",
            step_key=1
        )

    elif step == 2:
        st.write("---")
        st.write("对方向朋友借烟，朋友说：没有")
        choose(
            "你听到了，打算帮忙吗？",
            {
                "1": "是，起身去后备箱拿烟",
                "2": "否，继续吃饭没听到"
            },
            "1",
            step_key=2
        )

    elif step == 3:
        choose(
            "你会怎么做？",
            {
                "1": "哥们，我这儿正好有烟！你先抽着",
                "2": "这点事也值得叫服务员？",
                "3": "你抽不抽关我啥事？"
            },
            "1",
            step_key=3
        )

    elif step == 4:
        st.write("对方：这多不好意思，谢谢昂")
        choose(
            "你怎么回应？",
            {
                "1": "给你就拿着，别逼逼",
                "2": "大家都是弗雷尔卓德人，没有那些个",
                "3": "那你还我"
            },
            "2",
            step_key=4
        )

    elif step == 5:
        st.success("🎵 BGM: 提着昨日种种千辛万苦…")
        st.write("对方：你说这扯不扯？")
        choose(
            "你要怎么回应？",
            {
                "1": "这真挺扯的哈哈",
                "2": "你自己想想谁错？",
                "3": "哥们咱没啥聊的"
            },
            "1",
            step_key=5
        )

    elif step == 6:
        st.write("对方：行哥们，你先吃我们走了昂")
        st.write("我：服务员，买单")
        st.write("服务员：买过单了哥")
        st.write("朋友：我没买啊")
        st.write("服务员：刚才后面那桌一起结的。")
        choose(
            "你最后要说什么？",
            {
                "1": "哎，兄弟！🙏",
                "2": "看不出来你还有点人情味儿",
                "3": "你是不是图什么啊？结账干嘛？"
            },
            "1",
            step_key=6
        )

    elif step == 7:
        st.balloons()
        st.success("🎉 剧本结束，完美落幕！")
        if st.button("🔁 重新开始"):
            st.session_state.step = 0
            st.experimental_rerun()

if __name__ == "__main__":
    main()
