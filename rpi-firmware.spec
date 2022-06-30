%define debug_package %{nil}
Name:           rpi-firmware
Version:        5.15.41
Release:        0%{?dist}
Summary:        Firmware for older Raspberry Pi

License:        custom
URL:            https://github.com/raspberrypi/rpi-firmware

Source:         https://github.com/Leuca/rpi-firmware/archive/refs/heads/copr.zip

ExclusiveArch:  %{arm} aarch64

%description
Firmware files needed to boot older versions of the Raspberry Pi

%package        -n rpi4-firmware
Summary:        Firmware for Raspberry Pi 4

%description    -n rpi4-firmware
Firmware files needed to boot the Raspberry Pi 4

%prep
%setup -q

%install
mkdir -p %{buildroot}/boot/efi
install -m 700 bootcode.bin %{buildroot}/boot/efi
install -m 700 fixup.dat %{buildroot}/boot/efi
install -m 700 fixup4.dat %{buildroot}/boot/efi
install -m 700 fixup4cd.dat %{buildroot}/boot/efi
install -m 700 fixup4db.dat %{buildroot}/boot/efi
install -m 700 fixup4x.dat %{buildroot}/boot/efi
install -m 700 fixup_cd.dat %{buildroot}/boot/efi
install -m 700 fixup_db.dat %{buildroot}/boot/efi
install -m 700 fixup_x.dat %{buildroot}/boot/efi
install -m 700 start.elf %{buildroot}/boot/efi
install -m 700 start4.elf %{buildroot}/boot/efi
install -m 700 start4cd.elf %{buildroot}/boot/efi
install -m 700 start4db.elf %{buildroot}/boot/efi
install -m 700 start4x.elf %{buildroot}/boot/efi
install -m 700 start_cd.elf %{buildroot}/boot/efi
install -m 700 start_db.elf %{buildroot}/boot/efi
install -m 700 start_x.elf %{buildroot}/boot/efi

%files
%license LICENCE.broadcom
/boot/efi/bootcode.bin
/boot/efi/fixup.dat
/boot/efi/fixup_cd.dat
/boot/efi/fixup_db.dat
/boot/efi/fixup_x.dat
/boot/efi/start.elf
/boot/efi/start_cd.elf
/boot/efi/start_db.elf
/boot/efi/start_x.elf

%files -n rpi4-firmware
%license LICENCE.broadcom
/boot/efi/fixup4.dat
/boot/efi/fixup4cd.dat
/boot/efi/fixup4db.dat
/boot/efi/fixup4x.dat
/boot/efi/start4.elf
/boot/efi/start4cd.elf
/boot/efi/start4db.elf
/boot/efi/start4x.elf

%changelog
* Thu Jun 30 2022 Luca Magrone <luca.magrone@me.com>
- Initial package release
