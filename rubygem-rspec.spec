# Generated from rspec-1.1.3.gem by gem2rpm -*- rpm-spec -*-
%define ruby_sitelib %(ruby -rrbconfig -e "puts Config::CONFIG['sitelibdir']")
%define gemdir %(ruby -rubygems -e 'puts Gem::dir' 2>/dev/null)
%define gemname rspec
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Summary: Behaviour driven development (BDD) framework for Ruby
Name: rubygem-%{gemname}
Version: 1.2.7
Release: 1%{?dist}
Group: Development/Languages
License: GPLv2+ or Ruby
URL: http://rspec.rubyforge.org
Source0: http://gems.rubyforge.org/gems/%{gemname}-%{version}.gem
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: rubygems, ruby(abi)  = 1.8
BuildRequires: rubygems, ruby
BuildArch: noarch
Provides: rubygem(%{gemname}) = %{version}

%description
RSpec is a behaviour driven development (BDD) framework for Ruby.  RSpec was
created in response to Dave Astels' article _A New Look at Test Driven
Development_ which can be read at: http://daveastels.com/index.php?p=5  RSpec
is intended to provide the features discussed in Dave's article.


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --install-dir %{buildroot}%{gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{gemdir}/bin
find %{buildroot}%{geminstdir}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/*
%{gemdir}/gems/%{gemname}-%{version}/
%doc %{gemdir}/doc/%{gemname}-%{version}
#%doc %{geminstdir}/*.txt
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec


%changelog
* Mon Jun 22 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.7-1
- New Version

* Fri Mar 27 2009 Michael Stahnke <stahnma@fedoraproject.org> - 1.2.2-1
- New Version 

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 08 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.11-1
- New Version

* Mon Nov 03 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.8-3
- Updating to require ruby(abi)

* Mon Oct 13 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.8-1
- New version

* Wed May 14 2008 Michael Stahnke <stahnma@fedoraproject.org> - 1.1.3-1
- Initial package
