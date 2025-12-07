#code by 群阿巴阿巴 text and music by 度海


init python:
    import store
    mas_acs_ladmp = store.MASAccessory(
        "ladmp",
        "ladmp",
        MASPoseMap(
            default="0",
        ),
        stay_on_start=True,
        acs_type="table_acs",
        rec_layer=MASMonika.PST_ACS
    )


style monika_lad_ctext:
    font "mod_assets/font/shangshouyurenti.ttf"
    color "#fff"
    size 60
    text_align 0.5
    outlines []

style monika_lad_etext:
    font "gui/font/m1.ttf"
    color "#fff"
    size 50
    text_align 0.5
    outlines []

transform lad_chinese:
    xpos 0.5 xanchor 0.5 ypos 0.6 yanchor 0.6

transform lad_english:
    xpos 0.5 xanchor 0.5 ypos 0.7 yanchor 0.7

transform lad_back:
    xpos 0.5 xanchor 0.5 ypos 0.66 yanchor 0.66


image ladtback = "Submods/Literature_and_Daily_Life/L&DL_Assets/images/menu/lad_bar.png"

default  lad_ctext1 = [["你正和你女朋友聊电话 她不开心",
                        "因为你不合时宜的玩笑耍着脾气",
                        "她不像我  明白你的幽默",
                        "孤身一人坐在房间 又是个普通的周二晚上",
                        "我聆听着 她嗤之以鼻的乡村音乐",
                        "她无法像我一样 对你知根知底",
                        "她衣着短裙 我穿着T恤",
                        "她是场上的拉拉队长",
                        "我是看台上的邻家女孩",
                        "做梦都希望你会有一天起床发现",
                        "你追寻的东西一直在这",
                        "倘若你能够明白 我才能与你惺惺相惜",
                        "日复一日 痴痴等侯 你为何选择视而不见呢",
                        "你是属于我的",
                        "我才是你的归宿",
                        "你穿着破洞牛仔裤 和我漫步街头",
                        "我情不自禁 在脑海里描绘憧憬的景象",
                        "在公园长椅上独自傻笑，每每假想我们在一起",
                        "嘿 难道这不是轻而易举的吗？",
                        "你的会心一笑 便是点亮我心里城镇的光亮",
                        "和她分手后 我再也看不到你微笑的面庞",
                        "嘴上故作安好 可我明白 你本值得更好的选择",
                        "那么你会对这样的一个女孩做些什么？",
                        "她穿着个性高跟",
                        "我穿着运动跑鞋",
                        "她是球场的拉拉队长 我是看台上的邻家女孩",
                        "做梦都希望你会有一天起床发现",
                        "你追寻的东西一直在这",
                        "如果你能明白 我才是能与你惺惺相惜的人",
                        "日复一日 痴痴等侯 为何你却视而不见呢",
                        "你是属于我的",
                        "站在后门 呆望着你渐行渐远的背影",
                        "一直以来 你为何还未发现，宝贝",
                        "你是属于我的",
                        "我才是你的归宿",
                        "我想起你在半夜突然驾车到我家",
                        "当你要即将泣不成声",
                        "是我一扫你心中阴霾",
                        "我知道你最喜欢的音乐",
                        "你告诉我 你对未来的憧憬和期冀",
                        "我想 我知道你何去何从 你的归宿",
                        "我觉得你是属于我的",
                        "难道你一直都不明白 只有我才能与你惺惺相惜",
                        "日复一日 痴痴等侯 为何你却选择视而不见呢",
                        "你的心本属于我",
                        "站在后门 呆望着你渐行渐远的背影",
                        "久久等候 为何你不曾察觉我的真心？",
                        "你更该属于我",
                        "你更该属于我",
                        "你我更加般配",
                        "亲爱的 你难道就没想过",
                        "其实你我更合适",
                        "我才是你的归宿"],

                        ["我对圣诞要的不多",
                        "我只求一样",
                        "我不在乎礼物",
                        "那些埋在圣诞树下的",
                        "我不需要在火炉旁",
                        "挂上袜子",
                        "圣诞老人带来的礼物",
                        "无法让我开心",
                        "我只想要你属于我一个人",
                        "你不会知道我有多渴望",
                        "让我的愿望实现吧",
                        "我想要的圣诞礼物只有你",
                        "我只要你",
                        "这个圣诞节我不会要求很多",
                        "我甚至都不会为浪漫的雪许愿",
                        "我只想默默等待",
                        "在那槲寄生之下",
                        "我不会列个清单然后",
                        "寄到北极圣诞老人那",
                        "我甚至不会一直等着",
                        "兴致勃勃去听神奇驯鹿的声音",
                        "因为今晚我只想你在这里",
                        "紧紧地抱着我",
                        "除此我还能拥有什么愿望呢~",
                        "宝贝 我想要的圣诞礼物只有你~",
                        "我只要你~",
                        "宝贝 我想要的圣诞礼物只有你~",
                        "宝贝 我想要的圣诞礼物只有你~"
                        ]]



