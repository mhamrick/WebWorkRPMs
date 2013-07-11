%define wwdir /opt/webwork/webwork2
Name:           Webwork 
Version:        2.5
Release:        1%{?dist}
Summary:        Installs Webwork

#Group:          
License:        Webwork
URL:            http://webwork.maa.org
Source0:        webwork2.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:	noarch

Provides: perl(tools.pl),perl(WeBWorK::PG::IO),perl(WeBWorK::PG::ImageGenerator),perl(WeBWorK::PG::Translator),perl(webwork_xmlrpc_inc.pl),perl(Value::WeBWorK),perl(Value::AnswerChecker),perl(WWSafe),perl(WeBWorK::Constants),perl(Apache::Request),perl(mod_perl),perl(the)

#BuildRequires:  perl(the)
#Requires: mod-perl, dvipng,gcc,libapreq2,make,mod_perl,mysql-server,perl-CPAN,perl-DateTime,perl-Email-Address,perl-GD,perl-GDGraph,perl-LDAP,perl-libapreq2,perl-Locale-Maketext-Lexicon,perl-Mail-Sender,perl-PHP-Serialization,perl-PadWalker,perl-SOAP-Lite,perl-SQL-Abstract,perl-String-ShellQuote,perl-Tie-IxHash,perl-TimeDate,subversion,system-config-services,tex-preview,uuid-perl


%description
WEbwork Attempted RPM

%prep
%setup -q -n Webwork-%{version}
%build


%install
#rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT
#untar $RPM_BUILD_ROOT/webwork2-rel-2-4-9-1.tar.gz
rm -rf %{buildroot}
install -d %{buildroot}%{wwdir}
cp -pr * %{buildroot}%{wwdir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%wwdir


%changelog
