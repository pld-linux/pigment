Summary:	Animation frameworks for Elisa
Summary(pl.UTF-8):	Framework animacji dla projektu Elisa
Name:		pigment
Version:	0.1.5
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://elisa.fluendo.com/static/download/pigment/%{name}-%{version}.tar.gz
# Source0-md5:	d39000c031e35d5a5835343161ce4bf8
URL:		http://www.fluendo.com/elisa/pigment.php
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	cairo-devel >= 1.0.0
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	gstreamer-devel >= 0.10.0
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0
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
Summary:	Header files for libpgmrender library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libpgmrender
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libpgmrender library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libpgmrender.

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
rm -f $RPM_BUILD_ROOT%{_libdir}/pigment-*/{*.la,gstreamer/*.la}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/pgmrendermodule.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpgmrender-*.so.*.*.*
%dir %{_libdir}/%{name}-*
%attr(755,root,root) %{_libdir}/%{name}-*/libpgmrendergl1.so
%dir %{_libdir}/%{name}-*/gstreamer
%attr(755,root,root) %{_libdir}/%{name}-*/gstreamer/libpgmrendersink.so
%attr(755,root,root) %{py_sitedir}/pgmrendermodule.so
%{py_sitescriptdir}/pgm

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpgmrender-*.so
%{_libdir}/libpgmrender-*.la
%{_includedir}/pigment-*
%{_pkgconfigdir}/pigment-render-0.1.pc
%{_gtkdocdir}/pigment-render
