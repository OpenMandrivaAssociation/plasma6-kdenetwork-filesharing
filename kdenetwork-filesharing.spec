Summary:	Samba filesharing dialog for KDE4
Name:		kdenetwork-filesharing
Version:	15.08.2
Release:	1
Epoch:		3
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
Conflicts:	kde4-filesharing < 3:4.11.0
Obsoletes:	kde4-filesharing < 3:4.11.0

%description
Samba filesharing dialog for KDE4.

%files
%{_kde_libdir}/kde4/sambausershareplugin.so
%{_kde_services}/sambausershareplugin.desktop

#-------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 -DCMAKE_MINIMUM_REQUIRED_VERSION=2.6
%make

%install
%makeinstall_std -C build

