Name:           liquidshell
Version:        1.0
Release:        1
License:        GPLv3+
Summary:        Alternative desktop replacement for KDE Plasma
Group:          System/GUI/KDE
URL:            https://github.com/KDE/liquidshell
Source0:        https://github.com/KDE/liquidshell/archive/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  qmake5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  packagekit-qt
BuildRequires:  networkmanager-qt
BuildRequires:  bluez-qt
BuildRequires:  kcmutils
BuildRequires:  knewstuff
BuildRequires:  hicolor-icon-theme

%description
An alternative to plasmashell.
It does not use QtQuick but instead uses QtWidgets.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build

%files
%{_bindir}/%{name}
%{_datadir}/applications/org.kde.liquidshell.desktop
%{_datadir}/icons/hicolor/48x48/apps/liquidshell.png
%{_datadir}/knotifications5/liquidshell.notifyrc
