Summary:	YIFF Sound Systems
Summary(pl):	System d¼wiêku YIFF
Name:		yiff
Version:	2.12.3
# newer available; not tested yet
#Version:	2.12.4
Release:	1
License:	Modyfied GPL
Group:		Applications/Sound
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}%{version}.tgz
Source1:	%{name}config.desktop
Patch0:		%{name}-config_dir.patch
URL:		http://fox.mit.edu/xsw/yiff/
BuildRequires:	gtk+-devel
BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
Requires:	yiff-lib = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The YIFF sound server is a Y compliant sound server providing Y
compliant client applications with sound support. Uses either OSS or
ALSA sound drivers and follows OSS compliancy.

%description -l pl
Serwer d¼wiêku YIFF jest zgodnym z Y serwerem d¼wiêku daj±cym obs³ugê
d¼wiêku dla aplikacji klienckich zgodnych z Y. U¿ywa sterowników OSS
lub ALSA.

%package devel
Summary:	YIFF development package
Summary(pl):	Pakiet programistyczny YIFF
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}

%description devel
YIFF Sound Systems development files required to develop programs
using yiff.

%description devel -l pl
Pliki potrzebne do tworzenia programów u¿ywaj±cych systemu d¼wiêku
YIFF.

%package lib
Summary:	YIFF libraries
Summary(pl):	Biblioteki YIFF
Group:		Development/Libraries

%description lib
YIFF Sound Systems library required to run programs using yiff.

%description lib -l pl
Biblioteki potrzebne do uruchamiania programów korzystaj±cych z
systemu d¼wiêku YIFF.

%package config
Summary:	YIFF configuration utility
Summary(pl):	Narzêdzie konfiguracyjne do YIFF
Group:		Applications/Games
Requires:	%{name}-lib = %{version}
Requires:	%{name} = %{version}

%description config
YIFF Sound Systems configuration utility.

%description config -l pl
Narzêdzie konfiguracyjne do systemu d¼wiêku YIFF.

%prep
%setup -qn %{name}%{version}
%patch0 -p1

%build

%{__make} -C libY2 CFLAGS="-shared %{rpmcflags}"

%{__make} -C yiff CFLAGS="%{rpmcflags}"

%{__make} -C yiffconfig CFLAGS="`gtk-config --cflags` %{rpmcflags}"

%{__make} -C yiffutils CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir},%{_pixmapsdir}}
install -d $RPM_BUILD_ROOT{%{_datadir}/sounds,%{_applnkdir},%{_sysconfdir}}

%{__make} -C libY2 install \
	YLIB_DIR="$RPM_BUILD_ROOT%{_libdir}" \
	YINC_DIR="$RPM_BUILD_ROOT%{_includedir}/Y2" \
	YMAN_DIR="$RPM_BUILD_ROOT%{_mandir}/man3" \
	LDCONFIG="/bin/true"

%{__make} -C yiff install \
	ETC_DIR="$RPM_BUILD_ROOT%{_sysconfdir}" \
	SBIN_DIR="$RPM_BUILD_ROOT%{_sbindir}" \
	MAN_DIR="$RPM_BUILD_ROOT%{_mandir}/man8"
install yiff/yiffrc $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} -C yiffconfig install \
BIN_DIR="$RPM_BUILD_ROOT%{_prefix}/X11R6/bin" \
	ICONS_DIR="$RPM_BUILD_ROOT%{_pixmapsdir}" \
MAN_DIR="$RPM_BUILD_ROOT%{_prefix}/X11R6/man/man8"

%{__make} -C yiffutils install \
	PREFIX="$RPM_BUILD_ROOT" \
	BIN_DIR="%{_bindir}" \
	MAN_DIR="%{_mandir}/man1"

%{__make} -C stuff install \
	PREFIX="$RPM_BUILD_ROOT" \
	ICONS_DIR="%{_pixmapsdir}" \
	SOUNDS_DIR="%{_datadir}/sounds"
install -d $RPM_BUILD_ROOT%{_applnkdir}/Settings
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Settings

gzip -9nf README AUTHORS LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %config %verify(not size mtime md5) %{_sysconfdir}/yiffrc
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_pixmapsdir}/yiff.xpm
%{_pixmapsdir}/Y.xpm
%{_datadir}/sounds/*

%files lib
%defattr(644,root,root,755)
%doc LICENSE.gz
%attr(755,root,root) %{_libdir}/libY2.so.*
%attr(755,root,root) %{_libdir}/libY2.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/Y2
%{_mandir}/man3/*

%files config
%defattr(644,root,root,755)
%attr(755,root,root) %{_prefix}/X11R6/bin/*
%{_prefix}/X11R6/man*/*
%{_pixmapsdir}/yiffconfig*
%{_applnkdir}/Settings/*
