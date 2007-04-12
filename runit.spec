%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

Summary:	A UN*X init scheme with service supervision
Name:		runit
Version:	1.7.2
Release:	%mkrel 1
License:	BSD
Group:		System/Base
URL:		http://smarden.org/runit/
Source0:	http://smarden.org/runit/%{name}-%{version}.tar.bz2
BuildRequires:	dietlibc-devel >= 0.27-9mdk
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
runit is a daemontools alike replacement for SysV-init and other
init schemes. It currently runs on GNU/Linux, OpenBSD, FreeBSD,
and can easily be adapted to other Unix operating systems. runit
implements a simple three-stage concept. Stage 1 performs the
system's one-time initialization tasks. Stage 2 starts the
system's uptime services (via the runsvdir program). Stage 3
handles the tasks necessary to shutdown and halt or reboot. 

%prep

%setup -q -n admin

%build

pushd %{name}-%{version}/src
    echo "diet gcc -Os -pipe" > conf-cc
    echo "diet gcc -Os -static -s" > conf-ld
    make
popd
 
%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

install -d %{buildroot}/sbin/
install -d %{buildroot}%{_mandir}/man8

pushd %{name}-%{version}
    for i in `cat package/commands`; do
	install -m0755 src/$i %{buildroot}/sbin/
    done
popd

install -m0644 %{name}-%{version}/man/*.8 %{buildroot}%{_mandir}/man8/

%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{name}-%{version}/package/CHANGES
%doc %{name}-%{version}/package/README
%doc %{name}-%{version}/package/THANKS
%doc %{name}-%{version}/doc/*.html
%doc %{name}-%{version}/etc/2
%doc %{name}-%{version}/etc/debian
%attr(0755,root,root) /sbin/chpst
%attr(0755,root,root) /sbin/runit
%attr(0755,root,root) /sbin/runit-init
%attr(0755,root,root) /sbin/runsv
%attr(0755,root,root) /sbin/runsvchdir
%attr(0755,root,root) /sbin/runsvdir
%attr(0755,root,root) /sbin/sv
%attr(0755,root,root) /sbin/svlogd
%attr(0755,root,root) /sbin/utmpset
%attr(0644,root,root) %{_mandir}/man8/chpst.8*
%attr(0644,root,root) %{_mandir}/man8/runit-init.8*
%attr(0644,root,root) %{_mandir}/man8/runit.8*
%attr(0644,root,root) %{_mandir}/man8/runsv.8*
%attr(0644,root,root) %{_mandir}/man8/runsvchdir.8*
%attr(0644,root,root) %{_mandir}/man8/runsvdir.8*
%attr(0644,root,root) %{_mandir}/man8/sv.8*
%attr(0644,root,root) %{_mandir}/man8/svlogd.8*
%attr(0644,root,root) %{_mandir}/man8/utmpset.8*


