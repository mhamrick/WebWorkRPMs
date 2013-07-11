%define pgdir /opt/webwork/pg
Name:           PG 
Version:        2.5
Release:        1%{?dist}
Summary:        Installs Webwork

#Group:          
License:        Webwork
URL:            http://webwork.maa.org
Source0:        pg.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Provides: perl(PGcore),perl(PGrandom)
#BuildRequires:  
#Requires: 


%description
WEbwork Attempted RPM

%prep
%setup -q -n pg-%{version}


%build


%install
#rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
#untar $RPM_BUILD_ROOT/webwork2-rel-2-4-9-1.tar.gz
rm -rf %{buildroot}
install -d %{buildroot}%{pgdir}
cp -pr * %{buildroot}%{pgdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%pgdir


%changelog
