Summary:	PC/SC Lite driver for the Athena Smartcard Solutions II reader
Summary(pl):	Sterownik PC/SC Lite dla czytnika Athena Smartcard Solutions II
Name:		pcsc-driver-ase2
Version:	1.1.1
Release:	1
License:	see LICENSE
Group:		Libraries
Source0:	http://linuxnet.com/drivers/readers/files/ase_drive-%{version}.tar.gz
# Source0-md5:	7e925e329c35d9df1607ba505366f9cf
Patch0:		%{name}-make.patch
URL:		http://linuxnet.com/sourcedrivers.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PC/SC Lite driver for the Athena Smartcard Solutions II reader.

%description -l pl
Sterownik PC/SC Lite dla czytnika Athena Smartcard Solutions II.

%prep
%setup -q -n ase_drive
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers

install libase_*.so $RPM_BUILD_ROOT%{_libdir}/pcsc/drivers

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README etc/reader.conf
%attr(755,root,root) %{_libdir}/pcsc/drivers/libase_*.so
