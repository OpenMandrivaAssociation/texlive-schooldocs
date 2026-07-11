%global tl_name schooldocs
%global tl_revision 73466

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.6
Release:	%{tl_revision}.1
Summary:	Various layout styles for school documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/schooldocs
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schooldocs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schooldocs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/schooldocs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The aim of this package is to offer diverse layout styles for school-
related documents. It serves well in creating exercise sheets, exams,
course materials. The package sets the page geometry (dimensions of text
and margins) and the title formatting. Various styles are available
defining settings for headers, footers or alternative title formatting,
providing many customizable features.

