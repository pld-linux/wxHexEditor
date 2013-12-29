# TODO: package and switch to system-wide udis86
#
Summary:	Hex editor wxHeXEditor
Summary(pl.UTF-8):	Hex edytor wxHexEditor
Name:		wxHexEditor
Version:	0.22
Release:	1
License:	GPL v2
Group:		X11/Applications/Editors
Source0:	http://downloads.sourceforge.net/wxhexeditor/wxHexEditor/v0.22%20Beta/%{name}-v%{version}-src.tar.bz2
# Source0-md5:	eb88cfcda0553e23a2a9490197e18552
URL:		http://wxhexeditor.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	mhash-devel
BuildRequires:	wxGTK2-unicode-devel >= 2.8
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

%build
cd udis86
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
cd ..

%{__make} \
	WXCONFIG=wx-gtk2-unicode-config \
	LIBS='udis86/libudis86/.libs/libudis86.a -lmhash' \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/Change.log
%attr(755,root,root)%{_bindir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
