#
# Conditional build:
%bcond_without	tests		# build with tests
#
Summary:	Utility designed to clean up filenames
Name:		detox
Version:	3.0.1
Release:	1
License:	BSD-3-Clause
Group:		Applications
Source0:	https://github.com/dharple/detox/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	65cd26a1ed9753ad73be665066be695e
Patch0:		test-valgrind-opt-in.patch
URL:		https://github.com/dharple/detox
BuildRequires:	bison
BuildRequires:	flex
%{?with_tests:BuildRequires:	check-devel}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
detox is a utility designed to clean up filenames, especially those
created on other operating systems. It replaces non-standard
characters, such as spaces or Latin-1 characters, with standard
equivalents.

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	%{?with_tests:--with-check}
%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUILD.md CHANGELOG.md README.md THANKS.md
%attr(755,root,root) %{_bindir}/detox
%attr(755,root,root) %{_bindir}/inline-detox
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/detoxrc
%dir %{_datadir}/detox
%dir %{_datadir}/detox/legacy
%{_datadir}/detox/*.tbl
%{_datadir}/detox/legacy/*.tbl
%{_mandir}/man1/detox*
%{_mandir}/man1/inline-detox*
%{_mandir}/man5/detox*
