pins.set_pull(DigitalPin.P2, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P3, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P4, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P5, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P6, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P7, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P8, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P9, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P10, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P11, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P12, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P13, PinPullMode.PULL_UP)
pins.set_pull(DigitalPin.P14, PinPullMode.PULL_UP)
music.set_volume(60)

def on_forever():
    if pins.digital_read_pin(DigitalPin.P2) == 0:
        music.play_tone(262, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P3) == 0:
        music.play_tone(277, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P4) == 0:
        music.play_tone(294, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P5) == 0:
        music.play_tone(311, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P6) == 0:
        music.play_tone(330, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P7) == 0:
        music.play_tone(349, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P8) == 0:
        music.play_tone(370, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P9) == 0:
        music.play_tone(392, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P10) == 0:
        music.play_tone(415, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P11) == 0:
        music.play_tone(440, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P13) == 0:
        music.play_tone(494, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P14) == 0:
        music.play_tone(523, music.beat(BeatFraction.SIXTEENTH))
    if pins.digital_read_pin(DigitalPin.P12) == 0:
        music.play_tone(466, music.beat(BeatFraction.SIXTEENTH))
basic.forever(on_forever)

def on_forever2():
    pass
basic.forever(on_forever2)
