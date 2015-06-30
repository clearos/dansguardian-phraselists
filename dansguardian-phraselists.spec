Name: dansguardian-phraselists
Version: 2.9
Release: 3%{dist}
License: GPL
Group: Application/Misc
Packager: ClearFoundation
Requires: /sbin/service
Source: dansguardian-phraselists-%{version}.tar.gz
Patch1: dansguardian-phraselists-2.9-japanesep.patch
Patch2: dansguardian-phraselists-2.9-fark.patch
BuildArch: noarch
BuildRoot: /var/tmp/%{name}-%{version}
Summary: Content filter phrase lists

%description
Dansguardian content filter phrase lists.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%build

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

mkdir -p -m 755 $RPM_BUILD_ROOT/etc/dansguardian-av/lists/phraselists
cp -r phraselists $RPM_BUILD_ROOT/etc/dansguardian-av/lists/

%pre
if [ -L /etc/dansguardian-av/lists/phraselists ]; then
	rm /etc/dansguardian-av/lists/phraselists
fi

%postun
if [ "$1" -ge "1" ]; then
	CHECK=`/sbin/pidof dansguardian-av`
	if [ ! -z "$CHECK" ]; then
		service dansguardian-av restart >/dev/null 2>&1
	fi
fi

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root) /etc/dansguardian-av/lists/phraselists
%changelog
* Mon Nov 25 2013 ClearFoundation <developer@clearfoundation.com> - 2.9-3.clear
- Tweaked Malay phrase list [tracker #1339]

* Tue May 28 2013 ClearFoundation <developer@clearfoundation.com> - 2.9-2.clear
- Tweaked Japanese phrase list [tracker #1164]
