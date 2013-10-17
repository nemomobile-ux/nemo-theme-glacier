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
URL:        https://github.com/nemomobile/nemo-theme-default
Source0:    %{name}-%{version}.tar.bz2
Requires:   gconf
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
ln -sf %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-l-terminal.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-app-terminal.png
ln -sf %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-l-settings.png %{buildroot}/usr/share/themes/glacier/meegotouch/icons/icon-app-settings.png


%fdupes  %{buildroot}%{_datadir}

%post
Theme_Key="/meegotouch/theme/name"
Config_Src=`/usr/bin/gconftool-2 --get-default-source`

Theme_Name=`/usr/bin/gconftool-2 --direct --config-source $Config_Src \
            -g $Theme_Key`

if [ -z $Theme_Name ]; then
    echo "Setting theme name to %{theme_name}"
    /usr/bin/gconftool-2 --direct --config-source $Config_Src \
    -s -t string $Theme_Key %{theme_name}
fi

%files
%defattr(-,root,root,-)
%{_datadir}/themes/glacier/index.theme
%{_datadir}/themes/glacier/meegotouch/icons


