﻿define sage = Character("桑吉Sage", color="#E7374E", image="sage")
define asahi = Character("晨宝", color="#fda0a5", image="asahi")
define bf = Character("毕方", color="#fcce9a", image="bf")
define ly = Character("六翼", color="#a4faa1", image="ly")
define bl = Character("冰蓝", color="#95f3ff", image="bl")
define jj = Character("江江", color="#728A6A", image="jj")
define o27 = Character("027", color="#236a00", image="027")
define hb = Character("红白", color="#B93737", image="hb")
define xq = Character("袭秋", color="#70e2b1", image="xq")

image sage_i = "sage.png"
image side sage = "side_sage.png"
image side asahi = "side_asahi.png"
image side bf = "side_bf.png"
image side ly = "side_ly.png"
image side bl = "side_bl.png"
image side jj = "side_jj.png"
image side 027 = "side_027.png"
image side hb = "side_hb.png"
image side xq = "side_xq.png"

default choose_a1 = False
default choose_a2 = False
default choose_b1 = False
default choose_b2 = False
default choose_c1 = False
default choose_c2 = False
default label_airport_show = False
default label_company_show = False
default label_market_show = False

label before_main_menu:
    scene sky
    "今天你检查更新了吗？"
    menu:
        "是":
            return
        "否":
            $ updater.update("http://game.sage.osttsstudio.ltd/st/updates.json", base=None, force=False, public_key=None, simulate=None, add=[], restart=True, confirm=True, patch=True)

label start:
    scene sky
    play music "<from 13>audio/1.mp3"
    "... ..."
    "... ..."
    "很久很久以前，有一只谜之小生物。"

    "为了躲避调查员的追杀，小生物使用了由好心的外星猫猫提供的修女身体。"

    "可是，此时的小生物并不理解人类这一物种。"

    "为了更好藏匿在人类社会之中，小生物开始了对人类的调查"

menu:
    sage "去哪里调查人类？"

    "机场":
        jump label_airport

    "公司":
        jump label_company

    "菜市场":
        jump label_market

label label_airport:
    scene airport
    $ label_airport_show = True

    "小生物来到了一处机场"
    show sage_i at left
    sage "据猫猫说，这样的交通要道是人类聚集之地。"
    sage "想必在这样的地方，一定能看到不少有趣的人类故事。"
    hide sage_i
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
    jump label_choose1

