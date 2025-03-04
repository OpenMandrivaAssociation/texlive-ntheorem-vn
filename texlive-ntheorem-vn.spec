Name:		texlive-ntheorem-vn
Version:	15878
Release:	2
Summary:	TeXLive ntheorem-vn package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem-vn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem-vn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
