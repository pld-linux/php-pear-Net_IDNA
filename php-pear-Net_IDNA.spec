%define		_status		beta
%define		_pearname	Net_IDNA
Summary:	%{_pearname} - punycode encoding and decoding
Summary(pl.UTF-8):	%{_pearname} - kodowanie i dekodowanie punycode
Name:		php-pear-%{_pearname}
Version:	0.8.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	e436adb07e62375da7891e592a11a037
URL:		http://pear.php.net/package/Net_IDNA/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3.0
Requires:	php-pear
Obsoletes:	php-pear-Net_IDNA-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package helps you to encode and decode punycode strings easily.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa ułatwia kodowanie i dekodowanie ciągów znaków Unicode w
punycode.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Net/*.php