label label_company:
    scene company
    $ label_company_show = True

    "小生物来到了一处公司。"
    show sage_i at left
    sage "据说这里是人类用劳动力换取报酬的地方，这对小生物而言是一个全新的概念。"
    sage "想要用劳动力换取报酬的前提条件，则是参加一种名为“面试”的东西。"
    sage "今天，这家名为“楠桐工作室”的公司正在展开一场面试。"
    hide sage_i
    "好奇的小生物溜进去时，正好是面试的中途。"
    bl "你以为你接受的是谁的爱？是我的爱！"
    "坐在面试官位置的少女似乎正对面试者大发雷霆。"
    bl "我的爱！我的如此珍贵的爱！"
    bl "你竟敢拒绝我的爱！"
    "办公室的其他员工窃窃私语。"
    "(员工)游魂" "我又漏看了两集？冰蓝这是怎么了？"
    "(员工)桶鸟" "我不知道啊，昨天她不是和老G一起约会去了吗？照理说约会之后心情不应该非常好吗？"
    "(员工)027" "嘘——你忘啦？上次冰蓝妹妹背着gamer给我偷偷发消息的事情？就是那个“027，gamer不在，人家想你啦><”那个！"
    "(员工)猫店长" "这么说是有这么一回事，G先生该不会..."
    "(员工)雨林" "唔这么说gamer桑不太好吧..."
    "(员工)殷红" "哎呀兄弟们，这个我觉得还是得再看看再看看。总之先吃瓜——"
    "这些精确控制音量的八卦猜测并没有传到当事人的耳朵里，冰蓝只是气呼呼地瞪着面前的人。"
    "坐立不安的江江却听到了大家的讨论，有些尴尬地扭了扭脖子。"
    jj "那个..."
    "江江才张嘴，就换来对方的狠狠一瞪。"
    "他吞吞口水，艰难地说出了下半句话。"
    jj "我，那个，对不起，你，你是个好人。"
    "听了这句话，对面的火气更大了。"
    bl "为什么！！！你为什么要拒绝我的爱！"
    bl "没有人，没有人可以拒绝我的爱！"
    bl "只要你点点头接受了我，你现在就可以入职！"
    bl "不用再去参加任何的面试，不用再担心被开除。"
    bl "不用再担心像那个新闻里的45岁阿姨一样因为失业只能住桥洞里了。"
    bl "不用捡瓶盖，不用睡纸板箱，更不用担心半夜涨潮被河水冲走。"
    bl "你只需要接受我，然后在这份劳动合同上签名。"
    bl "然后每天工作18小时每周工作7天就可以了！"
    bl "还有经常的加班能够让你实现个人价值！这不是非常棒的条件吗！"
    bl "江江！把你余生的剩余价值交给我吧！"
    "说到激动处，冰蓝向对方伸出手，却被对方歪头躲过。"
    jj "不好意西我想起来还有三十分钟我最爱的节目假面来不打就要播了我先走了——"
    "江江宛如脱缰的菜狗一般冲出了办公室，只余下一片寂静。"
    "孤独的冰蓝呆呆矗立在办公室的中央，还维持着手臂前伸的姿势。"
    bl "..."
    "(员工)桶鸟" "冰蓝酱好像有点可怜啊，昨天才被老G那样对待今天又失恋了。"
    "(员工)露鸢" "比起可怜她，我想先问一下我们能挂她吗？"
    "(员工)殷红" "我也觉得该挂啊兄弟们。"
    "(员工)猫店长" "不太好吧，好歹过两天再挂。和G先生挂一起岂不是更好。"
    jump label_choose2

label label_market:
    scene market2
    $ label_market_show = True

    "小生物来到了一座菜市场。"
    show sage_i at left
    sage "正所谓人生在世，吃喝二字，要了解人类，就应该从人类的吃喝学起。"
    sage "菜市场就自然是一个非常值得调查的地方。"
    hide sage_i
    "小贩的吆喝声、顾客的讨价还价声、哐哐的剁肉声交织在一起，奏成了一首满是人间烟火气息的交响曲。"
    "小生物正跟随着人流缓慢前行着，她的目光突然被一处摊贩吸引。"
    "这个小摊处于菜市场的边缘位置，地上铺着一张红白蓝的塑料布，左半边不太齐整地排着几条不同种类的死鱼，而右半边则搁着一只水盆。水盆的旁边立着足有半人高的硬纸板，拿红漆刷着几个大字。"
    "“王靳鱼专卖”"
    "老板是皮肤发绿的健壮男人，光头在正午的太阳下折射出一片明亮的光辉，此时正忙着招揽面前的客人。"
    o27 "哟靓仔，买点什么不？看看新到的蛇和鱼和王靳鱼吗？"
    hb "？王靳鱼是什么东西"
    "老板露出一个营业笑容，伸手示意周围的客人都靠近一些。"
    "小生物也向前走了几步，这时它才清楚地看见，水盆里摆放着一条非常特别的鱼。"
    "它的形状有些许像缩小版的鲸鱼，但这条鱼的前脊处长着一排形状奇怪的鳍，从远处看仿佛头上顶着王冠。"
    o27 "来，看看这条鱼二位。这可是稀有的好东西。"
    o27 "据说这鱼产自极东之地的桑尾草园，非常受当地人的喜爱。"
    o27 "它不仅外表美丽，具有极高的使用价值；而且营养丰富，味道也极其鲜美。"
    o27 "是居家旅行必备之良品啊！"
    hb "哦哦，听老板这么说我有点心动了啊。既然是出了名的好吃的鱼，过几天家里人生日的主菜就用这个吧。"
    hb "正好拿王靳鱼做一道酸菜鱼。"
    "他已经掏出钱包，准备付钱。"
    "这时，一位青年挡在了他的面前。"
    xq "等等——"
    xq "能把这条鱼让给我吗？"
    xq "我，我爱上她了。"
    xq "我要让她成为我的一生挚爱。"
    o27 "？"
    hb "？"
    "青年十分腼腆地抿抿嘴唇，继续说到。"
    xq "不知为什么，冥冥之中，我竟觉得她跟我有一丝非常微妙的联系。"
    xq "我不知道怎么想的，就觉得她会是我命运中的另一半。在你看来我应该是个很幼稚很蠢的人吧。"
    xq "但是我相信我心中的感情！"
    xq "爱情就是这样的不讲道理，我看到她的第一眼，我就知道了。"
    "他的双颊通红，但是眼神却非常坚定。"
    "红白和鱼摊老板似乎都被这位青年的告白感动了。沉默了一会，老板开口了。"
    o27 "啊这，两位都想买啊。"
    o27 "凡事都讲先来后到，但是这位的理由确实又感人。可惜我这只有一条鱼呢..."
    o27 "要卖给谁好呢？"
    "老板似乎陷入了犹豫之中。"
    jump label_choose3

