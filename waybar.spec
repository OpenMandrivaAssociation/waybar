%define tarname Waybar
Name:           waybar
Version:	0.11.0
Release:	2
Group:          Graphical desktop/Other
Summary:        Customizable Wayland bar for Sway and Wlroots based compositors
License:        MIT
URL:            https://github.com/Alexays/Waybar
Source0:        https://github.com/Alexays/Waybar/archive/%{version}/%{tarname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  sndio-devel
BuildRequires:  cmake(date)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gdkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(jack)
BuildRequires:  stdc++-static-devel
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wireplumber-0.5)
BuildRequires:  pkgconfig(spdlog)
BuildRequires:  pkgconfig(xkbregistry)

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

BuildSystem:	meson
BuildOption:	-Dtests=disabled
BuildOption:	-Dmpris=disabled
BuildOption:	-Dcava=disabled

%patchlist
#https://github.com/Alexays/Waybar/commit/7725f6ed5aca20eff825666937e76ae80ab7ea7d.patch
#waybar-0.10.3-fmt11.patch


%description
Customizable Wayland bar for Sway and Wlroots based compositors.

%files
%{_sysconfdir}/xdg/waybar/
%{_bindir}/waybar
%{_mandir}/man?/%{name}*
%{_userunitdir}/waybar.service
