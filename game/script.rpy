# Определение персонажей игры.
define gg = Character("Варвара", color="#c8ffc8")
define mother = Character('Матушка', color="#c8ffc8")


# Выбор оружия
define sword = False
define baton = False
define stick = False

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    play music "les.mp3" fadein 1.0
    scene bg exmp1 with fade

    "В Залесье светало, первые лучи солнца пробивались в окно избы, а петухи завели свой утренний перекрик."

    scene bg exmp2 with fade

    "Из сеней послышался голос матушки"

    show mother happy with dissolve

    mother "Варвара, просыпайся!"
    mother "Гонец приходил, принес тебе княжеское распоряжение"

    "Матушка протянула берестяную грамоту"

    show exmp3 with dissolve
    window hide dissolve
    pause

    hide exmp3 with dissolve

    gg "Трудный бой ждет меня впереди"
    gg "Возьму все необходимое и немедленно выдвинусь в путь"

    show mother happy at left with moveinleft #потом мотхер сад нарисую

    mother "Какое оружие возьмешь с собой сегодня?"
    
    window hide dissolve
    show exmp4 at right with dissolve
    pause

    menu:
        "Острый меч":
                "Меч всегда служил мне правдой и ни разу не подвел"
                "У змея не будет шанса"
                $ sword = True
        
        "Тяжелая дубинка":
                "Соперник силен, думаю дубинка будет здесь уместна"
                "Ударив чудище по голове такой дубинкой, я смогу одолеть его"
                $ baton = True
        
        "Палка":
                "Хм, почему бы и нет" 
                "Я справлюсь с ним даже голыми руками, а раз в год и палка стреляет"
                $ stick = True

    "Что то там про то, что она вышла к конюшне" #йййооооооооооуууууууу
    #тут она выбирает лошадь и прошается с матушкой

    gg "Приготовления закончены"
    gg "Можно выдвигаться"

    jump rock

    

    label rock:

    jump les

       





    
    