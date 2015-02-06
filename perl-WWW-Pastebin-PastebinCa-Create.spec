%define realname   WWW-Pastebin-PastebinCa-Create

Name:		perl-%{realname}
Version:	%perl_convert_version 0.004
Release:	3
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Create new pastes on http://pastebin.ca/ from Perl
Source:		http://www.cpan.org/modules/by-module/WWW/WWW-Pastebin-PastebinCa-Create-0.004.tar.gz
Url:		http://search.cpan.org/dist/%{realname}

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Data::Accessor)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildRequires:	perl(WWW::Mechanize)
BuildRequires:	perl(overload)
BuildRequires:	perl(Module::Build::Compat)
# reported missing by pterjan:
Requires:	perl(Class::Data::Accessor)

BuildArch:	noarch

%description
The module provides means of pasting large texts into the
http://pastebin.ca/ manpage pastebin site.

%prep
%setup -qn WWW-Pastebin-PastebinCa-Create-0.004

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README META.yml Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


