Summary:	Reverb impulse response data files for JConvolver
Name:	jconvolver-reverbs
# Keep in sync with the %%version of jconvolver
Version:	1.1.0
Release:	1
License:	GPLv2+
Group:	Sound
Url:	https://www.kokkinizita.net/linuxaudio/
Source0:	http://www.kokkinizita.net/linuxaudio/downloads/%{name}.tar.bz2
BuildArch:	noarch

%description
Reverb example impulse responses for jconvolver, the convolution engine 
for JACK. They include true measured data acquired from several accoustic 
environments such as cathedral, concert hall and chapel. These files can 
be loaded into jconvolver to produce realistic reverb effects. 

%files
%{_datadir}/jconvolver/reverbs/*

#-----------------------------------------------------------------------------

%prep 
%autosetup -p1 -n reverbs


%build
# Nothing to do


%install
install -d %{buildroot}/%{_datadir}/jconvolver/reverbs
cp -a * %{buildroot}/%{_datadir}/jconvolver/reverbs
