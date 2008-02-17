Summary:	Animation frameworks for Elisa
Summary(pl.UTF-8):	Framework animacji dla projektu Elisa
Name:		pigment
Version:	0.3.4
Release:	0.1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://elisa.fluendo.com/static/download/pigment/%{name}-%{version}.tar.gz
# Source0-md5:	612acbe8a6c8ca1a2a268c08d05d92e0
URL:		http://www.fluendo.com/elisa/pigment.php
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	cairo-devel >= 1.4.0
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gstreamer-devel >= 0.10.13
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
BuildRequires:	pango-devel >= 1:1.16
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	python-pygobject-devel >= 2.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
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
Requires:	gtk+2-devel >= 2:2.12.0
Requires:	gstreamer-devel >= 0.10.13
Requires:	gstreamer-plugins-base-devel >= 0.10.0

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
rm -f $RPM_BUILD_ROOT%{_libdir}/pigment-0.3/%{version}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/_pgmmodule.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpigment-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpigment-0.3.so.3
%attr(755,root,root) %{_libdir}/libpigment-gtk-0.3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libpigment-gtk-0.3.so.3
%dir %{_libdir}/pigment-0.3
%dir %{_libdir}/pigment-0.3/%{version}
%dir %{_libdir}/pigment-0.3/%{version}/*.so*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpigment-0.3.so
%attr(755,root,root) %{_libdir}/libpigment-gtk-0.3.so
%{_libdir}/libpigment-0.3.la
%{_libdir}/libpigment-gtk-0.3.la
%{_includedir}/pigment-0.3
%{_pkgconfigdir}/pigment-0.3.pc
%{_pkgconfigdir}/pigment-gtk-0.3.pc
%{_gtkdocdir}/pigment

%files static
%defattr(644,root,root,755)
%{_libdir}/libpigment-0.3.a
%{_libdir}/libpigment-gtk-0.3.a
