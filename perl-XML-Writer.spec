#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Writer
Version  : 0.625
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/J/JO/JOSEPHW/XML-Writer-0.625.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JO/JOSEPHW/XML-Writer-0.625.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-writer-perl/libxml-writer-perl_0.625-1.debian.tar.xz
Summary  : Easily generate well-formed, namespace-aware XML.
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0 MIT
Requires: perl-XML-Writer-license
Requires: perl-XML-Writer-man

%description
XML::Writer is a simple Perl module for writing XML documents: it
takes care of constructing markup and escaping data correctly, and by
default, it also performs a significant amount of well-formedness
checking on the output, to make certain (for example) that start and
end tags match, that there is exactly one document element, and that
there are not duplicate attribute names.

%package license
Summary: license components for the perl-XML-Writer package.
Group: Default

%description license
license components for the perl-XML-Writer package.


%package man
Summary: man components for the perl-XML-Writer package.
Group: Default

%description man
man components for the perl-XML-Writer package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n XML-Writer-0.625
mkdir -p %{_topdir}/BUILD/XML-Writer-0.625/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/XML-Writer-0.625/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-XML-Writer
cp LICENSE %{buildroot}/usr/share/doc/perl-XML-Writer/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-XML-Writer/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/XML/Writer.pm

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-XML-Writer/LICENSE
/usr/share/doc/perl-XML-Writer/deblicense_copyright

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Writer.3
