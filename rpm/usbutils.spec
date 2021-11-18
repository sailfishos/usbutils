Name:       usbutils
Summary:    Linux USB utilities
Version:    014
Release:    1
License:    GPLv2+
URL:        http://www.linux-usb.org/
Source0:    %{name}-%{version}.tar.xz
Requires:   hwdata
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev) >= 196
BuildRequires:  autoconf
BuildRequires:  libtool

%description
This package contains utilities for inspecting devices connected to a
USB bus.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
./autogen.sh
%configure --disable-static \
    --sbindir=%{_sbindir} \
    --datadir=%{_datadir}/hwdata

%make_build

%install
%make_install

%files
%defattr(-,root,root,-)
%license LICENSES/GPL-2.0-only.txt
%{_bindir}/*
%exclude %{_mandir}/*/*
