Summary:	Minbif - IRC instant messaging gateway
Name:		minbif
Version:	1.0.2
Release:	0.1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://symlink.me/attachments/download/45/%{name}-%{version}.tar.gz
# Source0-md5:	32418078a1741da3b4028269666f2bac
URL:		http://www.minbif.im/
BuildRequires:	glib2
BuildRequires:	imlib2-devel
BuildRequires:	libcaca-devel
BuildRequires:	libpurple-devel >= 2.4
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Minbif aims to use the libpurple library from the Pidgin project to
provide an IRC-friendly instant messaging client.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
