Name:           {{{ git_dir_name }}}
Version:        {{{ git_dir_version }}}
Release:        2
Summary:        Firmware files for the Raspberry Pi

License:        custom
URL:            https://github.com/raspberrypi/rpi-firmware

VCS:            {{{ git_dir_vcs }}}

Source:         https://github.com/raspberrypi/rpi-firmware/archive/refs/heads/master.zip

ExclusiveArch:  %{arm} aarch64

%description
Firmware files for the Raspberry Pi.

%prep
%setup -q

%install
mkdir -p %{buildroot}/boot
install -m 700 bootcode.bin %{buildroot}/boot
install -m 700 fixup.dat %{buildroot}/boot
install -m 700 fixup4.dat %{buildroot}/boot
install -m 700 fixup4cd.dat %{buildroot}/boot
install -m 700 fixup4db.dat %{buildroot}/boot
install -m 700 fixup4x.dat %{buildroot}/boot
install -m 700 fixup_cd.dat %{buildroot}/boot
install -m 700 fixup_db.dat %{buildroot}/boot
install -m 700 fixup_x.dat %{buildroot}/boot
install -m 700 start.elf %{buildroot}/boot
install -m 700 start4.elf %{buildroot}/boot
install -m 700 start4cd.elf %{buildroot}/boot
install -m 700 start4db.elf %{buildroot}/boot
install -m 700 start4x.elf %{buildroot}/boot
install -m 700 start_cd.elf %{buildroot}/boot
install -m 700 start_db.elf %{buildroot}/boot
install -m 700 start_x.elf %{buildroot}/boot

%files
%license LICENCE.broadcom
/boot/bootcode.bin
/boot/fixup.dat
/boot/fixup4.dat
/boot/fixup4cd.dat
/boot/fixup4db.dat
/boot/fixup4x.dat
/boot/fixup_cd.dat
/boot/fixup_db.dat
/boot/fixup_x.dat
/boot/start.elf
/boot/start4.elf
/boot/start4cd.elf
/boot/start4db.elf
/boot/start4x.elf
/boot/start_cd.elf
/boot/start_db.elf
/boot/start_x.elf


%changelog
{{{ git_dir_changelog }}}
