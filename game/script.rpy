﻿define p = Character("旁白", color="#E7374E")
define sage = Character("桑吉Sage", color="#E7374E")
define asahi = Character("晨宝", color="#ffd900")
define bf = Character("毕方", color="#fcce9a")
define ly = Character("六翼", color="#a4faa1")

default choose_1 = False
default choose_2 = False

label start:

    play music "<from 13>audio/1.mp3"

    "很久很久以前，有一只谜之小生物。"

    "为了躲避调查员的追杀，小生物使用了由好心的外星猫猫提供的修女身体。"

    "可是，此时的小生物并不理解人类这一物种。"

    "为了更好藏匿在人类社会之中，小生物开始了对人类的调查"

    "去哪里调查人类？"

menu:

    "机场":
        jump label_airport

    "公司":
        jump label_company

    "菜市场":
        jump label_market

label label_airport:

    "小生物来到了一处机场"
    "据猫猫说，这样的交通要道是人类聚集之地。"
    "想必在这样的地方，一定能看到不少有趣的人类故事。"
    "可能是由于疫情缘由，机场的人并不算多。而这稀疏人群中，大厅正中央中伫立着的三位男性格外醒目。"
    "三人均是面色凝重，即便不熟悉人类文化的小生物也能感觉到空气中的沉重气氛。"
    "僵持许久，年纪最轻的男孩开口打破了沉默。"
    asahi "毕方...别走"
    "但仅仅短短四个字，宛如压垮骆驼的最后一根稻草，让对面的金发红瞳资本家泪如雨下。"
    bf "混蛋，你为什么来...!"
    bf "...混蛋，为什么你会找到啊！"
    "情感宛如涌出的泪水，无法压抑无法控制地随着重力坠落。"
    "“啪嗒”"
    "翻涌的内心，促使晨宝向对面奔去。"
    bf "！停下，晨宝，六翼在看着..."
    "这样是不行的。"
    "这样是不能被允许的。"
    "晨宝不应该背叛六翼。"
    "那个每天在群里笑笑闹闹，给自己发红豆流汗脸的六翼。"
    "那个打出“狠狠地撅晨宝”之后，又会附上傲娇表情的六翼。"
    "那个在DD歌会用歌声唱出“gamer和晨宝相比，那我还是觉得晨宝刺激”的六翼。"
    "那个一直守望着自己，说着“晨宝，就算你被撅了，我还是爱你的”的六翼。"
    "大脑在大声尖叫停止，心脏中负罪感多到快要爆炸了。"
    "可是，可是——"
    "即便如此，晨宝飞奔的脚步也没有停止。"
    "即便如此，晨宝身体中的每一个细胞都在尖叫，都在呐喊"
    "“晨宝好喜欢毕方。”"
    asahi "对不起，对不起，六翼..."
    "晨宝抱住了毕方。"
    scene cg1
    "他们接吻了。"
    "晨宝和毕方深深吻住了对方"
    "用仿佛明天世界就会毁灭一般的，仿佛这就是二人仅剩最后一秒般的热情亲吻对方。"
    bf "唔...晨宝...啾..."
    asahi "啾..."
    "一旁六翼注视着二人。"
    "用酸楚的，痛苦的，又温柔的希冀着二人获得幸福的目光默默地注视着他们。"
    "公主找到了王子，晨宝找到了毕方。"
    "从此他们就幸福地生活在了一起。"
    "对于传统意义上的故事而言，这应当就是Happy Ending了。"
    "和主角无关的配角就应当在这里退场，让主角满意，让作者满意，让观众满意。"
    "——可是，好不甘心。"
    "——可是，好痛苦。"
    ly "明明，是我先来的..."
    ly "拥抱也好，撅撅也好，明明都是我先来的..."
    ly "为什么会这样呢...一边是喜欢的晨宝，一边是水群的朋友，为什么..."
    ly "....不甘心，不甘心，不甘心...呜..."
    ly "...我...我应该怎么做..."
    "此时小生物应该...？"

menu:
    "劝说六翼放弃晨宝":
        $ choose_1 = True
        jump label_a1
    "劝说六翼继续追求晨宝":
        $ choose_2 = True
        jump label_a2


label label_company:


label label_market:


return