label label_end:
    scene sky
    "太阳落山了，小生物的人类调查到此结束。"
    show sage_i at left
    sage "是时候检查自己在本次调查中的收获了。"
    hide sage_i
    "它回到了自己的桥洞，开始回想自己今天的经历。"
    "今天是非常漫长的一天，它回想起了自己在旅途之中所下的决心——"
    if choose_a1 and choose_b1 and choose_c1:
        "... ..."
        "... ..."
        show sage_i at left
        sage "要成为一个能够守护楠桐之悲恋的人。"
        sage "要成为一个能够充满打工之力的人。"
        sage "成为一个能够守护规则的人。"
        hide sage_i
        "它开始翻看自己的背包。"
        "【六翼的好人卡*1】"
        "【冰蓝的好人卡*1】"
        "【红白的好人卡*1】"
        "小生物虽然没有改变途中遇到伙伴的现状，也没有改变故事结局，但是它获得了他人的称赞。"
        "它做到了成为一个好人。"
        "在今后的道路上，想必小生物也会继续做一个热爱楠桐，并且守护规则的楠桐爱好者吧。"
        "想到这里，小生物嘴角露出欣慰笑容，进入了快乐的梦乡。"
        "... ..."
        "第二天，附近的人们听说，桥下多出来了一座桥洞教堂。"
        "听说在哪里，有一位好人修女。"
        "虽然据说修女有爱好楠桐的怪癖，但只要是去过桥洞教堂的人们都会这样称赞她："
        "“是个好人。”"
        "Thank you for playing."
        "Normal Ending: 好人修女"
        "点击返回主界面"
        return

    elif choose_a2 and choose_b2 and choose_c2:
        "... ..."
        "... ..."
        show sage_i at left
        sage "要成为一个能够守护楠桐之执恋的人。"
        sage "要成为一个能够守护打工人的人。"
        sage "要成为一个能够守护超越人类之恋的人"
        hide sage_i
        "在这样的道路上，小生物改变了相遇之人的命运，也获得了悲恋之人的，打工之人和变tai...大爱无疆之人的认可。"
        "它做到了成为一个改变事物的人。"
        "在今后的道路上，想必小生物也会继续做一个守护各种恋情并保护打工人的人吧。"
        "虽然前行的道路是未知的，但是来自友人们的认可会是小生物心中永恒的宝物。"
        "这份宝物会给与她勇气，使她能够继续前进。"
        "... ..."
        "第二天，附近的人们听说，桥下多出来了一座桥洞教堂。"
        "听说在哪里，有一位不可思议的修女。"
        "虽然据说修女有爱好楠桐和欣赏超越人类理解范畴的恋爱的怪癖，但只要是去过桥洞教堂的人们都会这样称赞她："
        "“是个能带来改变，促使人不断前进的好修女。”"
        "Thank you for playing."
        "Good Ending: 变革的修女"
        "点击返回主界面"
        return

    else:
        "... ..."
        "... ..."
        show sage_i at left
        sage "似乎自己还没有足够的觉悟。"
        sage "又或许是还没有搜集到足够多的东西。"
        hide sage_i
        "... ..."
        "小生物闭上眼，进入了梦乡。"
        show sage_i at left
        sage "（呢喃）或许，或许——"
        sage "（呢喃）在下一次的冒险中，会有不同的结局...？"
        hide sage_i
        "Thank you for playing."
        "Bad Ending: 不知前路为何的修女"
        "点击返回主界面"
        return

