Name: usbutils
Version: 0.86
Release: 2
Source:	http://downloads.sourceforge.net/linux-usb/%{name}-%{version}.tar.gz
URL: http://www.linux-usb.org/
License: GPLv2+
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires: hwdata
BuildRequires: autoconf, libtool, libusb-devel >= 0.1.8
Summary: Linux USB utilities
Group: Applications/System
Patch0: usbutils-0.86-hwdata.patch
Source101: usbutils-rpmlintrc

%description 
This package contains utilities for inspecting devices connected to a
USB bus.

%prep
%setup -q
%patch0 -p1
autoreconf

%build
%configure --sbindir=%{_sbindir}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

# usb.ids is shipped in hwdata; nuke and adjust .pc file
sed -i 's|usbids=/usr/share/usb.ids|usbids=/usr/share/hwdata/usb.ids|' $RPM_BUILD_ROOT%{_datadir}/pkgconfig/usbutils.pc

%files
%defattr(-,root,root,-)
%{_mandir}/*/*
%{_sbindir}/*
%{_bindir}/*
%{_datadir}/pkgconfig/usbutils.pc
%doc AUTHORS COPYING ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT
