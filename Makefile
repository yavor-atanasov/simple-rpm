.PHONY: clean
clean:
	# Clean out any old RPMs from previous builds
	rm -rf SRPMS RPMS SOURCES

.PHONY: source
source:
	# Bundle up all the source code into a single .tar.gz file, used in
	# combination with the .spec file to create the RPM(s)
	mkdir -p SOURCES/
	tar -czf SOURCES/src.tar.gz src/

.PHONY: rpm
rpm: clean source
	mock-build --os 7
