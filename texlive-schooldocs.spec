Name:		texlive-schooldocs
Version:	61719
Release:	2
Summary:	Various layout styles for school documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/schooldocs
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schooldocs.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schooldocs.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/schooldocs.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The purpose of this package is to provide several layout styles
for school documents. It is useful for exercise sheets, exams,
course materials. The package sets the page geometry
(dimensions of text and margins) and the title typesetting; the
various styles define the header, footer and title formatting.
Many features are freely configurable.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/schooldocs
%{_texmfdistdir}/tex/latex/schooldocs
%doc %{_texmfdistdir}/doc/latex/schooldocs

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
