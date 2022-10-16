%define debug_package %{nil}

%global commit 516eaa0627854aa073859d4041c49eef786c2e27
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20221014
%global gitrel .%{commit_date}.git%{shortcommit}

%global installdir /boot/efi

Name:           rpi-firmware
Version:        0
Release:        2%{?gitrel}%{?dist}
Summary:        Firmware for legacy Raspberry Pi(s)
BuildArch:      noarch

License:        custom
URL:            https://github.com/raspberrypi/rpi-firmware

Source:         https://github.com/raspberrypi/rpi-firmware/archive/%{commit}/copr.zip

%description
Firmware files needed to boot older versions of the Raspberry Pi

%package        -n rpi4-firmware
Summary:        Firmware for Raspberry Pi 4

%description    -n rpi4-firmware
Firmware files needed to boot the Raspberry Pi 4

%package        -n rpi4-dtbs
Summary:        Device Tree binaries for Raspberry Pi 4 hardware
Requires:       rpi-dtbs-common%{_isa} = %{version}-%{release}

%description    -n rpi4-dtbs
Upstream Device Tree Binaries for Raspberry Pi 4 model B, CM4, CM4S, 400

%package        -n rpi3-dtbs
Summary:        Device Tree binaries for Raspberry Pi 3 hardware
Requires:       rpi-dtbs-common%{_isa} = %{version}-%{release}

%description    -n rpi3-dtbs
Upstream Device Tree Binaries for Raspberry Pi 3 model B, B+, CM3

%package        -n rpi2-dtbs
Summary:        Device Tree binaries for Raspberry Pi 2 hardware
Requires:       rpi-dtbs-common%{_isa} = %{version}-%{release}

%description    -n rpi2-dtbs
Upstream Device Tree Binaries for Raspberry Pi 2 model B, CM2

%package        -n rpi1-dtbs
Summary:        Device Tree binaries for the original Raspberry Pi hardware
Requires:       rpi-dtbs-common%{_isa} = %{version}-%{release}

%description    -n rpi1-dtbs
Upstream Device Tree Binaries for the original Raspberry Pi model B, B+, CM

%package        -n rpi0-dtbs
Summary:        Device Tree binaries for Raspberry Pi Zero hardware
Requires:       rpi-dtbs-common%{_isa} = %{version}-%{release}

%description    -n rpi0-dtbs
Upstream Device Tree Binaries for Raspberry Pi Zero (W)

%package        -n rpi02-dtbs
Summary:        Device Tree binaries for Raspberry Pi Zero 2 hardware
Requires:       rpi-dtbs-common%{_isa} = %{version}-%{release}

%description    -n rpi02-dtbs
Upstream Device Tree Binaries for Raspberry Pi Zero 2 (W)

%package        -n rpi-dtbs-common
Summary:        Device Tree binariy object overlays

%description    -n rpi-dtbs-common
Upstream Device Tree Binary Overlays for additional devices

% prep
%setup -q -n rpi-firmware-%{commit}

%install
mkdir -p %{buildroot}%{installdir}/overlays
install -m 700 bootcode.bin %{buildroot}%{installdir}
install -m 700 fixup* %{buildroot}%{installdir}
install -m 700 start* %{buildroot}%{installdir}
install -m 700 bcm2* %{buildroot}%{installdir}
install -m 700 overlays/* %{buildroot}%{installdir}/overlays

%files
%license LICENCE.broadcom
%{installdir}/bootcode.bin
%{installdir}/fixup.dat
%{installdir}/fixup_cd.dat
%{installdir}/fixup_db.dat
%{installdir}/fixup_x.dat
%{installdir}/start.elf
%{installdir}/start_cd.elf
%{installdir}/start_db.elf
%{installdir}/start_x.elf

%files -n rpi4-firmware
%license LICENCE.broadcom
%{installdir}/fixup4.dat
%{installdir}/fixup4cd.dat
%{installdir}/fixup4db.dat
%{installdir}/fixup4x.dat
%{installdir}/start4.elf
%{installdir}/start4cd.elf
%{installdir}/start4db.elf
%{installdir}/start4x.elf

%files -n rpi4-dtbs
%{installdir}/bcm2711*

%files -n rpi3-dtbs
%{installdir}/bcm2710-rpi-cm3.dtb
%{installdir}/bcm2710-rpi-3-*

%files -n rpi2-dtbs
%{installdir}/bcm2709-rpi-*
%{installdir}/bcm2710-rpi-2-b.dtb

%files -n rpi1-dtbs
%{installdir}/bcm2708-rpi-cm.dtb
%{installdir}/bcm2708-rpi-b*

%files -n rpi0-dtbs
%{installdir}/bcm2708-rpi-zero*

%files -n rpi02-dtbs
%{installdir}/bcm2710-rpi-zero-2*

%files -n rpi-dtbs-common
%{installdir}/overlays

%changelog
* Sun Oct 16 2022 Luca Magrone <luca@magrone.cc> - 0-2.20221014.git516eaa0
- Package device tree binaries

* Sat Oct 15 2022 Luca Magrone <luca@magrone.cc> - 0-1.20221014.git516eaa0
- Change versioning scheme
- Update to 516eaa0

* Thu Jun 30 2022 Luca Magrone <luca@magrone.cc> - 5.15.41-0
- Initial package release
