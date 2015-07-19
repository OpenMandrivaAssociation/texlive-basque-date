# revision 26477
# category Package
# catalog-ctan /macros/latex/contrib/basque-date
# catalog-date 2012-05-17 14:56:37 +0200
# catalog-license lppl1.2
# catalog-version 1.05
Name:		texlive-basque-date
Version:	1.05
Release:	9
Summary:	Print the date in Basque
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/basque-date
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-date.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-date.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/basque-date.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Aug 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.05-1
+ Revision: 813401
- Import texlive-basque-date
- Import texlive-basque-date

