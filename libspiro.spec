%define	major	1
%define	libname	%mklibname spiro %{major}
%define	devname	%mklibname -d spiro

Name:		libspiro
Version:	20221101
Release:	2
Summary:	Library to simplify the drawing of beautiful curves
Group:		System/Libraries
License:	GPLv2+
URL:		http://libspiro.sourceforge.net/
Source0:	https://github.com/fontforge/libspiro/releases/download/%{version}/libspiro-dist-%{version}.tar.gz

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
%autosetup -n libspiro-%{version}
autoreconf -fi

%build
%configure
%make_build

%install
%make_install

%files -n %{libname}
%doc README* ChangeLog AUTHORS
%{_libdir}/libspiro.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libspiro.so
%{_libdir}/pkgconfig/libspiro.pc
%{_mandir}/man3/libspiro.3*
