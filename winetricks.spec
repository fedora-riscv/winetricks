Name:           winetricks
Version:        20170517
Release:        1%{?dist}
Summary:        Work around common problems in Wine

License:        LGPLv2+
URL:            https://github.com/Winetricks/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

# need arch-specific wine, not available everywhere:
# - adopted from wine.spec
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
# - explicitly not ppc64* to hopefully not confuse koschei
ExcludeArch:    ppc64 ppc64le

# Error: nothing provides libLLVM-4.0.so needed by mesa-libOSMesa-17.1.1-2.fc26.i686
#BuildRequires:  wine-common
BuildRequires:  desktop-file-utils

# runtime dependencies
Requires:       wine-common
Requires:       cabextract gzip unzip wget which time
Requires:       hicolor-icon-theme

%description
Winetricks is an easy way to work around common problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also lets you install missing DLLs
or tweak various Wine settings individually.


%prep
%setup -q
sed -i -e s:steam:: -e s:flash:: tests/*

%build
# not needed

%install
%make_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :



%files
%license COPYING debian/copyright
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop


%changelog
* Sat Jun 10 2017 Builder <projects.rg@smart.ms> - 20170517-1
- new version
- drop 'BR: wine-common' as mesa dependencies seem to be instable

* Tue Mar 28 2017 Raphael Groner <projects.rg@smart.ms> - 20170326-1
- new version

* Sat Feb 11 2017 Raphael Groner <projects.rg@smart.ms> - 20170207-1
- new version
- drop additional icon and desktop file in favor of upstream ones

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20161107-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 05 2016 Builder <projects.rg@smart.ms> - 20161107-2
- add ExcludeArch

* Wed Nov 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161107-1
- new version

* Mon Nov 07 2016 Raphael Groner <projects.rg@smart.ms> - 20161012-1
- new version
- disable architectures without available wine
- don't check explicitly for wine version

* Sun Oct 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161005-2
- use apps subfolder for icon

* Sun Oct 09 2016 Raphael Groner <projects.rg@smart.ms> - 20161005-1
- new version
- add copyright
- add icon

* Fri Jul 29 2016 Raphael Groner <projects.rg@smart.ms> - 20160724-1
- new version

* Mon Jul 11 2016 Raphael Groner <projects.rg@smart.ms> - 20160709-1
- initial
