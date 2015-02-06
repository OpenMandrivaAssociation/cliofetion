Summary: command line libofetion client implemention
Name: cliofetion
Version: 2.2.0
Release: 3
Group: Networking/Instant messaging
License: GPLv2+
URL: http://code.google.com/p/ofetion/
Source0: http://ofetion.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires: libofetion-devel >= 2.2.0
BuildRequires: cmake

%description
OpenFetion is a IM client based on GTK+2.0, using CHINA MOBILE's Fetion
Protocol Version 4.

%prep
%setup -qn %name-%version

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%{_bindir}/%name
%{_mandir}/man1/*


%changelog
* Sat May 14 2011 Funda Wang <fwang@mandriva.org> 2.2.0-1mdv2011.0
+ Revision: 674491
- update file list
- new version 2.2.0

* Sun Dec 26 2010 Funda Wang <fwang@mandriva.org> 2.1.0-1mdv2011.0
+ Revision: 625229
- import cliofetion

