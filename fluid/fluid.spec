%undefine __cmake_in_source_build

%global snapdate @DATE@
%global snaphash @HASH@

Name:           fluid
Summary:        Library for QtQuick apps with Material Design
Version:        @VERSION@
Release:        0.1%{?snaphash:.%{snapdate}git%(echo %{snaphash} | cut -c -13)}%{?dist}
License:        MPLv2
Url:            https://liri.io
Source0:        https://github.com/lirios/%{name}/%{?snaphash:archive}%{!?snaphash:releases/download}/%{?snaphash}%{!?snaphash:v%{version}}/%{name}-%{?snaphash}%{!?snaphash:%{version}}.tar.gz

Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtquickcontrols2
Requires:       qt5-qtsvg

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  liri-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  qt5-doctools
BuildRequires:  qt5-qtbase-private-devel

%description
Library for fluid and dynamic development of QtQuick apps
with the Material Design language.


%prep
%setup -q -n %{?snaphash:%{name}-%{snaphash}}%{!?snaphash:%{name}-%{version}}


%build
%cmake_liri -DFLUID_USE_SYSTEM_LCS:BOOL=ON
%cmake_build


%install
%cmake_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml


%files
%license LICENSE.MPL2
%doc AUTHORS.md README.md
%{_bindir}/fluid-demo
%{_qt5_qmldir}/Fluid/
%{_datadir}/metainfo/io.liri.Fluid.Demo.appdata.xml
%{_datadir}/applications/io.liri.Fluid.Demo.desktop
%{_datadir}/icons/hicolor/*/apps/io.liri.Fluid.Demo.png
%{_datadir}/icons/hicolor/scalable/apps/io.liri.Fluid.Demo.svg
%{_datadir}/doc/fluid/html/
