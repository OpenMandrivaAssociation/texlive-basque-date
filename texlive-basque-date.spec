Name:		texlive-basque-date
Version:	26477
Release:	2
Summary:	Print the date in Basque
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/basque-date
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-date.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-date.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-date.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides two LaTeX commands to print the current
date in Basque according to the correct forms ruled by The
Basque Language Academy (Euskaltzaindia). The commands
automatically solve the complex declination issues of numbers
in Basque.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/basque-date/basque-date.sty
%doc %{_texmfdistdir}/doc/latex/basque-date/README
%doc %{_texmfdistdir}/doc/latex/basque-date/basque-date.pdf
#- source
%doc %{_texmfdistdir}/source/latex/basque-date/basque-date.dtx
%doc %{_texmfdistdir}/source/latex/basque-date/basque-date.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
