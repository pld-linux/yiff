Summary: yiff Y Sound System
Version: 2.8.0
Name: yiff
Release: 2
Copyright: Modified GPL
Group: X11/Sound
URL: http://fox.mit.edu/xsw/yiff
Source: %{name}-%{version}.tar.bz2
Packager: Charles Duffy <cduffy@bigfoot.com>
BuildRoot: /var/tmp/%{name}-root
Requires: yiff-libs
Obsoletes: yiff-server
Prefix: /usr


%description
Yiff is yet another sound server for UNIX.

%package devel
Summary: Yiff headers and development libraries
Group: Development/Sound

%description devel
Y Sound development libraries required to develop programs using yiff

%package libs
Summary: Yiff libraries
Group: X11/Sound/Libraries

%description libs
Y Sound libraries required to run programs using yiff

%prep
%setup

%build
%configure
make

%install
make install prefix=$RPM_BUILD_ROOT/%{prefix}
#install -m 0755 ./yiffstart $RPM_BUILD_ROOT/etc/rc.d/init.d/yiffstart

%post libs
ldconfig

%postun libs
ldconfig

%post
#/etc/rc.d/init.d/yiffstart restart

%files
%defattr(-,root,root)
%doc AUTHORS README INSTALL LICENSE
#%{_prefix}/sbin/*
#%{_prefix}/etc/*
%{_prefix}/bin/*
#%{_prefix}/X11R6/bin/yiffconfig
#/etc/rc.d/init.d/yiffstart

%files libs
%defattr(-,root,root)
%{_prefix}/lib/*.so*

%files devel
%{_prefix}/lib/*.a
%dir %{_prefix}/include/Y2
%{_prefix}/include/Y2/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* %{date} PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: yiff.spec,v $
Revision 1.2  2000-09-24 18:10:58  pascalek
- added $, $ and :$ section

* Sun Jun 25 2000 Charles Duffy <cduffy@bigfoot.com>

- Fixed bug causing headers to not be included in -devel package

* Sat Jun 24 2000 Charles Duffy <cduffy@bigfoot.com>

- Updated to yiff 2.8.0

* Fri Jun 23 2000 Charles Duffy <cduffy@bigfoot.com>

- Updated to work w/ autoconfigurated yiff

- Made the package relocatable. Removed yiffstart in doing so.

- Made yiff-server just yiff. Split off a yiff-devel package.

* Thu Dec 30 1999 Charles E. Leiserson, Jr. <locutus@mit.edu>

- first RPM release