default  lad_etext1 = [["You're on the phone with your girlfriend.She's upset",
                        "She's going off about something that you said",
                        "'Cause she doesn't get your humor like I do",
                        "I'm in the room,It's a typical Tuesday night",
                        "I'm listening to the kind of music she doesn't like",
                        "And she'll never know your story like I do",
                        "But she wears short skirts I wear T-shirt",
                        "She's cheer captain",
                        "And I'm on the bleachers",
                        "Dreaming about the day when you wake up",
                        "And find that what you're looking for has been here the whole time",
                        "If you could see that I'm the one who understands you",
                        "Been here all along so why can't you see",
                        "You belong with me",
                        "You belong with me",
                        "Walking in the streets with you and your worn-out jeans",
                        "I can't help thinking this is how it ought to be",
                        "Laughing on a park bench thinking to myself",
                        "Hey isn't this easy",
                        "And you've got a smile that could light up this whole town",
                        "I haven't seen it in a while since she brought you down",
                        "You say you're fine,I know you better then that",
                        "Hey what cha doing with a girl like that",
                        "She wears high heels",
                        "I wear sneakers",
                        "She's cheer captain and I'm on the bleachers",
                        "Dreaming about the day when you wake up",
                        "And find that what you're looking for has been here the whole time",
                        "If you could see that I'm the one who understands you",
                        "Been here all along so why can't you see",
                        "You belong with me",
                        "Standing by and waiting at your back door",
                        "All this time how could you not know Baby....",
                        "you belong with me",
                        "you belong with me",
                        "Oh I remember you driving to my house in the middle of the night",#18
                        "I'm the one who makes you laugh",
                        "When you know you're about to cry",
                        "And I know your favorite songs",
                        "And you tell me about your dreams",
                        "Think I know where you belong",
                        "Think I know it's with me",
                        "Can't you see that I'm the one who understands you",
                        "Been here all along so why can't you see",
                        "You belong with me",
                        "Standing by and waiting at your back door",
                        "All this time How could you not know Baby",
                        "you belong with me",
                        "You belong with me",
                        "You belong with me",
                        "Have you ever thought just maybe",
                        "You belong with me",
                        "You belong with me"],#1

                        ["I don't want a lot for Chrismas",
                        "There is just one thing I need",
                        "I don't care about the presents",
                        "Underneath the Chrismas tree",
                        "I don't need to hang my stocking",
                        "There upon the fireplace",
                        "Santa Claus won't make me happy",
                        "With a toy on Christmas Day",
                        "I just want you for my own",
                        "More than you could ever know",
                        "Make my wish come true",
                        "All I want for Christmas is you",
                        "You~ baby",
                        "Oh I won't ask for much this Christmas",
                        "I won't even wish for snow",
                        "I'm just gonna keep on waiting",
                        "Underneath the mistletoe",
                        "I won't make a list and send it",
                        "To the North Pole for Saint Nick",
                        "I won't even stay awake to",
                        "Hear those magic reindeer click",
                        "'Cause I just want you here tonight~",
                        "Holding on to me so tight~",
                        "What more can I do~",
                        "baby all I want for Christmas is you~",
                        "You~ baby",
                        "All I Want For Christmas Is You",
                        "All I Want For Christmas Is You"
                        ]]

default  lad_num = 0
default  lad_music = 0
default  lad_anima = False
default  persistent.LDL_Christmas = 0


image lad_etext:
    Text(lad_etext1[lad_music][lad_num], style="monika_lad_etext")

image lad_ctext:
    Text(lad_ctext1[lad_music][lad_num], style="monika_lad_ctext")
     

label lad_show_text():
    hide lad_etext 
    hide lad_ctext 
    show lad_ctext zorder 50 at lad_chinese
    with dissolve
    show lad_etext zorder 50 at lad_english
    with dissolve
    $ lad_num += 1
    return


    

init 5 python:
    addEvent(Event(persistent.event_database,
        eventlabel="Monika_YBWM_again",
        category=["音乐"],
        prompt="你可以为我再唱一次<You belong with me>吗",
        random=False))