label label_choose1:

    menu:
        sage "此时我应该...？"

        "劝说六翼放弃晨宝":
            $ choose_a1 = True
            jump label_a1
        "劝说六翼继续追求晨宝":
            $ choose_a2 = True
            jump label_a2

label label_choose2:

    menu:
        sage "此时我应该...？"

        "安慰冰蓝":
            $ choose_b1 = True
            jump label_b1
        "和员工一起挂冰蓝":
            $ choose_b2 = True
            jump label_b2

label label_choose3:

    menu:
        sage "此时我应该劝说老板...？"

        "把王靳鱼卖给红白":
            $ choose_c1 = True
            jump label_c1
        "把王靳鱼卖给袭秋":
            $ choose_c2 = True
            jump label_c2

label label_a1:
    show sage_i at left
    sage "爱情想必是强求不来的东西。"
    sage "或许放弃对于双方来说才是最好的选择。"
    hide sage_i
    ly "你是说，我应该，给他自由吗..."
    ly "可是，可是，我放不下晨宝。"
    ly "我知道的，其实我一直都知道的。晨宝是个花心的孩子。他一直都那么交际花。"
    ly "他每天都在群里发撅撅我，又说要啃狐师傅高师傅头皮，还整天撩铜宝，甚至和秋暝击剑的次数我都数不清了。我知道的，我一直都知道的。"
    ly "他一向是一个，会自己寻找幸福的孩子。"
    ly "可是，我的幸福，却只有他一个人能给。"
    ly "即使！即使是他被别人撅了！"
    ly "...看到他被撅开心的脸我也就已经很幸福了。"
    ly "我无法放弃晨宝。"
    ly "还是谢谢你愿意劝说我。"
    ly "你真是个好人。"
    "【获得道具：六翼的好人卡*1】"
    "小生物大受感动。"
    "离开机场时，它暗自发誓，要成为一个能够守护楠桐之悲恋的人。"
    if label_airport_show and label_company_show and label_market_show:
        jump label_end
    else:
        jump label_choose_label

label label_a2:
    show sage_i at left
    sage "既然不甘心，既然痛苦。"
    sage "那就应当拿出行动，继续努力。"
    hide sage_i
    ly "继续...努力吗？"
    ly "结婚之前都是公平竞争？你说的...好像是有些道理。"
    ly "的确，这不应该是结局。"
    ly "就这样放弃自己心爱的人或许太过轻易了。我的内心在大喊着不应该就这样结束。"
    ly "我不甘心，我不甘心。"
    ly "——而不甘心就应该去争取。"
    ly "的确，晨宝今天抛弃我选择了毕方，那么在将来他也有可能会离开毕方而重新选择其他人。"
    ly "这个其他人或许是鸽子王，或许是红月，或许……也可以是我！"
    ly "谢谢你，我下定决心了。"
    ly "我一定要撅到晨宝！"
    "【获得道具：楠桐六翼的认可*1】"
    "小生物大受感动。"
    "离开机场时，它暗自发誓，要成为一个能够守护楠桐之执恋的人。"
    if label_airport_show and label_company_show and label_market_show:
        jump label_end
    else:
        jump label_choose_label

