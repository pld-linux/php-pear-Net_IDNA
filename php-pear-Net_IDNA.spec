%include	/usr/lib/rpm/macros.php
%define		_class		Net
%define		_subclass	IDNA
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - punycode encoding and decoding
Summary(pl):	%{_pearname} - kodowanie i dekodowanie punycode
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	620b036b46f76d1d0f409241688a1e11
URL:		http://pear.php.net/package/Net_IDNA/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package helps you to encode and decode punycode strings easily.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa u³atwia kodowanie i dekodowanie ci±gów znaków Unicode w
punycode.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/test
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
