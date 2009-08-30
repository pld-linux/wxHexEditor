Summary:	Hex editor wxHeXEditor
Summary(pl.UTF-8):	Hex edytor wxHexEditor
Name:		wxHexEditor
Version:	0.07
Release:	1
License:	GPL v2
Group:		X11/Applications/Editor
Source0:	http://dl.sourceforge.net/project/wxhexeditor/wxHexEditor/v0.07%20Alpha/%{name}-v%{version}_alpha-src.tar.bz2
# Source0-md5:	f93821aa23f72aa28ed0b5869591fc1e
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-build.patch
URL:		http://wxhexeditor.sourceforge.net/
BuildRequires:	wxGTK2-unicode-devel >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxHexEditor is another Hex Editor, build because of there is no good
hex editor for Linux system, specially for big files. It supports
files up to 2^64 bytes.

%description -l pl.UTF-8
wxHexEditor to kolejny hex editor, stworzony ponieważ nie ma dobrych
edytorów dla systemu Linux, szczególnie dla dużych plików. Wspiera
pliki do rozmiaru 2^64 bajtów.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build

%{__make} \
	CPP="%{__cxx} %{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root)%{_bindir}/%{name}
