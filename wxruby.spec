
Summary:	wxWindows for Ruby
Summary(pl):	wxWindows dla Ruby
Name:		wxruby
Version:	0.1.0
Release:	1
License:	Expat (MIT) License
Group:		Development/Libraries
Source0:	http://rubyforge.org/download.php/60/%{name}-%{version}.tgz
# Source0-md5:	7bf0482298a1f3559068f02c1488c6eb
Patch0:	wxruby-extconf.patch
URL:		http://www.wxruby.org/
BuildRequires:	ruby-devel >= 1.8.0
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wxruby is a binding for the wxWindows library for Ruby.

%description -l pl
wxruby jest dowi±zaniem biblioteki wxWindows dla jêzyka Ruby.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
cd src
ruby extconf.rb
%{__make}

%install
%ifarch athlon
%define _arch i686
%endif
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/ruby/1.8/%{_arch}-linux
install src/%{name}.so $RPM_BUILD_ROOT/usr/lib/ruby/1.8/%{_arch}-linux/
install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}
cp -a samples/* $RPM_BUILD_ROOT/usr/src/examples/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog    LICENSE  README.linux  README.mswin 
%doc COPYING.LIB  README   README.mingw  README.osx 

%attr(755,root,root) %{_libdir}/ruby/1.8/%{_arch}-linux/*
/usr/src/examples/%{name}
