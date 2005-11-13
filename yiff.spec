Summary:	YIFF Sound Systems
Summary(pl):	System d¼wiêku YIFF
Name:		yiff
Version:	2.14.2
Release:	4
License:	GPL-like
Group:		Applications/Sound
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
# Source0-md5:	00c446190892989a167769fb9ea2c037
Source1:	%{name}config.desktop
Patch0:		%{name}-config_dir.patch
Patch1:		%{name}-glibc.patch
Patch2:		%{name}-cpp.patch
Patch3:		%{name}-nolibz.patch
Patch4:		%{name}-gcc33.patch
Patch5:		%{name}-gcc4.patch
URL:		http://wolfpack.twu.net/YIFF/
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
Requires:	yiff-lib = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_soundsdir	/usr/share/sounds

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
Requires:	%{name}-lib = %{version}-%{release}

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
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description config
YIFF Sound Systems configuration utility.

%description config -l pl
Narzêdzie konfiguracyjne do systemu d¼wiêku YIFF.

%prep
%setup -q
bzip2 -d yiff/yiff.8.bz2
%patch0 -p1
bzip2 yiff/yiff.8
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
# (unset) LIBS is abused to pass SONAME
%{__make} -C libY2 \
	CFLAGS="-shared %{rpmcflags} -fPIC" \
	LIBS="-Wl,-soname=libY2.so.14"

%{__make} -C yiff \
	CFLAGS="%{rpmcflags}"

%{__make} -C yiffconfig \
	CFLAGS="`gtk-config --cflags` %{rpmcflags}"

%{__make} -C yiffutils \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir},%{_pixmapsdir}}
install -d $RPM_BUILD_ROOT{%{_datadir}/sounds,%{_desktopdir},%{_sysconfdir}}

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
	BIN_DIR="$RPM_BUILD_ROOT%{_bindir}" \
	ICONS_DIR="$RPM_BUILD_ROOT%{_pixmapsdir}" \
	MAN_DIR="$RPM_BUILD_ROOT%{_mandir}/man1"

%{__make} -C yiffutils install \
	BIN_DIR="$RPM_BUILD_ROOT%{_bindir}" \
	MAN_DIR="$RPM_BUILD_ROOT%{_mandir}/man1"

%{__make} -C stuff install \
	PREFIX="$RPM_BUILD_ROOT" \
	ICONS_DIR="%{_pixmapsdir}" \
	SOUNDS_DIR="%{_soundsdir}"

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

bzip2 -d $RPM_BUILD_ROOT%{_mandir}/man?/*.bz2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/y[!i]*
%attr(755,root,root) %{_sbindir}/*
%attr(644,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/yiffrc
%{_mandir}/man1/y[!i]*
%{_mandir}/man8/*
%{_pixmapsdir}/yiff.xpm
%{_pixmapsdir}/Y.xpm
%{_soundsdir}/*

%files lib
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README
%attr(755,root,root) %{_libdir}/libY2.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libY2.so
%{_includedir}/Y2
%{_mandir}/man3/*

%files config
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/yiffconfig
%{_mandir}/man1/yiffconfig.1*
%{_pixmapsdir}/yiffconfig*
%{_desktopdir}/*
