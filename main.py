def worm():
    basic.show_leds("""
        . # . . .
        . # # . .
        . # # . .
        . # # . .
        . . # . .
        """)
    basic.pause(10)
    basic.show_leds("""
        . . # . .
        . # # . .
        . # # . .
        . # # . .
        . # . . .
        """)
    basic.show_leds("""
        . # . . .
        . # # . .
        . # # . .
        . # # . .
        . . # . .
        """)
    basic.pause(10)
    basic.show_leds("""
        . . # . .
        . # # . .
        . # # . .
        . # # . .
        . # . . .
        """)
    basic.show_leds("""
        . . . . .
        . # # . .
        . # # . .
        . # # . .
        . . . . .
        """)

def on_button_pressed_a():
    squalk()
input.on_button_pressed(Button.A, on_button_pressed_a)

def squalk():
    basic.show_leds("""
        . . . . .
        . # # . .
        . # # . .
        . # # . .
        . . . . .
        """)
    basic.pause(100)
    basic.show_leds("""
        . . . . .
        # . # . .
        # . # . .
        # . # . .
        . . . . .
        """)
    basic.show_leds("""
        . . . . .
        . # # . .
        . # # . .
        . # # . .
        . . . . .
        """)
    music.play(music.string_playable("C#5 ", 200),
        music.PlaybackMode.UNTIL_DONE)

def on_button_pressed_b():
    worm()
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    . . . . .
    . # # . .
    . # # . .
    . # # . .
    . . . . .
    """)