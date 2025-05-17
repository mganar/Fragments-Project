# definitions.rpy 
# definitions.rpy

# Initialize voice callback system
init python:
    renpy.music.register_channel(name='beeps', mixer='voice')

    # Voice callbacks per character
    def amari_voice(event, **kwargs):
        if event == "show":
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def cael_voice(event, **kwargs):
        if event == "show":
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def iven_voice(event, **kwargs):
        if event == "show":
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def lune_voice(event, **kwargs):
        if event == "show":
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def maika_voice(event, **kwargs):
        if event == "show":
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def niko_voice(event, **kwargs):
        if event == "show":
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def renn_voice(event, **kwargs):
        if event == "show":
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def suki_voice(event, **kwargs):
        if event == "show":
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def tomo_voice(event, **kwargs):
        if event == "show":
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

    def veyla_voice(event, **kwargs):
        if event == "show":
            build_sentence(_last_say_what, "eileen")
            renpy.sound.play("audio/output.wav", channel="beeps", loop=False)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="beeps")

# Character definitions with voice callbacks
define a = Character("Amari", color="#DD1FFF", what_prefix="“", what_suffix="”", callback=amari_voice)
define c = Character("Cael", color="#8BFF1F", what_prefix="“", what_suffix="”", callback=cael_voice)
define i = Character("Iven", color="#FF1F40", what_prefix="“", what_suffix="”", callback=iven_voice)
define l = Character("Lune", color="#FF931F", what_prefix="“", what_suffix="”", callback=lune_voice)
define m = Character("Maika", color="#4C00FF", what_prefix="“", what_suffix="”", callback=maika_voice)
define n = Character("Niko", color="#FF1FA9", what_prefix="“", what_suffix="”", callback=niko_voice)
define r = Character("Renn", color="#FF1FA9", what_prefix="“", what_suffix="”", callback=renn_voice)
define s = Character("Suki", color="#1FCBFF", what_prefix="“", what_suffix="”", callback=suki_voice)
define t = Character("Tomo", color="#FFF01F", what_prefix="“", what_suffix="”", callback=tomo_voice)
define v = Character("Veyla", color="#1FFFD6", what_prefix="“", what_suffix="”", callback=veyla_voice)