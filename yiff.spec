Summary:	YIFF Sound Systems
Name:		yiff
Version:	2.12.3
Release:	1
License:	extended GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Source0:	ftp://fox.mit.edu/pub/xsw/%{name}%{version}.tgz
BuildRequires:	gtk+-devel
BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
Requires:	yiff-lib = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description 
The YIFF sound server is a Y compliant sound server providing Y
compliant client applications with sound support. Uses either OSS or
ALSA sound drivers and follows OSS compliancy.

%package devel
Summary:	YIFF development package
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-lib = %{version}

%description devel
YIFF development package

%package lib
Summary:	YIFF libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description lib
YIFF libraries

%package config
Summary:	YIFF configuration utility
Group:		Applications/Games
Group(de):	Applikationen/Spiele
Group(pl):	Aplikacje/Gry
Requires:	%{name}-lib = %{version}
Requires:	%{name} = %{version}

%description config
YIFF configuration utility

%prep
%setup -qn %{name}%{version}

%build
cd libY2
%{__make} CFLAGS="-shared %{rpmcflags}"
cd ..

cd yiff
%{__make} CFLAGS="%{rpmcflags}"
cd ..

cd yiffconfig
%{__make} CFLAGS="`gtk-config --cflags` %{rpmcflags}"
cd ..

cd yiffutils
%{__make} CFLAGS="%{rpmcflags}"
cd ..

%install
rm -rf $RPM_BUILD_ROOT

cd libY2
%{__make} install \
	YLIB_DIR="$RPM_BUILD_ROOT%{_libdir}" \
	YINC_DIR="$RPM_BUILD_ROOT%{_includedir}/Y2" \
	YMAN_DIR="$RPM_BUILD_ROOT%{_mandir}/man3" \
	LDCONFIG="/bin/true"
cd ..

cd yiff
%{__make} install \
	ETC_DIR="$RPM_BUILD_ROOT%{_sysconfdir}" \
	SBIN_DIR="$RPM_BUILD_ROOT%{_sbindir}" \
	MAN_DIR="$RPM_BUILD_ROOT%{_mandir}/man8" 
cd ..

cd yiffconfig
%{__make} install \
BIN_DIR="$RPM_BUILD_ROOT%{_prefix}/X11R6/bin" \
	ICONS_DIR="$RPM_BUILD_ROOT%{_pixmapsdir}" \
MAN_DIR="$RPM_BUILD_ROOT%{_prefix}/X11R6/man/man8"
cd ..

install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir}}
cd yiffutils
%{__make} install \
	PREFIX="$RPM_BUILD_ROOT" \
	BIN_DIR="%{_bindir}" \
	MAN_DIR="%{_mandir}/man1" 
cd ..


gzip -9nf README AUTHORS LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man8/*

%files lib
%defattr(644,root,root,755)
%doc LICENSE.gz
%attr(755,root,root) %{_libdir}/libY2.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/Y2
%{_mandir}/man3/*
%attr(755,root,root) %{_libdir}/libY2.so

%files config
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/*
%{_prefix}/X11R6/man*/*
%{_pixmapsdir}/*
