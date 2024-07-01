#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Writer
Version  : 0.900
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/J/JO/JOSEPHW/XML-Writer-0.900.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JO/JOSEPHW/XML-Writer-0.900.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-writer-perl/libxml-writer-perl_0.625-1.debian.tar.xz
Summary  : Easily generate well-formed, namespace-aware XML.
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0 MIT
Requires: perl-XML-Writer-license = %{version}-%{release}
Requires: perl-XML-Writer-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
XML::Writer is a simple Perl module for writing XML documents: it
takes care of constructing markup and escaping data correctly, and by
default, it also performs a significant amount of well-formedness
checking on the output, to make certain (for example) that start and
end tags match, that there is exactly one document element, and that
there are not duplicate attribute names.

%package dev
Summary: dev components for the perl-XML-Writer package.
Group: Development
Provides: perl-XML-Writer-devel = %{version}-%{release}
Requires: perl-XML-Writer = %{version}-%{release}

%description dev
dev components for the perl-XML-Writer package.


%package license
Summary: license components for the perl-XML-Writer package.
Group: Default

%description license
license components for the perl-XML-Writer package.


%package perl
Summary: perl components for the perl-XML-Writer package.
Group: Default
Requires: perl-XML-Writer = %{version}-%{release}

%description perl
perl components for the perl-XML-Writer package.


%prep
%setup -q -n XML-Writer-0.900
cd %{_builddir}
tar xf %{_sourcedir}/libxml-writer-perl_0.625-1.debian.tar.xz
cd %{_builddir}/XML-Writer-0.900
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/XML-Writer-0.900/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
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
mkdir -p %{buildroot}/usr/share/package-licenses/perl-XML-Writer
cp %{_builddir}/XML-Writer-0.900/LICENSE %{buildroot}/usr/share/package-licenses/perl-XML-Writer/0baf8d8f6dac79b5561f10f712a193017ea6951c
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-XML-Writer/450078e1b7634599c359700351c91571ea6569ea
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
/usr/share/man/man3/XML::Writer.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-XML-Writer/0baf8d8f6dac79b5561f10f712a193017ea6951c
/usr/share/package-licenses/perl-XML-Writer/450078e1b7634599c359700351c91571ea6569ea

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
