######################################################
# SpecFile: ascii-design.spec 
# Generato: http://www.mandrivausers.ro/
# MRB-Falticska Florin
######################################################
%define use_ccache	1
%define ccachedir	~/.ccache-OOo%{distsuffix}
%{?_with_ccache: %global use_ccache 1}
%{?_without_ccache: %global use_ccache 0}
%define  dist	stella
%define debug_package	%{nil}

Name:       ascii-design
Version:    1.0.1
Release:    1%{?dist}
License:    GPLv2
Summary:    Create awesome ascii art text
Url:         http://ascii-design.sourceforge.net/
Group:      Applications/Publishing
Source0:    http://surfnet.dl.sourceforge.net/project/ascii-design/ascii-design/Ascii-Design%201.0.1/%{name}-%{version}.tar.bz2
Source1:    http://ascii-design.sourceforge.net/figlet_fonts.zip	
# aplied upstream
# Patch0:     ascii-design-fsf-adress.patch

BuildRequires:  gcc-c++ 
BuildRequires:  cmake  
BuildRequires:  make 
BuildRequires:  desktop-file-utils
BuildRequires:  unzip
BuildRequires:  qt4-devel

Requires:	figlet



%description
Free program, based on figlet engine, that enables you 
to create awesome ascii art text. 
You can create art based text for 
many types of decorations for web sites, e-mail, text files etc...
Ascii Design is able to use dozens of special fonts 
to create various styles of ascii arts.

%prep
%setup -q -a 1
sed -i 's/\r//' {COPYING,INSTALL}.TXT
#patch0 -p0
%__rm -fr fonts/.directory

%build
%__mkdir -p build && cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT -C build

# fix desktop
rm -fr $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

cat << EOF > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
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

# fonts -alternative to figlet-fonts-
%__mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -R fonts $RPM_BUILD_ROOT%{_datadir}/%{name}

%__chmod a+x $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING.TXT INSTALL.TXT
%{_bindir}/ascii-design
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ascii-design.png
%{_datadir}/%{name}/fonts/

%changelog
* Thu May 02 2013 Falticska Florin <symbianflo@mandrivausers.ro> - 1.0.1-1stella
- Backport for stella project
- MRB-Mandriva Users.Ro

