%define oname Ascii-Design

Name:       ascii-design
Version:    1.0.3
Release:    1
License:    GPLv2
Summary:    Create awesome ascii art text
Url:        http://ascii-design.sourceforge.net/
Group:      Office
Source0:    https://github.com/Faster3ck/Ascii-Design/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++ 
BuildRequires:  cmake  
BuildRequires:  make 
BuildRequires:  kdelibs4-devel
BuildRequires:  desktop-file-utils
BuildRequires:  jpeg-devel

Requires:	figlet
Requires:	figlet-more-fonts

%description
Free program, based on figlet engine, that enables you 
to create awesome ascii art text. 
You can create art based text for 
many types of decorations for web sites, e-mail, text files etc...
Ascii Design is able to use dozens of special fonts 
to create various styles of ascii arts.

%prep
%setup -qn %{oname}-%{version}
sed -i 's/\r//' {COPYING,INSTALL}.TXT
cd src
find . -name "*.cpp" -o -name "*.h" -o -name "*.cpp" |xargs chmod 0644
cd -

perl -pi -e "s|/share/appdata/|/share/ascii-design/|appdata/|"  CMakeLists.txt

%build
%cmake_kde4 -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT%{_prefix} 
%make

%install
%makeinstall -C build

# fix desktop
rm -fr $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Categories=Office;
Comment=Start Ascii Design
Exec=ascii-design
Icon=ascii-design
Name=Ascii Design
StartupNotify=true
Terminal=false
Type=Application
EOF

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop


%files
%doc COPYING.TXT INSTALL.TXT
%{_bindir}/ascii-design
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ascii-design.png
%{_datadir}/%{name}/appdata/

