%define name            jconvolver-reverbs
%define version         0.8.4
%define release         %mkrel 1

%define jconv_name      jconvolver

Name:           %{name}
Summary:        Reverb impulse response data files for JConvolver
Version:        %{version} 
Release:        %{release}

Source:         http://www.kokkinizita.net/linuxaudio/downloads/jconvolver-reverbs.tar.bz2
URL:            http://www.kokkinizita.net/linuxaudio/
License:        GPLv2
Group:          Sound


%description
Reverb example impulse responses for Jconvolver, the Convolution Engine 
for JACK. They include true measured data acquired from several accoustic 
environments such as cathedral, concert hall and chapel. These files can 
be loaded into JConvolver to produce realistic reverb effects. 

%prep 
%setup -q -n reverbs

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_datadir}/%jconv_name/reverbs
cp -a * %{buildroot}/%{_datadir}/%jconv_name/reverbs

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_datadir}/%jconv_name/reverbs/*
