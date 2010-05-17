#
# Conditional build:
%bcond_without	imlib		# Compile minbif without imlib
%bcond_without	caca		# Compile with the libcaca support
%bcond_with		video		# Compile with the video support
%bcond_with		purple		# Compile libpurple plugins
%bcond_with		pam			# Compile with the pam support
%bcond_with		tls			# Compile with the tls support

Summary:	Minbif - IRC instant messaging gateway
Name:		minbif
Version:	1.0.3
Release:	0.2
License:	GPL v2
Group:		Applications/Communications
Source0:	http://symlink.me/attachments/download/50/%{name}-%{version}.tar.gz
# Source0-md5:	c08add6234a6dd4a45b46b590fa63268
URL:		http://www.minbif.im/
BuildRequires:	cmake
BuildRequires:	glib2
BuildRequires:	imlib2-devel
BuildRequires:	libcaca-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pidgin-devel >= 2.4
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minbif aims to use the libpurple library from the Pidgin project to
provide an IRC-friendly instant messaging client.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DMAN_PREFIX=%{_mandir}/man8 \
	-DCONF_PREFIX=%{_sysconfdir}/%{name} \
	-DDOC_PREFIX=%{_docdir}/%{name} \
	-DCMAKE_VERBOSE_MAKEFILE=1 \
	-DENABLE_IMLIB=%{!?with_imlib:OFF}%{?with_imlib:ON} \
	-DENABLE_CACA=%{!?with_caca:OFF}%{?with_caca:ON} \
	-DENABLE_VIDEO=%{!?with_video:OFF}%{?with_video:ON} \
	-DENABLE_PLUGIN=%{!?with_purple:OFF}%{?with_purple:ON} \
	-DENABLE_PAM=%{!?with_pam:OFF}%{!?with_pam:ON} \
	-DENABLE_TLS=%{!?with_tls:OFF}%{?with_tls:ON} \
	-DDEBUG=%{!?debug:OFF}%{?debug:ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/minbif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%doc doc/minbif.xinetd
%attr(755,root,root) %{_bindir}/minbif
%dir %{_sysconfdir}/minbif
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/minbif/minbif.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/minbif/minbif.motd
%{_mandir}/man8/minbif.8*