label label_b1:
    show sage_i at left
    sage "即便是邪恶的资本家，也拥有追求爱情的权力。"
    sage "即使是罪恶的资本家，在感到悲伤时也应被温柔以待。"
    hide sage_i
    bl "谢谢你，你真是个温柔的好人。"
    "【获得道具：冰蓝的好人卡*1】"
    bl "但总是沉溺于悲伤的情感可不行，得抬头往前走。我现在必须得寻找我的下一个打工人了。"
    bl "说起来，你现在有工作吗？"
    bl "要是没有工作，有兴趣来我们这里打工吗？"
    bl "只要做7休0，每天只用上班18小时就可以了。"
    bl "是非常有竞争力的工作时间呢，还有经常的加班让你的能力得到更好的锻炼。"
    bl "如何？很宽厚的条件吧？"
    bl "今天签合同还送不锈钢大铁盆和牙刷牙杯，以后在公司打地铺加班的时候就更方便了。"
    "收到邀请的小生物大受感动。"
    "离开公司时，它暗自发誓，要成为一个能够充满打工之力的人。"
    if label_airport_show and label_company_show and label_market_show:
        jump label_end
    else:
        jump label_choose_label

label label_b2:
    show sage_i at left
    sage "正义理应得到伸张。"
    sage "被压迫的打工人们渴望自由，渴望处刑为他们带来痛苦的源头。"
    hide sage_i
    "员工们纷纷向小生物叙述自己曾经遭遇过的被压迫故事，让小生物听得眼泪汪汪。"
    "小生物决心加入他们。"
    "【获得道具：打工群友的认可*1】"
    bl "你们，你们这是要做什么？！"
    bl "我给了你们工作，你们难道不应该感恩吗？"
    bl "觉得工资不够花，你们不会一天干25小时，一周干8天吗？"
    bl "快停下，没了我，你们连工作都没有——"
    "这次团结的经历让小生物大受感动。"
    "离开机场时，它暗自发誓，要成为一个能够守护打工人的人。"
    if label_airport_show and label_company_show and label_market_show:
        jump label_end
    else:
        jump label_choose_label

label label_c1:
    show sage_i at left
    sage "先来后到，遵守规则。"
    sage "把这条鱼让给先来的人吧，况且他家人生日这样的时机，要是有了这样的好食材，可谓锦上添花。"
    hide sage_i
    "老板听了小生物的劝说，也认可地摸摸下巴。"
    "哐哐几刀下去，老板就熟练地宰杀了王靳鱼。他把鱼肉和内脏分开塞进了不同的塑料袋，然后递给红白。"
    "红白则非常高兴地向小生物点点头。"
    hb "哎呀，你真是个好人。"
    "【获得道具：红白的好人卡*1】"
    show sage_i at left
    sage "想必之后，他们会有一场非常愉快的家庭聚会吧。"
    hide sage_i
    "小生物想着这一点，露出了笑容。"
    "离开菜市场时，小生物暗暗发誓。"
    "它一定要成为一个守护规则的人。"
    if label_airport_show and label_company_show and label_market_show:
        jump label_end
    else:
        jump label_choose_label

label label_c2:
    show sage_i at left
    sage "即使是人和鱼的感情也是伟大的。"
    sage "这份爱情虽然不为世人所容，但是它的真挚却无可否认。"
    hide sage_i
    xq "！"
    xq "你，你能理解我吗？"
    xq "我，我其实已经做好了被骂恶心，被骂变态，被骂滚出去的心理准备了。"
    xq "但是...谢谢你——谢谢——"
    "青年握着小生物的手，一时泪如雨下。"
    "【获得道具：变tai..大爱无疆者的认可*1】"
    "看到这样的场面，一开始有些犹豫的老板和红白也有些感动。"
    hb "...算了，让给他吧。"
    hb "比起被我吃掉，或许这才是更好的结局。"
    o27 "是啊，让他们获得幸福吧。"
    "青年捧着王靳鱼，开心地离开了。"
    "小生物大受感动。"
    "离开菜市场时，它暗自发誓，要成为一个能够守护超越人类之恋的人。"
    if label_airport_show and label_company_show and label_market_show:
        jump label_end
    else:
        jump label_choose_label

label label_choose_label:
    "......"
    "......"

    menu:
        sage "去哪里调查人类？"

        "机场" if not label_airport_show:
            jump label_airport

        "公司" if not label_company_show:
            jump label_company

        "菜市场" if not label_market_show:
            jump label_market