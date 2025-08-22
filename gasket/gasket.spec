%global debug_package %{nil}

%global commit 5815ee3908a46a415aac616ac7b9aedcb98a504c
%global shortcommit %(commit=%{commit}; echo ${commit:0:7})
%global archive gasket-driver-%{commit}

Name:           gasket
Summary:        Driver for Google Coral ("Apex") Edge TPUs
Version:        0
Release:        1.git%{shortcommit}%{?dist}
License:        GPL-2.0
URL:            https://github.com/google/gasket-driver
Source0:        https://github.com/google/gasket-driver/archive/%{commit}/gasket-driver-%{shortcommit}.tar.gz
Source1:        gasket.modules
Source2:        gasket.rules
Source3:        gasket.sysusers

BuildArch:      noarch
Provides:       %{name}-kmod-common = %{version}
Requires:       %{name}-kmod >= %{version}

Requires(pre):  shadow-utils

%description
Driver for Google Coral ("Apex") Edge TPUs.

%prep
%setup -q -c -T -a 0

%install
install -Dpm 0644 %{S:1} %{buildroot}%{_sysconfdir}/modules-load.d/gasket.conf
install -Dpm 0644 %{S:2} %{buildroot}%{_sysconfdir}/udev/rules.d/65-gasket.rules
install -Dpm 0644 %{S:3} %{buildroot}%{_sysusersdir}/gasket.conf

%files
%config(noreplace) %{_sysconfdir}/modules-load.d/gasket.conf
%config(noreplace) %{_sysconfdir}/udev/rules.d/65-gasket.rules
%doc %{archive}/CONTRIBUTING.md
%doc %{archive}/README.md
%license %{archive}/LICENSE
%{_sysusersdir}/gasket.conf

%changelog
%autochangelog
