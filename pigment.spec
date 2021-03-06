Summary:	Animation frameworks for Elisa
Summary(pl.UTF-8):	Framework animacji dla projektu Elisa
Name:		pigment
Version:	0.3.17
Release:	10
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://elisa.fluendo.com/static/download/pigment/%{name}-%{version}.tar.bz2
# Source0-md5:	b0947a18cc9265f3129ff4b069c1ed0c
URL:		https://code.fluendo.com/pigment/trac
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	gstreamer-devel >= 0.10.13
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	pango-devel >= 1:1.16
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	xorg-lib-libXrandr-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rendering, animation and widget frameworks for Elisa.

%description -l pl.UTF-8
Framework renderowania animacji i widgetów dla projektu Elisa.

%package devel
Summary:	Header files for pigment libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek pigment
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.8.0
Requires:	gstreamer-devel >= 0.10.13
Requires:	gstreamer-plugins-base-devel >= 0.10.0
Requires:	gtk+2-devel >= 2:2.12.0

%description devel
Header files for pigment libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek pigment.

%package static
Summary:	Static pigment libraries
Summary(pl.UTF-8):	Statyczne biblioteki pigment
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static pigment libraries.

%description static -l pl.UTF-8
Statyczne biblioteki pigment.

%prep
%setup -q

%build
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{_libdir}/pigment-0.3/%{version}/*.{la,a}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpigment-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpigment-0.3.so.11
%attr(755,root,root) %{_libdir}/libpigment-gtk-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpigment-gtk-0.3.so.11
%attr(755,root,root) %{_libdir}/libpigment-imaging-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpigment-imaging-0.3.so.11
%dir %{_libdir}/pigment-0.3
%dir %{_libdir}/pigment-0.3/%{version}
%dir %{_libdir}/pigment-0.3/%{version}/*.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpigment-0.3.so
%attr(755,root,root) %{_libdir}/libpigment-gtk-0.3.so
%attr(755,root,root) %{_libdir}/libpigment-imaging-0.3.so
%{_includedir}/pigment-0.3
%{_pkgconfigdir}/pigment-0.3.pc
%{_pkgconfigdir}/pigment-gtk-0.3.pc
%{_pkgconfigdir}/pigment-imaging-0.3.pc
%{_gtkdocdir}/pigment

%files static
%defattr(644,root,root,755)
%{_libdir}/libpigment-0.3.a
%{_libdir}/libpigment-gtk-0.3.a
%{_libdir}/libpigment-imaging-0.3.a