init 5 python:
        addEvent(Event(persistent.event_database,
            eventlabel="lad_music1",
            category=["音乐"],
            prompt="YOU BELONG WITH ME",
            conditional="_mas_getAffection() >= 600",
            action=EV_ACT_PUSH
            ))




label lad_music1(skip_leadin=False):
    m 1eua "嘿,[player]."
    m 3fub "每次你还没来见我之前,我都有在练习发声哦."
    m 5euc "你或许会想,发声不应该是很简单的事吗?"
    m 2eud "比如我在唱起《Your reality》的时候."
    m 3hua "但实际是我需要练习很久才能发出你所能听到的,正常女孩的声音."
    m 6eub "嗯......我现在还不能做到随口就可以进行流利的对话,因此,我总是需要付出大量的时间来完成对一段话、{w=0.9}一首歌的练习."
    m 1fubla "只是为了你,[player],"
    extend 1hubfb "你值得我这样......"
    m 6eub "如你所见,我在这段时间已经练习好一首曲子了,正好我现在唱给你听听."
    m 3fua "但在此之前,我希望你不要在中途关闭和移动窗口,因为这个地方也不是很稳定了."
    m 5eublb "我也不想让我的努力白费......"
    m 3hua "好了好了,我现在就去进行一下准备工作."
label Monika_YBWM_again(skip_leadin=False):
    $ lad_music = 0
    $ persistent._mas_disable_animations = True
    call mas_transition_to_emptydesk
    pause (2)
    $ store.mas_sprites.zoom_out()
    pause (2)
    $ renpy.store.monika_chr.wear_acs(mas_acs_ladmp)
    call mas_transition_from_emptydesk()
    $ mas_drawSpaceroomMasks(dissolve_masks=False)
    m "让我们开始吧"####################
    $ original_music = renpy.music.get_playing(channel='music')
    $HKBHideButtons()
    window hide
    show screen mas_py_console_teaching
    $ store.mas_ptod.rst_cn()
    show monika at t22
    call mas_wx_cmd ("#play the song <<You Belong With Me>>")
    call mas_wx_cmd ("#Play the instrumental version of a song.")
    call mas_wx_cmd ("#play successed")
    $ mas_play_song("Submods/Literature_and_Daily_Life/L&DL_Assets/music/You_Belong_With_Me.ogg",loop=False)
    pause(2)
    hide screen mas_py_console_teaching
    show monika 1eua at t11
    show ladtback zorder 49 at lad_back
    with dissolve
    pause (5.26)
    show monika 2rsd
    call lad_show_text
    pause (3.4)
    show monika 3tub
    call lad_show_text
    pause (3.45)
    show monika 1fub
    call lad_show_text
    pause (4.9)
    hide lad_etext 
    hide lad_ctext 
    show monika 6hua
    pause (1.433)
    show monika 1hub
    call lad_show_text
    pause (3.5)
    show monika 3rub
    call lad_show_text
    pause (3.2)
    show monika 4rub
    call lad_show_text
    pause (3.85)
    hide lad_etext with dissolve
    hide lad_ctext with dissolve
    show monika 1hubla
    pause (1.2)
    show monika 3fud
    call lad_show_text
    pause (3.266)
    show monika 6esd
    call lad_show_text
    pause (1.083)
    show monika 1fublb
    call lad_show_text
    pause (1.566)
    show monika 1hublb
    call lad_show_text
    pause (2.15)
    show monika 1hublb
    call lad_show_text
    pause (3.016)
    show monika 2wublb
    call lad_show_text
    pause (4.316)
    show monika 6kublb
    call lad_show_text
    pause (4.5)
    show monika 3fublb
    call lad_show_text
    pause (3.15)
    show monika 1hublb
    call lad_show_text
    pause (3.133)
    hide lad_etext with dissolve
    hide lad_ctext with dissolve
    show monika 6hubla
    pause (1.266)
    show monika 3fublb
    call lad_show_text
    pause (3.383)
    show monika 1hubfb
    call lad_show_text
    pause (3.283)
    show monika 1fublb
    call lad_show_text
    pause (3.066)
    show monika 1wublb
    call lad_show_text
    pause (2.866)
    show monika 1hublb
    call lad_show_text
    pause (2.9)
    show monika 2esd
    call lad_show_text
    pause (3.433)
    show monika 1tub
    call lad_show_text
    pause (2.8)
    show monika 1fubfb
    call lad_show_text
    pause (2.966)
    show monika 3rsd
    call lad_show_text
    pause (1.483)
    show monika 6hub
    call lad_show_text
    pause (1.483)
    show monika 3fublb
    call lad_show_text
    pause (3.483)
    show monika 1fublb
    call lad_show_text
    pause (1.633)
    show monika 3hublb
    call lad_show_text
    pause (3.866)
    show monika 4fublb
    call lad_show_text
    pause (3.533)
    show monika 2dkb
    call lad_show_text
    pause (5.85)
    show monika 3dublb
    call lad_show_text
    pause (4.15)
    show monika 1dublb
    call lad_show_text
    pause (3.55)
    show monika 2eub
    call lad_show_text
    pause (5.2)
    show monika 1fublb
    call lad_show_text
    pause (3.583)
    show monika 3hublb
    call lad_show_text
    pause (2.05)
    show monika 1hublu
    hide lad_ctext with dissolve
    hide lad_etext with dissolve
    pause (9.116)
    show monika 3hublb
    call lad_show_text
    pause (4.466)
    show monika 1fubld
    call lad_show_text
    pause (1.25)
    show monika 1hubfb
    call lad_show_text
    pause (1.466)
    show monika 6eublb
    call lad_show_text
    pause (0.966)
    show monika 1hubfb
    call lad_show_text
    pause (1.516)
    show monika 2wublb
    call lad_show_text
    pause (1.55)
    show monika 2hublb
    call lad_show_text
    pause (2.766)
    show monika 3rubld
    call lad_show_text
    pause (3.816)
    show monika 6dfbld
    call lad_show_text
    pause (5.166)
    show monika 3rublb
    call lad_show_text
    pause (4.516)
    show monika 1eublb
    call lad_show_text
    pause (3.233)
    show monika 1eublb
    call lad_show_text#
    pause (5.483)
    show monika 3hublb
    call lad_show_text
    pause (3.233)
    show monika 1fublb
    call lad_show_text
    pause (2.266)
    hide lad_ctext with dissolve
    hide lad_etext with dissolve
    show monika 1hub
    pause (0.5)
    call lad_show_text
    pause (2.0)
    show monika 3dublb
    call lad_show_text
    pause (4.516)
    show monika 1wublb
    call lad_show_text
    pause (3.316)
    show monika 6hublb
    call lad_show_text
    pause (2.3)
    hide lad_etext with dissolve
    hide lad_ctext with dissolve
    show monika 1hubla
    pause (8.916)
    $ mas_unlockEVL("Monika_Piano_YBWM", "EVE")
    hide lad_etext
    hide lad_ctext
    hide ladtback
    $ lad_num = 0
    stop music
    call mas_transition_to_emptydesk
    $ monika_chr.remove_acs(mas_acs_ladmp)
    pause (4)
    call mas_transition_from_emptydesk()
    $ mas_unlockEVL("Monika_YBWM_again", "EVE")
    $HKBShowButtons()
    m 5fubla "喜欢吗,[player]?"
    $ persistent._mas_disable_animations = False
    m 3eubfb "为了你,哪怕付出多少时间我都愿意."
    $ mas_drawSpaceroomMasks(dissolve_masks=False)
    m 1fubla "我现在依旧在练习,只为了在某天能再次给你一个惊喜."
    m 5fubfb "爱你,[player]."
    return "love"



