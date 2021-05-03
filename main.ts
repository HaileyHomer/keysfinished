pins.setPull(DigitalPin.P2, PinPullMode.PullUp)
pins.setPull(DigitalPin.P3, PinPullMode.PullUp)
pins.setPull(DigitalPin.P4, PinPullMode.PullUp)
pins.setPull(DigitalPin.P5, PinPullMode.PullUp)
pins.setPull(DigitalPin.P6, PinPullMode.PullUp)
pins.setPull(DigitalPin.P7, PinPullMode.PullUp)
pins.setPull(DigitalPin.P8, PinPullMode.PullUp)
pins.setPull(DigitalPin.P9, PinPullMode.PullUp)
pins.setPull(DigitalPin.P10, PinPullMode.PullUp)
pins.setPull(DigitalPin.P11, PinPullMode.PullUp)
pins.setPull(DigitalPin.P12, PinPullMode.PullUp)
pins.setPull(DigitalPin.P13, PinPullMode.PullUp)
pins.setPull(DigitalPin.P14, PinPullMode.PullUp)
music.setVolume(255)
basic.forever(function () {
    if (pins.digitalReadPin(DigitalPin.P2) == 0) {
        music.playTone(262, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P3) == 0) {
        music.playTone(277, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P4) == 0) {
        music.playTone(294, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P5) == 0) {
        music.playTone(311, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P6) == 0) {
        music.playTone(330, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P7) == 0) {
        music.playTone(349, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P8) == 0) {
        music.playTone(370, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P9) == 0) {
        music.playTone(392, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P10) == 0) {
        music.playTone(415, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P11) == 0) {
        music.playTone(440, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P13) == 0) {
        music.playTone(494, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P14) == 0) {
        music.playTone(523, music.beat(BeatFraction.Sixteenth))
    }
    if (pins.digitalReadPin(DigitalPin.P12) == 0) {
        music.playTone(466, music.beat(BeatFraction.Sixteenth))
    }
})
