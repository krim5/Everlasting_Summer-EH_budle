init -1 python hide:

    if persistent.choices == None:
        persistent.choices = []

    persistent.hentai = False

    config.default_afm_time = 0

    config.default_afm_enable = None

    config_session = False





    _preferences.self_voicing = False




    config.developer = False

    want_label_select = False

    config.skip_indicator = False

    config.screen_width = 1920
    config.screen_height = 1080

    if not persistent._use_custom_menu:
        config.window_title = u"Бесконечное лето"
        config.name = "Everlasting Summer"
        config.version = "1.2"
        config.window_icon = "images/misc/icon.png"
        config.windows_icon = "images/misc/icon.png"
    else:
        config.window_title = u"Бесконечное лето: Endless Horizons"
        config.name = "Everlasting Summer: EH"
        config.version = current_ver
        config.window_icon = "images/custom_gui/icons/eh_icon.png"
        config.windows_icon = "images/custom_gui/icons/eh_icon.png"




    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    

    config.default_fullscreen = True

    config.has_autosave = True

    config.gl_resize = True

    config.default_text_cps = 50

    # config.mouse = { }
    # config.mouse["default"] = [
    #     ("images/misc/mouse/1.png",  0, 0)

    #     ]

    _game_menu_screen = "game_menu_selector"

    config.layers = ['underlay', 'master','mapoverlay', 'widgetoverlay', 'transient','screens','overlay']

    #config.main_menu_music = "sound/music/blow_with_the_fires.ogg"

    theme.roundrect(
        widget = "#003c78",
        widget_hover = "#0050a0",
        widget_text = "#c8ffff",
        widget_selected = "#ffffc8",
        disabled = "#404040",
        disabled_text = "#c8c8c8",
        label = "#ffffff",
        frame = "#6496c8",
        rounded_window = False,
        mm_root = "main_menu",
        gm_root = "#dcebff",
        less_rounded = True,       
        )


    config.has_sound = True
    config.has_music = True
    config.has_voice = True

    config.rollback_length = 1000
    config.hard_rollback_limit = 1000







    config.enter_transition = Dissolve(.25)
    config.exit_transition = Dissolve(.25)
    config.intra_transition = Dissolve(.25)
    config.main_game_transition = Dissolve(.25)
    config.game_main_transition = Dissolve(.25)
    config.end_splash_transition = Dissolve(.25)
    config.end_game_transition = fade
    config.after_load_transition = dissolve
    config.window_show_transition = Dissolve(.25)
    config.window_hide_transition = Dissolve(.25)

    config.quit_action = ui.gamemenus("_confirm_quit")

    def new_screenshot_callback(fn):
        renpy.notify(__("Saved screenshot as " + fn.rsplit("\\",1)[1]))

    config.screenshot_callback = new_screenshot_callback

init python: ## СБОРКА
    build.directory_name = "Everlasting_Summer-EH_" + config.version
    build.executable_name = "Everlasting_Summer-EH"
    build.include_update = False

    ## Удаление
    build.classify('**debug.rpy**', None)
    build.classify('**hentai.rpy**', None)
    build.classify('**hentai.rpyc**', None)
    build.classify('**dev-mode.rpy**', None)
    build.classify('**dev-mode.rpyc**', None)
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpy', None)
    build.classify('**.bat', None)
    build.classify('**.txt', None)
    build.classify('**.bak', None)
    build.classify('**.rpy#', None)
    build.classify('**.log', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('**activate_es_menu.rpy**', None)
    build.classify('**activate_es_menu.rpyc**', None)

    ## Лишние файлы с гитхаба
    build.classify('**.md', None)
    build.classify('readme_files/**.png', None)
    build.classify('readme_files/**.gif', None)


    ## Архивирование бинарных файлов
    build.archive("loner-data", "all")
    build.archive("limb-data", "all")
    build.archive("data", "all")
    build.archive("update-data", "all")
    build.archive("v1.05-data", "all")


    build.classify('game/mods/Loner/**deleted**', 'v1.05-data')
    build.classify('game/mods/Loner/**ext_beach_fire_red.jpg', 'v1.05-data')
    build.classify('game/mods/Loner/**ed_beach_fire_un_shadow.jpg', 'v1.05-data')
    build.classify('game/mods/Loner/**ed_beach_fire_un**.jpg', 'v1.05-data')
    build.classify('game/mods/Loner/**ed_scene_un_**.jpg', 'v1.05-data')
    build.classify('game/mods/Loner/**ed_un_d2_scary_shadow_3.png', 'v1.05-data')
    build.classify('game/mods/Loner/**ed_un_d2_smile_pioneer_red.png', 'v1.05-data')

    build.classify('game/mods/Limb/**us_dwarf.png', 'v1.05-data')

    build.classify('game/images/custom_gui/o_rly/custom_base.png', 'v1.05-data')
    

    build.classify('game/mods/Loner/**', 'loner-data')

    build.classify('game/mods/Limb/**', 'limb-data')

    build.classify('game/update/**', 'update-data')

    build.classify('game/**.png', 'data')
    build.classify('game/**.jpg', 'data')
    build.classify('game/**.ogg', 'data')
    build.classify('game/**.wav', 'data')
    build.classify('game/**.mp3', 'data')
    build.classify('game/**.ttf', 'data')
