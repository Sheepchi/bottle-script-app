# -*- coding: utf-8 -*-
"""
瓶盖飞进菜里：原剧本基础 + 正误选项互动 + 红温结局 + 是否起身判断
"""

def prompt_enter(msg="按回车继续…"):
    input(f"\n[{msg}]")

def choose(prompt, options, correct_key):
    print(f"\n{prompt}")
    print("（请输入数字，然后回车）")
    for key, desc in options.items():
        print(f"  {key}. {desc}")
    choice = None
    while choice not in options:
        choice = input("你的选择: ").strip()
    if choice != correct_key:
        trigger_red_alert()
    return options[choice]

def trigger_red_alert():
    print("\n对方：你什么意思？啊？👿👊")
    print("【结局】对方红温，饭局提前结束，烟也没了，饭也没吃。")
    print("💥 剧本中断。")
    retry = input("\n是否重新开始？(y/n): ").strip().lower()
    if retry == "y":
        print("\n🔄 正在重新开始剧本...\n")
        main()  # 重新启动
    else:
        print("\n❌ 剧本终止。再见！")
        exit()

def main():
    print("🎬 剧情开始：你开瓶盖，瓶盖飞入对方菜里")
    prompt_enter("按回车“啪”地开瓶盖")

    print("\n对方：ber哥们咋开的瓶盖啊？都开我菜里啦！")
    apology = choose(
        "你要怎么回应？",
        {
            "1": "对不起哥们，我给你换一盘吧，实在对不住。",
            "2": "怪我咯？你自己坐太近了吧。",
            "3": "开个瓶盖都不行？我还不能吃饭了？"
        },
        correct_key="1"
    )
    print(f"\n我：{apology}")
    prompt_enter("按回车继续")

    print("\n对方：你都这么说了那还说啥了？拿出来扔了就完事了呗")
    followup = choose(
        "你要怎么回应？",
        {
            "1": "实在是不好意思",
            "2": "你计较太多了吧",
            "3": "菜又没坏，不至于吧"
        },
        correct_key="1"
    )
    print(f"\n我：{followup}")
    prompt_enter("按回车回到自己桌前继续吃饭")

    print("\n--- 大家各自回桌继续吃饭 ---")
    prompt_enter("按回车进入“要烟”环节")

    print("\n对方：哎哥们你还有烟吗？")
    print("朋友：没有")
    print("对方：哎，服务员……")

    # 新增：是否起身帮忙判断
    help_decision = choose(
        "你听到了这一幕，打算起身帮忙吗？",
        {
            "1": "是，让老婆去拿烟",
            "2": "否，继续吃饭当没听见"
        },
        correct_key="1"
    )

    smoke_help = choose(
        "你会怎么做？",
        {
            "1": "哥们，我这儿正好有烟！你先抽着",
            "2": "这点事也值得叫服务员？自己去买呗。",
            "3": "你抽不抽关我啥事？"
        },
        correct_key="1"
    )
    print(f"\n我：{smoke_help}")
    print("对方：这多不好意思")

    reply_help = choose(
        "你会怎么回应？",
        {
            "1": "给你就拿着，别逼逼",
            "2": "大家都是弗弗雷尔卓德人，没有那些个",
            "3": "那你还我"
        },
            correct_key = "2"
    )

    # 对方小总结
    print("\n对方：你说这扯不扯？")
    prompt_enter("按回车继续")

    # 对方路过告别
    print("\n对方：行哥们，你先吃我们走了昂")

    # 你结账
    print("\n我：服务员，买单")
    print("服务员：买过单了哥")
    print("我：媳妇，你买单了吗？")
    print("老婆：我没买啊")
    print("我：谁买的？")
    print("服务员：刚才后面那桌一起结的。")

    # 大结局
    prompt_enter("你站起身，看着他们走到门口")
    final_thanks = choose(
        "你最后要说什么？",
        {
            "1": "哎，兄弟！🙏",
            "2": "看不出来你还有点人情味儿",
            "3": "你是不是图什么啊？结账干嘛？"
        },
        correct_key="1"
    )
    print(f"\n我：{final_thanks}")
    prompt_enter("你双手合十表示感谢")

    print("🙏🙏")

    prompt_enter("按回车播放 BGM")
    print("【BGM】“提着昨日种种千辛万苦，向明天换一些美满和幸福……”")

    print("对方：🙏（合十并挥手）")

    # 结束
    prompt_enter("按回车退出剧本")
    print("\n🎉 剧本结束，完美落幕！")

if __name__ == "__main__":
    main()
