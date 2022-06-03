#
# Conditional build:
%bcond_without	static_libs	# static library
#
Summary:	libenchant - generic spell checking library
Summary(pl.UTF-8):	libenchant - ogólna biblioteka sprawdzania pisowni
Name:		enchant2
Version:	2.3.2
Release:	2
License:	LGPL v2+
Group:		Libraries
#Source0Download: https://github.com/AbiWord/enchant/releases
Source0:	https://github.com/AbiWord/enchant/releases/download/v%{version}/enchant-%{version}.tar.gz
# Source0-md5:	5a680a39c64c4ebb1bc02098cb5ed40b
Patch0:		%{name}-link.patch
URL:		https://github.com/AbiWord/enchant
BuildRequires:	aspell-devel >= 2:0.50.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.62
BuildRequires:	glib2-devel >= 1:2.12.0
BuildRequires:	hspell-devel >= 0.9-3
BuildRequires:	hunspell-devel
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	libtool >= 2:2
BuildRequires:	libvoikko-devel
BuildRequires:	nuspell-devel >= 4.1.0
BuildRequires:	pkgconfig
Requires:	glib2 >= 1:2.12.0
Suggests:	%{name}-backend
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This project aims to provide an efficient, extensible abstraction for
dealing with different spell checking libraries. Enchant is meant to
provide a generic interface into various existing spell checking
libraries. These include, but are not limited to: Aspell/Pspell,
Hunspell, Hspell.

Enchant is also meant to be used in a cross-platform environment. Part
of this means that Enchant wants to limit its number of external
dependencies to 0, or as close is as humanly possible. Also, any
enchant consumer (i.e. a Word Processor) should not need to know about
what backend providers Enchant knows about. In fact, Enchant shouldn't
even need to know this information itself. To accomplish this, all of
Enchant's providers are dynamically loaded modules.

Enchant is also meant to be used in a multi-user environment, such as
Unix. It is preferable to have both a $USER and a $GLOBAL location for
both provider modules and for dictionaries themselves, when possible.
Enchant's module location algorithm takes this into account, and gives
preference to the $USER resources, when found.

%description -l pl.UTF-8
Celem projektu jest dostarczenie wydajnej i rozszerzalnej abstrakcji
do obsługi różnych bibliotek kontroli pisowni. Enchant ma dostarczać
ogólny interfejs do różnych istniejących bibliotek. Obejmują one (ale
nie są ograniczone do): Aspella/Pspella, Hunspella, Hspella.

Enchant ma być także używany w środowisku wieloplatformowym. Oznacza
to między innymi, że Enchant ma mieć ograniczoną liczbę zewnętrznych
zależności do zera lub najbliżej jak to możliwe. Także dowolny klient
enchanta (czyli procesor tekstu) nie powinien potrzebować wiedzy,
jakie backendy są dostępne dla Enchanta. W rzeczywistości nawet
Enchant nie powinien potrzebować takiej informacji. Aby to osiągnąć,
wszystkie backendy Enchanta są dynamicznie ładowanymi modułami.

Enchant ma być także używany w środowisku wieloużytkownikowym, takim
jak Unix. Preferuje się, żeby istniały zarówno specyficzne dla
użytkownika jak i globalne lokalizacje zarówno dla modułów jak i
samych słowników, jeśli to możliwe. Algorytm poszukiwania modułów
Enchanta bierze to pod uwagę i preferuje zasoby użytkownika, jeśli
takie znajdzie.

%package devel
Summary:	Header files for enchant library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki enchant
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.12.0

%description devel
Header files for enchant library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki enchant.

%package static
Summary:	Static enchant library
Summary(pl.UTF-8):	Statyczna biblioteka enchant
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static enchant library.

%description static -l pl.UTF-8
Statyczna biblioteka enchant.

%package aspell
Summary:	aspell provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący aspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	aspell >= 2:0.50.0
Provides:	%{name}-backend

%description aspell
aspell provider module for Enchant.

%description aspell -l pl.UTF-8
Moduł obsługujący aspella dla Enchanta.

%package hspell
Summary:	hspell provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący hspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-backend

%description hspell
hspell provider module for Enchant.

%description hspell -l pl.UTF-8
Moduł obsługujący hspella dla Enchanta.

%package hunspell
Summary:	hunspell provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący hunspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-backend

%description hunspell
hunspell provider module for Enchant.

%description hunspell -l pl.UTF-8
Moduł obsługujący hunspella dla Enchanta.

%package nuspell
Summary:	nuspell provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący nuspella dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	nuspell-libs >= 4.1.0
Provides:	%{name}-backend

%description nuspell
nuspell provider module for Enchant.

%description nuspell -l pl.UTF-8
Moduł obsługujący nuspella dla Enchanta.

%package voikko
Summary:	Voikko provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący backend voikko dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-backend

%description voikko
Voikko (Finnish) provider module for Enchant.

%description voikko -l pl.UTF-8
Moduł obsługujący backend voikko (fiński) dla Enchanta.

%package zemberek
Summary:	Zemberek provider module for Enchant
Summary(pl.UTF-8):	Moduł obsługujący backend zemberek dla Enchanta
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib >= 0.62
Provides:	%{name}-backend

%description zemberek
Zemberek (Turkish) provider module for Enchant.

%description zemberek -l pl.UTF-8
Moduł obsługujący backend zemberek (turecki) dla Enchanta.

%prep
%setup -q -n enchant-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	--with-aspell \
	--with-hspell \
	--with-hunspell \
	--with-hunspell-dir=/usr/share/myspell \
	--with-nuspell \
	--with-zemberek

%{__make} \
	pkgdatadir=%{_datadir}/enchant-2

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgdatadir=%{_datadir}/enchant-2

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

# useless - modules loaded through libgmodule
%{__rm} $RPM_BUILD_ROOT%{_libdir}/enchant-2/*.la
%if %{with static_libs}
%{__rm} $RPM_BUILD_ROOT%{_libdir}/enchant-2/*.a
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS HACKING NEWS README
%attr(755,root,root) %{_bindir}/enchant-2
%attr(755,root,root) %{_bindir}/enchant-lsmod-2
%attr(755,root,root) %{_libdir}/libenchant-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libenchant-2.so.2
%dir %{_libdir}/enchant-2
%{_datadir}/enchant-2
%{_mandir}/man1/enchant-2.1*
%{_mandir}/man1/enchant-lsmod-2.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libenchant-2.so
%{_includedir}/enchant-2
%{_pkgconfigdir}/enchant-2.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libenchant-2.a
%endif

%files aspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant-2/enchant_aspell.so

%files hspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant-2/enchant_hspell.so

%files hunspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant-2/enchant_hunspell.so

%files nuspell
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant-2/enchant_nuspell.so

%files voikko
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant-2/enchant_voikko.so

%files zemberek
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/enchant-2/enchant_zemberek.so