#code by 群阿巴阿巴 text and music by 度海



init 5 python:
    addEvent(Event(persistent.event_database,
        eventlabel="Monika_AIWFCIY_again",
        category=["音乐"],
        prompt="你可以为我再唱一次All_I_Want_for_Christmas_Is_You吗",
        random=False))

init 5 python:
        addEvent(Event(persistent.event_database,
            eventlabel="lad_music2",
            category=["音乐"],
            prompt="All I Want for Christmas Is You",
            conditional="_mas_getAffection() >= 600",
            start_date=mas_d25,
            end_date=mas_d25p,
            action=EV_ACT_PUSH,
            years=[]
            ))

label lad_music2(skip_leadin=False):
    m 6eud "[player],我想和你说件事."
    m 3rusdld "在今天说或许是个坏消息."
    m 3euc "那就是......{w=0.9}"
    m 1hubfb "我又为你准备了一个小礼物."
    m 1fubla "哈哈,你是不是觉得是什么大事."
    m 5hublb "放心,我只是想淘气一下."
    m 1hua "不过,你肯定好奇这个小礼物是什么吧,我现在就拿给你."
    m 6eub "在此之前我希望你不要在中途关闭和移动窗口哦."
    m 3hua "就这样,我现在就去准备一下."
label Monika_AIWFCIY_again(skip_leadin=False):
    $ lad_music = 1
    $ persistent._mas_disable_animations = True
    call mas_transition_to_emptydesk
    pause (2)
    $ store.mas_sprites.zoom_out()
    pause (2)
    $ renpy.store.monika_chr.wear_acs(mas_acs_ladmp)
    call mas_transition_from_emptydesk()
    $ mas_drawSpaceroomMasks(dissolve_masks=False)
    m "让我们开始吧"############################
    $ original_music = renpy.music.get_playing(channel='music')
    $HKBHideButtons()
    window hide
    show screen mas_py_console_teaching
    $ store.mas_ptod.rst_cn()
    show monika at t22
    call mas_wx_cmd ("#play the song <<All I Want for Christmas Is You>>")
    call mas_wx_cmd ("#Play the instrumental version of a song.")
    call mas_wx_cmd ("#play successed")
    $ mas_play_song("Submods/Literature_and_Daily_Life/L&DL_Assets/music/AIWFCIY.ogg",loop=False)
    pause (1.85)
    hide screen mas_py_console_teaching
    show monika 1eubla at t11
    show ladtback zorder 49 at lad_back
    pause (12.383)
    show monika 5hubla
    pause (8.066)
    show monika 6rubla
    pause (7.383)
    show monika 1hubla
    pause (7.866)
    show monika 1eubla
    pause (7.466)
    show monika 6hubla
    pause (12.366)
    show monika 1fubla
    pause (6.9)
    show monika 1rublb
    call lad_show_text
    pause (2.533)
    show monika 1fublb
    call lad_show_text
    pause (2.466)
    show monika 6hua
    hide lad_ctext with dissolve
    hide lad_etext with dissolve
    pause (0.133)
    show monika 3rublb
    call lad_show_text
    pause (2.033)
    show monika 1hub
    call lad_show_text
    pause (2.766)
    show monika 1fub
    call lad_show_text
    pause (2.583)
    show monika 3rublb
    call lad_show_text
    pause (3.316)
    show monika 1hublb
    call lad_show_text
    pause (2.216)
    show monika 1dublb
    call lad_show_text
    pause (2.933)
    show monika 6eubfb
    call lad_show_text
    pause (2.566)
    show monika 3hubfb
    call lad_show_text
    pause (2.433)
    show monika 1wublb
    call lad_show_text
    pause (2.733)
    show monika 1fubfb
    call lad_show_text
    pause (4.95)
    show monika 6hubla
    hide lad_ctext with dissolve
    hide lad_etext with dissolve
    pause (0.3)
    show monika 1eubfb
    call lad_show_text
    pause (2.166)
    show monika 1hubfb
    call lad_show_text
    pause (2.683)
    show monika 6hublb
    call lad_show_text
    pause (3.216)
    show monika 1dubfb
    call lad_show_text
    pause (2.066)
    show monika 6fud
    call lad_show_text
    pause (2.533)
    show monika 1rub
    call lad_show_text#
    pause (2.716)
    show monika 3eud
    call lad_show_text#
    pause (3.216)
    show monika 1hub
    call lad_show_text#
    pause (2.266)
    show monika 3rub
    call lad_show_text#
    pause (2.383)
    show monika 3fublb
    call lad_show_text
    pause (2.4)
    show monika 6hublb
    call lad_show_text
    pause (2.7)
    show monika 1fublb
    call lad_show_text
    pause (2.4)
    show monika 2eublb
    call lad_show_text
    pause (5.233)
    show monika 1tubla
    hide lad_ctext with dissolve
    hide lad_etext with dissolve
    pause (0.433)
    show monika 1fublb
    call lad_show_text
    pause (2.616)
    show monika 1hubfb
    call lad_show_text
    pause (5.583)
    show monika 6fubfb
    call lad_show_text
    pause (5.966)
    show monika 1hua
    hide lad_ctext with dissolve
    hide lad_etext with dissolve
    pause (2.716)
    $ lad_num = 0
    stop music
    hide ladtback
    ###放麦克风前的话
    call mas_transition_to_emptydesk
    $ monika_chr.remove_acs(mas_acs_ladmp)
    pause (4)
    call mas_transition_from_emptydesk()
    $ mas_unlockEVL("Monika_AIWFCIY_again", "EVE")
    ###放麦克风后的话
    $ persistent.LDL_Christmas += 1
    $HKBShowButtons()
    m 5hubla "圣诞节快乐,[player]."
    $ persistent._mas_disable_animations = False
    m 3eubfb "希望你在这个节日和家人朋友很开心的度过."
    $ mas_drawSpaceroomMasks(dissolve_masks=False)
    m 1fubla "或者,这个特殊日子多陪陪我,好吗?"
    m 5fubfb "爱你,[player]."
    return "love"
    
    

