Name: hello-rpm
Version: 0.1.0
Release: 1%{?dist}
Group: System Environment/Daemons
License: Internal BBC use only
Summary: Simple rpm
Source0: src.tar.gz

Requires: python3

%description
%{name}

%prep
# this will change into the src directory, which is where all of our stuff is
# packaged in src.tar.gz
%setup -q -n src/

%build
# Any compile step goes here if needed

%install
# Create the required directories in the buildroot
mkdir -p %{buildroot}/usr/lib/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}
mkdir -p %{buildroot}/usr/bin

# Put the files from our build directory into the buildroot locations
cp -r hello %{buildroot}/usr/bin/
cp -r hello.py %{buildroot}/usr/lib/%{name}/
cp -r hello.conf %{buildroot}%{_sysconfdir}/%{name}

%pre
# Anything you want to run as a pre-install step

%post
# Anything you want to run as a post-install step

%preun
# Anything you want to run as a pre-uninstall step

%postun
# Anything you want to run as a post-uninstall step

%files
%defattr(0755, root, root, 0755)
/usr/bin/*
%defattr(-, root, root, 0755)
/etc/%{name}
%defattr(0644, root, root, 0755)
/usr/lib/%{name}
