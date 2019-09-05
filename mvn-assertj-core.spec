#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-assertj-core
Version  : 3.8.0
Release  : 3
URL      : https://github.com/joel-costigliola/assertj-core/archive/assertj-core-3.8.0.tar.gz
Source0  : https://github.com/joel-costigliola/assertj-core/archive/assertj-core-3.8.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/assertj/assertj-core/3.12.2/assertj-core-3.12.2.jar
Source2  : https://repo1.maven.org/maven2/org/assertj/assertj-core/3.12.2/assertj-core-3.12.2.pom
Source3  : https://repo1.maven.org/maven2/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.jar
Source4  : https://repo1.maven.org/maven2/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-assertj-core-data = %{version}-%{release}
Requires: mvn-assertj-core-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
# AssertJ - Fluent assertions for java
`master:` [![Build Status (master)](https://travis-ci.org/joel-costigliola/assertj-core.svg?branch=master)](https://travis-ci.org/joel-costigliola/assertj-core) `2.x:` [![Build Status (2.x)](https://travis-ci.org/joel-costigliola/assertj-core.svg?branch=2.x)](https://travis-ci.org/joel-costigliola/assertj-core/branches) [![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.assertj/assertj-core/badge.svg)](https://maven-badges.herokuapp.com/maven-central/org.assertj/assertj-core)

%package data
Summary: data components for the mvn-assertj-core package.
Group: Data

%description data
data components for the mvn-assertj-core package.


%package license
Summary: license components for the mvn-assertj-core package.
Group: Default

%description license
license components for the mvn-assertj-core package.


%prep
%setup -q -n assertj-core-assertj-core-3.8.0

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-assertj-core
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-assertj-core/LICENSE.txt
cp licence-header.txt %{buildroot}/usr/share/package-licenses/mvn-assertj-core/licence-header.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.12.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.12.2/assertj-core-3.12.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.12.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.12.2/assertj-core-3.12.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/assertj/assertj-core/3.12.2/assertj-core-3.12.2.jar
/usr/share/java/.m2/repository/org/assertj/assertj-core/3.12.2/assertj-core-3.12.2.pom
/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.jar
/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-assertj-core/LICENSE.txt
/usr/share/package-licenses/mvn-assertj-core/licence-header.txt
