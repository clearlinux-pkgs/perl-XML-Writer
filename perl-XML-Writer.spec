#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-Writer
Version  : 0.625
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/J/JO/JOSEPHW/XML-Writer-0.625.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/J/JO/JOSEPHW/XML-Writer-0.625.tar.gz
Summary  : Easily generate well-formed, namespace-aware XML.
Group    : Development/Tools
License  : unrestricted
Requires: perl-XML-Writer-man

%description
XML::Writer is a simple Perl module for writing XML documents: it
takes care of constructing markup and escaping data correctly, and by
default, it also performs a significant amount of well-formedness
checking on the output, to make certain (for example) that start and
end tags match, that there is exactly one document element, and that
there are not duplicate attribute names.

%package man
Summary: man components for the perl-XML-Writer package.
Group: Default

%description man
man components for the perl-XML-Writer package.


%prep
%setup -q -n XML-Writer-0.625

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

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/XML::Writer.3
