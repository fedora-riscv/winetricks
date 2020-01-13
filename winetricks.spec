# Uncomment these, set snapshot to 0.
%global snapshot 0
%global commit0  43314ed7895396bfd625824d88b5e19c25f46cac

Name:           winetricks
Version:        20191224
Release:        1%{?dist}

Summary:        Work around common problems in Wine

License:        LGPLv2+
URL:            https://github.com/Winetricks/%{name}
%if 0%{?snapshot}
Source0:        %{url}/archive/%{commit0}.tar.gz#/%{name}-%{commit0}.tar.gz
%else
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildArch:      noarch

# need arch-specific wine, not available everywhere:
# - adopted from wine.spec
ExclusiveArch:  %{ix86} x86_64 %{arm} aarch64
# - explicitly not ppc64* to hopefully not confuse koschei
ExcludeArch:    ppc64 ppc64le

BuildRequires:  wine-common
BuildRequires:  desktop-file-utils

Requires:       wine-common
Requires:       cabextract gzip unzip wget which
Requires:       hicolor-icon-theme
Requires:       (kdialog if kdialog else zenity)

%description
Winetricks is an easy way to work around common problems in Wine.

It has a menu of supported games/apps for which it can do all the
workarounds automatically. It also lets you install missing DLLs
or tweak various Wine settings individually.


%prep
%if 0%{?snapshot}
%setup -qn%{name}-%{commit0}
%else
%setup -q
%endif

sed -i -e s:steam:: -e s:flash:: tests/*

%build
# not needed

%install
%make_install
# some tarballs do not install appdata
install -m0644 -D -t %{buildroot}%{_datadir}/metainfo src/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%files
%license COPYING debian/copyright
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml


%changelog
* Mon Jan 13 2020 - Ernestas Kulik <ekulik@redhat.com> - 20191224-1
- Build 20191224
