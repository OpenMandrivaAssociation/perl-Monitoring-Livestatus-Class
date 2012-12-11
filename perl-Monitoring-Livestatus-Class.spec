%define upstream_name    Monitoring-Livestatus-Class
%define upstream_version 0.03

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Monitoring::Livestatus::Class::Abstract::Filter\\)|perl\\(Monitoring::Livestatus::Class::Abstract::Stats\\)'
%endif

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Class for servicesbyhostgroup table
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Monitoring/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(Monitoring::Livestatus)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module is an object-oriented interface for Monitoring::Livestatus

*The module is still in an early stage of development, there can be some
api changes between releases.*

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 657796
- rebuild for updated spec-helper

* Sat Jan 01 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 627250
- import perl-Monitoring-Livestatus-Class

