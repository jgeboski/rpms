# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://golift.io/cnfg
%global goipath         golift.io/cnfg
%global forgeurl        https://github.com/golift/cnfg
Version:                0.2.3

%gometa -f

%global common_description %{expand:
Procedures for parsing configs files and environment variables.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Procedures for parsing configs files and environment variables

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
