#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-assertj-core
Version  : 3.8.0
Release  : 1
URL      : https://github.com/joel-costigliola/assertj-core/archive/assertj-core-3.8.0.tar.gz
Source0  : https://github.com/joel-costigliola/assertj-core/archive/assertj-core-3.8.0.tar.gz
Source1  : https://repo1.maven.org/maven2/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.jar
Source2  : https://repo1.maven.org/maven2/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-assertj-core-data = %{version}-%{release}

%description
# AssertJ - Fluent assertions for java
`master:` [![Build Status (master)](https://travis-ci.org/joel-costigliola/assertj-core.svg?branch=master)](https://travis-ci.org/joel-costigliola/assertj-core) `2.x:` [![Build Status (2.x)](https://travis-ci.org/joel-costigliola/assertj-core.svg?branch=2.x)](https://travis-ci.org/joel-costigliola/assertj-core/branches) [![Maven Central](https://maven-badges.herokuapp.com/maven-central/org.assertj/assertj-core/badge.svg)](https://maven-badges.herokuapp.com/maven-central/org.assertj/assertj-core)

%package data
Summary: data components for the mvn-assertj-core package.
Group: Data

%description data
data components for the mvn-assertj-core package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.jar
/usr/share/java/.m2/repository/org/assertj/assertj-core/3.8.0/assertj-core-3.8.0.pom
