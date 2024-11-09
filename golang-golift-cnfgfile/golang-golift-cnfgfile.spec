# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://golift.io/cnfgfile
%global goipath         golift.io/cnfgfile
%global forgeurl        https://github.com/golift/cnfgfile
%global commit          a5436d84eb481ffa82fbe72fa37b5ec4b27df370

%gometa -f

%global common_description %{expand:
Abstracted configuration file loading for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Abstracted configuration file loading for Go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

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
