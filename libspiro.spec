%define	major	0
%define	libname	%mklibname spiro %{major}
%define	devname	%mklibname -d spiro

Name:		libspiro
Version:	0.2.20130930
Release:	2
Summary:	Library to simplify the drawing of beautiful curves
Group:		System/Libraries
License:	GPLv2+
URL:		http://libspiro.sourceforge.net/
Source0:	%{name}-%{version}.tar.xz

%description
This library will take an array of spiro control points and 
convert them into a series of bézier splines which can then 
be used in the myriad of ways the world has come to use béziers. 

%package -n	%{libname}
Summary:	Library to simplify the drawing of beautiful curves
Group:		System/Libraries

%description -n	%{libname}
This library will take an array of spiro control points and 
convert them into a series of bézier splines which can then 
be used in the myriad of ways the world has come to use béziers. 

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	spiro-devel = %{EVRD}

%description -n	%{devname}
This package contains libraries and header files for developing applications
that use %{name}.

%prep
%setup -q
autoreconf -fi

%build
%configure
%make

%install
%makeinstall_std

%files -n %{libname}
%doc README* ChangeLog AUTHORS
%{_libdir}/libspiro.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libspiro.so

%changelog
* Fri Feb 21 2014 Per Øyvind Karlsen  <proyvind@moondrake.org> 20130930-1
- initial Moondrake import

* Wed Oct 02 2013 Kevin Fenzi <kevin@scrye.com> 20130930-1
- Update to 20130930 version

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Mar 23 2013 Kevin Fenzi <kevin@scrye.com> 20071029-10
- Add patch to add aarch64 support. Fixes bug #925890

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 22 2012 Parag <paragn AT fedoraproject DOT org> - 20071029-8
- Resolves:rh#879153 - spec cleanup for recent packaging guidelines

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jan 10 2012 Nils Philippsen <nils@redhat.com> - 20071029-6
- rebuild for gcc 4.7

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 15 2009 Parag <paragn AT fedoraproject.org> - 20071029-4
- Fix rpmlint error "libspiro.src:53: E: files-attr-not-set"

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20071029-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 16 2008 Kevin Fenzi <kevin@tummy.com> - 20071029-1
- Initial version for Fedora
