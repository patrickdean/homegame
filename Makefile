

dependencies:
	npm install

build:
	mkdir -p dist/css
	cp phb.standalone.css dist/css
	node assemble.js

publish:
