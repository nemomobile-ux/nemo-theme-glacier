cmake_minimum_required(VERSION 3.10)

project(nemo-theme-glacier
    VERSION 0.0.0
    DESCRIPTION "Nemo Mobile Glacier UI theme"
    LANGUAGES NONE)

if(NOT DEFINED CMAKE_INSTALL_DATADIR)
    set(CMAKE_INSTALL_DATADIR "share" CACHE PATH "Read-only architecture-independent data")
endif()

# Theme metadata
install(FILES index.theme
    DESTINATION ${CMAKE_INSTALL_DATADIR}/themes/glacier)

# Icons
install(DIRECTORY icons/fontawesome/
    DESTINATION ${CMAKE_INSTALL_DATADIR}/themes/glacier/fontawesome/icons)

install(DIRECTORY icons/meegotouch/
    DESTINATION ${CMAKE_INSTALL_DATADIR}/themes/glacier/meegotouch/icons)

# Sounds
install(DIRECTORY sounds/glacier/stereo/
    DESTINATION ${CMAKE_INSTALL_DATADIR}/sounds/glacier/stereo)

# Compatibility and launcher icon symlinks
install(CODE "
    if(IS_ABSOLUTE \"${CMAKE_INSTALL_DATADIR}\")
        set(_full_datadir \"${CMAKE_INSTALL_DATADIR}\")
    else()
        set(_full_datadir \"\${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_DATADIR}\")
    endif()
    set(_icon_dir \"\${_full_datadir}/themes/glacier/meegotouch/icons\")
    set(_dest \"\$ENV{DESTDIR}\${_icon_dir}\")
    file(MAKE_DIRECTORY \"\${_dest}\")

    function(_glacier_icon_symlink link_name target_name)
        file(REMOVE \"\${_dest}/\${link_name}\")
        execute_process(
            COMMAND \"${CMAKE_COMMAND}\" -E create_symlink
                \"\${_icon_dir}/\${target_name}\"
                \"\${_dest}/\${link_name}\"
        )
    endfunction()

    _glacier_icon_symlink(icon-l-terminal.png        icon-app-terminal.png)
    _glacier_icon_symlink(icon-l-settings.png        icon-app-settings.png)
    _glacier_icon_symlink(icon-launcher-screenshot.png icon-app-screenshot.png)
    _glacier_icon_symlink(icon-launcher-browser.png  icon-app-browser.png)
    _glacier_icon_symlink(icon-launcher-calculator.png icon-app-calculator.png)
    _glacier_icon_symlink(icon-launcher-calendar.png icon-app-calendar.png)
    _glacier_icon_symlink(icon-launcher-camera.png   icon-app-camera.png)
    _glacier_icon_symlink(icon-launcher-clock.png    icon-app-clock.png)
    _glacier_icon_symlink(icon-launcher-email.png    icon-app-email.png)
    _glacier_icon_symlink(icon-launcher-gallery.png  icon-app-gallery.png)
    _glacier_icon_symlink(icon-launcher-mediaplayer.png icon-app-music.png)
    _glacier_icon_symlink(icon-launcher-messaging.png icon-app-conversation.png)
    _glacier_icon_symlink(icon-launcher-notes.png    icon-app-notes.png)
    _glacier_icon_symlink(icon-launcher-office.png   icon-app-documents.png)
    _glacier_icon_symlink(icon-launcher-people.png   icon-app-contacts.png)
    _glacier_icon_symlink(icon-launcher-phone.png    icon-app-dialer.png)
    _glacier_icon_symlink(icon-launcher-settings.png icon-app-settings.png)
    _glacier_icon_symlink(icon-launcher-shell.png    icon-app-terminal.png)
    _glacier_icon_symlink(icon-launcher-store.png    icon-app-packages.png)
    _glacier_icon_symlink(icon-launcher-weather.png  icon-app-weather.png)
")
