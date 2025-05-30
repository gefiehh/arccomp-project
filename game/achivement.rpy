label achive:

    "Достижения, полученные за прохождение: "

    if leshi_alive and dragon_good:
        show achiv1 with dissolve

    if leshi_alive and dragon_bad:
        show achiv2 with dissolve

    if leshi_alive and (dragon_dead_by_weapon or dragon_dead_by_fire):
        show achiv3 with dissolve

    if leshi_dead and dragon_good:
        show achiv4 with dissolve

    if leshi_dead and dragon_bad:
        show achiv5 with dissolve

    if leshi_dead and dragon_dead_by_weapon:
        show achiv6 with dissolve

    if leshi_dead and dragon_dead_by_fire:
        show achiv7 with dissolve

    pause

    return
