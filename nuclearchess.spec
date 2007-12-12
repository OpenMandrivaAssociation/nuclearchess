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

mkdir -p %{buildroot}%{_menudir}
cat << _EOF_ > %{buildroot}%{_menudir}/%{name}
?package(%{name}): \
 command="%{_gamesbindir}/%{name}" \
 icon="boards_section.png" \
 longtitle="%{summary}" \
 needs="x11" \
 section="Amusement/Boards" \
 title="Nuclear Chess"
_EOF_

%clean
rm -rf %{buildroot}

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog COPYING README
%{_gamesbindir}/*
%{_gamesdatadir}/%{name}
%{_menudir}/%{name}

