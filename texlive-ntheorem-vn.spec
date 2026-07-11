%global tl_name ntheorem-vn
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.203
Release:	%{tl_revision}.1
Summary:	Vietnamese translation of documentation of ntheorem
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/ntheorem/vn
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem-vn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ntheorem-vn.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a translation of the documentation provided with ntheorem.

