Summary:	Samba filesharing dialog for KDE4
Name:		kdenetwork-filesharing
Version:	19.08.0
Release:	2
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
Conflicts:	kde4-filesharing < 3:4.11.0
Obsoletes:	kde4-filesharing < 3:4.11.0
Requires:	samba-client

%description
Samba filesharing dialog for KDE5.

%files -f kfileshare.lang
%{_libdir}/qt5/plugins/sambausershareplugin.so
%{_datadir}/kservices5/sambausershareplugin.desktop

#-------------------------------------------

%prep
%setup -q
%cmake_kde5 -DSAMBA_INSTALL=OFF

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kfileshare --with-html
