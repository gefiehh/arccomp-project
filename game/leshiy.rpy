define leshiy = Character("Леший", color="#c8ffc8")

label les:
    scene bg forest
    "Впереди показалась фигурка маленького старичка."
    "Нос его был больше похож на шишку, одежда состояла из коры и листьев, а длинная борода касалась земли."

    show leshiy at center with dissolve
    leshiy "Стой, странница. Я — Леший, хозяин этого леса. Чего тебе понадобилось на моей территории?"

    gg "Я — богатырша Варвара, по поручению князя отправилась в дальний путь. Змей чудовищный посягнул на наши земли. Я одолею его и избавлю людей от бед."

    leshiy "Хорошо, но так просто ты не пройдешь. Коль твой путь пролегает по моему лесу, реши мои задачки, тогда отпущу тебя."

    label riddles:
        scene bg forest_path with fade
        show leshiy at center with dissolve

        leshiy "Первая задачка. Чему равна производная от натурального логарифма?"

        menu:
            "1) lnx":
                jump wrong
            "2) 1/x":
                pass
            "3) x^2":
                jump wrong

        leshiy "Вторая задачка. Какую траву можно узнать даже с закрытыми глазами?"

        menu:
            "1) Мокрица":
                jump wrong
            "2) Подорожник":
                jump wrong
            "3) Крапива":
                pass

        leshiy "Третья задачка. Какая цифра уменьшится на треть, если её перевернуть?"

        menu:
            "1) Девять":
                pass
            "2) Тридцать три":
                jump wrong
            "3) Четыре":
                jump wrong

                label wrong:

                    leshiy "Леший нахмурился, сдвинув свои густые брови к носу. Он явно был зол."
                    "Старик медленно подошел к Варваре, пока не сократил расстояние до вытянутой руки."
                    "Он схватил девушку и утащил в лесную чащу..."
                    scene die_in_forest with fade
                    pause
                    jump riddles


    scene bg night_forest with fade
    show leshiy at center with dissolve

    leshiy "Вижу, действительно достойна ты сразиться со змеем и спасти род человеческий. Не посрамишь достоинства людского. Ты готова, можешь идти по моему лесу."

    jump dragon

    return    