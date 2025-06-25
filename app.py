import streamlit as st

def choose(question, opts, correct):
    st.write(question)
    choice = st.radio("", list(opts.keys()), format_func=lambda x: f"{x}: {opts[x]}")
    if st.button("确认"):
        if choice != correct:
            st.error("👿 对方红温，局面瞬间失控……")
            if st.button("🔁 重新开始"):
                st.experimental_rerun()
            st.stop()
        return opts[choice]
    st.stop()

def main():
    st.title("🍺 瓶盖飞进菜里 · 互动剧本")

    st.write("你开瓶盖，“啪”一声，瓶盖飞到对方的菜里。")
    st.write("对方：**“ber哥们咋开的瓶盖啊？都开我菜里啦！”**")

    apology = choose(
        "你要怎么回应？",
        {
            "1": "对不起哥们，我给你换一盘吧，实在对不住。",
            "2": "怪我咯？你自己坐太近了吧。",
            "3": "开个瓶盖都不行？我还不能吃饭了？"
        },
        "1"
    )
    st.write(f"我：{apology}")

    st.write("对方：你都这么说了那还说啥了？拿出来扔了就完事了呗")
    followup = choose(
        "你接着怎么说？",
        {
            "1": "实在是不好意思",
            "2": "你计较太多了吧",
            "3": "菜又没坏，不至于吧"
        },
        "1"
    )
    st.write(f"我：{followup}")

    st.write("---\n对方向朋友借烟，朋友回答 “没有”")
    help_decision = choose(
        "你听到了，打算帮忙吗？",
        {
            "1": "是，起身去后备箱拿烟",
            "2": "否，继续吃饭没听到"
        },
        "1"
    )
    st.write(f"我：{help_decision}")

    smoke_help = choose(
        "你接下来怎么做？",
        {
            "1": "哥们，我这儿正好有烟！你先抽着",
            "2": "这点事也值得叫服务员？",
            "3": "你抽不抽关我啥事？"
        },
        "1"
    )
    st.write(f"我：{smoke_help}")
    st.write("对方：这多不好意思，谢谢昂")

    st.write("对方：你说这扯不扯？")
    if st.button("回应“这真挺扯的哈哈”"):
        st.write("我：这真挺扯的哈哈")
    else:
        st.error("👿 触发红温！")
        if st.button("🔁 重新开始"):
            st.experimental_rerun()
        st.stop()

    st.write("对方：行哥们，你先吃我们走了昂")
    st.write("我：服务员，买单")
    st.write("服务员：买单了哥")
    st.write("朋友：我没买啊")
    st.write("服务员：刚才后面那桌一起结的。")

    final_thanks = choose(
        "你最后要说什么？",
        {
            "1": "哎，兄弟！🙏",
            "2": "看不出来你还有点人情味儿",
            "3": "你是不是图什么啊？结账干嘛？"
        },
        "1"
    )
    st.write(f"我：{final_thanks}")

    st.write("🙏🙏")
    st.write("🎵 BGM: ‘提着昨日种种千辛万苦…’")
    st.balloons()
    if st.button("🔁 重新开始"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
