#
# Conditional build:
%bcond_without	javascript	# build without JavaScript interpreter
%bcond_without	graphics	# build without graphics support
%bcond_without	fb		# build without Linux Framebuffer graphics driver
%bcond_without	sdl		# build without SDL graphics driver
%bcond_without	svga		# build without svgalib graphics driver
%bcond_without	x		# build without X Window System graphics driver
#
Summary:	Lynx-like WWW browser
Summary(es):	El links es un browser para modo texto, similar a lynx
Summary(pl):	Podobna do Lynksa przegl╠darka WWW
Summary(pt_BR):	O links И um browser para modo texto, similar ao lynx
Summary(ru):	Текстовый WWW броузер типа Lynx
Summary(uk):	Текстовий WWW броузер типу Lynx
Name:		links2
%define	pre	pre17
Version:	2.1%{pre}
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Networking
Source0:	ftp://atrey.karlin.mff.cuni.cz/pub/local/clock/links/links-%{version}.tar.bz2
# Source0-md5:	94315d9ba68bbb543d93b3b3b4f07582
Source1:	%{name}.desktop
Source2:	%{name}.1.pl
Source3:	%{name}.png
Source4:	glinks.desktop
Patch0:		%{name}-links-g_if_glinks.patch
Patch1:		%{name}-ac25x.patch
Patch2:		%{name}-reallyquit.patch
Patch3:		%{name}-img.patch
Patch4:		%{name}-convert-old-bookmarks.patch
Patch5:		%{name}-cookies-save.patch
Patch7:		%{name}-config-dirs.patch
Patch8:		%{name}-gzip_fallback.patch
Patch9:		%{name}-js-Date-getTime.patch
Patch10:	%{name}-js-submit-nodefer.patch
Patch11:	%{name}-segv.patch
Patch12:	%{name}-pl-update.patch
Patch13:	%{name}-ac.patch
#Patch15:	%{name}-home_etc.patch
URL:		http://atrey.karlin.mff.cuni.cz/~clock/twibright/links/
BuildRequires:	autoconf
BuildRequires:	automake
%{?with_javascript:BuildRequires:	bison}
%{?with_javascript:BuildRequires:	flex}
BuildRequires:	gpm-devel
BuildRequires:	ncurses-devel >= 5.1
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	zlib-devel
%if %{with graphics}
%{?with_fb:BuildRequires:	DirectFB-devel >= 0.9.17}
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2.0}
%{?with_x:BuildRequires:	XFree86-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
%{?with_svga:BuildRequires:	svgalib-devel}
%endif
Provides:	webclient
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Links is a WWW browser, at first look similiar to Lynx, but somehow
different:

- renders tables and frames,
- displays colors as specified in current HTML page,
- uses drop-down menu (like in Midnight Commander),
- can download files in background.

%{?with_graphics:This version can work in graphical mode.}
%{?with_javascript:This version has support for JavaScript.}

%description -l es
Links es un browser WWW modo texto, similar al Lynx. El links muestra
tablas, hace baja archivos en segundo plano, y usa conexiones HTTP/1.1
keepalive.

%description -l pl
Links jest przegl╠dark╠ WWW, na pierwszy rzut oka podobn╠ do Lynksa,
ale mimo wszystko inn╠:

- renderuje tabelki i ramki,
- wy╤wietla kolory zgodnie z definicjami w ogl╠danej stronie HTML,
- u©ywa opuszczanego menu (jak w Midnight Commanderze),
- mo©e ╤ci╠gaФ pliki w tle.

%{?with_graphics:Ta wersja mo©e pracowaФ w trybie graficznym.}
%{?with_javascript:Ta wersja obsЁuguje JavaScript.}

%description -l pt_BR
Links И um browser WWW modo texto, similar ao Lynx. O Links exibe
tabelas, faz baixa arquivos em segundo plano, e usa as conexУes
HTTP/1.1 keepalive.

%description -l ru
Links - это текстовый WWW броузер, на первый взгляд похожий на Lynx,
но несколько отличающийся:

- отображает таблицы и (скоро) фреймы,
- показывает цвета как указано в HTML странице,
- использует выпадающие меню (как в Midnight Commander),
- может загружать файлы в фоне.

%description -l uk
Links - це текстовий WWW броузер, на перший погляд схожий на Lynx, але
трохи в╕дм╕нний в╕д нього:

- в╕добража╓ таблиц╕ та (незабаром) фрейми,
- показу╓ кольори як вказано в HTML стор╕нц╕,
- використову╓ випадаюч╕ меню (як в Midnight Commander),
- може завантажувати файли в фон╕.

%prep
%setup -q -n links-%{version}
%{?with_graphics:%patch0 -p1}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

cd intl
./gen-intl

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--program-suffix=2 \
	%{?with_graphics:--enable-graphics} \
	%{?with_javascript:--enable-javascript} \
	%{!?with_fb:--without-fb} \
	%{!?with_sdl:--without-sdl} \
	%{!?with_svga:--without-svgalib} \
	%{!?with_x:--without-x}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}} \
	$RPM_BUILD_ROOT%{_mandir}/pl/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with graphics}
ln -sf links2 $RPM_BUILD_ROOT%{_bindir}/glinks
echo ".so links2.1" > $RPM_BUILD_ROOT%{_mandir}/man1/glinks.1
echo ".so links2.1" > $RPM_BUILD_ROOT%{_mandir}/pl/man1/glinks.1
install %{SOURCE4} $RPM_BUILD_ROOT%{_desktopdir}
%endif

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/links2.1
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog README SITES TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man*/*
%lang(pl) %{_mandir}/pl/man*/*
