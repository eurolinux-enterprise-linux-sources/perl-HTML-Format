Name:           perl-HTML-Format
Version:        2.10
Release:        7%{?dist}
Summary:        HTML formatter modules
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/HTML-Format/
Source0:        http://www.cpan.org/authors/id/N/NI/NIGELM/HTML-Format-%{version}.tar.gz
# Work-around testsuite failure
Patch0:         %{name}-%{version}.diff
Requires:  perl(:MODULE_COMPAT_%(eval "$(perl -V:version)"; echo $version))

BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(base)
BuildRequires:  perl(bytes)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Font::Metrics::Courier)
BuildRequires:  perl(Font::Metrics::CourierBold)
BuildRequires:  perl(Font::Metrics::CourierBoldOblique)
BuildRequires:  perl(Font::Metrics::CourierOblique)
BuildRequires:  perl(Font::Metrics::Helvetica)
BuildRequires:  perl(Font::Metrics::HelveticaBold)
BuildRequires:  perl(Font::Metrics::HelveticaBoldOblique)
BuildRequires:  perl(Font::Metrics::HelveticaOblique)
BuildRequires:  perl(Font::Metrics::TimesBold)
BuildRequires:  perl(Font::Metrics::TimesBoldItalic)
BuildRequires:  perl(Font::Metrics::TimesItalic)
BuildRequires:  perl(Font::Metrics::TimesRoman)
BuildRequires:  perl(HTML::Element) >= 3.15
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Build)
# for release-testing tests
%if 0%{?rhel} < 7
BuildRequires:  perl(Pod::Wordlist::hanekomu)
%endif
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::DistManifest)
BuildRequires:  perl(Test::EOL)
BuildRequires:  perl(Test::HasVersion)
BuildRequires:  perl(Test::MinimumVersion)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::NoTabs)
BuildRequires:  perl(Test::Pod) >= 1.41
BuildRequires:  perl(Test::Portability::Files)
%if 0%{?rhel} < 7
BuildRequires:  perl(Test::Spelling) > 0.12
%endif
BuildRequires:  perl(Test::Synopsis)
BuildRequires:  perl(Test::Vars)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# These must match
# %FontFamilies in lib/HTML/FormatPS.pm
Requires:       perl(Font::Metrics::Courier)
Requires:       perl(Font::Metrics::CourierBold)
Requires:       perl(Font::Metrics::CourierBoldOblique)
Requires:       perl(Font::Metrics::CourierOblique)
Requires:       perl(Font::Metrics::Helvetica)
Requires:       perl(Font::Metrics::HelveticaBold)
Requires:       perl(Font::Metrics::HelveticaBoldOblique)
Requires:       perl(Font::Metrics::HelveticaOblique)
Requires:       perl(Font::Metrics::TimesBold)
Requires:       perl(Font::Metrics::TimesBoldItalic)
Requires:       perl(Font::Metrics::TimesItalic)
Requires:       perl(Font::Metrics::TimesRoman)

%description
A collection of modules that formats HTML as plain text, PostScript or RTF.

# Build in a subdirectory, otherwise the testsuites fail
%prep
%setup -q -c -T -n %{name}-%{version}
%setup -q -T -D -n %{name}-%{version} -a0
cd HTML-Format-%{version}
%patch0 -p1
cd ..

%build
cd HTML-Format-%{version}
perl Build.PL installdirs=vendor
./Build
cd ..

%install
cd HTML-Format-%{version}
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
cd ..

%check
cd HTML-Format-%{version}
RELEASE_TESTING=1 ./Build test
cd ..

%files
%doc HTML-Format-%{version}/Changes HTML-Format-%{version}/README HTML-Format-%{version}/LICENSE
%{perl_vendorlib}/HTML
%{_mandir}/man3/HTML*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.10-7
- Mass rebuild 2013-12-27

* Tue Jul 23 2013 Petr Šabata <contyk@redhat.com> - 2.10-6.1
- Add some missing dependencies

* Thu Nov 08 2012 Petr Šabata <contyk@redhat.com> - 2.10-6
- Add a few missing deps to avoid possible FTBFS
- Whitespace cleanup

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Petr Pisar <ppisar@redhat.com> - 2.10-4
- Perl 5.16 rebuild

* Thu Jun  7 2012 Marcela Mašláňová <mmaslano@redhat.com> - 2.10-3
- conditionalize dependency on Pod::Wordlist::hanekomu 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.10-1
- Upstream update.
- Build in HTML-Format-%%{version} subdir.
- Add HTML-Format-2.10.diff.

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 2.09-2
- Perl mass rebuild

* Sun Jul 17 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.09-1
- Upstream update.

* Fri Apr 29 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.07-1
- Upstream update.
- Reflect upstream having switched to Build.PL.

* Thu Mar 03 2011 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.05-1
- Upstream update.
- Reflect Source0:-URL having changed.
- Rework spec-file.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 17 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.04-14
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 2.04-13
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.04-12
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.04-8
- Rebuild for perl 5.10 (again)

* Sun Jan 20 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.04-7
- rebuild for new perl

* Mon Sep 03 2007 Ralf Corsépius <rc040203@freenet.de> - 2.04-6
- Update license tag.
- BR: perl(ExtUtils::MakeMaker).

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 2.04-5
- Mass rebuild.

* Wed Mar 01 2006 Ralf Corsépius <rc040203@freenet.de> - 2.04-4
- Rebuild for perl-5.8.8.

* Wed Aug 31 2005 Ralf Corsepius <rc040203@freenet.de> - 2.04-3
- Improve summary.

* Fri Aug 26 2005 Ralf Corsepius <ralf@links2linux.de> - 2.04-2
- Add Requires: perl(Font::Metrics:*).
- Minor Spec cleanup.

* Thu Aug 18 2005 Ralf Corsepius <ralf@links2linux.de> - 2.04-1
- FE submission.
