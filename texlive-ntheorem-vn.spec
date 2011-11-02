Name:		texlive-ntheorem-vn
Version:	20111102
Release:	1
Summary:	TeXLive ntheorem-vn package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem-vn.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem-vn.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive ntheorem-vn package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/COPYING
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/FILELIST
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/README
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/ntheorem-doc-vn.pdf
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/Makefile
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/README.src
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/TODO
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/endmarks.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/example.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/help.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/interference.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/intro.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/license.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/ntheorem-doc-vn.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/preamble.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/thanks.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/title-abstract.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/src/user-interface.tex
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/test.pdf
%doc %{_texmfdistdir}/doc/latex/ntheorem-vn/test.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
