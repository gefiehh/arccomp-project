# Определение персонажей игры.
define gg = Character("Варвара", color="#c8ffc8")
define mother = Character('Матушка', color="#c8ffc8")

# Выбор оружия
define sword = False
define baton = False
define stick = False

# Выбор скакуна 
define horse = False
define donkey = False
define hobbyhorse = False
define onfoot = False

# Доастижения
define leshi_alive = False
define leshi_dead = False
define dragon_good = False
define dragon_bad = False
define dragon_dead_by_weapon = False
define dragon_dead_by_fire = False

# Игра начинается здесь:
label start:

        play music "les.mp3" fadein 1.0
        
        scene bg home with fade

        "В Залесье светало, первые лучи солнца пробивались в окно избы, а петухи завели свой утренний перекрик."
        "Из сеней послышался голос матушки"

        show mother happy with dissolve

        mother "Варвара, просыпайся!"
        mother "Гонец приходил, принес тебе княжеское распоряжение"

        "Матушка протянула берестяную грамоту"

        show letter with dissolve
        window hide dissolve
        pause

        "От князя Святослава храброй Варваре"
        "Пришло на наши земли чудище страшное – змей окаянный. Мы молим тебя, храбрая Варвара, да возьмешь на себя сию благородную задачу и победишь его. Иди по пути, где встретишь камень, поверни налево. Пусть меч твой будет острым!"

        hide letter with dissolve

        gg "Трудный бой ждет меня впереди"
        gg "Возьму все необходимое и немедленно выдвинусь в путь"

        show mother happy at left with moveinleft #потом мотхер сад нарисую

        mother "Какое оружие возьмешь с собой сегодня?"
        
        window hide dissolve
        show weapons at right with dissolve
        pause

        menu:
                "Острый меч":
                        gg "Меч всегда служил мне правдой и ни разу не подвел"
                        gg "У змея не будет шанса"
                        $ sword = True
                
                "Тяжелая дубинка":
                        gg "Соперник силен, думаю дубинка будет здесь уместна"
                        gg "Ударив чудище по голове такой дубинкой, я смогу одолеть его"
                        $ baton = True
                
                "Палка":
                        gg "Хм, почему бы и нет" 
                        gg "Я справлюсь с ним даже голыми руками, а раз в год и палка стреляет"
                        $ stick = True

        scene bg stable with fade
        show horses with dissolve

        "Выбрав оружие, Варвара отправилась в конюшню"
        "Девушка вошла в большое светлое помещение и огляделась"

        gg "Теперь мне нужно выбрать скакуна"
        gg "Путь предстоит неблизкий"
        gg "Возьму.."

        menu:
                "Сильного жеребца":
                        gg "Мой верный конь Ворон вмиг донесет меня до места назначения, преодолев любые препятствия"
                        $ horse = True

                "Осла":
                        gg "Этот осел вынослив"
                        gg "Он, конечно, не так быстр, но зато протянет без еды долгое время"
                        $ donkey = True

                "Палку с головой лошади":
                        gg "Эта загадочная палка с головой лошади давно стоит у нас в конюшне"
                        gg "Пришел ее час"
                        $ hobbyhorse = True

                "Ничего не буду брать":
                        gg "Нет ничего надежнее моих собственных ног"
                        gg "Пусть не так быстро, но они приведут меня к цели"
                        $ onfoot = True

        scene bg home with fade
        show mother happy with dissolve

        "Вернувшись из конюшни, Варвара подошла к матушке, получить благословление на трудный и далекий путь"
        "Женщина обняла дочь"

        mother "Да хранит тебя Господь, Варвара, на каждом шагу"
        mother "Пусть меч твой будет остер, а разум ясен"
        mother "Не бойся трудностей, ведь смелое сердце и чистая совесть сильнее любого змея"

        hide mother happy with dissolve

        "Простившись, девушка отправилась в путь"

        jump rock

        return