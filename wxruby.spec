Summary:	wxWindows for Ruby
Summary(pl):	wxWindows dla Ruby
Name:		wxruby
Version:	0.1.0
Release:	1
License:	wxWindows License
Group:		Development/Libraries
Source0:	http://rubyforge.org/download.php/60/%{name}-%{version}.tgz
# Source0-md5:	7bf0482298a1f3559068f02c1488c6eb
Patch0:		%{name}-extconf.patch
URL:		http://www.wxruby.org/
BuildRequires:	ruby-devel >= 1.8.0
BuildRequires:	wxGTK2-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')

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
%{__make} \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags} -fPIC `wxgtk2-2.4-config --cxxflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{_examplesdir}/%{name}-%{version}}

install src/%{name}.so $RPM_BUILD_ROOT%{ruby_archdir}

cp -a samples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README README.linux
%attr(755,root,root) %{ruby_archdir}/*.so
%{_examplesdir}/%{name}-%{version}
