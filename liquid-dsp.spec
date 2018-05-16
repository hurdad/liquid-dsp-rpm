Name:           liquid-dsp
Version:	%{VERSION}
Release:        2%{?dist}
Summary:	digital signal processing library for software-defined radios
License:	MIT
URL:		http://liquidsdr.org
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	automake
BuildRequires:	fftw3-devel
BuildRequires:	libfec-odr-devel
Provides:	libliquid.so()(64bit)

%description
Software-Defined Radio Digital Signal Processing Library 

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%prep
%setup -n %{name}-%{version}

%build
./bootstrap.sh
CFLAGS="-march=native -O3" ./configure --prefix=$RPM_BUILD_ROOT/usr --libdir=/lib64
make %{?_smp_mflags}

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_libdir}/*.so

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.a

%changelog

