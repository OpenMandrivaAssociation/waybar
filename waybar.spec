Summary:	Customizable Wayland bar for Sway and Wlroots based compositors
Name:		waybar
Version:	0.9.5
Release:	1
License:	MIT
URL:		https://github.com/Alexays/Waybar
Source0:	https://github.com/Alexays/Waybar/archive/%{version}.tar.gz
BuildRequires:	pkgconfig(fmt)
BuildRequires:	pkgconfig(gtk-layer-shell-0)
BuildRequires:	pkgconfig(gdkmm-3.0)
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	stdc++-static-devel
BuildRequires:	pkgconfig(udev)
BuildRequires:	meson
BuildRequires:	spdlog-devel
# optional: man pages
BuildRequires:	scdoc
# optional: tray module
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
# optional: network
BuildRequires:	pkgconfig(libnl-3.0)
# optional: audio
BuildRequires:	pkgconfig(libpulse)
# optional: mpd module
BuildRequires:	pkgconfig(libmpdclient)
# optional: sway integration
Recommends:	sway

%description
Customizable Wayland bar for Sway and Wlroots based compositors.

%prep
%autosetup -n Waybar-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%{_sysconfdir}/xdg/waybar/
%{_bindir}/waybar
%{_mandir}/man?/%{name}*
%{_userunitdir}/waybar.service
