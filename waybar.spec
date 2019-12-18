Name:           waybar
Version:        0.8.0
Release:        4
Summary:        Customizable Wayland bar for Sway and Wlroots based compositors
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/Alexays/Waybar
Source0:         https://github.com/Alexays/Waybar/archive/%{version}.tar.gz
Source1:	waybar.config
Source2:	style.css
BuildRequires:  cmake
BuildRequires:  fmt-devel
BuildRequires:  pkgconfig(gdkmm-3.0)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  stdc++-static-devel
BuildRequires:  pkgconfig(udev)
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  spdlog-devel
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
%setup -q -n Waybar-%{version}

%build
%meson
%meson_build

%install
%meson_install

install -m0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/waybar/config
install -m0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/xdg/waybar/style.css

%files
%{_sysconfdir}/xdg/waybar/
%{_bindir}/waybar
%{_mandir}/man?/%{name}*
%{_userunitdir}/waybar.service
