Name:           fdm
Version:        6.33.2
Release:        1%{?dist}
Summary:        Free Download Manager

License:        Freeware
URL:            https://www.freedownloadmanager.org/

Source0:        https://github.com/putraapj/komodo/releases/download/fdmcopr/fdm_6.33.2_amd64.deb

BuildArch:      x86_64
ExclusiveArch:  x86_64

Requires:       libX11
Requires:       libXext
Requires:       libXrender
Requires:       libXtst
Requires:       libXScrnSaver
Requires:       gtk3
Requires:       nss
Requires:       alsa-lib
BuildRequires: binutils
BuildRequires: xz
BuildRequires: zstd

%description
Free Download Manager is a download accelerator and organizer.

%prep
mkdir -p build
cd build

ar x %{SOURCE0}

if [ -f data.tar.xz ]; then
    tar xf data.tar.xz
elif [ -f data.tar.gz ]; then
    tar xf data.tar.gz
elif [ -f data.tar.zst ]; then
    tar --use-compress-program=unzstd -xf data.tar.zst
fi

%install
rm -rf %{buildroot}

cp -a build/usr %{buildroot}/ || true
cp -a build/opt %{buildroot}/ || true

%files
/opt/*
/usr/*

%changelog
* Mon May 04 2026 Putra Junitri - 6.33.2-1
- Initial COPR package
