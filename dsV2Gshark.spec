Name:           dsV2Gshark
Version:        1.3.0
Release:        1%{?dist}
License:        MIT
Summary:        Wireshark plugin for EV/EVSE
Url:            https://github.com/dspace-group/dsV2Gshark
Source:         %{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-static
BuildRequires:  pkgconfig(wireshark)

%description
This Wireshark plugin allows to analyze and decode packets between
electric vehicles (EV)  and charging stations (EVSE),
also known as V2G messages.

#---------------------------------------------
%prep
cd V2G_Libraries
chmod a+x ./build_all_linux.sh

#---------------------------------------------
%build
cd V2G_Libraries
./build_all_linux.sh

#---------------------------------------------
%install

mkdir -p %{buildroot}%{_libdir}/wireshark/plugins/4.0/%{name}

cp Wireshark/plugins/* %{buildroot}%{_libdir}/wireshark/plugins/

cd V2G_Libraries
cp ./CertificateInfos/bin/* %{buildroot}%{_libdir}/wireshark/plugins/4.0/%{name}
cp ./V2GDecoder/bin/* %{buildroot}%{_libdir}/wireshark/plugins/4.0/%{name}


#---------------------------------------------
%files
%defattr(-,root,root)
%dir %{_libdir}/wireshark/plugins/*/%{name}
%{_libdir}/wireshark/plugins/*
%{_libdir}/wireshark/plugins/*/%{name}/*

#---------------------------------------------
%changelog
