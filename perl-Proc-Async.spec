Name:           perl-Proc-Async
Version:        1.0.0
Release:        3
Summary:        Running and monitoring processes asynchronously
License:        GPL+ or Artistic
Group:          Development/Libraries
Source:         %{name}-%{version}.tar.bz2
Packager:	Andrea Righi <andrea@betterservers.com>
BuildArch:      noarch
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(File::Which)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Proc::Daemon)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)
Requires:       perl(Config)
Requires:       perl(constant)
Requires:       perl(File::Path)
Requires:       perl(File::Slurp)
Requires:       perl(File::Spec)
Requires:       perl(File::Temp)
Requires:       perl(Proc::Daemon)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module can execute an external process, monitor its state, get its
results and, if needed, kill it prematurely and remove its results. There
are, of course, many modules that cover similar functionality, including
functions directly built-in in Perl. So why to have this module, at all?
The main feature is hidden in the second part of the module name, the word
Async. The individual methods (to execute, to monitor, to get results,
etc.) can be called (almost) independently from each other, from separate
Perl programs, and there may be any delay between them.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/share/perl5/Proc/Async
install -m 0644 lib/Proc/Async.pm  %{buildroot}/usr/share/perl5/Proc/Async.pm
install -m 0644 lib/Proc/Async/Config.pm  %{buildroot}/usr/share/perl5/Proc/Async/Config.pm

%files
%dir /usr/share/perl5/Proc
%dir /usr/share/perl5/Proc/Async
%attr(644, -, -) /usr/share/perl5/Proc/Async.pm
%attr(644, -, -) /usr/share/perl5/Proc/Async/Config.pm

%changelog
* Fri Sep 15 2017 Andrea Righi <andrea@betterservers.com> 1.0.0-3
- Introduce option DETACHED

* Tue Nov 29 2016 Andrea Righi <andrea@betterservers.com> 1.0.0-2
- Properly get exit code from the executed child process

* Wed Sep 14 2016 Andrea Righi <andrea@betterservers.com> 1.0.0-1
- Initil release
