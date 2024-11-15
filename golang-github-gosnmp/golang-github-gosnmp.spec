# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/gosnmp/gosnmp
%global goipath         github.com/gosnmp/gosnmp
Version:                1.38.0

%gometa -f

%global common_description An SNMP library written in Go.

%global golicenses      LICENSE
%global godocs          AUTHORS.md CHANGELOG.md README.md RELEASE.md trap.md

Name:           %{goname}
Release:        %autorelease
Summary:        An SNMP library written in Go

License:        BSD
URL:            %{gourl}
Source:         %{gosource}

%description
%{common_description}

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
