Summary:	Animation frameworks for Elisa
Summary(pl):	Framework animacji dla projektu Elisa
Name:		pigment
Version:	0.1.4
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://www.fluendo.com/elisa/downloads/pigment/%{name}-%{version}.tar.gz
# Source0-md5:	3b04d2781d90dcd3bfcd860f819632b1
URL:		http://www.fluendo.com/elisa/pigment.php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Rendering, animation and widget frameworks for Elisa.

%description -l pl
Framework renderowania animacji i widgetów dla projektu Elisa.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT%{py_sitescriptdir}/pgm -name "*.py" -exec rm {} \;
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_libdir}/*.so*
%dir %{_libdir}/%{name}*
%attr(755,root,root) %{_libdir}/%{name}*/libpgmrendergl1.so
%dir %{_libdir}/%{name}*/gstreamer
%attr(755,root,root) %{_libdir}/%{name}*/gstreamer/libpgmrendersink.so
%attr(755,root,root) %{py_sitedir}/pgmrendermodule.so
%{_pkgconfigdir}/%{name}-render-0.1.pc
%{py_sitescriptdir}/pgm
