Summary:	yiff Y Sound System
Version:	2.8.0
Name:		yiff
Release:	2
License:	Modified GPL
Group:		Applications/Sound
Group(de):	Applikationen/Laut
Group(pl):	Aplikacje/D¼wiêk
Source0:	%{name}-%{version}.tar.bz2
URL:		http://fox.mit.edu/xsw/yiff/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	yiff-server

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Yiff is yet another sound server for UNIX.

%package devel
Summary:	Yiff headers and development libraries
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-libs = %{version}

%description devel
Y Sound development libraries required to develop programs using yiff.

%package libs
Summary:	Yiff libraries
Group:		X11/Libraries
Group(de):	X11/Libraries
Group(pl):	X11/Biblioteki

%description libs
Y Sound libraries required to run programs using yiff.

%prep
%setup -q

%build
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install prefix=$RPM_BUILD_ROOT/%{_prefix}
#install yiffstart $RPM_BUILD_ROOT/etc/rc.d/init.d/yiffstart

%post   libs -p /snin/ldconfig
%postun libs -p /sbin/ldconfig

%post
#/etc/rc.d/init.d/yiffstart restart

%files
%defattr(644,root,root,755)
%doc AUTHORS README INSTALL LICENSE
#%{_prefix}/sbin/*
#%{_prefix}%{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
#%{_prefix}/X11R6/bin/yiffconfig
#/etc/rc.d/init.d/yiffstart

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libs*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libs*.so
%{_includedir}/Y2

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT
