#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Sort-Versions
Version  : 1.62
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Sort-Versions-1.62.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Sort-Versions-1.62.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libs/libsort-versions-perl/libsort-versions-perl_1.62-1.debian.tar.xz
Summary  : 'a perl 5 module for sorting of revision-like numbers'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Sort-Versions-license = %{version}-%{release}
Requires: perl-Sort-Versions-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This archive contains the distribution Sort-Versions,
version 1.62:
a perl 5 module for sorting of revision-like numbers

%package dev
Summary: dev components for the perl-Sort-Versions package.
Group: Development
Provides: perl-Sort-Versions-devel = %{version}-%{release}
Requires: perl-Sort-Versions = %{version}-%{release}

%description dev
dev components for the perl-Sort-Versions package.


%package license
Summary: license components for the perl-Sort-Versions package.
Group: Default

%description license
license components for the perl-Sort-Versions package.


%package perl
Summary: perl components for the perl-Sort-Versions package.
Group: Default
Requires: perl-Sort-Versions = %{version}-%{release}

%description perl
perl components for the perl-Sort-Versions package.


%prep
%setup -q -n Sort-Versions-1.62
cd %{_builddir}
tar xf %{_sourcedir}/libsort-versions-perl_1.62-1.debian.tar.xz
cd %{_builddir}/Sort-Versions-1.62
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Sort-Versions-1.62/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Sort-Versions
cp %{_builddir}/Sort-Versions-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Sort-Versions/611bb7067cb4a6e6ff1c98d94d402c2704d3567c || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Sort::Versions.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Sort-Versions/611bb7067cb4a6e6ff1c98d94d402c2704d3567c

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
