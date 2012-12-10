%define name            jconvolver-reverbs
%define version         0.8.4
%define release         %mkrel 3

%define jconv_name      jconvolver

Name:           %{name}
Summary:        Reverb impulse response data files for JConvolver
Version:        %{version} 
Release:        %{release}

Source:         http://www.kokkinizita.net/linuxaudio/downloads/jconvolver-reverbs.tar.bz2
URL:            http://www.kokkinizita.net/linuxaudio/
License:        GPLv2
Group:          Sound
BuildArch:      noarch

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


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.4-3mdv2011.0
+ Revision: 612442
- the mass rebuild of 2010.1 packages

* Thu Mar 04 2010 Frank Kober <emuse@mandriva.org> 0.8.4-2mdv2010.1
+ Revision: 514269
- fix build arch: noarch

* Tue Mar 02 2010 Frank Kober <emuse@mandriva.org> 0.8.4-1mdv2010.1
+ Revision: 513685
- import jconvolver-reverbs


