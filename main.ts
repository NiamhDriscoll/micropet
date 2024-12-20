function worm() {
    basic.showLeds(`
        . # . . .
        . # # . .
        . # # . .
        . # # . .
        . . # . .
        `)
    basic.pause(10)
    basic.showLeds(`
        . . # . .
        . # # . .
        . # # . .
        . # # . .
        . # . . .
        `)
    basic.showLeds(`
        . # . . .
        . # # . .
        . # # . .
        . # # . .
        . . # . .
        `)
    basic.pause(10)
    basic.showLeds(`
        . . # . .
        . # # . .
        . # # . .
        . # # . .
        . # . . .
        `)
    basic.showLeds(`
        . . . . .
        . # # . .
        . # # . .
        . # # . .
        . . . . .
        `)
}

input.onButtonPressed(Button.A, function on_button_pressed_a() {
    squalk()
})
function squalk() {
    basic.showLeds(`
        . . . . .
        . # # . .
        . # # . .
        . # # . .
        . . . . .
        `)
    basic.pause(100)
    basic.showLeds(`
        . . . . .
        # . # . .
        # . # . .
        # . # . .
        . . . . .
        `)
    basic.showLeds(`
        . . . . .
        . # # . .
        . # # . .
        . # # . .
        . . . . .
        `)
    music.play(music.stringPlayable("C#5 ", 200), music.PlaybackMode.UntilDone)
}

input.onButtonPressed(Button.B, function on_button_pressed_b() {
    worm()
})
basic.showLeds(`
    . . . . .
    . # # . .
    . # # . .
    . # # . .
    . . . . .
    `)
