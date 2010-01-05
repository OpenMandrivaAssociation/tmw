Name:		tmw
Version:	0.0.29.1
Release:	%mkrel 1
Summary:	A 2D MMORPG : The Mana World
Group:		Games/Other
License:	GPLv2+
Url:		http://themanaworld.org/
Source0:	http://downloads.sourceforge.net/themanaworld/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
Buildrequires:	SDL_net-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	physfs-devel
BuildRequires:	curl-devel
BuildRequires:	guichan-devel
BuildRequires:	libxml2-devel
BuildRequires:	libpng-devel

%description
The Mana World (TMW) is a serious effort to create an innovative free 
and open source MMORPG. TMW uses 2D graphics and aims to create a large 
and diverse interactive world.

%prep
%setup -q

%build
%configure --disable-rpath
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING docs/*.txt NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}*
