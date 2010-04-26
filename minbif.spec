Summary:	Minbif - IRC instant messaging gateway
Name:		minbif
Version:	1.0.2
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://symlink.me/attachments/download/45/%{name}-%{version}.tar.gz
# Source0-md5:	32418078a1741da3b4028269666f2bac
Patch0:		gcc.patch
URL:		http://www.minbif.im/
BuildRequires:	cmake
BuildRequires:	glib2
BuildRequires:	imlib2-devel
BuildRequires:	libcaca-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pidgin-devel >= 2.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minbif aims to use the libpurple library from the Pidgin project to
provide an IRC-friendly instant messaging client.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	PREFIX=%{_prefix} \
	MAN_PREFIX=%{_mandir}/man8 \
	CONF_PREFIX=%{_sysconfdir}/%{name} \
	DOC_PREFIX=%{_docdir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/minbif
%dir %{_sysconfdir}/minbif
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/minbif/minbif.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/minbif/minbif.motd
%{_mandir}/man8/minbif.8*
