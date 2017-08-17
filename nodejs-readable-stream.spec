# spec file for package nodejs-nodejs-readable-stream
%{?scl:%scl_package nodejs-nodejs-readable-stream}
%{!?scl:%global pkg_name %{name}}

%global npm_name readable-stream
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-readable-stream
Version:    2.1.4
Release:    2%{?dist}
Summary:	Streams3, a user-land copy of the stream library from iojs v2.x
Url:		https://github.com/nodejs/readable-stream#readme
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch
ExclusiveArch:	%{ix86} x86_64 %{arm}} noarch

BuildRequires:	%{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:	npm(tap)
BuildRequires:	npm(tape)
BuildRequires:	npm(zuul)
%endif

%description
Streams3, a user-land copy of the stream library from iojs v2.x

%prep
%setup -q -n package

%nodejs_fixdep inherits 2.0.0

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr lib/ package.json *.js \
	%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}
%check
%{nodejs_symlink_deps} --check
tap test/parallel/*.js
%endif

%files
%{nodejs_sitelib}/readable-stream

%doc README.md LICENSE

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.4-2
- rh-nodejs8 rebuild

* Thu Sep 15 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.1.4-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.2-6
- Use macro in -runtime dependency
- Rebuilt with updated metapackage

* Tue Sep 22 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.2-3
- Add lib/ to %%install

* Thu Aug 20 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.2-2
- Add %%nodejs_fixdep macro

* Thu Aug 13 2015 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.2-1
- Initial build
