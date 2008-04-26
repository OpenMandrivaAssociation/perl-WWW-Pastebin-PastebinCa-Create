%define realname   WWW-Pastebin-PastebinCa-Create
%define version    0.001
%define release    %mkrel 2

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    create new pastes on http://pastebin.ca/ from Perl
Source:     http://www.cpan.org/modules/by-module/WWW/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Data::Accessor)
# reported missing by pterjan:
Requires: perl(Class::Data::Accessor)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(WWW::Mechanize)
BuildRequires: perl(overload)
BuildRequires: perl(Module::Build::Compat)

BuildArch: noarch

%description

The module provides means of pasting large texts into the
http://pastebin.ca/ manpage pastebin site.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README META.yml Changes
%{_mandir}/man3/*
%perl_vendorlib/*
