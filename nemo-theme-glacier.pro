TEMPLATE = subdirs

isEmpty(PREFIX): PREFIX=/usr
THEME_DIR=$$PREFIX/share/themes

index.files = index.theme
index.path = $$THEME_DIR/glacier/

cc3.files = cc3/icons
cc3.path = $$THEME_DIR/glacier/meegotouch
cc3.CONFIG += no_check_exist

INSTALLS += index cc3