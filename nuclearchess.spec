%define summary Chess variant that cause surronding pieces to disappear
Summary:	%{summary}
Name:		nuclearchess
Version:	1.0.0
Release:	4
License:	GPLv2
Source:		http://user.cs.tu-berlin.de/~karlb//%{name}/%{name}-%{version}.tar.gz
Group:		Games/Boards
URL:		http://www.linux-games.com/nuclearchess/
BuildRequires:	libSDL_image-devel

%description
NuclearChess is a chess variant. Whenever a piece is captured, both
pieces and all pieces on neighbour fields die.

%prep
%setup -q

%build
export LDFLAGS="-lm"
%configure2_5x --datadir=%{_gamesdatadir} --bindir=%{_gamesbindir}
%make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications/
cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=boards_section
Comment=%{summary}
Categories=BoardGame;
Name=Nuclear Chess
EOF

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING README
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop



%changelog
* Sat Dec 11 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2011.0
+ Revision: 620511
- the mass rebuild of 2010.0 packages

* Tue May 19 2009 Jérôme Brenier <incubusss@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 377684
- update to new version 1.0.0
- fix BR
- fix desktop file
- fix license (GPLv2)
- fix source url

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 0.9.2-3mdv2008.1
+ Revision: 133912
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import nuclearchess


* Sun Nov 21 2004 Abel Cheung <deaddog@deaddog.org> 0.9.2-3mdk
- Rebuild

* Wed Oct 08 2003 Abel Cheung <deaddog@deaddog.org> 0.9.2-2mdk
- move data files and binary to appropriate games dirs

* Tue Sep 23 2003 Abel Cheung <deaddog@deaddog.org> 0.9.2-1mdk
- First Mandrake package
