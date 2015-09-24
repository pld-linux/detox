#
# TODO: move samples to docs
#
Summary:	Utility designed to clean up filenames
Name:		detox
Version:	1.2.0
Release:	3
License:	BSD-like
Group:		Applications
Source0:	http://downloads.sourceforge.net/detox/%{name}-%{version}.tar.gz
# Source0-md5:	04f1bc8501cd40c21610ea3fee7a6fc5
Patch0:		format-security.patch
URL:		http://detox.sourceforge.net/
#BuildRequires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
detox is a utility designed to clean up filenames, especially those
created on other operating systems. It replaces non-standard
characters, such as spaces or Latin-1 characters, with standard
equivalents.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/detox
%attr(755,root,root) %{_bindir}/inline-detox
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/detoxrc
%dir %{_datadir}/detox
%{_datadir}/detox/*.tbl
%{_mandir}/man1/detox*
%{_mandir}/man5/detox*
