Name:           remnote
Version:        1.22.7
Release:        0
Summary:        All-in-one workspace for note-taking, learning, and knowledge management
ExclusiveArch:  x86_64
License:        NonFree
URL:            https://www.remnote.com
Source0:        https://download2.remnote.io/remnote-desktop2/RemNote-%{version}.AppImage
Source1:        remnote.sh
Source2:        remnote.desktop

BuildRequires:  fdupes
BuildRequires:  fuse

%description
RemNote is an all-in-one workspace for note-taking, learning, organizing
thoughts and growing knowledge. It combines note-taking with spaced repetition
and knowledge management features.

%prep
chmod +x %{SOURCE0}
%{SOURCE0} --appimage-extract

%build

%install
install -dm0755 %{buildroot}%{_libdir}/remnote
cp -a squashfs-root/* %{buildroot}%{_libdir}/remnote/
rm -rf %{buildroot}%{_libdir}/remnote/usr/lib

find %{buildroot}%{_libdir}/%{name} -type d -exec chmod 755 {} \;

install -Dm755 %{SOURCE1} %{buildroot}%{_bindir}/remnote
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/applications/remnote.desktop
install -Dm644 squashfs-root/remnote.png %{buildroot}%{_datadir}/pixmaps/remnote.png

%fdupes %{buildroot}%{_libdir}/remnote

%files
%{_bindir}/remnote
%{_datadir}/applications/remnote.desktop
%{_datadir}/pixmaps/remnote.png
%{_libdir}/remnote/

%changelog