%define version 1.0.0
%define release %mkrel 1

%define summary Chess variant that cause surronding pieces to disappear
Summary:	%{summary}
Name:		nuclearchess
Version:	%{version}
Release:	%{release}
License:	GPLv2
Source:		http://user.cs.tu-berlin.de/~karlb//%{name}/%{name}-%{version}.tar.gz
Group:		Games/Boards
URL:		http://www.linux-games.com/nuclearchess/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	libSDL_image-devel

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

