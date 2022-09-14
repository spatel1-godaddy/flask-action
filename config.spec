%define name flask_actions
%define version 0.0.22
%define unmangled_version 0.0.22
%define release 1

Summary: Flask Actions
Name: %{name}
Version: %{version}
Release: %{release}
License: NOLICENSE

%description


%prep

%build

%install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
