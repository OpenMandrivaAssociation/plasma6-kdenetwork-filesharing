%define stable %([ "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

Summary:	Samba filesharing dialog for KDE6
Name:		plasma6-kdenetwork-filesharing
Version:	24.01.90
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
Source0:	http://download.kde.org/%{stable}/release-service/%{version}/src/kdenetwork-filesharing-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6Declarative)
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6QuickWidgets)
BuildRequires:	cmake(QCoro6)
BuildRequires:	cmake(packagekitqt6)
BuildRequires:	samba-client
Requires:	samba-client

%description
Samba filesharing dialog for KDE6.

%files -f kfileshare.lang
%{_libdir}/qt6/plugins/kf6/propertiesdialog/sambausershareplugin.so
%{_libdir}/qt6/plugins/kf6/propertiesdialog/SambaAcl.so
%{_datadir}/metainfo/org.kde.kdenetwork-filesharing.metainfo.xml
%{_libdir}/libexec/kf6/kauth/authhelper
%{_datadir}/dbus-1/system-services/org.kde.filesharing.samba.service
%{_datadir}/dbus-1/system.d/org.kde.filesharing.samba.conf
%{_datadir}/polkit-1/actions/org.kde.filesharing.samba.policy

#-------------------------------------------

%prep
%autosetup -p1 -n kdenetwork-filesharing-%{?git:master}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja -DSAMBA_INSTALL=OFF

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kfileshare --with-html
