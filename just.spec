Name:           just
Version:        1.43.0
Release:        1
Summary:        Commmand runner
License:        (Apache-2.0 OR MIT) AND Unicode-DFS-2016 AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (MIT OR Unlicense) AND Apache-2.0 AND BSD-3-Clause AND CC0-1.0 AND MIT AND CC0-1.0
Group:          Development/Tools/Building
URL:            https://github.com/casey/just
Source0:        https://github.com/casey/just/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  bash-completion
BuildRequires:  rust-packaging
#BuildRequires:  fish
BuildRequires:  git
BuildRequires:  python
BuildRequires:  zsh
BuildRequires:  zstd

%description
Just is a command runner. Although it shares
some similarities with "make", it is not a build
system.

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description bash-completion
Bash command-line completion support for %{name}.

%package fish-completion
Summary:        Fish Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and fish)
Recommends:       fish
BuildArch:      noarch

%description fish-completion
Fish command-line completion support for %{name}.

%package zsh-completion
Summary:        Zsh Completion for %{name}
Group:          System/Shells
Supplements:    (%{name} and zsh)
Requires:       zsh
BuildArch:      noarch

%description zsh-completion
Zsh command-line completion support for %{name}.

%prep
%autosetup -a1
%cargo_prep -v vendor

%build
%cargo_build 
#--all-features
#mkdir completions
./target/release/just --completions bash > completions/just.bash
./target/release/just --completions fish > completions/just.fish
./target/release/just --completions zsh > completions/just.zsh

%install
%cargo_install 
#--all-features
install -Dm644 -T completions/%{name}.bash %{buildroot}%{_datadir}/bash-completion/completions/%{name}
install -Dm644 -T completions/%{name}.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{name}.fish
install -Dm644 -T completions/%{name}.zsh %{buildroot}%{_datadir}/zsh/site-functions/_%{name}

%files
%license LICENSE
%doc *.md
%{_bindir}/%{name}

%files bash-completion
%{_datadir}/bash-completion/*

%files fish-completion
%dir %{_datadir}/fish
%{_datadir}/fish/*

%files zsh-completion
%dir %{_datadir}/zsh
%{_datadir}/zsh/*
