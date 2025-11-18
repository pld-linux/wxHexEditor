# TODO: switch to system-wide udis86
#
Summary:	Hex editor wxHeXEditor
Summary(pl.UTF-8):	Hex edytor wxHexEditor
Name:		wxHexEditor
Version:	0.24
Release:	3
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://downloads.sourceforge.net/wxhexeditor/wxHexEditor/v0.24%20Beta/%{name}-v%{version}-src.tar.xz
# Source0-md5:	6e54b7e640bf5296137b765488ec78a6
Patch0:		wxWidgets3.patch
URL:		http://www.wxhexeditor.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mhash-devel
BuildRequires:	wxGTK3-unicode-devel >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxHexEditor is another Hex Editor, build because of there is no good
hex editor for Linux system, specially for big files. It supports
files up to 2^64 bytes and devices. Designed for reverse enginering
binary files.

%description -l pl.UTF-8
wxHexEditor to kolejny edytor szesnastkowy, stworzony ponieważ nie ma
dobrych edytorów dla systemu Linux, szczególnie dla dużych plików.
Wspiera pliki do rozmiaru 2^64 bajtów i urządzenia blokowe. Został
dostosowany do reverse engineringu plików binarnych.

%prep
%setup -q -n %{name}
%patch -P0 -p1

%build
cd udis86
mkdir -p build/m4
%{__aclocal} -I build/m4
%{__autoconf}
%{__libtoolize}
%{__autoheader}
%{__automake}
%configure
%{__make}
cd ..

%{__make} \
	WXCONFIG=wx-gtk3-unicode-config \
	LIBS='udis86/libudis86/.libs/libudis86.a -lmhash' \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_localedir}/hu{_HU,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/ja{_JP,}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/nl{_NL,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/Change.log
%attr(755,root,root)%{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
