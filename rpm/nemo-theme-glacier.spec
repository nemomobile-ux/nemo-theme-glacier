Name:       nemo-theme-glacier
# >> macros
%define theme_name glacier
# << macros

Summary:    Nemo Mobile Glacier UI theme
Version:    0.0.0
Release:    1
Group:      System/GUI/Other
License:    CC BY-SA 3.0
BuildArch:  noarch
URL:        https://github.com/nemomobile-ux/nemo-theme-glacier
Source0:    %{name}-%{version}.tar.bz2

BuildRequires: fdupes
BuildRequires: qt5-qmake
 
%description
This package contains default theme graphic files.

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake5_install
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-terminal.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-l-terminal.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-settings.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-l-settings.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-screenshot.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-screenshot.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-browser.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-browser.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-calculator.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-calculator.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-calendar.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-calendar.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-camera.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-camera.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-clock.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-clock.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-email.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-email.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-gallery.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-gallery.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-music.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-mediaplayer.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-conversation.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-messaging.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-notes.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-notes.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-documents.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-office.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-contacts.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-people.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-dialer.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-phone.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-settings.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-settings.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-terminal.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-shell.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-packages.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-store.png
ln -sf /usr/share/themes/glacier/meegotouch/icons/icon-app-weather.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-launcher-weather.png

%fdupes  %{buildroot}%{_datadir}

%post

%files
%defattr(-,root,root,-)
%{_datadir}/themes/glacier/index.theme
%{_datadir}/themes/glacier/meegotouch/icons
%{_datadir}/themes/glacier/fontawesome/icons
%{_datadir}/sounds/glacier/stereo


