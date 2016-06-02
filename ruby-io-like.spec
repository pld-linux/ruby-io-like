%define	pkgname	io-like
Summary:	A module which provides the functionality of an IO object to any class which provides a couple of simple methods
Name:		ruby-%{pkgname}
Version:	0.3.0
Release:	1
License:	GPL v2+ or Ruby
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	7a16ea4dfd897a9af9855d19416f3e4a
URL:		http://io-like.rubyforge.org/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IO::Like module provides the methods of an IO object based upon on
a few simple methods provided by the including class: unbuffered_read,
unbuffered_write, and unbuffered_seek.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{ruby_vendorlibdir}/io
%{ruby_vendorlibdir}/io/like.rb
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
