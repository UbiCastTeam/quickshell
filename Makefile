all: install

install:
	python setup.py build && sudo python setup.py install

uninstall:
	sudo rm -rvf /usr/lib/python2.5/site-packages/quickshell
	sudo rm -rvf /usr/lib/python2.5/site-packages/quickshell*.egg-info
	sudo rm -rvf /usr/lib/python2.6/dist-packages/quickshell
	sudo rm -rvf /usr/lib/python2.6/dist-packages/quickshell*.egg-info
	sudo rm -rvf /usr/local/lib/python2.5/site-packages/quickshell
	sudo rm -rvf /usr/local/lib/python2.5/site-packages/quickshell*.egg-info
	sudo rm -rvf /usr/local/lib/python2.6/dist-packages/quickshell
	sudo rm -rvf /usr/local/lib/python2.6/dist-packages/quickshell*.egg-info
	sudo rm -vf `which qs`

clean:
	rm -rf build
	rm -f build-stamp
	find . -name "*.pyc" -o -name "*~" | xargs -r rm

builddeb:
	dpkg-buildpackage -rfakeroot

