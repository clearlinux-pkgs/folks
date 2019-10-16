#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : folks
Version  : 0.13.1
Release  : 10
URL      : https://download.gnome.org/sources/folks/0.13/folks-0.13.1.tar.xz
Source0  : https://download.gnome.org/sources/folks/0.13/folks-0.13.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: folks-bin = %{version}-%{release}
Requires: folks-data = %{version}-%{release}
Requires: folks-lib = %{version}-%{release}
Requires: folks-license = %{version}-%{release}
Requires: folks-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : evolution-data-server-data
BuildRequires : evolution-data-server-dev
BuildRequires : libgee-dev
BuildRequires : ncurses-dev
BuildRequires : pkgconfig(gee-0.8)
BuildRequires : readline-dev
BuildRequires : vala
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Folks
=====
libfolks is a library that aggregates people from multiple sources (eg,
Telepathy connection managers) to create metacontacts.

%package bin
Summary: bin components for the folks package.
Group: Binaries
Requires: folks-data = %{version}-%{release}
Requires: folks-license = %{version}-%{release}

%description bin
bin components for the folks package.


%package data
Summary: data components for the folks package.
Group: Data

%description data
data components for the folks package.


%package dev
Summary: dev components for the folks package.
Group: Development
Requires: folks-lib = %{version}-%{release}
Requires: folks-bin = %{version}-%{release}
Requires: folks-data = %{version}-%{release}
Provides: folks-devel = %{version}-%{release}
Requires: folks = %{version}-%{release}

%description dev
dev components for the folks package.


%package lib
Summary: lib components for the folks package.
Group: Libraries
Requires: folks-data = %{version}-%{release}
Requires: folks-license = %{version}-%{release}

%description lib
lib components for the folks package.


%package license
Summary: license components for the folks package.
Group: Default

%description license
license components for the folks package.


%package locales
Summary: locales components for the folks package.
Group: Default

%description locales
locales components for the folks package.


%prep
%setup -q -n folks-0.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568081169
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dtelepathy_backend=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/folks
cp COPYING %{buildroot}/usr/share/package-licenses/folks/COPYING
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang folks

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/folks-import
/usr/bin/folks-inspect

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Folks-0.6.typelib
/usr/lib64/girepository-1.0/FolksDummy-0.6.typelib
/usr/lib64/girepository-1.0/FolksEds-0.6.typelib
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.freedesktop.folks.gschema.xml
/usr/share/vala/vapi/folks-dummy.deps
/usr/share/vala/vapi/folks-dummy.vapi
/usr/share/vala/vapi/folks-eds.deps
/usr/share/vala/vapi/folks-eds.vapi
/usr/share/vala/vapi/folks.deps
/usr/share/vala/vapi/folks.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/folks/folks-dummy.h
/usr/include/folks/folks-eds.h
/usr/include/folks/folks.h
/usr/lib64/libfolks-dummy.so
/usr/lib64/libfolks-eds.so
/usr/lib64/libfolks.so
/usr/lib64/pkgconfig/folks-dummy.pc
/usr/lib64/pkgconfig/folks-eds.pc
/usr/lib64/pkgconfig/folks.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/folks/45/backends/bluez/bluez.so
/usr/lib64/folks/45/backends/dummy/dummy.so
/usr/lib64/folks/45/backends/eds/eds.so
/usr/lib64/folks/45/backends/key-file/key-file.so
/usr/lib64/folks/45/backends/ofono/ofono.so
/usr/lib64/libfolks-dummy.so.25
/usr/lib64/libfolks-dummy.so.25.20.0
/usr/lib64/libfolks-eds.so.25
/usr/lib64/libfolks-eds.so.25.20.0
/usr/lib64/libfolks.so.25
/usr/lib64/libfolks.so.25.20.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/folks/COPYING

%files locales -f folks.lang
%defattr(-,root,root,-)

