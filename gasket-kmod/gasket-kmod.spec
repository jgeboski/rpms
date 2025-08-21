%define buildforkernels current
%define repo rpmfusion
%global debug_package %{nil}

%global commit 5815ee3908a46a415aac616ac7b9aedcb98a504c
%global shortcommit %(commit=%{commit}; echo ${commit:0:7})
%global archive gasket-driver-%{commit}

Name:           gasket-kmod
Summary:        Kernel module (kmod) for gasket
Version:        0
Release:        1.git%{shortcommit}%{?dist}
License:        GPL-2.0
URL:            https://github.com/google/gasket-driver
Source0:        https://github.com/google/gasket-driver/archive/%{commit}/gasket-driver-%{shortcommit}.tar.gz
Patch0:         gasket-kmod-kernel-6.13.patch

BuildRequires:  %{_bindir}/kmodtool

%{!?kernels:BuildRequires: buildsys-build-rpmfusion-kerneldevpkgs-%{?buildforkernels:%{buildforkernels}}%{!?buildforkernels:current}-%{_target_cpu} }

%{expand:%(kmodtool --target %{_target_cpu} --repo %{repo} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null) }

%description
Driver for Google Coral ("Apex") Edge TPUs.

%prep
%{?kmodtool_check}

kmodtool  --target %{_target_cpu}  --repo %{repo} --kmodname %{name} %{?buildforkernels:--%{buildforkernels}} %{?kernels:--for-kernels "%{?kernels}"} 2>/dev/null

%setup -q -c -T -a 0

(cd %{archive}
%patch 0 -p1
)

for kernel_version in %{?kernel_versions} ; do
  cp -a %{archive}/src _kmod_build_${kernel_version%%___*}
done

%build
for kernel_version in %{?kernel_versions}; do
    make %{?_smp_mflags} -C ${kernel_version##*___} M=${PWD}/_kmod_build_${kernel_version%%___*} modules
done

%install
for kernel_version in %{?kernel_versions}; do
    make -C ${kernel_version##*___} \
        M=${PWD}/_kmod_build_${kernel_version%%___*} \
        INSTALL_MOD_PATH=%{buildroot}/%{kmodinstdir_prefix}/${kernel_version%%___*}/%{kmodinstdir_postfix} \
        modules_install
done

%{?akmod_install}

%changelog
%autochangelog
