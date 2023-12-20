%global uuid pano@elhan.io

Name:        gnome-shell-extension-pano
# renovate: datasource=git-refs depName=oae/gnome-shell-pano packageName=https://github.com/oae/gnome-shell-pano branch=master
Version:     2361af0ba76b2b9c20853636fd3c1329bc6f140d
Release:     1%{?dist}
Summary:     Next-gen Clipboard Manager for Gnome Shell 

Group:       User Interface/Desktops
License:     GPLv2
URL:         https://github.com/oae/gnome-shell-pano
Source0:     %{url}/archive/refs/heads/master.tar.gz
BuildArch:   noarch

Requires:    gnome-shell >= 3.12
Requires:    libgda
Requires:    libgda-sqlite

BuildRequires: cogl-devel
BuildRequires: gsound-devel
BuildRequires: libgda-devel
BuildRequires: yarn

%description
Next-gen Clipboard Manager for Gnome Shell 

%prep
%autosetup -n gnome-shell-extension-pano-master

%build
yarn install
yarn build

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
cp -r dist/* %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%doc README.md
%license LICENSE
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
