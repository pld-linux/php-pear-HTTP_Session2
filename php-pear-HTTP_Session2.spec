%define		_status		beta
%define		_pearname	HTTP_Session2
Summary:	%{_pearname} - PHP5 Session Handler
Summary(pl.UTF-8):	%{_pearname} - obsługa sesji w PHP5
Name:		php-pear-%{_pearname}
Version:	0.7.3
Release:	3
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	eb8e2d1aa651a927c3e0d96e8d8225ce
URL:		http://pear.php.net/package/HTTP_Session2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Suggests:	php-pear-DB
Suggests:	php-pear-MDB2
Obsoletes:	php-pear-HTTP_Session2-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(DB.*) pear(MDB2.*)

%description
PHP5 Object-oriented interface to the session_* family functions it
provides extra features such as database storage for session data
using DB package. Supported containers are Creole, PEAR::DB and
PEAR::MDB. It introduces new methods like isNew(), useCookies(),
setExpire(), setIdle(), isExpired(), isIdled() and others.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten zorientowany obiektowo interfejs PHP5 do rodziny funkcji session_*
udostępnia dodatkową funkcjonalność taką jak przechowywanie danych
sesji w bazie danych przy użyciu pakietu DB. Obsługiwane kontenery to
Creole, PEAR::DB oraz PEAR::MDB. Udostępnione są nowe metody takie jak
isNew(), useCookies(), setExpire(), setIdle(), isExpired(), isIdled()
i inne.

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
%doc install.log docs/HTTP_Session2/docs
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTTP/Session2
%{php_pear_dir}/HTTP/Session2.php
