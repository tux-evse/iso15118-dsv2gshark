Name:           dsv2gshark
Version:        1.3.0
Release:        1%{?dist}
License:        MIT
Summary:        Wireshark plugin for iso15118 EV/EVSE
Url:            https://github.com/dspace-group/dsV2Gshark
Source0:         %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(wireshark)

%define LUA_VER 5.1

%if 0%{?suse_version}
BuildRequires:  pkgconfig(lua%{LUA_VER})
%else
BuildRequires:  libstdc++-static
BuildRequires:  pkgconfig(lua-%{LUA_VER})
%endif

%description
This Wireshark plugin allows to analyze and decode packets between
electric vehicles (EV)  and charging stations (EVSE),
also known as V2G messages.

#---------------------------------------------
%prep
%autosetup -p 1

cd V2G_Libraries
chmod a+x ./build_all_linux.sh

#---------------------------------------------
%build

%if 0%{?suse_version}
export LUAFLAGS="-I$(pkg-config --variable=includedir lua%{LUA_VER})"
%else
export LUAFLAGS="-I$(pkg-config --variable=includedir lua-%{LUA_VER})/lua-%{LUA_VER}"
%endif
cd V2G_Libraries
./build_all_linux.sh

#---------------------------------------------
%install

%if 0%{?suse_version}
LUA_CMOD=$(pkg-config --variable=INSTALL_CMOD lua%{LUA_VER})
%else
LUA_CMOD=%{_libdir}/lua/%{LUA_VER}
%endif

mkdir -p %{buildroot}%{_libdir}/wireshark/plugins/
mkdir -p %{buildroot}${LUA_CMOD}
cp Wireshark/plugins/*                    %{buildroot}%{_libdir}/wireshark/plugins/
cp ./V2G_Libraries/v2gLib/bin/*           %{buildroot}${LUA_CMOD}

#---------------------------------------------
%files
%defattr(-,root,root)
%dir %{_libdir}/wireshark/plugins/
%{_libdir}/wireshark/plugins/*
%{_libdir}/lua/%{LUA_VER}/*
#---------------------------------------------
%changelog
