%define tarname Waybar

Name:           waybar
Version:	0.9.3
Release:	1
Summary:        Customizable Wayland bar for Sway and Wlroots based compositors
License:        MIT
URL:            https://github.com/Alexays/Waybar
Source0:        https://github.com/Alexays/Waybar/archive/%{version}/%{tarname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  cmake(date)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gdkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  stdc++-static-devel
BuildRequires:  pkgconfig(udev)
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig(spdlog)
# optional: man pages
BuildRequires:  scdoc
# optional: tray module
BuildRequires:  libdbusmenu-gtk-devel
# optional: network
BuildRequires:  libnl3-devel
# optional: audio
BuildRequires:  pkgconfig(libpulse)
# optional: mpd module
BuildRequires:  libmpdclient-devel
# optional: sway integration
Recommends:     sway

%description
Customizable Wayland bar for Sway and Wlroots based compositors.

%prep
%setup -q -n %{tarname}-%{version}

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
