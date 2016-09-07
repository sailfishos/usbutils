Name:       usbutils
Summary:    Linux USB utilities
Version:    008
Release:    1
Group:      Applications/System
License:    GPLv2+
URL:        http://www.linux-usb.org/
Source0:    %{name}-%{version}.tar.xz
Source1:    usbutils-rpmlintrc
Patch0:     usbutils-006-hwdata.patch
Patch1:     usbutils-make-hwdata.patch
Requires:   hwdata
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(udev) >= 196
BuildRequires:  autoconf
BuildRequires:  libtool

%description
This package contains utilities for inspecting devices connected to a
USB bus.

%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%setup -q -n %{name}-%{version}/%{name}

# usbutils-006-hwdata.patch
%patch0 -p1
# usbutils-make-hwdata.patch
%patch1 -p1

%build
./autogen.sh
%configure --disable-static \
    --sbindir=%{_sbindir} \
    --datadir=%{_datadir}/hwdata \
    --disable-usbids

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_datadir}/pkgconfig/usbutils.pc
%{_mandir}/*/*

