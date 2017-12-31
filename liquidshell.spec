Name:           liquidshell
Version:        1.0
Release:        1
License:        GPLv3+
Summary:        Alternative desktop replacement for KDE Plasma
Group:          Graphical desktop/KDE
URL:            https://github.com/KDE/liquidshell
Source0:        https://dl.opendesktop.org/api/files/downloadfile/id/1514638966/s/1e4264c1a4823bb0536e287edba0b92f/t/1514716279/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  qmake5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  cmake(KF5)
BuildRequires:  cmake(packagekitqt5)
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5Solid)
BuildRequires:  cmake(KF5Notifications)
BuildRequires:  cmake(KF5BluezQt)
BuildRequires:  cmake(KF5Crash)

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
