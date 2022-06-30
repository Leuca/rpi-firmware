%define debug_package %{nil}
Name:           {{{ git_dir_name }}}
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Firmware files for the Raspberry Pi

License:        custom
URL:            https://github.com/raspberrypi/rpi-firmware

VCS:            {{{ git_dir_vcs }}}

Source:         https://github.com/raspberrypi/rpi-firmware/archive/refs/heads/master.zip

ExclusiveArch:  %{arm} aarch64

%description
Empty package for firmware files for the Raspberry Pi.

%package        rpi
Summary:        Firmware for older Raspberry Pi

%description    rpi
Firmware files needed to boot older versions of the Raspberry Pi

%package        rpi4
Summary:        Firmware for Raspberry Pi 4

%description    rpi4
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

# Empty package
%files

%files rpi
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

%files rpi4
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
{{{ git_dir_changelog }}}
