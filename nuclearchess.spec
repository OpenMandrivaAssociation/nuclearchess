%define version 0.9.2
%define release %mkrel 3

%define summary Chess variant that cause surronding pieces to disappear
Summary:	%{summary}
Name:		nuclearchess
Version:	%{version}
Release:	%{release}
License:	GPL
Source:		nuclearchess-0.9.2.tar.bz2
Group:		Games/Boards
URL:		http://www.linux-games.com/nuclearchess/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	SDL_image1.2-devel

%description
NuclearChess is a chess variant. Whenever a piece is captured, both
pieces and all pieces on neighbour fields die.

%prep
%setup -q

%build
%configure2_5x --datadir=%{_gamesdatadir} --bindir=%{_gamesbindir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name} 
Icon=boards_section 
Comment=%{summary}  
Categories=BoardGame; 
Name=Nuclear Chess
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING README
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

